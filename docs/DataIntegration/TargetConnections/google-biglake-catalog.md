---
title: "Google Lakehouse runtime catalog"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/google-biglake-catalog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Set up connections to data catalogs"]
---

# Google Lakehouse runtime catalog

Connect to a Google Lakehouse runtime catalog to use as a target in your Qlik Open Lakehouse projects.

Using Google Lakehouse runtime catalog as the target provides integration with the Google Cloud analytics ecosystem and enables Qlik Open Lakehouse to interoperate with a unified metadata layer. Google Lakehouse runtime catalog acts as the centralized catalog, allowing Qlik to write Apache Iceberg tables that are immediately queryable by Google Cloud services such as BigQuery, without additional configuration. Data written by Qlik is also available to third-party tools that support the Iceberg REST catalog protocol without replication.

## Prerequisites

To create a Google Lakehouse runtime catalog connection, you need:

- A Google Cloud Platform (GCP) project with BigLake enabled.
- A Google Cloud Storage (GCS) bucket to store your Iceberg table data.
- If you are using **Service Account Impersonation** authentication, you need:

  - Permission to access the network integration you want to use. For details on the required permissions, see the guidance provided during configuration.
  - The service account email.
- If you are using **Service Account Key** authentication, you need a JSON service account key file.

**Security note:** Service account keys are sensitive credentials. If using Service Account Key authentication, follow Google Cloud best practices for key rotation and secure storage.

### Catalog service account permissions

Grant the catalog service account the following permissions:

- `biglake.catalogs.get`.
- `biglake.namespaces.list`, `biglake.namespaces.get`, and `biglake.namespaces.create`.
- `biglake.tables.list`, `biglake.tables.get`, `biglake.tables.create`, `biglake.tables.update`, and `biglake.tables.delete`.
- `storage.buckets.get`, `storage.objects.get`, `storage.objects.list`, `storage.objects.create`, and `storage.objects.delete`.
- `storage.multipartUploads.create`, `storage.multipartUploads.abort`, and `serviceusage.services.use`.

Restrict Cloud Storage permissions to the target bucket where possible.

## Setting Google Lakehouse runtime catalog connection properties

To configure the connection, do the following:

1. In Connections, click Create connection.
2. Select the Space where you want to create the connection, or choose Create new data space. The default is your Personal space.
3. Select Google Lakehouse runtime catalog (BigLake metastore) from the Connector name list or use the Search box.
4. Click Create, and configure the properties:

   - Cloud Storage Target Bucket: Enter the GCS bucket name without the `gs://` prefix. This is where your Iceberg table data will be stored.
5. For Authentication Type, select from the dropdown list:

   - Service Account Impersonation (recommended for production environments)
   - Service Account Key
6. Complete the authentication configuration for your selection (see [Service Account Impersonation](#ServiceAccountImpersonation) or [Service Account Key](#ServiceAccountKey) below).
7. In Connection Name, enter a display name for the connection.
8. Click Test connection to verify the configuration. If successful, the connection is validated. If it fails, review the error message and correct any configuration issues.
9. Click Create to save the connection. To discard changes, click Cancel.

### Service Account Impersonation

Service Account Impersonation uses a network integration to authenticate without exposing service account keys. This method is recommended for production environments.

Network Integration: Select the network integration from the list. The connection dialog displays its Compute Cluster trusted identity.

On the catalog service account's Permissions tab, grant the Compute Cluster trusted identity the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`). This allows the compute cluster to impersonate the catalog service account.

Service Account Email: Enter the email address of the catalog service account, in the format `service-account@project-id.iam.gserviceaccount.com`.

For instructions on creating a GCP service account and configuring impersonation, click the Click here for guidance hyperlink.

### Service Account Key

Service Account Key authentication uses a JSON key file downloaded from GCP. This method is suitable for non-production environments or when network integration is not available.

Service Account Key (JSON file): Upload the JSON file containing your service account credentials. Download this file when you create the service account key in the GCP Console.

**Security best practice:** Store the JSON key file securely and rotate keys regularly. Delete old keys from the GCP Console after uploading to avoid unauthorized access.

For instructions on creating a GCP service account and downloading a key, click the Click here for guidance hyperlink.

## Next steps

- [Create a data project](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Data-projects.htm)
- [Design your data pipeline](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Designing-data-pipeline.htm)
- [*Step 1: Create a network integration*](../Lakehouse/network-integration.htm)
