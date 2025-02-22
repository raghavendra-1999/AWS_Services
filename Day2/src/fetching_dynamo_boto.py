import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference the 'Users' table (ensure the name is correct without spaces)
table = dynamodb.Table('raghav_boto_table')  # Correct table name without any extra spaces

# Fetch data (GetItem)
def fetch_data():
    try:
        response = table.get_item(
            Key={
                'UserId': 'admin123',
                'Email': 'raghav@gmail.com'
            }
        )
        if 'Item' in response:
            print("Data Retrieved:", response['Item'])
        else:
            print("Item not found.")
    except ClientError as e:
        print("Error fetching item:", e)

# Call the fetch function to check if the item exists
fetch_data()
