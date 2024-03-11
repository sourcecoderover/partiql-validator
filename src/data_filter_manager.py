import logging

from botocore.exceptions import ClientError

from src.aws_utils import save_to_dynamodb, fetch_records_from_dynamodb, create_filter_permission, \
    create_data_cell_filter
from src.query_validator import with_syntactic_validator
from src.row_level_filter import DFRowLevelFilter

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@with_syntactic_validator
def create_filter_if_exist(df_row_level_filter: DFRowLevelFilter, catalog_id):
    is_filter_present, filter_name = False, None
    if df_row_level_filter is not None:
        is_filter_present, filter_name = check_existing_filters(catalog_id, df_row_level_filter)
    return is_filter_present, filter_name


def create_row_level_filter(catalog_id, account, permissions, df_row_level_filter: DFRowLevelFilter):
    filter_name = create_data_cell_filter(catalog_id, df_row_level_filter)
    save_to_dynamodb(catalog_id, filter_name, df_row_level_filter)
    return create_filter_permission(catalog_id, account, permissions, filter_name, df_row_level_filter)


def check_existing_filters(catalog_id, df_row_level_filter):
    is_filter_present, filter_name = False, None
    filter_records = fetch_records_from_dynamodb(catalog_id, df_row_level_filter)
    if filter_records:
        first_record = filter_records[0]
        logger.info(f"Matched Filter Record is: {first_record}")
        is_filter_present, filter_name = (True, first_record.filter_name) if first_record else (False, None)

    return is_filter_present, filter_name



