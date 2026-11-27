---
title: "Monitoring detailed consumption for capacity-based subscriptions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/usage-metrics-app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Monitoring system and resources", "Monitoring resource consumption"]
---

# Monitoring detailed consumption for capacity-based subscriptions

With the Data Capacity Reporting App, you can monitor how your organization consumes licensed capacity—both at a high level and in detail. The detailed reports help you understand how usage aligns with your subscription entitlements. For example, you can see exactly which reloads, automations, or reports that contributed to the consumption.

Information note

The Data Capacity Reporting App is available with Qlik Cloud capacity-based subscriptions.

## Application content

### Overview sheet

The Overview sheet shows your subscription entitlements and usage. Use it to track current capacity and monthly usage over the past 12 months across all Qlik Cloud value meters.

### Detailed sheets

The application also includes detailed sheets with usage metrics for the current and previous two months. These metrics include:

- Data for Analysis: Total data loaded into or created in Qlik Cloud. Data is counted once, regardless of how many times it is analyzed. This metric is measured monthly based on peak usage compared to purchased capacity. See [*Data for Analysis*](subscription-value-meters.htm#Data) for details.
- Data Moved: Total volume of data moved to cloud destinations, with an unlimited number of sources and targets. Data moved into Qlik Cloud is excluded. Available source types depend on your subscription, while data can be moved to any target type. This metric is measured from the start of each month. See [*Data Moved*](subscription-value-meters.htm#Data2) for details.
- Third Party Transformations: Applies to all datasets that are registered and used in transformations but not delivered by Qlik Talend Data Integration. Measured from the start of each month.
- Open Lakehouse compute: Total quantity of Open Lakehouse compute hours used. Measured from the start of each month. See [*Open Lakehouse compute*](subscription-value-meters.htm#Open) for details.
- Automation Runs: All automation executions using Automations. Measured from the start of each month.
- Reports: Reports distributed using Qlik Reporting Service to other Qlik Cloud Analytics users in your tenant. Measured from the start of each month.

Example of the Data for Analysis sheet in the Data Capacity Reporting App.

![The Data for Analysis sheet in the data capacity reporting app](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_detailed_consumption.png "Click to view full size")

### Talend-specific metrics

If you have a Qlik Talend Cloud subscription, you can also view Talend-specific metrics:

- Job executions: Number of Job task runs.
- Job duration: Total duration of your Job executions.

To track Talend metrics, Qlik Cloud must be linked to Talend Cloud. If unified administration is enabled for your account, the tenants are linked automatically. If it is not enabled yet, you must complete the manual steps in Qlik Cloud and Talend Cloud:

- Configuration instructions: [*Accessing Talend account metadata*](mc-administer-access-talend-metadata.htm)
- Details on Talend metrics: [Monitoring capacity usage by executions with detailed consumption reports](https://help.qlik.com/talend/en-US/management-console-user-guide/cloud/monitoring-operations-executions-with-qlik-cbp-capacity-based-pricing)

## How consumption data is updated

Consumption data is collected continuously as usage occurs. For consumption metering, this data is aggregated every 6 hours based on the timestamp of the system event.

The customer-facing consumption report is updated once per day. The update becomes available at the following times, based on the account region:

- **APAC:** 01:00 UTC
- **EMEA:** 09:00 UTC
- **AMERICAS:** 14:00 UTC

The consumption date is based on the timestamp of the system event in the tenant's regional timezone, not on when the data is aggregated or when the consumption report is updated. For example, usage from an event that occurred on August 16, 2026 at 12:11:10 in the tenant's regional timezone is counted as consumption for August 16, regardless of when the data is aggregated or when the daily report update becomes available.

When a tenant switches to a capacity-based license, consumption data might not be available in the consumption report immediately. You must wait until the next scheduled report update for the data to become available.

## Distributing detailed consumption reports

You must be a tenant administrator with the Private Analytics Content Creator role to distribute detailed consumption reports. The reports are delivered through an application generated from the Administration activity center and stored in your personal space. You can publish the application to any managed space.

To ensure you provide the most recent data, publish a new version of the application every day.

Applications generated previously and stored on your tenant can't be refreshed and aren't updated. You must replace them with newly distributed versions and share those versions again if needed.

Do the following:

1. In the Administration activity center, go to the Settings page.
2. Select the Email and reports tab.
3. In the Detailed consumption reports section, click Distribute.

   ![The Distribute consumption reports setting in the Management Console](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-detailed-consumption-reports.png "Click to view full size")

   The application is now available in your personal space.
