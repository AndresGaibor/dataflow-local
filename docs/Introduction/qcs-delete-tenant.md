---
title: "Deleting a Qlik Cloud tenant"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qcs-delete-tenant.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing your Qlik Cloud subscription"]
---

# Deleting a Qlik Cloud tenant

This article explains how Qlik handles deletion of Qlik Cloud tenants. Tenants are automatically deleted when trials, evaluations or paid subscriptions expire, but you can also request tenant deletion if you are the service account owner (SAO) of the subscription. You can view the expiration date of your subscription within My Qlik.

Qlik Cloud has different classifications for tenants depending on how tenant creation was requested. The three types of tenants discussed on this page are:

- Trial tenants

  You have a trial tenant if you completed a form on [Qlik.com](https://www.qlik.com/) to try Qlik Cloud.
- Evaluation tenants

  You have an evaluation tenant if you are working with the Qlik sales team, and they have issued a Qlik Cloud tenant for your review.
- Paid subscriptions

  For more information about Qlik Cloud paid subscription options, see [*Qlik Cloud capacity-based subscriptions*](../Admin/subscription-options-qlik-cloud.htm).

These timelines apply to Qlik Cloud and Qlik Talend Cloud tenants. They do not apply to Talend Cloud-only tenants. For the separate lifecycle for Talend Cloud-only tenants in Azure, see [Talend-only tenant lifecycle](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/tmc-account-license-info).

## Retrieving your data

You should always try to retrieve the data from a tenant before the trial, evaluation, or paid subscription expires. Upon expiration, you have 30 days during which you can still retrieve, or delete, any content from the tenant before it is set to a disabled state. The 30-day period cannot be extended.

## Requesting deletion of a tenant

You can request deletion of a tenant prior to the expiration date. The timeline for tenant deletion begins when you confirm the decision to delete the tenant.

- Trial tenants and evaluation tenants

  You can request deletion before the expiration date in the Administration [activity center](#glossary-0 "Glossary term"), on the Tenant tab of the Settings page.
- Paid subscription tenants

  If you have a paid subscription, the service account owner of the tenant can request tenant deletion prior to the expiration date by contacting Qlik Customer Support. Qlik Customer Support will activate a capability enabling you to perform the tenant deletion process.

Timeline for requested deletion of a tenant

| Timeline | Tenant status |
| --- | --- |
| Day 0 | The tenant is disabled. All data is intact but no longer accessible. |
| Day 30 | The tenant is deleted. |
| Day 60 | Tenant backups are deleted. |

## Automatic deletion of a tenant with expired license

When your trial license or evaluation license has expired, the tenant, and all data stored on the tenant, will automatically move through the following steps. The timelines are different for paid subscription tenants and trial or evaluation tenants.

### Deleting a trial or evaluation tenant

Timeline for deletion of a trial tenant or an evaluation tenant with expired license

| Timeline | Tenant status |
| --- | --- |
| Day 0-30 | You have full access to download or delete all data in the tenant. |
| Day 30 | The tenant is disabled. All data is intact but no longer accessible. |
| Day 60 | The tenant is deleted. |
| Day 90 | Tenant backups are deleted. |

### Deleting a paid subscription tenant

Timeline for deletion of a paid subscription tenant with expired license

| Timeline | Tenant status |
| --- | --- |
| Day 0-30 | You have full access to download or delete all data in the tenant. |
| Day 30 | The tenant is disabled. All data is intact but no longer accessible. |
| Day 180 | The tenant is deleted. |
| Day 210 | Tenant backups are deleted. |

## Requesting tenant reactivation

You can reactivate a Qlik Cloud tenant that was requested to be deleted, or where the license expired. The service account owner must contact Qlik Customer Support to reactivate the tenant within the following timelines:

- Trial tenants and evaluation tenants

  If deletion was requested: Within 30 days of activating the tenant deletion process.

  If the license expired: Within 60 days of license expiration.
- Paid subscription tenants

  If deletion was requested: Within 30 days of activating the tenant deletion process.

  If the license expired: Within 180 days of license expiration.

## OEM tenant deletion

Tenants created with an OEM subscription may initiate tenant deletion using the tenant deletion API. The API permits scheduling the date a tenant will be deleted. The specified deletion date must be between 10 days and 90 days from the date the API request is made.

Tenants scheduled for deletion using the API will be disabled for a minimum of 10 days, so that the tenant can be reactivated if it was disabled prematurely.

As with non-OEM subscriptions, tenant backups will be deleted 30 days after the tenant has been deleted.
