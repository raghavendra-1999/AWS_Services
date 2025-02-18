# AWS_S3

### **What is Amazon S3?**
Simple Storage Service is a scalable and secure cloud storage service provided by Amazon Web Services (AWS). It allows you to store and retrieve any amount of data from anywhere on the web.

### **What are S3 buckets?**
S3 buckets are containers for storing objects (files) in Amazon S3. Each bucket has a unique name globally across all of AWS. You can think of an S3 bucket as a top-level folder that holds your data.

### **Why use S3 buckets?**
S3 buckets provide a reliable and highly scalable storage solution for various use cases. They are commonly used for backup and restore, data archiving, content storage for websites, and as a data source for big data analytics.

### **Key Concepts**
- **Bucket**: Here we store data in the form of objects.
- **Object**: Data stored in a bucket (e.g., CSV files, images, text files, etc.).

### **Advantages of Amazon S3**
- **Scalability**: Supports unlimited storage for growing workloads.
- **High Durability**: 99.999999999% (11 nines) durability.
- **Security**: Encryption, access control, and IAM integration.
- **Cost-Effective**: Pay-as-you-go pricing with multiple storage classes.
- **Accessibility**: Access via AWS Console, API, CLI, or SDK
- **Serverless Static Website Hosting** – Allows hosting of static websites (HTML, CSS, JavaScript) without managing servers.
- **Performance Optimization** – Integrates with CloudFront (CDN), AWS Lambda, and analytics services for faster content delivery and efficient processing.

### **Use Cases**
- **Data Backup and Archiving**: Store long-term backups and automate database backups.
- **Big Data and Analytics**: Serve as a data lake for ML analytics tools like AWS Glue, Athena, and Redshift.
- **Static Website Hosting**: Serve HTML, CSS, and JavaScript directly from an S3 bucket.
- **Media Storage and Streaming**: Store and stream images, videos, and audio files.
- **Disaster Recovery**: Multi-region replication and versioning for data protection.

### **S3 Configuration using AWS CLI**
#### **1. Configure AWS CLI**
```sh
aws configure
```
Provide:
- **Access Key**: AKIAYWBJYTU6DJGJF5M3
- **Secret Key**: 
- **Region**: us-east-2
- **Output Format**

#### **2. Verify Configuration**
```sh
aws configure list
```

#### **3. Create an S3 Bucket**
```sh
aws s3 mb s3://raghavclibucket1
```
#### **4. uploaded a txt file using cli**
```sh
aws s3 cp /C:\Users\ragha\OneDrive\Desktop\s3_sample_files s3://raghavsfirstbucket1/
```
<img width="737" alt="s3_cli_bucket" src="https://github.com/user-attachments/assets/32e98a92-a6ca-4b27-ac0a-b7f78144f229" />

<img width="614" alt="created_s3_cli" src="https://github.com/user-attachments/assets/d877f158-5a36-482c-a598-4253dbf96686" />

### **S3 Configuration using Python (Boto3)**
#### **Creating an S3 Bucket**

```python
import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region="us-east-2"):
    s3_client = boto3.client("s3", region_name=region)
    try:
        if region == "us-east-1":  # AWS does not require LocationConstraint for us-east-1
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
        print(f"Bucket '{bucket_name}' created successfully in region {region}.")
    except ClientError as e:
        print(f"Error: {e}")

# Call function with a valid bucket name and region
create_bucket("raghavbotobucket11", "us-east-2")
```
#### **Uploading a File to S3**
```python
def upload_object(bucket_name, object_name, file_path):
    s3_client = boto3.client("s3")
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded as '{object_name}' in bucket '{bucket_name}'.")
    except ClientError as e:
        print(f"Error: {e}")
```
<img width="505" alt="create_s3_bucket(boto)" src="https://github.com/user-attachments/assets/c6d8b800-8675-470a-a64a-5b95b020a740" />



<img width="748" alt="console_s3_output" src="https://github.com/user-attachments/assets/9d7731ee-30b4-40fa-8622-09d973d38ad6" />


