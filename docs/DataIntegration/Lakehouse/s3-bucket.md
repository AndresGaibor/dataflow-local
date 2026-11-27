---
title: "S3 bucket"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/s3-bucket.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in AWS"]
---

# S3 bucket

The metadata definitions, configurations, and intermediate data for managing your Iceberg lakehouse are stored in a designated Amazon S3 bucket.

An Amazon S3 bucket is a cloud-based container used to store and organize data in the form of objects. Buckets provide scalable, durable, and highly available storage for a wide range of use cases.

In Qlik Open Lakehouse architecture, an S3 bucket stores the metadata object definitions, configuration files, and intermediate data necessary for managing your Iceberg-based lakehouse. This bucket serves as the central storage location that supports core operations such as data cataloging, versioning, and job execution.

To ensure consistent functionality, the S3 bucket must be created and accessible in the same AWS region as your lakehouse resources.

## Prerequisites

Ensure you have created the VPC and subnet and Availability Zones for hosting your Qlik Open Lakehouse.

## Creating an S3 bucket

To create an S3 bucket, do the following:

1. In the AWS console, go to S3, and click Buckets.
2. In General purpose buckets, click Create bucket and configure it:

- Bucket type: Ensure General purpose is selected.
- Bucket name: Provide a name for your bucket, for example, qlik-open-lakehouse-bucket.

3. Create the bucket and make a note of the bucket name.
