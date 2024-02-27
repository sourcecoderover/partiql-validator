import boto3
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@with_syntactic_validator
def create_filter_if_not_exist():
    database_name=""
    table_name=""
    filter_expression=""
    exists, filter_name = check_existing_filters(filter_expression)
    if exists:
        return filter_name
    else:
        return create_filter()


def create_filter():
    database_name=""
    table_name=""
    filter_expression=""
    filter_name = get_lake_formation_client().create_filter()
    insert_into_dynaomdb(filter_name,database_name,table_name,filter_expression)
    return filter_name

def get_lake_formation_client():
    lf_client = boto3.client('lakeformation', region_name='us-east-1')
    return lf_client


def check_existing_filters(catalog_id, principal_arn, database_name, table_name):

    resource_types = ['CATALOG', 'DATABASE', 'TABLE']
    resources = {'Database': {'CatalogId': catalog_id, 'Name': database_name},
                 'Table': {'CatalogId': catalog_id, 'DatabaseName': database_name, 'Name': table_name}}

    existing_filters = []

    for resource_type in resource_types:
        print(f"Permissions for ResourceType: {resource_type}")
        lf_params = {
            'CatalogId': catalog_id,
            'Principal': {
                'DataLakePrincipalIdentifier': principal_arn
            },
            'ResourceType': resource_types,
            'Resource': resources,
            'MaxResults': 50
        }
        response = get_from_dynamodb()
        permissions = response.get('PrincipalResourcePermissions', [])
        for permission in permissions:
            logger.info(f"Permission: {permission}")
            if 'Condition' in permission and 'FilterExpression' in permission['Condition']:
                existing_filters.append(permission['Condition']['FilterExpression'])

        return existing_filters


def grant_row_level_permission(catalog_id, database_name, table_name, principal, filter_expression):

    lf_client = get_lake_formation_client()
    existing_filters = check_existing_filters(catalog_id, principal, database_name, table_name)

    if filter_expression in existing_filters:
        logger.info("Row-level data filter already exists with the provided filter expression.")
        return f"Data filter with filter-expression {filter_expression} already exists"

    resource = {
        'DatabaseName': database_name,
        'TableWithColumns': {
            'DatabaseName': database_name,
            'Name': table_name,
            'ColumnNames': [],  # If specific columns are needed, add them here
            'ColumnWildcard': {'ExcludedColumnNames': []}
        }
    }

    permissions = ['SELECT', 'DESCRIBE', 'DROP']

    lf_client.grant_permissions(
        Principal=principal,
        Resource=resource,
        Permissions=permissions,
        PermissionsWithGrantOption=[],
        PermissionsToGrant=[],
        PermissionsToRevoke=[],
        PermissionsToApply=[],
        Condition={
            'FilterExpression': filter_expression
        }
    )

    return f"Row-level permission granted successfully"

class DFRowLevelFilter:
    normalized_expression = ""


    def __init__(self,database_name,table_name,expression):
        ## TODO setters
        self.normalized_expression = self.get_normalized_expression()


    def get_normalized_expression(self):
        print()

