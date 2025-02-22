import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-2')  # Change to your region

# Create DynamoDB table
response = dynamodb.create_table(
    TableName='raghav_boto_table',
    AttributeDefinitions=[
        {
            'AttributeName': 'UserId',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Email',
            'AttributeType': 'S'
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'UserId',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'Email',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table creation started:", response)
