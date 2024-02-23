import boto3
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_lake_formation_client():
    lf_client = boto3.client('lakeformation', region_name='us-east-1')
    return lf_client


def check_existing_filters(catalog_id, principal_arn, database_name, table_name):
    lf_client = get_lake_formation_client()

    resource_types = ['CATALOG', 'DATABASE', 'TABLE']
    resources = {'Database': {'CatalogId': catalog_id, 'Name': database_name},
                 'Table': {'CatalogId': catalog_id, 'DatabaseName': database_name, 'Name': table_name}}

    existing_filters = []

    for resource_type in resource_types:
        print(f"Permissions for ResourceType: {resource_type}")
        lf_params = {
            'CatalogId': catalog_id,
            'Principal': {
                # arn:aws:iam::919872893264:root
                'DataLakePrincipalIdentifier': principal_arn
            },
            'ResourceType': resource_types,
            'Resource': resources,
            'MaxResults': 50
        }
        response = lf_client.list_permissions(**lf_params)
        # Process the response
        permissions = response.get('PrincipalResourcePermissions', [])
        # Display retrieved permissions
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
