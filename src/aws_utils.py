import boto3
import logging

from src.filter_record import FilterRecord
from src.row_level_filter import DFRowLevelFilter

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_lake_formation_client():
    lf_client = boto3.client('lakeformation', region_name='us-east-1')
    return lf_client


def get_dynamodb_client():
    dynamodb = boto3.resource('dynamodb')
    return dynamodb


def save_to_dynamodb(df_row_level_filter: DFRowLevelFilter):
    dynamodb = get_dynamodb_client()
    table = dynamodb.Table("df_filters_data")
    dynamodb_filter_record = FilterRecord(df_row_level_filter.expression,
                                          df_row_level_filter.get_normalized_expression(),
                                          df_row_level_filter.database_name, df_row_level_filter.table_name,
                                          'system', 'system')
    item = dynamodb_filter_record.to_dynamodb_item()
    table.put_item(Item=item)
    logger.info("Record inserted successfully.")


def fetch_records_from_dynamodb(df_row_level_filter: DFRowLevelFilter):
    dynamodb = get_dynamodb_client()
    table = dynamodb.Table("table_name")

    logger.info("Constructing the filter expression")
    normalized_expression = df_row_level_filter.get_normalized_expression()
    if not normalized_expression:
        print("Invalid filter expression.")
        return

    filter_expression = "filter_expression = :exp or normalized_expression = :normalized_exp"
    expression_attribute_values = {":exp": df_row_level_filter.expression, ":normalized_exp": normalized_expression}

    logger.info(f"Query the table using the filter expression: {df_row_level_filter.expression}, "
                f"normalized_expression: {normalized_expression}")
    response = table.scan(FilterExpression=filter_expression, ExpressionAttributeValues=expression_attribute_values)
    items = response['Items']

    records = [FilterRecord().from_dynamodb_item(item) for item in items]

    return records


def create_filter_permission(df_row_level_filter: DFRowLevelFilter):

    lf_client = get_lake_formation_client()
    resource = {
        'DatabaseName': df_row_level_filter.database_name,
        'TableWithColumns': {
            'DatabaseName': df_row_level_filter.database_name,
            'Name': df_row_level_filter.table_name,
            'ColumnNames': [],
            'ColumnWildcard': {'ExcludedColumnNames': []}
        }
    }

    permissions = ['SELECT', 'DESCRIBE', 'DROP']

    lf_client.grant_permissions(
        Principal="principal",
        Resource=resource,
        Permissions=permissions,
        PermissionsWithGrantOption=[],
        PermissionsToGrant=[],
        PermissionsToRevoke=[],
        PermissionsToApply=[],
        Condition={
            'FilterExpression': df_row_level_filter.expression
        }
    )

    return f"Row-level permission granted successfully"
