## What is AWS SNS? 
AWS Simple Notification Service (SNS) is a fully managed messaging service designed to facilitate communication between publishers and subscribers using different protocols such as SMS, email, HTTP, SQS, and AWS Lambda. It allows users to send notifications or messages to multiple subscribers simultaneously, making it a reliable service for distributing information in real-time.

## Key Features of SNS
**Publish-Subscribe Model**
→ Enables one-to-many messaging. Publishers send messages to SNS topics, and SNS distributes them to all subscribers.

**Multiple Protocols Supported**
→ SNS supports various communication protocols, including:

**Email: Sends notifications via email.**

**SMS: Sends notifications via text message.**

**HTTP/HTTPS: Sends notifications to a web server.**

**AWS Lambda: Triggers a Lambda function.**

**SQS: Delivers messages to an SQS queue.**

**Event-Driven**
→ SNS integrates seamlessly with other AWS services such as S3, EC2, and Lambda, making it ideal for event-driven architectures.

**Scalable & Serverless**
→ Automatically scales to handle high-volume traffic without the need to manage servers or infrastructure.

## How AWS SNS Works
A publisher (can be an AWS service or external source) sends a message to an SNS topic.
The SNS topic distributes the message to all registered subscribers.
Subscribers, based on the chosen protocols (Email, SMS, HTTP, SQS, Lambda), receive the message.

## Creating SNS through CLI
```sh
 aws sns create-topic --name my-sns-cli
 ```

<img width="759" alt="CLI_sns" src="https://github.com/user-attachments/assets/5ec996d0-8d02-47c2-81ee-1f3d7b38c021" />

## 
```sh
aws sns subscribe --topic-arn "arn:aws:sns:us-east-2:597088050492:my-sns-cli" --protocol sms --notification-endpoint "+8722795542"
```

<img width="764" alt="CLI_Subscription" src="https://github.com/user-attachments/assets/1fb9a412-7b63-4589-b296-e1697f423e00" />

## SNS by using python Boto3

```python
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
```
<img width="764" alt="Boto_sns" src="https://github.com/user-attachments/assets/55d3eaf0-05f7-4369-870b-e67fcc356547" />

## subscription_boto

```python
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
```

<img width="787" alt="Boto_Subscription" src="https://github.com/user-attachments/assets/87c89043-7ca4-41b2-b7ac-584b5b133708" />
