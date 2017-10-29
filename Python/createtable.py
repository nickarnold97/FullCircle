import boto3

# Get the service resource.
client = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'string',
            'AttributeType': 'S'|'N'|'B'
        },
    ],
    TableName='string',
    KeySchema=[
        {
            'AttributeName': 'string',
            'KeyType': 'HASH'|'RANGE'
        },
    ],
    LocalSecondaryIndexes=[
        {
            'IndexName': 'string',
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'Projection': {
                'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                'NonKeyAttributes': [
                    'string',
                ]
            }
        },
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'string',
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'Projection': {
                'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                'NonKeyAttributes': [
                    'string',
                ]
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 123,
                'WriteCapacityUnits': 123
            }
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 123,
        'WriteCapacityUnits': 123
    },
    StreamSpecification={
        'StreamEnabled': True|False,
        'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print(table.item_count)
