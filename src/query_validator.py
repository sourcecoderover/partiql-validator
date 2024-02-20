import boto3
from antlr4 import *
from PartiQLTokens import PartiQLTokens
from PartiQLParser import PartiQLParser


def validate_partiql(partiql_query):
    # Create a lexer and parser for the PartiQL syntax
    lexer = PartiQLTokens(InputStream(partiql_query))
    stream = CommonTokenStream(lexer)
    parser = PartiQLParser(stream)

    try:
        # Try parsing the query, if successful, return True
        parser.root()
        return True
    except Exception as e:
        # If parsing fails, return False
        return False


def execute_query(partiql_query):
    # Validate the PartiQL syntax before executing the query
    if not validate_partiql(partiql_query):
        return {"error": "Invalid PartiQL syntax"}

    # Initialize AWS Athena client
    athena_client = boto3.client('athena')

    # Execute the query in Athena
    response = athena_client.start_query_execution(
        QueryString=partiql_query,
        QueryExecutionContext={
            'Database': 'your_database_name'  # Replace 'your_database_name' with your actual database name
        },
        ResultConfiguration={
            'OutputLocation': 's3://your-bucket-name/athena-results/'  # Replace 'your-bucket-name' with your actual S3 bucket name
        }
    )

    # Return query execution response
    return response


# Example usage
partiql_query = """
    SELECT name, age
    FROM users
    WHERE age > 18
    """
print(validate_partiql(partiql_query))
print(execute_query(partiql_query))
