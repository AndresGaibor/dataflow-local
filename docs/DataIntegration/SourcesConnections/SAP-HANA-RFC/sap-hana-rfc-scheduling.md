---
title: "Schedule and manage capture jobs"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA-RFC/sap-hana-rfc-scheduling.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP HANA RFC"]
---

# Schedule and manage capture jobs

The SAP scheduler watchdog adjusts capture jobs to the fastest polling interval requested by active subscriptions. SAP enforces the registered table's minimum interval. This SAP-side capture schedule is separate from running a data task in Qlik Talend Data Integration.

Large tables receive dedicated jobs, and smaller tables are batched into shared jobs. For the one-time watchdog startup procedure, see [*SAP Application setup*](sap-hana-rfc-sap-setup.htm).

## Monitor automatic scheduling

A table is eligible for a capture job when it is enabled, active, and has an active subscriber. The watchdog creates or reschedules eligible jobs and removes jobs for tables that are no longer eligible, unless a job is currently running.

Review the watchdog job log in transaction SM37. The log summarizes processed tables, created and rescheduled jobs, and errors. A warning when 20 or more capture jobs are running does not throttle those jobs.

## Manage scheduler options

SAP scheduler fields

| Field | Value or purpose |
| --- | --- |
| Program Name | /QTQVC/CDC\_SCHEDULER |
| Action | Select Schedule (new job) to create the watchdog job. |
| Job Name | /QTQVC/CDC/SCHEDULER |
| Period | How often the watchdog runs. The default is 5 minutes. |
| Execute | Schedule the watchdog using the specified program, job name, and period. |

Keep the watchdog job name and period at the configured values. Do not change the capture-job prefix after setup. SAP locates jobs by their names; renamed jobs are not realigned or cleaned up automatically.
