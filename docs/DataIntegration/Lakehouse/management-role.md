---
title: "Management role"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/management-role.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in AWS"]
---

# Management role

Create a management role to enable Qlik Cloud to configure instances and elastic IPs within your lakehouse environment.

A management role is an IAM role that you create to grant Qlik the necessary permissions to interact with your AWS environment on your behalf. This role is assumed by Qlik during deployment and runtime operations to securely access and manage AWS resources required for your Iceberg lakehouse.

The role is associated with a custom IAM policy that defines the specific actions Qlik is authorized to perform—such as reading from and writing to S3 buckets, managing EC2 instances, and interacting with other services like AWS Glue or KMS.

This role ensures secure, least-privilege access while allowing Qlik to automate and orchestrate key tasks such as metadata management, data movement, and job execution within your AWS account.

To function correctly, the role must be created with the required trust relationship and permissions policy as outlined in the setup instructions.

## Prerequisites

Ensure you have created the VPC and subnet and Availability Zones for hosting your Qlik Open Lakehouse, and you have the following details:

- Your AWS account ID.
- The symmetric KMS key ARN.

## Creating a management role

To create a management role, do the following:

1. In the AWS console, go to IAM
2. In Roles, click Create role and configure it:

- Trusted entity type: Select Custom trust policy.

- Statement: In the code pane, paste the Trusted entity policy created in the Management role configuration guide in Qlik Cloud.

3. Create the role and make a note of the ARN value. This should be formatted as follows:

   arn:aws:iam::<ACCOUNT\_ID>:role/<ROLE\_NAME>.

## Creating a policy

1. In IAM, click Roles, and select the role you created above.
2. Click Add permissions.
3. Select Create inline policy.
4. In Policy editor, select JSON. Paste in the following text, and make sure to:

- Change the <AWS\_ACCOUNT\_ID> parameter to your account.
- Update the <KMS\_SYMMETRIC\_KEY\_ARN> value with your key ARN.

