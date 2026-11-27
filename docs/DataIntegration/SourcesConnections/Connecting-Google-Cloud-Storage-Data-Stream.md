---
title: "Google Cloud Storage Data Stream"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Connecting-Google-Cloud-Storage-Data-Stream.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to data streams"]
---

# Google Cloud Storage Data Stream

Connect a Google Cloud Storage bucket as a streaming source in your Qlik Open Lakehouse project. Use this connection with the Streaming landing task and Streaming Transform task.

## Prerequisites

To create a connection, you need:

- A Google Cloud Storage bucket that contains the files to ingest.
- A Google Cloud service account with permission to list the bucket and read and delete its objects.
- A network integration configured for the compute cluster if you use service account impersonation.

## Set connection properties

To create a Google Cloud Storage Data Stream connection, do the following:

1. In Connections, click Create connection.
2. Select the Space where you want to create the connection, or create a new data space.
3. Select Google Cloud Storage Data Stream from the Connector list.
4. In GCS bucket, enter the bucket name.
5. Optionally, in GCS directory, enter a directory or prefix in the bucket. Leave this field blank to use the entire bucket.
6. In Authentication type, select Service Account Impersonation or Service Account Key, then configure the authentication details.

### Service Account Impersonation

1. For Network integration, select the network integration configured for your compute cluster.
2. In Service account email, enter the email address of the Google Cloud service account.
3. Grant the trusted identity shown in the connection guide the Service Account Token Creator role on this service account.

### Service Account Key

Upload the JSON key file for the Google Cloud service account.

The service account must have the following permissions:

- `storage.buckets.get`
- `storage.objects.delete`
- `storage.objects.get`
- `storage.objects.list`

### Create the connection

1. In Name, enter a name for the connection.
2. Click Test connection to validate the connection.
3. Click Create.
