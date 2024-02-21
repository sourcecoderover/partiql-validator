import unittest

from src.query_validator import validate_partiql


class TestPartiQLValidation(unittest.TestCase):

    def test_valid_partiql_query(self):
        partiql_query = "SELECT * FROM table_name"
        self.assertTrue(validate_partiql(partiql_query))

    def test_invalid_partiql_query(self):
        partiql_query = "a 10"
        self.assertFalse(validate_partiql(partiql_query))

    def test_empty_query(self):
        partiql_query = ""
        self.assertFalse(validate_partiql(partiql_query))

    def test_null_query(self):
        partiql_query = None
        self.assertFalse(validate_partiql(partiql_query))


if __name__ == '__main__':
    unittest.main()