```
			{
			"Version": "2012-10-17",
			"Statement": [
			{
			"Effect": "Allow",
			"Resource": [
			"*"
			],
			"Action": [
			"ec2:CancelSpotInstanceRequests",
			"ec2:CreateLaunchTemplate",
			"ec2:CreateTags",
			"ec2:CreateVolume",
			"ec2:DescribeAddresses",
			"ec2:DescribeImageAttribute",
			"ec2:DescribeImages",
			"ec2:DescribeInstanceStatus",
			"ec2:DescribeInstanceTypeOfferings",
			"ec2:DescribeInstanceTypes",
			"ec2:DescribeInstances",
			"ec2:DescribeLaunchTemplateVersions",
			"ec2:DescribeLaunchTemplates",
			"ec2:DescribeSpotInstanceRequests",
			"ec2:DescribeSpotPriceHistory",
			"ec2:DescribeTags",
			"ec2:DescribeRegions",
			"ec2:DescribeSubnets",
			"ec2:DescribeRouteTables",
			"ec2:DescribeSecurityGroups",
			"ec2:RequestSpotInstances",
			"ec2:DescribeVolumes"
			]
			},
			{
			"Effect": "Allow",
			"Resource": [
			"arn:aws:ec2:*::image/*",
			"arn:aws:ec2:*:*:instance/*",
			"arn:aws:ec2:*:*:key-pair/*",
			"arn:aws:ec2:*:*:launch-template/*",
			"arn:aws:ec2:*:*:network-interface/*",
			"arn:aws:ec2:*:*:security-group/*",
			"arn:aws:ec2:*:*:subnet/*",
			"arn:aws:ec2:*:*:volume/*"
			],
			"Action": [
			"ec2:RunInstances"
			]
			},
			{
			"Effect": "Allow",
			"Resource": [
			"*"
			],
			"Action": [
			"ec2:AttachVolume",
			"ec2:DeleteVolume",
			"ec2:DetachVolume",
			"ec2:DeleteLaunchTemplate",
			"ec2:TerminateInstances",
			"ec2:StartInstances",
			"ec2:ModifyLaunchTemplate",
			"ec2:DeleteLaunchTemplateVersions",
			"ec2:CreateLaunchTemplateVersion"
			],
			"Condition": {
			"Null": {
			"aws:ResourceTag/qlik_cluster": "false"
			}
			}
			},
			{
			"Effect": "Allow",
			"Resource": [
			"*"
			],
			"Action": [
			"autoscaling:DeleteAutoScalingGroup",
			"autoscaling:DeletePolicy",
			"autoscaling:DeleteTags",
			"autoscaling:PutScalingPolicy",
			"autoscaling:StartInstanceRefresh",
			"autoscaling:TerminateInstanceInAutoScalingGroup",
			"autoscaling:UpdateAutoScalingGroup"
			],
			"Condition": {
			"Null": {
			"aws:ResourceTag/qlik_cluster": "false"
			}
			}
			},
			{
			"Effect": "Allow",
			"Resource": [
			"*"
			],
			"Action": [
			"autoscaling:CreateAutoScalingGroup",
			"autoscaling:CreateOrUpdateTags",
			"autoscaling:DescribeAutoScalingGroups",
			"autoscaling:DescribeInstanceRefreshes",
			"autoscaling:DescribePolicies",
			"autoscaling:DescribeScalingActivities",
			"autoscaling:DescribeTags"
			]
			},
			{
			"Effect": "Allow",
			"Resource": [
			"*"
			],
			"Action": [
			"ec2:DescribeRegions",
			"ec2:DescribeSubnets",
			"ec2:DescribeRouteTables",
			"ec2:DescribeSecurityGroups",
			"ec2:DescribeKeyPairs"
			]
			},
			{
			"Effect": "Allow",
			"Resource": [
			"*"
			],
			"Action": [
			"cloudwatch:DescribeAlarmHistory",
			"cloudwatch:DescribeAlarms",
			"cloudwatch:DescribeAlarmsForMetric",
			"cloudwatch:GetMetricStatistics",
			"cloudwatch:ListMetrics",
			"cloudwatch:PutMetricData"
			]
			},
			{
			"Effect": "Allow",
			"Resource": [
			"*"
			],
			"Action": [
			"cloudwatch:DeleteAlarms"
			],
			"Condition": {
			"Null": {
			"aws:ResourceTag/qlik_cluster": "false"
			}
			}
			},
			{
			"Effect": "Allow",
			"Resource": [
			"*"
			],
			"Action": [
			"cloudwatch:PutMetricAlarm"
			],
			"Condition": {
			"Null": {
			"aws:RequestTag/qlik_cluster": "false"
			}
			}
			},
			{
			"Effect": "Allow",
			"Resource": [
			"*"
			],
			"Action": [
			"iam:AddRoleToInstanceProfile",
			"iam:CreateServiceLinkedRole",
			"iam:GetPolicy",
			"iam:GetPolicyVersion",
			"iam:ListAccountAliases",
			"iam:ListAttachedRolePolicies",
			"iam:ListInstanceProfiles",
			"iam:ListInstanceProfilesForRole",
			"iam:ListPolicies",
			"iam:ListRoles",
			"iam:PassRole"
			]
			},
			{
			"Effect": "Allow",
			"Resource": [
			"*"
			],
			"Action": [
			"sts:DecodeAuthorizationMessage"
			]
			},
			{
			"Effect": "Allow",
			"Resource": [
			"arn:aws:ssm:*:<AWS_ACCOUNT_ID>:parameter/qlik/*"
				],
				"Action": [
				"ssm:PutParameter"
				]
				},
				{
				"Effect": "Allow",
				"Resource": [
				"<KMS_SYMMETRIC_KEY_ARN>"
					],
					"Action": [
					"kms:GenerateDataKeyPairWithoutPlaintext",
					"kms:Encrypt"
					]
					}
					]
					}

```

## Requirement permission justifications

The following table explains each permission of the management role:

