---
title: "Management service account"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/gcp-management-service-account.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in GCP"]
---

# Management service account

Create a management service account to enable Qlik Cloud to create and manage the Compute Engine instances and instance groups within your lakehouse environment.

A management service account is a Google Cloud service account that you create to grant Qlik the necessary permissions to interact with your Google Cloud project on your behalf. Qlik impersonates this account during deployment and runtime operations to securely access and manage the Google Cloud resources required for your Iceberg lakehouse.

The account is granted a custom role that defines the specific actions Qlik is authorized to perform, such as creating instance templates and managing instance groups. This ensures secure, least-privilege access while allowing Qlik to automate and orchestrate tasks such as instance provisioning, scaling, and rolling updates.

## Prerequisites

Ensure you have created the VPC network and subnet for hosting your Qlik Open Lakehouse, and you have the following details:

- Your Google Cloud project ID.
- Access to the Configuration guide next to Management service account email in the network integration wizard.

## Creating a management service account

To create a management service account, do the following:

1. In the Google Cloud console, go to IAM & Admin > Service Accounts.
2. Click Create Service Account and configure it:

   - Service account name: Enter a name, for example qlik-lakehouse-management.
   - Description: Optionally, add a description.
3. Click Create and Continue, then Done.
4. Make a note of the service account email. It is formatted as <NAME>@<PROJECT\_ID>.iam.gserviceaccount.com.

## Allowing Qlik to impersonate the account

1. In the Google Cloud console, go to the Service Accounts page and select your project.
2. Click the email address of the service account you created, and select the Permissions tab.
3. In the Principals with access to this service account section, click Grant access.
4. In New principals, enter the principal set shown in the Configuration guide next to Management service account email.
5. Click Select a role, and select the Workload Identity User role (`roles/iam.workloadIdentityUser`).
6. Click Save.

## Creating a role and granting management permissions

1. In the network integration wizard, open the Configuration guide next to Management service account email and copy the management permission list.
2. In the Google Cloud console, go to the Roles page and select your project.
3. Click Create custom role.
4. Enter a Title, for example Qlik Lakehouse Management, and click Add Permissions.
5. Select the permissions you copied, click Add Permissions, and then click Create.
6. Go to the IAM page and select your project.
7. Click Grant Access, and enter the management service account email.
8. Click Select a role, select the role you created, and click Save.

Information noteIf your organization maps permissions to predefined roles instead, ensure the combined roles cover every permission on the list.
