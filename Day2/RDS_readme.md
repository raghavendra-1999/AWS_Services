## **Amazon RDS - Relational Database Service **

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
aws rds create-db-instance --db-instance-identifier raghavcli --db-instance-class db.t3.micro --engine mysql --master-username admin --master-user-password Raghav123 --allocated-storage 20 --backup-retention-period 7 --no-multi-az --region us-east-2
```
**To verify it**
```sh
aws rds describe-db-instances --db-instance-identifier mydbinstance --query "DBInstances[0].Endpoint.Address"
"raghavcli.cjuasg0kyyl8.us-east-2.rds.amazonaws.com"
```

### **Connecting to RDS using Python**
```python
import mysql.connector

db_host = "mydbinstance.cjuasg0kyyl8.us-east-2.rds.amazonaws.com"  # Your RDS endpoint
db_user = "admin"  # Master username
db_password = "Raghav123"  # Your master password
db_name = "mydbinstance"  # Ensure this database exists, or use `None` first

try:
    print(f"Attempting to connect to {db_host}...")

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
<img width="761" alt="RDS_Using_cli" src="https://github.com/user-attachments/assets/a62e08a6-5aca-4985-8dcc-0d4a8e356ed9" />
<img width="624" alt="python_rds" src="https://github.com/user-attachments/assets/baecd658-8093-4b87-8c93-2c3597e6854f" />

**To verify it**
```sh
aws rds describe-db-instances --db-instance-identifier mydbinstance --query "DBInstances[0].Endpoint.Address"
"mydbinstance.cjuasg0kyyl8.us-east-2.rds.amazonaws.com"
```
**RDS Data Insertion**
```python
import mysql.connector

# RDS Configuration
db_host = "mydbinstance.cjuasg0kyyl8.us-east-2.rds.amazonaws.com"  # Your RDS endpoint
db_user = "admin"  # Master username
db_password = "Raghav123"  # Your master password
db_name = "mydbinstance"  # Ensure this database exists

try:
    print(f"Connecting to {db_host}...")
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()

    # Create 'employees' table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        department VARCHAR(50),
        salary DECIMAL(10,2)
    );
    """
    cursor.execute(create_table_query)
    print("Table 'employees' created successfully!")

except mysql.connector.Error as err:
    print(f" Error: {err}")

finally:
    cursor.close()
    conn.close()
```
<img width="548" alt="table_creation" src="https://github.com/user-attachments/assets/dd2477ca-63c4-4deb-857e-85472a5006e2" />

**Insert Data into RDS**
```python
import mysql.connector

db_host = "mydbinstance.cjuasg0kyyl8.us-east-2.rds.amazonaws.com"
db_user = "admin"
db_password = "Raghav123"
db_name = "mydbinstance"

try:
    print(f"Connecting to {db_host}...")
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()

    # Insert data into 'employees' table
    insert_query = "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)"
    employees = [
        ("Alice Johnson", "IT", 75000.00),
        ("Bob Smith", "Finance", 80000.00),
        ("Charlie Brown", "HR", 70000.00)
    ]

    cursor.executemany(insert_query, employees)
    conn.commit()
    print(f" {cursor.rowcount} rows inserted into 'employees' table successfully!")

except mysql.connector.Error as err:
    print(f" Error: {err}")

finally:
    cursor.close()
    conn.close()
```
<img width="593" alt="Data_Inserted_output" src="https://github.com/user-attachments/assets/3c164fb2-f8c2-4718-8898-4a533324851f" />

**Fetch and Display Data from RDS**
```python
import mysql.connector

db_host = "mydbinstance.cjuasg0kyyl8.us-east-2.rds.amazonaws.com"
db_user = "admin"
db_password = "Raghav123"
db_name = "mydbinstance"

try:
    print(f"Connecting to {db_host}...")
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()

    # Fetch and display data
    cursor.execute("SELECT * FROM employees;")
    rows = cursor.fetchall()

    print("\n Data in 'employees' table:")
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    conn.close()
```
<img width="587" alt="Fetch_data_output" src="https://github.com/user-attachments/assets/76555ed1-9769-4176-8169-e5d6c91d1edf" />

