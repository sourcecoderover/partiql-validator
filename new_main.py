from src.catalog_service import share_catalog_to_role
from src.row_level_filter import DFRowLevelFilter

catalog_id = '590183925259'
database_name = 'partiql-txndb'
table_name = 'partiql-txn-table'
permissions = ['SELECT']
account = 'arn:aws:iam::590183925259:user/lf-admin'
filter_expression = "transaction_id='TXN002'"

df_row_level_filter = DFRowLevelFilter(database_name, table_name, filter_expression)
response = share_catalog_to_role(catalog_id, account, permissions, df_row_level_filter)
print(f"filter creation successful with response {response}")
