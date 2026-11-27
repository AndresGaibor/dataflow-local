---
title: "Intacct"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Intacct.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Intacct

Intacct is a cloud-based financial management and accounting solution.

Intacct integration relies on Intacct’s [Data Delivery Service (DDS)](https://developer.intacct.com/data-delivery-service/) for Amazon S3. Intacct DDS exports reports in CSV format to Amazon S3.

This integration does not use the Intacct API.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up the connection, ensure you have the following:

- An active subscription to Intacct’s Data Delivery Service (DDS). Integration with Intacct does not interact with the Intacct REST API; instead, it relies on DDS to publish CSV data to an AWS S3 bucket, from which the data is then consumed. For more information, see [Data Delivery Service](https://developer.intacct.com/data-delivery-service/).
- Sufficient permissions in AWS Identity and Access Management (IAM) to create policies, roles, and attach policies to roles. These permissions are required to authorize Qlik Talend Cloud to access your S3 bucket and to read and extract data published to the bucket.

To configure your Amazon S3 access:

1. Log into your Amazon Web Services account.
2. Navigate to the Amazon S3 bucket you want to use as the Cloud Storage Target for Intacct.
3. Enable Intacct to access the AWS S3 buckets by following [Intacct's documentation](https://www.intacct.com/ia/docs/en_US/help_action/Reporting/Distribute_and_run_reports/Store_reports/cloud-storage-for-reports.htm?cshid=Setting_up_cloud_storage#HowtosetupasupportedCloudStoragetarget).

To configure your Automatic Data Delivery Service:

1. In your Intacct account, navigate to Company > Data Delivery Service > Automatic.
2. Click Add.
3. In the File attributes section, define the settings as follows:
   - Delimiter: Commas
   - Text qualifier (delimiter): Double quote (")
   - Encryption: Do not encrypt
4. In the Delivery options section, define the settings as follows:
   - Cloud storage destination: Select the Amazon S3 Cloud Storage Target you created.
   - Frequency: Select the frequency you want to use to trigger a data export in Intacct.
5. In the Objects section, select the objects you want to include in the export.
6. Save the schedule.

To retrieve your company ID:

1. Log into your Intacct account.
2. Navigate to Company > Setup > Company > General Information tab.
3. Find your Company ID under Company Information.
4. Copy and paste your company ID into a secured file.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Fill in the required connection properties.
2. Provide a name for the connection in Connection name.
3. Select Open connection metadata to define metadata for the connection when it has been created.
4. Click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Company ID | Company ID. |
| S3 Bucket | Name of the S3 bucket. |
| AWS Account ID | AWS Account ID that owns the S3 bucket containing the DDS CSV files published by Intacct. |
| Path (optional) | Path configured in Intacct for use in the S3 bucket. |
