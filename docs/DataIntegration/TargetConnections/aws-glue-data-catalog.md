---
title: "AWS Glue Data Catalog"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/aws-glue-data-catalog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Set up connections to data catalogs"]
---

# AWS Glue Data Catalog

Connect to your AWS Glue Data Catalog to use as a target in your Qlik Open Lakehouse projects.

Using AWS Glue Data Catalog as the target provides integration with the AWS analytics ecosystem and enables Qlik Open Lakehouse to interoperate with a centralized metadata store. AWS Glue Data Catalog acts as the unified metadata layer, allowing Qlik to write Iceberg tables that are immediately queryable by AWS-native services such as Amazon Athena, without additional configuration. Data written by Qlik is also available to third-party tools without replication.

## Prerequisites

To create an AWS Glue Data Catalog connection, you need:

- An Amazon S3 target bucket.
- If you are using role-based authentication to access the bucket, you need:

  - Permission to access the network integration you want to use for the connection.
  - The role ARN.
- If you are using access key authentication to access the bucket, you need:

  - Your AWS Access Key ID.
  - Your AWS Secret Access Key.

## Setting AWS Glue Data Catalog connection properties

To configure the connection, do the following:

1. In Connections, click Create connection.
2. Select the Space where you want to create the connection, or choose Create new data space.
3. Select AWS Glue Data Catalog from the Connector name list or use the Search box.
4. Click Create, and configure the properties:

- Catalog region: From the list, select the region for your catalog.
- S3 target bucket: Enter the name of the bucket.

5. Configure the Authentication type. From the list, select Role-based or Access key authentication and complete the following information for your selection:

### Role-based

- Network integration: Select the network integration from the list.
- ARN role: Enter the ARN role created in AWS.

Information noteClick the link, Click here for guidance, to display the following instructions for accessing your trusted entity policy and creating the role ARN.

#### Create an AWS role

To create an AWS role, do the following:

1. In the AWS Console, go to IAM.
2. In Roles, click Create role.
3. For Trusted entity type, select Custom trust policy.
4. In Qlik Cloud, in the Create an AWS role dialog, copy the Trusted entity, which is the entity assigned to the clusters in your integration. Paste it into the console in AWS.
5. Click Roles, and select the role you created above.
6. In Permission policies, click Add permissions, and select Create inline policy.
7. In Qlik Cloud, in the Create an AWS role dialog, copy the inline policy below, and paste it into the console in AWS, and change the <bucket\_name> value to your bucket location:

```
						{
						"Version": "2012-10-17",
						"Statement": [
						{
						"Effect": "Allow",
						"Action": [
						"glue:CreateTable",
						"glue:UpdateTable",
						"glue:DeleteTable",
						"glue:BatchDeleteTable",
						"glue:GetTable",
						"glue:GetTables",
						"glue:CreateDatabase",
						"glue:UpdateDatabase",
						"glue:GetDatabase",
						"glue:GetDatabases",
						"glue:GetUserDefinedFunction"
						],
						"Resource": [
						"arn:aws:glue:us-east-2:*:catalog",
						"arn:aws:glue:us-east-2:*:database/*",
						"arn:aws:glue:us-east-2:*:table/*/*"
						]
						},
						{
						"Effect": "Allow",
						"Action": [
						"s3:ListBucket",
						"s3:GetBucketLocation"
						],
						"Resource": "arn:aws:s3:::<bucket_name>"
							},
							{
							"Effect": "Allow",
							"Action": [
							"s3:PutObject",
							"s3:DeleteObject",
							"s3:DeleteObjectVersion",
							"s3:GetObject",
							"s3:GetObjectVersion"
							],
							"Resource": "arn:aws:s3:::<bucket_name>/*"
								}
								]
								}
```

8. From the Role page, in Summary, copy the ARN.
9. In Qlik Cloud, close the Create an AWS role dialog, and paste the ARN value into ARN role.

### Access key

- Access key: Enter your unique AWS Access Key ID to use for authentication.
- Secret key: Enter your AWS Secret Access Key to use with your access key.

Information noteClick the link, Click here for guidance, to display the following instructions for creating the inline policy for the role.

#### Define user permissions

To create an inline policy in AWS, do the following:

1. In the AWS Console, go to IAM.
2. Navigate to Policies > Create policy.
3. In Qlik Cloud, in the Create an AWS role dialog, copy the policy.
4. In AWS, in the Policy editor, paste in the policy, and change the <bucket\_name> parameter to your bucket location:

```
						{
						"Version": "2012-10-17",
						"Statement": [
						{
						"Effect": "Allow",
						"Action": [
						"glue:CreateTable",
						"glue:UpdateTable",
						"glue:DeleteTable",
						"glue:BatchDeleteTable",
						"glue:GetTable",
						"glue:GetTables",
						"glue:CreateDatabase",
						"glue:UpdateDatabase",
						"glue:GetDatabase",
						"glue:GetDatabases",
						"glue:GetUserDefinedFunction"
						],
						"Resource": [
						"arn:aws:glue:us-east-2:*:catalog",
						"arn:aws:glue:us-east-2:*:database/*",
						"arn:aws:glue:us-east-2:*:table/*/*"
						]
						},
						{
						"Effect": "Allow",
						"Action": [
						"s3:ListBucket",
						"s3:GetBucketLocation"
						],
						"Resource": "arn:aws:s3:::<bucket_name>"
						},
						{
						"Effect": "Allow",
						"Action": [
						"s3:PutObject",
						"s3:DeleteObject",
						"s3:DeleteObjectVersion",
						"s3:GetObject",
						"s3:GetObjectVersion"
						],
						"Resource": "arn:aws:s3:::<bucket_name>/*"
						}
						]
						}

```

5. Add the policy to the user that gives access to Qlik.

In Name, enter the display name for the connection.

## Supported data types

The table below shows the supported Iceberg source data types and their default mapping to Qlik Talend Data Integration data types.

| Qlik Talend Data Integration data types | Iceberg data types |
| --- | --- |
| BOOLEAN | BOOLEAN |
| BYTES | FIXED |
| DATE | DATE |
| TIME | TIME |
| DATETIME | TIMESTAMP |
| INT1 | INT |
| INT2 | INT |
| INT4 | INT |
| INT8 | LONG |
| NUMERIC | DECIMAL(precision, scale) |
| REAL4 | FLOAT |
| REAL8 | DOUBLE |
| UINT1 | INT |
| UINT2 | LONG |
| UINT4 | LONG |
| UINT8 | DECIMAL(20, 0) |
| STRING | STRING |
| WSTRING | STRING |
| BLOB | BINARY |
| NCLOB | STRING |
| CLOB | STRING |
