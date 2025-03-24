import boto3

# Create an SNS client
sns = boto3.client("sns", region_name="us-east-2")  # Changed region to us-east-2

# Replace with the ARN of your SNS topic
topic_arn = "arn:aws:sns:us-east-2:597088050492:sns_by_python"  # Updated ARN

# Replace with the email or phone number you want to subscribe
protocol = "email"  # Change to "sms" for phone numbers
endpoint = "ryerramsetty@govst.edu"  # Change this to the recipient's email or phone number

# Subscribe to the topic
response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol=protocol,
    Endpoint=endpoint
)

# Print the subscription ARN
print("Subscription ARN:", response["SubscriptionArn"])
