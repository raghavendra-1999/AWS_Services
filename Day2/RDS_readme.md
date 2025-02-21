## **Amazon RDS - Relational Database Service**

### **What is Amazon RDS?**
Amazon RDS is a fully managed relational database service that simplifies database operations, maintenance, and scaling.

### **Advantages of RDS**
- **Managed Database**: AWS handles backups, scaling, security, and maintenance.
- **High Availability**: Supports Multi-AZ deployments.
- **Automatic Backups**: Enables daily backups and snapshots.
- **Scalability**: Easily scale storage and compute resources.
- **Security**: Supports IAM roles, encryption, and VPC isolation.

  ### **Common Use Cases**

- **Web Applications**: Use RDS as the backend database for high-performance, scalable applications.
- **Data Warehousing**: Store structured data for reporting and analytics with tools like Tableau, Power BI, and AWS Redshift.
- **ETL Pipelines**: Serve as an intermediate storage layer for extracting, transforming, and loading (ETL) data.
- **Multi-Tenant Applications**: Support multiple users with isolated databases for SaaS platforms.
- **Machine Learning Workloads**: Store processed data before feeding it into AWS SageMaker or other ML models.
- **Disaster Recovery**: Enable automated failover with Multi-AZ deployments and cross-region replication..
- **Hybrid Cloud Integration**: Extend on-premises databases into the cloud for scalability and reliability.

### **RDS Configuration using AWS CLI**
#### **1. Create an RDS Instance**

```sh
aws rds create-db-instance --db-instance-identifier mydbinstance --db-instance-class db.t3.micro --engine mysql --master-username admin --master-user-password Raghav123 --allocated-storage 20 --backup-retention-period 7 --no-multi-az --region us-east-2
```
```sh
aws rds describe-db-instances --db-instance-identifier mydbinstance --query "DBInstances[0].Endpoint.Address"
"mydbinstance.cjuasg0kyyl8.us-east-2.rds.amazonaws.com"
```
<img width="761" alt="RDS_Using_cli" src="https://github.com/user-attachments/assets/a62e08a6-5aca-4985-8dcc-0d4a8e356ed9" />

### **Connecting to RDS using Python**
```python
import mysql.connector

# RDS Configuration
db_host = "mydbinstance.cjuasg0kyyl8.us-east-2.rds.amazonaws.com"  # Your RDS endpoint
db_user = "admin"  # Master username
db_password = "Raghav123"  # Your master password
db_name = "mydbinstance"  # Ensure this database exists, or use `None` first

try:
    print(f"Attempting to connect to {db_host}...")

    # Connect to MySQL without specifying a database first
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password
    )
    cursor = conn.cursor()
    print(" Connection successful!")

    # Check if the database exists
    cursor.execute("SHOW DATABASES;")
    databases = [db[0] for db in cursor.fetchall()]
    
    if db_name not in databases:
        print(f" Database '{db_name}' not found. Creating it now...")
        cursor.execute(f"CREATE DATABASE {db_name};")
        print(f" Database '{db_name}' created successfully!")

    # Now connect to the specific database
    conn.database = db_name
    print(f"Switched to database: {db_name}")

    # Get MySQL version
    cursor.execute("SELECT VERSION();")
    version = cursor.fetchone()
    print(f"MySQL version: {version[0]}")

except mysql.connector.Error as err:
    print(f" Error: {err}")

finally:
    # Ensure cursor and connection are closed properly
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
```
