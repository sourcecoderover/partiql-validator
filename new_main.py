from src.data_filter_manager import create_filter_if_not_exist
from src.row_level_filter import DFRowLevelFilter

catalog_id = '590183925259'
database_name = 'partiql-txndb'
table_name = 'partiql-txn-table'
principal = 'arn:aws:iam::590183925259:user/lf-admin'
filter_expression = "transaction_id=TXN001"

df_row_level_filter = DFRowLevelFilter(database_name, table_name, filter_expression)
create_filter_if_not_exist(df_row_level_filter)
print("success")
