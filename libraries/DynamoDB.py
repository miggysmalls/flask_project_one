import boto3
from config.system import dynamodb


class DynamoDB(object):

    def __init__(self):
        self.client = boto3.client('dynamodb', region_name='us-east-1', endpoint_url=dynamodb)
        self.resource = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url=dynamodb)

    def list_all_tables(self):
        return self.client.list_tables()

    def scan_table(self, table_name):
        return self.resource.Table(table_name).scan()

    def create_table(self, table_name, partition_name, partition_type, sort_name, sort_type):
        key_schema = [
            {
                'AttributeName': partition_name,
                'KeyType': 'HASH'
            },
            {
                'AttributeName': sort_name,
                'KeyType': 'RANGE'
            }
        ]
        attribute_defs = [
            {
                'AttributeName': partition_name,
                'AttributeType': partition_type
            },
            {
                'AttributeName': sort_name,
                'AttributeType': sort_type
            },
        ]
        return self.resource.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_defs,
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )

    def get_table(self, table_name):
        pass

    def delete_table(self, table_name):
        return self.client.delete_table(TableName=table_name)
