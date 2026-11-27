---
title: "Instances service account"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/gcp-instances-service-account.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in GCP"]
---

# Instances service account

Define a service account for your Qlik-managed Compute Engine instances. This account is used by the instances running in your Google Cloud lakehouse environment.

In Google Cloud, a VM runs as a service account. Applications on the instance obtain short-lived credentials for that account automatically through the instance metadata server. This allows the instance to make authorized API requests to Google Cloud services such as Cloud Storage.

Using a service account attached to the instance improves security and simplifies credential management by:

- Eliminating hard-coded credentials or key files on the instance.
- Automatically rotating credentials.
- Enforcing least privilege through fine-grained roles granted to the account.

## Prerequisites

Ensure you have created the VPC network and subnet for hosting your Qlik Open Lakehouse, and have the following details:

- Your Google Cloud project number.
- The name of the Cloud Storage internal bucket for Qlik to store internal metadata files. For more information, see [*Cloud Storage internal bucket*](gcp-cloud-storage-bucket.htm).
- The management service account email. For more information, see [*Management service account*](gcp-management-service-account.htm).
- Access to the Configuration guide next to Instances service account email in the network integration wizard.

## Creating an instances service account

1. In the Google Cloud console, go to IAM & Admin > Service Accounts.
2. Click Create Service Account and configure it:

   - Service account name: Enter a name, for example qlik-lakehouse-instances.
   - Description: Optionally, add a description.
3. Click Create and Continue, then Done.
4. Make a note of the service account email.

## Allowing the management service account to attach it

1. In the Google Cloud console, go to the Service Accounts page and select your project.
2. Click the email address of the instances service account, and select the Permissions tab.
3. In the Principals with access to this service account section, click Grant access.
4. Enter the management service account email.
5. Click Select a role, and select the Service Account User role (`roles/iam.serviceAccountUser`).
6. Click Save.

## Granting runtime permissions

Create four custom roles, one for each row of the table. The Configuration guide provides the permission list for each role.

| Role | Granted on | Condition |
| --- | --- | --- |
| general | Project | None |
| compute | Project | Instance name starts with qlik- |
| storage | Bucket | None |
| secret | Project | Secret name starts with qlik- |

### Creating the roles

Repeat for each role:

1. In the network integration wizard, open the Configuration guide next to Instances service account email and copy the permission list for the role.
2. In the Google Cloud console, go to the Roles page, select your project, and click Create custom role.
3. Enter a Title, for example Qlik Lakehouse Instances - general, and add the permissions you copied.
4. Click Create.

### Granting the general, compute, and secret roles

Repeat for each role:

1. Go to the IAM page and select your project.
2. Click Grant Access, and enter the instances service account email.
3. Click Select a role, select the role, and click Save.

### Adding the IAM conditions

Repeat for the compute and secret roles:

1. On the IAM page, find the instances service account and click Edit principal.
2. Find the role and click Add IAM condition.
3. Enter the Title from the table below, select the Condition editor tab, and enter the expression. Replace <PROJECT\_NUMBER> with your project number.
4. Click Save, and then click Save in the Edit access panel.

| Role | Title | Expression |
| --- | --- | --- |
| compute | `AllowMetadataOnlyForOlhServerInstances` | `resource.name.extract("/instances/{instance_name}").startsWith("qlik-")` |
| secret | `QlikSecretsAccess` | `resource.name.startsWith("projects/<PROJECT_NUMBER>/secrets/qlik-")` |

### Granting the storage role

1. Go to the Cloud Storage Buckets page, and click the name of the internal bucket.
2. Select the Permissions tab, and click Grant access.
3. Enter the instances service account email, select the storage role, and click Save.

Information noteAlternatively, run the script in the Configuration guide.

Copy the instances service account email and paste it into the Instances service account email field in the wizard.
