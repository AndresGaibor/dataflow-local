---
title: "AWS S3 Data Stream"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Connecting-AWS-S3-Data-Stream.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to data streams"]
---

# AWS S3 Data Stream

Connect to your AWS S3 Data Stream to use as a data source in your Qlik Open Lakehouse projects. AWS S3 Data Stream connections can only be used with the Streaming landing task and the Streaming transform task.

Unlike traditional batch ETL from S3, this implementation treats S3 as a streaming source with continuous monitoring and near real-time data ingestion. You can configure streams to automatically ingest data from S3 buckets as new files arrive. The AWS S3 Data Stream enables you to configure streaming data pipelines from S3, including file pattern matching, schema configuration, and initial backfill options. The stream continuously monitors S3 and ingests new data in near real-time (within minutes) and is ideal for organizational data such as logs, events, exports from external systems, or partner data feeds.

## Prerequisites

To create a connection to your AWS S3 Data Stream, you require the following:

- If you are using role-based authentication to access the bucket, you need:

  - Permission to access the network integration you want to use for the connection.
  - The ARN role, or you can create one during the set-up process. The network integration cluster must have access to the ARN S3 account.

- If you are using access key authentication to connect to the bucket, you need:

  - Your AWS Access Key ID.
  - Your AWS Secret Access Key.

## Setting S3 data stream connection properties

Information noteWhen using this connector to ingest data from Qlik Talend Data Integration, makes sure the bucket name and directory (if provided) are identical to those specified in the Qlik Talend Data Integration Amazon S3 target endpoint.

To configure your S3 connection, do the following:

1. In Connections, click Create connection.
2. Select the Space where you want to create the connection or choose Create new data space.
3. Select S3 from the Connector name list or use the Search box. Ensure the Type is Source and the Category is Streaming.
4. In S3 bucket name, enter the name of your S3 bucket.
5. Optional. In S3 directory, enter the name of a folder in your S3 bucket.
6. In Authentication type, select how you want to connect, and configure the settings.

### Role-based

Complete the following steps to use role-based authentication.

#### Create ARN role

- Network integration: Select the network integration from the list.
- ARN role: Enter the ARN role created in AWS. This should be in the format, arn:aws:iam::{account number}:role/{role name}.

Information noteClick the link, Click here for guidance, to display the following instructions for accessing your trusted entity policy and creating the role ARN.

#### Create an AWS Role

Follow the steps to create an AWS role:

1. Create role

   - In the AWS Console, go to IAM.
   - In Roles, click Create role and configure it:
   - Trusted entity type: Select Custom trust policy.
   - Statement: Copy the Trusted entity policy created in the Create an AWS role  in Qlik Cloud into the code pane in AWS.
   - Create the role.
2. Create inline policy

   - In the AWS Console, in Roles, click the role you created in Step 1.
   - In Permissions policies, click Add permissions > Create inline policy.
   - Copy the code in Qlik Cloud and paste it into the policy in AWS.
3. Copy ARN role

   - From the Roles page in the AWS console, locate the ARN value in the Summary section.
   - Copy the ARN and paste it in ARN role in Qlik Cloud.

### Access key

Complete the following steps to use an access key to authenticate your connection:

- Access key: Enter your unique AWS Access Key ID to use for authentication.
- Secret key: Enter your AWS Secret Access Key to use with your access key.

Information noteClick the link, Click here for guidance, to display the following instructions for creating the policy for the role.

1. Create policy
   - In the AWS Console, go to IAM.
   - Navigate to Policies> Create policy.
   - In Qlik Cloud, in the Create an AWS role dialog, copy the policy.
   - In AWS, in the Policy editor, paste in the policy.
2. Attach new policy to a user

   - Attach the new policy to the user you want to provide access to.

### Create the connection

When you have configured your security method, complete the following steps to create your connection:

- In Name, enter the display name for the connection, for example, My AWS S3 Streaming Source connection.
- Click Test connection to validate the credentials.
- Click Create.

## Syntax examples

| Syntax | Description | Example |
| --- | --- | --- |
| Text | General text/string input based on the AWS Naming Amazon S3 objects guidelines. | s3://MyS3Bucket/MyDir/MyFile.csv |
| Wildcard | An \* character that acts as a "wildcard" in the path/filename. Using a wildcard in a path includes all folders and subfolders from that path. | myS3Bucket/myDir/\*  myS3Bucket/myDir/\*.csv  myS3Bucket/myDir/\*\_customers.csv  myS3Bucket/regions/\*/\*\_customers.csv |
| Pattern | The date pattern syntax indicates the location of the date pattern within the file name. | myS3Bucket/myDir/<yyyy>\_<MM>\_<dd>\_<HH>\_<mm>\_orders.csv  myS3Bucket/myDir/<yyyy>/<MM>/<dd>/<HH>\_<mm>\_orders.csv |

## Target dataset naming rules

The target dataset name must:

- Be unique and not already used by other datasets in the target catalog.
- Comply with the target catalog naming rules:

  - Start with a letter (A–Z, a–z) or underscore (\_).
  - Contain only letters, underscores, digits (0–9), or the dollar sign ($).
  - Not exceed 255 characters, including spaces.
