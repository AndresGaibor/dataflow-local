---
title: "EC2 instance profile"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/ec2-instance-profile.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in AWS"]
---

# EC2 instance profile

Define an IAM role for your Qlik-managed EC2 instances. This role is used by the instances running in your AWS lakehouse environment.

An EC2 instance profile is a container for an IAM role that can be assigned to an EC2 instance. It allows the instance to access AWS services securely without the need to store AWS credentials on the instance.

When an instance is launched with an instance profile, the associated IAM role’s temporary credentials are automatically made available to applications running on the instance via the instance metadata service. This enables the instance to make authorized API requests to AWS services such as Amazon S3, DynamoDB, or CloudWatch.

Using instance profiles improves security and simplifies credential management by:

- Eliminating hard-coded credentials in application code or configuration files.
- Automatically rotating credentials.
- Enforcing least privilege through fine-grained IAM policies attached to the role.

Instance profiles are commonly used in scenarios where EC2 instances need to interact with other AWS resources securely and programmatically.

## Prerequisites

Ensure you have created the VPC and subnet and Availability Zones for hosting your Qlik Open Lakehouse, and have the following details:

- The URL of the S3 bucket for Qlik to store internal metadata files.

## Creating an instance profile

To create a management role, do the following:

1. In the AWS console, go to IAM
2. In Roles, click Create role, and configure it:

- Trusted entity type: Select AWS service from the options.
- Service or use case: Select EC2.
- Use case: Select EC2.

3. Create the role. Return to the Roles page and click the role you created.
4. Click the Copy icon next to the Instance profile ARN name and save this value.
5. Click Add permissions and select Create inline policy.
6. Policy editor: Select JSON. Paste in the following text, and make sure to:

   - Change the <BUCKET\_NAME> parameter to your [*S3 bucket*](s3-bucket.htm).

```
			{
			"Version": "2012-10-17",
			"Statement": [
			{
			"Effect": "Allow",
			"Action": [
			"ec2:AttachVolume",
			"ec2:DetachVolume",
			"autoscaling:SetInstanceHealth"
			],
			"Resource": "*",
			"Condition": {
			"Null": {
			"aws:ResourceTag/qlik_cluster": "false"
			}
			}
			},
			{
			"Effect": "Allow",
			"Action": "cloudwatch:PutMetricData",
			"Resource": "*"
			},
			{
			"Effect": "Allow",
			"Action": [
			"s3:PutObject",
			"s3:GetObject",
			"s3:AbortMultipartUpload",
			"s3:DeleteObjectVersion",
			"s3:ListBucket",
			"s3:DeleteObject",
			"s3:GetObjectVersion"
			],
			"Resource": [
			"arn:aws:s3:::<BUCKET_NAME>",
			"arn:aws:s3:::<BUCKET_NAME>/*"
			]
			},
			{
			"Effect": "Allow",
			"Action": [
			"ssm:GetParameter",
			"ssm:PutParameter"
			],
			"Resource": "arn:aws:ssm:*:*:parameter/qlik/*"
			},
			{
			"Effect": "Allow",
			"Action": "kms:*",
			"Resource": "<SYMMETRIC_KMS_KEY>"
			},
			{
			"Effect": "Allow",
			"Action": "sts:AssumeRole",
			"Resource": "*",
			"Condition": {
			"StringEquals": {
			"sts:ExternalId": "6b69f9c3c8f502f2ddfc8434d443f172ebe4c032f4ef1a3c51215d27a58ca799"
			}
			}
			}
			]
			}

```

## Requirement permission justifications

The following table explains each permission granted to the EC2 instance:

| Policy | Permissions | Explanation |
| --- | --- | --- |
| Attach Volume Policy | {  "Version": "2012-10-17",  "Effect": "Allow",  "Resource": [  "\*"  ],  "Action": [  "ec2:AttachVolume",  "ec2:DetachVolume",  "autoscaling:SetInstanceHealth"  ],  "Condition": {  "Null": {  "aws:ResourceTag/qlik\_cluster": "false"  }  }  }  ]  }   ```  ``` | This policy grants EC2 instances permissions to attach Persistent EBS volumes created by Qlik. This allows data to persist between Gateway machine upgrades. |
| CloudWatch | {  "Version": "2012-10-17",  "Effect": "Allow",  "Resource": [  "\*"  ],  "Action": [  "cloudwatch:PutMetricData"  }  ]  }   ```  ``` | This policy allows EC2 instances to push custom metrics to CloudWatch, which are used to auto-scale Qlik clusters based on software performance. |
| Internal Bucket | {  "Version": "2012-10-17",  "Effect": "Allow",  "Resource": [  "arn:aws:s3:::<BUCKET\_NAME>",  "arn:aws:s3:::<BUCKET\_NAME>/\*"  ],  "Action": [  "s3:PutObject",  "s3:GetObject",  "s3:AbortMultipartUpload",  "s3:DeleteObjectVersion",  "s3:ListBucket",  "s3:DeleteObject",  "s3:GetObjectVersion"  ]  }  ]  }   ```  ``` | The policy allows EC2 instances permissions to store, read, and delete internal data. The internal data contains real user data that is held in intermediate storage for processing. <BUCKET\_NAME> is a user configured value. |
