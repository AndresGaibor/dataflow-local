---
title: "Cloud Storage internal bucket"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/gcp-cloud-storage-bucket.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in GCP"]
---

# Cloud Storage internal bucket

The metadata definitions, configurations, and intermediate data for managing your Iceberg lakehouse are stored in a designated Cloud Storage bucket.

A Cloud Storage bucket is a cloud-based container used to store and organize data in the form of objects. Buckets provide scalable, durable, and highly available storage for a wide range of use cases.

In Qlik Open Lakehouse architecture, this bucket stores the metadata object definitions, configuration files, and intermediate data necessary for managing your Iceberg-based lakehouse. It serves as the central storage location that supports core operations such as data cataloging, versioning, and job execution.

To ensure consistent functionality, the bucket must be created in the same region as your lakehouse resources.

## Prerequisites

Ensure you have created the VPC network and subnet for hosting your Qlik Open Lakehouse. For more information, see [*VPC network and subnet*](gcp-vpc-network-subnet.htm).

## Creating a Cloud Storage bucket

To create a Cloud Storage bucket, do the following:

1. In the Google Cloud console, go to the Cloud Storage Buckets page.
2. Click Create.
3. On the Create a bucket page, configure the bucket, clicking Continue after each section:

   - Get started: Enter a globally unique name for your bucket, for example, qlik-open-lakehouse-bucket.
   - Choose where to store your data: For Location type, select Region, and for Location, select the same region as your subnet.
4. Click Create and make a note of the bucket name.
