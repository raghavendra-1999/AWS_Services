import boto3

# Create an SNS client
sns = boto3.client("sns", region_name="us-east-2")  # Change region if needed

# Define a topic name
topic_name = "sns_by_python"

# Create the SNS topic
response = sns.create_topic(Name=topic_name)

# Get the topic ARN
topic_arn = response["TopicArn"]
print(f"SNS Topic Created: {topic_arn}")
