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

## 3. Create and Attach an Inline Policy
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
  aws iam put-user-policy --user-name raghav_boto_user --policy-name s3_limited_policy --policy-document file://s3_limited_policy.json
```

Verify the policy:

```sh
aws iam list-user-policies --user-name raghav_boto_user
```
