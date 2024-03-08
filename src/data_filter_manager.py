import logging

from botocore.exceptions import ClientError

from src.aws_utils import save_to_dynamodb, fetch_records_from_dynamodb, create_filter_permission, \
    create_data_cell_filter
from src.query_validator import with_syntactic_validator
from src.row_level_filter import DFRowLevelFilter

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@with_syntactic_validator
def create_filter_if_not_exist(df_row_level_filter: DFRowLevelFilter):
    is_filter_present, filter_name = False, None
    if df_row_level_filter is not None:
        is_filter_present, filter_name = check_existing_filters(df_row_level_filter)
    if is_filter_present:
        return filter_name
    else:
        return create_row_level_filter(df_row_level_filter)


def create_row_level_filter(df_row_level_filter: DFRowLevelFilter):
    filter_name = create_data_cell_filter(df_row_level_filter)
    if filter_name is not None:
        create_filter_permission(df_row_level_filter, filter_name)
        save_to_dynamodb(df_row_level_filter, filter_name)
        return filter_name
    else:
        raise ClientError("Something went wrong. Could not create row level data filter & associated permissions")


def check_existing_filters(df_row_level_filter):
    is_filter_present, filter_name = False, None
    filter_records = fetch_records_from_dynamodb(df_row_level_filter)
    if filter_records:
        first_record = filter_records[0]
        logger.info(f"Matched Filter Record is: {first_record}")
        is_filter_present, filter_name = (True, first_record.filter_name) if first_record else (False, None)

    return is_filter_present, filter_name



