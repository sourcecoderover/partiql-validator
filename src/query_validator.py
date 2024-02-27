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
        parser.root()
        return not parser.getNumberOfSyntaxErrors()
    except Exception as e:
        return False


def with_syntactic_validator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        if validate_partiql(query):
            return func(*args, **kwargs)
        else:
            raise ValueError("Invalid PartiQL query provided.")

    return wrapper
