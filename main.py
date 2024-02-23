from src.data_filter_manager import grant_row_level_permission
from src.query_validator import validate_partiql


catalog_id = '919872893264'
database_name = 'risk_transactions_db'
table_name = 'executions'
principal = 'arn:aws:iam::205083977700:user/risk-lf-analyst'
filter_expression = "clientid='ClientABC'"

validate_partiql(filter_expression)
grant_row_level_permission(catalog_id, database_name, table_name, principal, filter_expression)
