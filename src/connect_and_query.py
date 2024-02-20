import boto3

# Define AWS region and Athena database and table details
region_name = 'ap-south-1'  # e.g., 'us-east-1'
database = 'parti_txn_db'
table = 'parti_txn_data_table'

# Initialize Athena client
athena_client = boto3.client('athena', region_name=region_name)


# Execute Athena query
def execute_athena_query(athena_query):
    response = athena_client.start_query_execution(
        QueryString=athena_query,
        QueryExecutionContext={
            'Database': database
        },
        ResultConfiguration={
            'OutputLocation': 's3://code-reover-results/txn-data/'
        }
    )
    exec_id = response['QueryExecutionId']
    return exec_id


# Check query execution status
def check_query_status(exec_id):
    response = athena_client.get_query_execution(
        QueryExecutionId=exec_id
    )
    final_state = response['QueryExecution']['Status']['State']
    return final_state


# Get query results
def get_query_results(exec_id):
    response = athena_client.get_query_results(
        QueryExecutionId=exec_id
    )
    final_results = response['ResultSet']['Rows']
    return final_results


# Example query
query = f"SELECT * FROM {table} LIMIT 1"

# Execute query
execution_id = execute_athena_query(query)

# Wait for query execution to complete
while True:
    state = check_query_status(execution_id)
    if state in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
        break

# If query succeeded, fetch and print results
if state == 'SUCCEEDED':
    results = get_query_results(execution_id)
    for row in results:
        print([data.get('VarCharValue') for data in row['Data']])
else:
    print("Query execution failed or was cancelled.")
