import keyword

import sqlparse


class DFRowLevelFilter:

    def __init__(self, database_name=None, table_name=None, expression=None):
        self._database_name = database_name
        self._table_name = table_name
        self._expression = expression
        self._normalized_expression = self.get_normalized_expression()

    @property
    def database_name(self):
        return self._database_name

    @database_name.setter
    def database_name(self, value):
        self._database_name = value

    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, value):
        self._table_name = value

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, value):
        self._expression = value

    def __repr__(self):
        return f"DFRowLevelFilter(database_name={self._database_name}, " \
               f"table_name={self._table_name}, expression={self._expression})"

    def get_normalized_expression(self):
        try:
            parsed_sql = sqlparse.parse(self._expression)[0]
            normalized_tokens = [str(token).strip() for token in parsed_sql.tokens if not token.is_whitespace]
            normalized_tokens = [token.upper() if keyword.iskeyword(token) else token for token in normalized_tokens]
            normalized_tokens.sort()
            normalized_expression = " ".join(normalized_tokens)
            return normalized_expression
        except SyntaxError as e:
            return e.msg
