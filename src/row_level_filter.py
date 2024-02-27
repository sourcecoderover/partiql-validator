import ast


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
            parsed_expression = ast.parse(self._expression, mode='eval')
            normalized_expression = ast.dump(parsed_expression)
            return normalized_expression
        except SyntaxError:
            return None
