from datetime import datetime


class FilterRecord:
    def __init__(self, filter_name, filter_expression, normalized_expression, database_name, table_name,
                 created_by, updated_by):
        self.filter_name = filter_name
        self.filter_expression = filter_expression
        self.normalized_expression = normalized_expression
        self.database_name = database_name
        self.table_name = table_name
        self.created_at = datetime.now().isoformat()
        self.created_by = created_by
        self.updated_at = self.created_at
        self.updated_by = updated_by

    def __repr__(self):
        return f"DynamoDBRecord(filter_name='{self.filter_name}'," \
               f"filter_expression='{self.filter_expression}', " \
               f"normalized_expression='{self.normalized_expression}', " \
               f"database_name='{self.database_name}', table_name='{self.table_name}', " \
               f"created_at='{self.created_at}', created_by='{self.created_by}', " \
               f"updated_at='{self.updated_at}', updated_by='{self.updated_by}')"

    def to_dynamodb_item(self):
        return {
            'filter_name': self.filter_name,
            'filter_expression': self.filter_expression,
            'normalized_expression': self.normalized_expression,
            'database_name': self.database_name,
            'table_name': self.table_name,
            'created_at': self.created_at,
            'created_by': self.created_by,
            'updated_at': self.updated_at,
            'updated_by': self.updated_by
        }

    def from_dynamodb_item(self, item):
        self.filter_expression = item['filter_expression']
        self.normalized_expression = item['normalized_expression']
        self.database_name = item['database_name']
        self.table_name = item['table_name']
        self.created_at = item.get('created_at')
        self.created_by = item['created_by']
        self.updated_at = item.get('updated_at')
        self.updated_by = item['updated_by']
        return self
