---
title: "AWS Kinesis Data Stream"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Connecting-AWS-Kinesis-Data-Stream.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to data streams"]
---

# AWS Kinesis Data Stream

Connect to your Amazon Kinesis service to use as a data source in your Qlik Open Lakehouse projects. Kinesis connections can only be used with the Streaming landing task and the Streaming transform task.

An AWS Kinesis Data Stream is a fully managed service for continuously capturing and processing real-time data streams. In a Qlik Open Lakehouse project, a Kinesis stream can be used as a streaming data source to ingest high-velocity events and records into Apache Iceberg tables. Data read from the stream is processed through the Streaming landing and Streaming transform tasks, enabling near-real-time ingestion, transformation, and storage of streaming data in an open, queryable table format suitable for downstream analytics and consumption. Streams can be split into multiple datasets using a transformation task.

## Prerequisites

To create a connection to your Amazon Kinesis service, you require the following:

- If you are using role-based authentication to access the bucket, you need:

  - Permission to access the network integration you want to use for the connection.
  - The ARN role, or you can create one during the set-up process.

- If you are using access key authentication to access the bucket, you need:

  - Your AWS Access Key ID.
  - Your AWS Secret Access Key.

## Setting Kinesis connection properties

To configure your Kinesis connection, do the following:

1. In Connections, click Create connection.
2. Select the Space where you want to create the connection or choose Create new data space.
3. Select Kinesis from the Connector name list or use the Search box. Ensure the Type is Source and the Category is Streaming.
4. Select the Region where your Kinesis service is hosted.
5. In Authentication type, select how you want to connect, and configure the settings.

### Role-based

Complete the following steps to use role-based authentication.

#### Create ARN role

- Select the Network integration for your connection.
- Enter your ARN role if you already have it.

Information noteClick the link, Click here for guidance, to display the following instructions for creating the ARN role.

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

     Information noteThe code grants the Kinesis connection access to all Kinesis streams across all AWS accounts in the selected region.
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

     Information noteThe code grants the Kinesis connection access to all Kinesis streams across all AWS accounts in the selected region.
2. Attach new policy to a user

   - Attach the new policy to the user you want to provide access to.

### Create the connection

When you have configured your security method, complete the following steps to create your connection:

- In Name, enter the display name for the connection, for example, My Kinesis Streaming Source connection.
- Click Test connection to validate the credentials.
- Click Create.
