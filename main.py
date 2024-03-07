from src.data_filter_manager import create_filter_if_not_exist
from src.row_level_filter import DFRowLevelFilter

catalog_id = '919872893264'
database_name = 'risk_transactions_db'
table_name = 'executions'
principal = 'arn:aws:iam::205083977700:user/risk-lf-analyst'

# filter_expression_1 = "column1 > 10 AND column2 < 20"
# filter_expression_2 = "column2 < 20 AND column1 > 10"

filter_expression_1 = "col3 > 100 AND col4 IN (5, 20) AND col5 < 100 ORDER BY col3 DESC;"
filter_expression_2 = "col5 < 100 AND col4 IN (5, 20) AND col3 > 100 ORDER BY col3 DESC;"

# filter_expression_1 = "SELECT t1.col1, t2.col2, SUM(t3.col3) AS total FROM table1 t1 " \
#                       "JOIN table2 t2 ON t1.id = t2.id JOIN table3 t3 ON t1.id = t3.id " \
#                       "GROUP BY t1.col1, t2.col2 HAVING total > 1000"
# filter_expression_2 = "SELECT t1.col1, t2.col2, SUM(t3.col3) AS total FROM table3 t3 " \
#                       "JOIN table1 t1 ON t1.id = t3.id JOIN table2 t2 ON t1.id = t2.id " \
#                       "GROUP BY t1.col1, t2.col2 HAVING total > 1000"

# validate_partiql(filter_expression)
# grant_row_level_permission(catalog_id, database_name, table_name, principal, filter_expression)

df_row_level_filter_1 = DFRowLevelFilter(database_name, table_name, filter_expression_1)
df_row_level_filter_2 = DFRowLevelFilter(database_name, table_name, filter_expression_2)

# create_filter_if_not_exist(df_row_level_filter)
normalized_sql1 = df_row_level_filter_1.get_normalized_expression()
normalized_sql2 = df_row_level_filter_2.get_normalized_expression()


if normalized_sql1 == normalized_sql2:
    print("The queries are equivalent")
else:
    print("The queries are not equivalent")
