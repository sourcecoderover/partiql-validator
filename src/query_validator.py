from antlr4 import *
from functools import wraps

from PartiQLTokens import PartiQLTokens
from PartiQLParser import PartiQLParser


def validate_partiql(query):
    if query is None:
        return False

    lexer = PartiQLTokens(InputStream(query))
    stream = CommonTokenStream(lexer)
    parser = PartiQLParser(stream)

    try:
        tree = parser.root()
        print(tree.toStringTree(recog=parser))
        return not parser.getNumberOfSyntaxErrors()
    except Exception as e:
        return False


def with_syntactic_validator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        df_data_filter_object = args[0]
        if validate_partiql(df_data_filter_object.expression):
            return func(*args, **kwargs)
        else:
            raise ValueError("Invalid PartiQL query provided.")

    return wrapper
