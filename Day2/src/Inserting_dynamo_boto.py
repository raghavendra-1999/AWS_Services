import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference the 'Users' table
table = dynamodb.Table('raghav_boto_table')

# Insert data (PutItem)
def insert_data():
    try:
        response = table.put_item(
            Item={
                'UserId': 'admin123',  # Primary key
                'Email': 'raghav@gmail.com',  # Range key
                'Name': 'Raghavendra',  # Additional attribute
                'Age': 25  # Additional attribute
            }
        )
        print("Insert Successful:", response)
    except ClientError as e:
        print("Error inserting item:", e)

# Call the function to insert data
insert_data()
