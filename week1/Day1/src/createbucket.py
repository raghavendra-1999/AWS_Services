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
