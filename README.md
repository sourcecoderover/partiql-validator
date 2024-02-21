###### **PartiQL Syntactic Validation**

PartiQL Syntactic Validation is a Python project that provides a simple way to validate PartiQL queries for correctness.

**Features**
Syntax Validation: Validate the syntax of PartiQL queries to ensure they adhere to the PartiQL grammar.
Simple Interface: Easy-to-use interface for validating PartiQL queries.

**Installation**
1. Clone the repository: 
   git clone https://github.com/your-username/partiql-syntactic-validation.git
   
2. Install dependencies:
   pip install -r requirements.txt
   
**Usage**
To validate a PartiQL query, simply call the validate_partiql function and pass the query as a string parameter:

from partiql_validation import validate_partiql

partiql_query = "SELECT * FROM table_name"
print(validate_partiql(partiql_query))  # True or False

**Contributing**
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new pull request.

****Steps to configure the repository
1. Import the PartiQL.g4 and PartiQLTokens.g4 grammar files from https://partiql.org/syntax/antlr.html
2. Alternatively, the github repo can also be referred: https://github.com/partiql/partiql-lang-kotlin/tree/c3b6e66647cdee421dd43abe1cfca8546f0f5529
3. Download the antlr complete jar from antlr official page.
4. Execute antlr command to parse PartiQLTokens.g4
   java -jar antlr-4.13.1-complete.jar PartiQLTokens.g4 -Dlanguage=Python3
   
5. Execute antlr command to parse PartiQL.g4
   java -jar antlr-4.13.1-complete.jar PartiQL.g4 -Dlanguage=Python3

6. Pip install antlr4-python3-runtime
   pip install boto3 antlr4-python3-runtime

7. Verify PartiQLParser.py, PartiQLListener.py and PartiQLTokens.py files has been generated after executing the above steps.

