from antlr4 import *

from PartiQLTokens import PartiQLTokens
from PartiQLParser import PartiQLParser


def validate_partiql(query):

    if query is None:
        return False

    lexer = PartiQLTokens(InputStream(query))
    stream = CommonTokenStream(lexer)
    parser = PartiQLParser(stream)

    try:
        parser.root()
        return not parser.getNumberOfSyntaxErrors()
    except Exception as e:
        return False


partiql_query = "a 10"
print(validate_partiql(partiql_query))
