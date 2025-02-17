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
