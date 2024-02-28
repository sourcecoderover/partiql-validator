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
            parsed = sqlparse.parse(self._expression)
            normalized = sqlparse.format(str(parsed[0]), reindent=True, keyword_case='upper', strip_comments=True)
            return normalized
        except SyntaxError as e:
            return e.msg
