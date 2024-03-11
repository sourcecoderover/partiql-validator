import os
import json

from src.aws_utils import create_filter_permission
from src.data_filter_manager import create_filter_if_exist, create_row_level_filter
from src.row_level_filter import DFRowLevelFilter


def share_catalog_to_role(catalog_id, account, permissions, df_row_level_filter: DFRowLevelFilter):
    response = grant_table_filter_permission(catalog_id, account, permissions, df_row_level_filter)
    return response


def grant_table_filter_permission(catalog_id, account, permissions, df_row_level_filter: DFRowLevelFilter):
    is_filter_present, filter_name = create_filter_if_exist(df_row_level_filter, catalog_id)
    if is_filter_present:
        return create_filter_permission(catalog_id, account, permissions, filter_name, df_row_level_filter)
    else:
        return create_row_level_filter(catalog_id, account, permissions, df_row_level_filter)
