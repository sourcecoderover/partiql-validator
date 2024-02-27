import logging

from src.aws_utils import save_to_dynamodb, fetch_records_from_dynamodb, create_filter_permission
from src.query_validator import with_syntactic_validator
from src.row_level_filter import DFRowLevelFilter

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@with_syntactic_validator
def create_filter_if_not_exist(df_row_level_filter: DFRowLevelFilter):
    is_filter_present = False
    filter_name = None
    if df_row_level_filter is not None:
        is_filter_present, filter_name = check_existing_filters(df_row_level_filter)
    if is_filter_present:
        return filter_name
    else:
        return create_row_level_filter(df_row_level_filter)


def create_row_level_filter(df_row_level_filter: DFRowLevelFilter):
    filter_name = create_filter_permission(df_row_level_filter)
    save_to_dynamodb(df_row_level_filter)
    return filter_name


def check_existing_filters(df_row_level_filter):
    is_filter_present = False
    first_record = None
    filter_records = fetch_records_from_dynamodb(df_row_level_filter)

    if filter_records:
        first_record = filter_records[0]
        logger.info(f"Matched Filter Record is: {first_record}")
        is_filter_present = True if first_record else False

    return is_filter_present, first_record.filter_name



