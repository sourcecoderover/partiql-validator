from datetime import datetime


class FilterRecord:
    def __init__(self, catalog_id=None, filter_name=None, filter_expression=None, normalized_expression=None, database_name=None,
                 table_name=None, created_by=None, updated_by=None):
        self.catalog_id = catalog_id
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
        return f"DynamoDBRecord(catalog_id='{self.catalog_id}',"\
               f"filter_name='{self.filter_name}'," \
               f"filter_expression='{self.filter_expression}', " \
               f"normalized_expression='{self.normalized_expression}', " \
               f"database_name='{self.database_name}', table_name='{self.table_name}', " \
               f"created_at='{self.created_at}', created_by='{self.created_by}', " \
               f"updated_at='{self.updated_at}', updated_by='{self.updated_by}')"

    def to_dynamodb_item(self):
        return {
            'data_catalog': {'S': self.catalog_id + "|" + self.database_name + "|" + self.table_name},
            'filter_name': {'S': self.filter_name},
            'filter_expression': {'S': self.filter_expression},
            'normalized_expression': {'S': self.normalized_expression},
            'catalog_id': {'S': self.catalog_id},
            'database_name': {'S': self.database_name},
            'table_name': {'S': self.table_name},
            'created_at': {'S': self.created_at},
            'created_by': {'S': self.created_by},
            'updated_at': {'S': self.updated_at},
            'updated_by': {'S': self.updated_by}
        }

    def from_dynamodb_item(self, item):
        self.catalog_id = item['catalog_id']
        self.filter_name = item['filter_name']
        self.filter_expression = item['filter_expression']
        self.normalized_expression = item['normalized_expression']
        self.database_name = item['database_name']
        self.table_name = item['table_name']
        self.created_at = item.get('created_at')
        self.created_by = item['created_by']
        self.updated_at = item.get('updated_at')
        self.updated_by = item['updated_by']
        return self