| Policy | Permissions | Explanation |
| --- | --- | --- |
| EC2 - Resource Management Actions | {  "Version": "2012-10-17",  "Statement": [  {  "Action": [  "ec2:CancelSpotInstanceRequests",  "ec2:CreateLaunchTemplate",  "ec2:CreateTags",  "ec2:CreateVolume",  "ec2:DescribeAddresses",  "ec2:DescribeImageAttribute",  "ec2:DescribeImages",  "ec2:DescribeInstanceStatus",  "ec2:DescribeInstanceTypeOfferings",  "ec2:DescribeInstanceTypes",  "ec2:DescribeInstances",  "ec2:DescribeLaunchTemplateVersions",  "ec2:DescribeLaunchTemplates",  "ec2:DescribeSpotInstanceRequests",  "ec2:DescribeSpotPriceHistory",  "ec2:DescribeTags",  "ec2:DescribeRegions",  "ec2:DescribeSubnets",  "ec2:DescribeRouteTables",  "ec2:DescribeSecurityGroups",  "ec2:RequestSpotInstances",  "ec2:DescribeVolumes"  ],  "Effect": "Allow",  "Resource": "\*"  },  {  "Action": "ec2:RunInstances",  "Effect": "Allow",  "Resource": [  "arn:aws:ec2:\*:\*:subnet/\*",  "arn:aws:ec2:\*:\*:network-interface/\*",  "arn:aws:ec2:\*::image/\*"  ]  }  ]  }   ```  ``` | This policy grants Qlik permission to manage EC2 instances and resources, such as volumes, security groups, and subnets. No conditions are included, as all methods are either describe or create actions. |
| EC2 - Resource Manipulation Actions | {  "Version": "2012-10-17",  "Statement": [  {  "Action": [  "ec2:AttachVolume",  "ec2:DeleteVolume",  "ec2:DetachVolume",  "ec2:DeleteLaunchTemplate",  "ec2:TerminateInstances",  "ec2:StartInstances",  "ec2:ModifyLaunchTemplate",  "ec2:DeleteLaunchTemplateVersions",  "ec2:CreateLaunchTemplateVersion"  ],  "Condition": {  "Null": {  "aws:ResourceTag/qlik\_cluster": "false"  }  },  "Effect": "Allow",  "Resource": "\*"  },  {  "Action": [  "autoscaling:PutScalingPolicy",  "autoscaling:UpdateAutoScalingGroup",  "autoscaling:DeleteAutoScalingGroup",  "autoscaling:DeletePolicy",  "autoscaling:DeleteTags",  "autoscaling:StartInstanceRefresh"  ],  "Condition": {  "Null": {  "aws:ResourceTag/qlik\_cluster": "false"  }  },  "Effect": "Allow",  "Resource": "\*"  }  ]  }   ```  ``` | This policy grants Qlik permission to manage the EC2 instances and resources created by Qlik, based on the tag, qlik\_cluster. Permissions include actions such as attaching volumes, terminating instances, and modifying launch templates. |
| EC2 - Validation Actions | {  "Version": "2012-10-17",  "Statement": [  {  "Sid": "VisualEditor0",  "Effect": "Allow",  "Action": [  "ec2:DescribeRegions",  "ec2:DescribeSubnets",  "ec2:DescribeRouteTables",  "ec2:DescribeSecurityGroups",  "ec2:DescribeKeyPairs"  ],  "Resource": "\*"  }  ]  }   ```  ``` | This policy grants Qlik permissions to validate inputs when creating network integrations. The actions are not mandatory and only required when specific inputs are provided. |
| IAM - Instance Profile Actions | {  "Version": "2012-10-17",  "Statement": [  {  "Action": [  "iam:AddRoleToInstanceProfile",  "iam:CreateServiceLinkedRole",  "iam:GetPolicy",  "iam:GetPolicyVersion",  "iam:ListAccountAliases",  "iam:ListAttachedRolePolicies",  "iam:ListInstanceProfiles",  "iam:ListInstanceProfilesForRole",  "iam:ListPolicies",  "iam:ListRoles",  "iam:PassRole"  ],  "Effect": "Allow",  "Resource": "\*"  }  ]  }   ```  ``` | This policy allows the management role to handle EC2 instance profiles, including actions such as creating service-linked roles, and passing roles to EC2 instances. |
| STS - Authorization Action | {  "Version": "2012-10-17",  "Statement": [  {  "Action": "sts:DecodeAuthorizationMessage",  "Effect": "Allow",  "Resource": "\*"  }  ]  }   ```  ``` | This policy grants Qlik permission to decode authorization messages to help troubleshoot authorization issues. |
| SSM - Secret Management Actions | {  "Version": "2012-10-17",  "Statement": [  {  "Action": [  "ssm:PutParameter"  ],  "Effect": "Allow",  "Resource": "arn:aws:ssm:\*:<AWS\_ACCOUNT\_ID>:parameter/qlik/\*",  }  ]  }   ```  ``` | This policy grants the management role permission to store secrets in AWS Systems Manager Parameter Store. These secrets will be read by instances provisioned by Qlik.<AWS\_ACCOUNT\_ID> is a user configured value |
| KMS | {  "Version": "2012-10-17",  "Statement": [  {  "Sid": "VisualEditor0",  "Effect": "Allow",  "Action": [  "kms:GenerateDataKeyPairWithoutPlaintext",  "kms:Encrypt"  ],  "Resource": "<KMS\_SYMMETRIC\_KEY\_ARN>"  }  ]  }   ```  ``` | This policy grants Qlik permission to generate encryption key-pairs without access to the private key, and to encrypt data that will be read and decrypted by machines provisioned by Qlik. <KMS\_SYMMETRIC\_KEY\_ARN> is a user configured value. |
