import boto3
import os
from botocore.exceptions import ClientError

def upload_object(bucket_name, object_name, file_path):
    s3_client = boto3.client("s3")

    # Check if the file exists before uploading
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded as '{object_name}' in bucket '{bucket_name}'.")
    except ClientError as e:
        print(f"Error: {e}")


# Call function with correct path
upload_object("raghavbotobucket1", "uploaded_file.txt", r"C:/Users/ragha/OneDrive/Desktop/AWS_IAM/index")
