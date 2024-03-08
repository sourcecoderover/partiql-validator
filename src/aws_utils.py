import logging
import uuid
import boto3
from botocore.exceptions import ClientError

from src.app_config import get_from_config_file
from src.constants import SUCCESS
from src.filter_record import FilterRecord
from src.row_level_filter import DFRowLevelFilter

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

config = get_from_config_file()


def get_lake_formation_client():
    lf_client = boto3.client('lakeformation', region_name='ap-south-1')
    return lf_client


def get_dynamodb_client():
    dynamodb = boto3.resource('dynamodb')
    return dynamodb


def save_to_dynamodb(df_row_level_filter: DFRowLevelFilter, filter_name):
    dynamodb = get_dynamodb_client()
    table = dynamodb.Table(config['dynamodb_table'])
    dynamodb_filter_record = FilterRecord(filter_name, df_row_level_filter.expression,
                                          df_row_level_filter.get_normalized_expression(),
                                          df_row_level_filter.database_name, df_row_level_filter.table_name,
                                          'system', 'system')
    item = dynamodb_filter_record.to_dynamodb_item()
    table.put_item(Item=item)
    logger.info("Record inserted successfully.")


def fetch_records_from_dynamodb(df_row_level_filter: DFRowLevelFilter):
    dynamodb = get_dynamodb_client()
    table = dynamodb.Table(config['dynamodb_table'])

    logger.info("Constructing the filter expression")
    normalized_expression = df_row_level_filter.get_normalized_expression()
    if not normalized_expression:
        raise KeyError("Invalid filter expression.")

    filter_expression = "filter_expression = :exp or normalized_expression = :normalized_exp"
    expression_attribute_values = {":exp": df_row_level_filter.expression, ":normalized_exp": normalized_expression}

    logger.info(f"Query the table using the filter expression: {df_row_level_filter.expression}, "
                f"normalized_expression: {normalized_expression}")
    response = table.scan(FilterExpression=filter_expression, ExpressionAttributeValues=expression_attribute_values)
    items = response['Items']

    filter_record = FilterRecord()
    records = [filter_record.from_dynamodb_item(item) for item in items]

    return records


def create_data_cell_filter(df_row_level_filter: DFRowLevelFilter):
    lf_client = get_lake_formation_client()
    filter_name = 'data-filter' + str(uuid.uuid4())
    try:
        response = lf_client.create_data_cells_filter(
            TableData={
                'TableCatalogId': config['lf_catalog_id'],
                'DatabaseName': df_row_level_filter.database_name,
                'TableName': df_row_level_filter.table_name,
                'Name': filter_name,
                'RowFilter': {'FilterExpression': df_row_level_filter.expression},
                "ColumnWildcard": {}
            }
        )
        return filter_name if response['ResponseMetadata']['HTTPStatusCode'] == SUCCESS else None
    except ClientError as e:
        logger.error(f"Something went wrong. Client Error: {e.response}")
        raise ValueError(f"Something went wrong. Unable to create Data Filter due to reason: {e.response}")


def create_filter_permission(df_row_level_filter: DFRowLevelFilter, filter_name):
    lf_client = get_lake_formation_client()
    permissions = ['SELECT']
    try:
        response = lf_client.grant_permissions(
            CatalogId=config['lf_catalog_id'],
            Principal={'DataLakePrincipalIdentifier': 'arn:aws:iam::590183925259:user/lf-admin'},
            Resource={
                'DataCellsFilter': {
                    'TableCatalogId': config['lf_catalog_id'],
                    'DatabaseName': df_row_level_filter.database_name,
                    'TableName': df_row_level_filter.table_name,
                    'Name': filter_name
                }
            },
            Permissions=permissions,
            PermissionsWithGrantOption=[]
        )
        return f"Row-level permission granted successfully: {response}"
    except ClientError as e:
        logger.error(f"Something went wrong. Client Error: {e.response}")
        raise ClientError(f"Something went wrong. Unable to create Data Filter permissions due to reason: {e.response}")
