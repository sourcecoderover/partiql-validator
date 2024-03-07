import keyword
import logging

import boto3
import sqlparse

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
    table = dynamodb.Table("lf-data-filters")

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

    #records = [FilterRecord.from_dynamodb_item(item) for item in items]
    filter_record = FilterRecord()
    for item in items:
        records = filter_record.from_dynamodb_item(item)

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
        },
        'Database': {
            'CatalogId': '590183925259',
            'Name': df_row_level_filter.database_name
        },
        'Table': {
            'CatalogId': '590183925259',
            'DatabaseName': df_row_level_filter.database_name,
            'Name': df_row_level_filter.table_name
        }
    }

    permissions = ['SELECT']

    # lf_client.grant_permissions(
    #     # Principal="arn:aws:iam::590183925259:user/lf-admin",
    #     # Resource=resource,
    #     # Permissions=permissions,
    #     # PermissionsWithGrantOption=[],
    #     # PermissionsToGrant=[],
    #     # PermissionsToRevoke=[],
    #     # PermissionsToApply=[],
    #     # Condition={
    #     #     'FilterExpression': df_row_level_filter.expression
    #     # }
    #
    # )

    response = lf_client.grant_permissions(
        CatalogId='590183925259',
        Principal={
            'DataLakePrincipalIdentifier': 'arn:aws:iam::590183925259:user/lf-admin'
        },
        Resource={
            'Catalog': {}
            ,
            'Database': {
                'CatalogId': 'string',
                'Name': 'string'
            },
            'Table': {
                'CatalogId': 'string',
                'DatabaseName': 'string',
                'Name': 'string',
                'TableWildcard': {}

            },
            'TableWithColumns': {
                'CatalogId': 'string',
                'DatabaseName': 'string',
                'Name': 'string',
                'ColumnNames': [
                    'string',
                ],
                'ColumnWildcard': {
                    'ExcludedColumnNames': [
                        'string',
                    ]
                }
            },
            'DataLocation': {
                'CatalogId': 'string',
                'ResourceArn': 'string'
            },
            'DataCellsFilter': {
                'TableCatalogId': 'string',
                'DatabaseName': 'string',
                'TableName': 'string',
                'Name': 'string'
            },
            'LFTag': {
                'CatalogId': 'string',
                'TagKey': 'string',
                'TagValues': [
                    'string',
                ]
            },
            'LFTagPolicy': {
                'CatalogId': 'string',
                'ResourceType': 'DATABASE' | 'TABLE',
                'Expression': [
                    {
                        'TagKey': 'string',
                        'TagValues': [
                            'string',
                        ]
                    },
                ]
            }
        },
        Permissions=[
            'ALL' | 'SELECT' | 'ALTER' | 'DROP' | 'DELETE' | 'INSERT' | 'DESCRIBE' | 'CREATE_DATABASE' | 'CREATE_TABLE' | 'DATA_LOCATION_ACCESS' | 'CREATE_LF_TAG' | 'ASSOCIATE' | 'GRANT_WITH_LF_TAG_EXPRESSION',
        ],
        PermissionsWithGrantOption=[
            'ALL' | 'SELECT' | 'ALTER' | 'DROP' | 'DELETE' | 'INSERT' | 'DESCRIBE' | 'CREATE_DATABASE' | 'CREATE_TABLE' | 'DATA_LOCATION_ACCESS' | 'CREATE_LF_TAG' | 'ASSOCIATE' | 'GRANT_WITH_LF_TAG_EXPRESSION',
        ]
    )

    return f"Row-level permission granted successfully"