
## **Amazon DynamoDB - NoSQL Database Service**

 **What is Amazon DynamoDB?**
Amazon DynamoDB is a fully managed, serverless, key-value and document database that offers fast and predictable performance with seamless scalability. It is designed for applications that require low-latency data access at any scale.

**Advantages of DynamoDB**
- **Fully Managed**: AWS handles the operational tasks like provisioning hardware, software patches, scaling, and backups.
- **Scalability**: Automatically scales throughput capacity to support application needs without manual intervention.
- **Low Latency**: Provides consistent, single-digit millisecond response times at any scale.
- **Serverless**: No need to manage servers or infrastructure, DynamoDB automatically scales to accommodate workloads.
- **High Availability and Durability**: Supports Multi-AZ deployments with built-in replication across multiple AWS regions.
- **Security**: Integrated with AWS Identity and Access Management (IAM), encryption at rest, and VPC support for isolation.
- **Global Tables**: Supports multi-region, fully replicated tables, ensuring high availability and low-latency access globally.
**Common Use Cases**
- **Mobile Applications**: Store session data, user preferences, and activity logs for mobile apps with high availability and low latency.
- **E-Commerce**: Manage product catalogs, customer orders, and inventory in high-traffic e-commerce sites.
- **Content Management Systems (CMS)**: Store dynamic content, metadata, and user-generated content for websites or apps.
- **Real-Time Analytics**: Handle real-time data processing with DynamoDB Streams, triggering events to Lambda for data processing or analytics.

### **DynamoDB Configuration using AWS CLI**
#### **1. Create an Dynamo Table**

```sh
aws dynamodb create-table --table-name Users --attribute-definitions AttributeName=UserId,AttributeType=S AttributeName=Email,AttributeType=S --key-schema AttributeName=UserId,KeyType=HASH AttributeName=Email,KeyType=RANGE --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```
<img width="760" alt="DynamoTable_cli" src="https://github.com/user-attachments/assets/fcf24fb6-2234-4bba-961c-bb0f719d9eb4" />

#### **2. Inserting values to table**
```sh
aws dynamodb put-item --table-name Users --item "{\"UserId\": {\"S\": \"admin\"}, \"Email\": {\"S\": \"rag@gmail.com\"}}"
```
<img width="520" alt="puttables_DB" src="https://github.com/user-attachments/assets/a999d5c8-6b9a-4b6e-b944-ba521fb53632" />

#### **3. Get Item from Table**

```sh
aws dynamodb get-item --table-name Users --key '{"UserId": {"S": "admin"}, "Email": {"S": "rag@gmail.com"}}'
```
<img width="853" alt="Gettable_cli" src="https://github.com/user-attachments/assets/e90c3483-befb-4ff2-b0b6-e6a565a4d43e" />

## Create a DynamoDB Table using boto3
```python
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
```

<img width="771" alt="dynamotable_boto" src="https://github.com/user-attachments/assets/5300f6a7-e7a8-4301-a1ac-7864cbfd2747" />

## **Inserting Data into DynamoDB**

```python
import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference the 'Users' table
table = dynamodb.Table('Users')

# Insert data (PutItem)
def insert_data():
    try:
        response = table.put_item(
            Item={
                'UserId': 'admin',  # Primary key
                'Email': 'rag@gmail.com',  # Range key
                'Name': 'Raghavendra',  # Additional attribute
                'Age': 25  # Additional attribute
            }
        )
        print("Insert Successful:", response)
    except ClientError as e:
        print("Error inserting item:", e)

# Call the function to insert data
insert_data()
```

<img width="520" alt="Inserting_data_boto" src="https://github.com/user-attachments/assets/94ee66e1-da14-40f5-98bb-b5c3aabae154" />





