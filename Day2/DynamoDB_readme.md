## **Amazon RDS - Relational Database Service**

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
