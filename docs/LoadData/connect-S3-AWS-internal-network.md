---
title: "Connecting to Amazon S3 through the AWS internal network"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/connect-S3-AWS-internal-network.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics"]
---

# Connecting to Amazon S3 through the AWS internal network

The underlying infrastructure of Qlik Cloud has an added benefit to customers who connect to Amazon S3 for analytics workloads. All data transferred from Amazon S3 buckets in the same region as a Qlik Cloud tenant traverse through the AWS (Amazon Web Services) internal network. This provides an additional level of security and protection for your data in-transit.

## Connecting to Amazon S3

Connecting to Amazon S3 for analytics workloads requires an Access Key and a Secret Key from AWS to authenticate your connection. When you use an Amazon S3 connector and the S3 bucket is in the same region as your Qlik Cloud tenant, no additional data connection configuration is required to benefit from this change in Qlik Cloud.

## Limitations

Keep in mind the following limitations that apply when connecting data from Amazon S3 to your Qlik Cloud tenant.

- AWS limits connections over its internal network between Amazon S3 and AWS services within the same region. Any network connections between an Amazon S3 bucket in one region, and a Qlik Cloud tenant in a different region, will go through the public Internet. This behavior is the same with AWS PrivateLink.
- Connections that require FIPS compliant support will not work with this capability.
- The Amazon S3 connectors in Qlik Cloud cannot be used with AWS IAM roles to authenticate connectivity.
- The Qlik VPC endpoint configuration is subject to change frequently. Therefore, do not configure a bucket policy scoped to IP addresses, VPC sources, or VPC endpoints as you may experience connectivity disruptions. Qlik is not responsible for connectivity errors related to Amazon S3 bucket policy configurations.

## Validating the Amazon S3 connection

You can validate the internal network connection between an Amazon S3 bucket and your Qlik Cloud tenant using the following AWS options. In both cases, additional AWS charges may apply.

- Turn on Amazon S3 access logs from the AWS console where you configured the S3 bucket. This method will output the source of connection requests.

  [Enabling Amazon S3 server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html)
- Use AWS CloudTrail to access data events and requests made to the Amazon S3 buckets.

  [Logging Amazon S3 API calls using AWS CloudTrail](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-logging.html)

[Logging options for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/logging-with-S3.html)
