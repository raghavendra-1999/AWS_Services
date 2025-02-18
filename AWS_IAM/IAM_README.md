<img width="734" alt="Console_output_IAM(boto) (2)" src="https://github.com/user-attachments/assets/30729fb8-5f48-4d29-9068-df57a23a6f01" />
# IAM

AWS IAM (Identity and Access Management) is a service provided by Amazon Web Services (AWS) that helps you manage access to your AWS resources. It's like a security system for your AWS account.

IAM allows you to create and manage users, groups, and roles. Users represent individual people or entities who need access to your AWS resources. Groups are collections of users with similar access requirements, making it easier to manage permissions. Roles are used to grant temporary access to external entities or services.
 
By using AWS IAM, you can effectively manage and secure access to your AWS resources, ensuring that only authorized individuals have appropriate permissions and actions are logged for accountability and compliance purposes.

# Types of IAM Policies:
a) AWS Managed Policies:
Predefined policies created and managed by AWS.
Useful for common permissions across AWS services.
Example: AmazonS3FullAccess, AdministratorAccess.

b) Customer Managed Policies:
Custom policies created by the AWS account owner.
Provides more control and flexibility.

c) AWS Managed Job Function Policy: AWS provides AWS Managed Job Function Policies, which are pre-configured IAM policies designed to align with common job roles in an organization. These policies help assign permissions quickly based on typical responsibilities.

## Components of IAM
- **Users**: IAM users are individual identities with unique credentials used for authentication and access control in AWS.  
- **Groups**: IAM groups are collections of users that share permissions, making access management easier.  
- **Roles**: IAM roles provide temporary access to AWS resources for applications, services, or users.  
- **Policies**: IAM policies are JSON documents that define and control permissions for users, groups, and roles.

  ---
# IAM Configuration using AWS CLI
## 1. Create an IAM User 

```sh
aws iam create-user --user-name raghav_boto_user
```

## 2. Create and Attach an Inline Policy
```sh
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Deny",
			"Action": [
				"s3:GetObject",
				"s3:ListAllMyBuckets",
				"s3:ListBucket"
			],
			"Resource": "*"
		}
	]
}
```
Attach the inline policy to the IAM user:
```sh
aws iam put-user-policy --user-name raghav_iam_cli --policy-name S3ReadOnlyPolicy12 --policy-document file://C:/Users/ragha/Devops_Training/week1/Day1/src/s3_limited_policy.json
```
<img width="724" alt="inlinepolicy_cli" src="https://github.com/user-attachments/assets/1487368b-eb93-4c33-ae51-28de06f1e6b4" />

Verify the policy:
```sh
aws iam list-user-policies --user-name raghav_boto_user
```

## 4. Attach a Standard AWS Managed Policy
Attach the `AmazonS3ReadOnlyAccess` managed policy to the IAM user:

```sh
aws iam attach-user-policy --user-name raghav_boto_user --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```
<img width="722" alt="managed_cli" src="https://github.com/user-attachments/assets/7b725976-3d9c-432a-8b60-cd7ed13e3097" />

## 5. IAM Configuration Using Python (Boto3)
```python
import boto3
import json
# AWS Configuration
AWS_REGION = "us-east-2"
USER_NAME = "raghav_boto3"
INLINE_POLICY_NAME = "S3WriteOnlyPolicy"
MANAGED_POLICY_ARN = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"

# Initialize AWS clients
iam_client = boto3.client("iam", region_name=AWS_REGION)

# Inline policy document
inline_policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": "*"
        }
    ]
}
##  IAM Configuration Using Python (Boto3)
The following Python script automates the IAM user and policy setup using `boto3`:
# Create IAM user
def create_iam_user(user_name):
    try:
        response = iam_client.create_user(UserName=user_name)
        print(f"User '{user_name}' created successfully.")
        return response
    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"User '{user_name}' already exists.")
        return None

# Attach inline policy to IAM user
def attach_inline_policy(user_name, policy_name, policy_document):
    try:
        iam_client.put_user_policy(
            UserName=user_name,
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_document)
        )
        print(f" Inline policy '{policy_name}' attached to user '{user_name}' successfully.")
    except Exception as e:
        print(f"Error attaching inline policy: {e}")

# Attach managed policy to IAM user
def attach_managed_policy(user_name, policy_arn):
    try:
        iam_client.attach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )
        print(f"Managed policy '{policy_arn}' attached to user '{user_name}' successfully.")
    except Exception as e:
        print(f"Error attaching managed policy: {e}")

# Main function
def main():
    create_iam_user(USER_NAME)
    attach_inline_policy(USER_NAME, INLINE_POLICY_NAME, inline_policy_document)
    attach_managed_policy(USER_NAME, MANAGED_POLICY_ARN)

if __name__ == "__main__":
    main()
```
<img width="843" alt="created_iam_user(boto)" src="https://github.com/user-attachments/assets/97c4ba80-7b53-46e7-8aa2-536cd37c9dab" />

<img width="752" alt="console_output_iam(boto)" src="https://github.com/user-attachments/assets/d114f108-7604-4b17-b8b2-63b8c7dd3f8f" />


