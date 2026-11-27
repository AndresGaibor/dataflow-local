---
title: "SAP Application setup"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA-RFC/sap-hana-rfc-sap-setup.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP HANA RFC"]
---

# SAP Application setup

An SAP admin installs the ABAP package, registers each table for capture, and starts the scheduler before the tables can be used in a data task.

## Install the ABAP package

Install the Qlik-delivered package on the SAP system. It runs in its registered QTQVC namespace. Follow the SAP add-on installation procedure in [*Prerequisites*](sap-hana-rfc-prereq.htm).

## Capture data objects

The add-on maintains source capture metadata, snapshots, and changelogs independently of the Cloud target datasets.

SAP-side capture objects

| Object | Purpose |
| --- | --- |
| CDC\_REG | Registered tables, enabled state, and status. |
| CDC\_SUB | Subscriber watermarks, polling intervals, and retention. The minimum consumed watermark across subscribers determines the cleanup boundary. |
| CDC\_AMDP | Primary-key columns and snapshot pair names for each table. |
| CDC\_FCAT | Cached column types, lengths, and key flags. |
| CDC\_CFG | Global minimum polling interval, maximum retention, and parallelism limits. |
| CDC\_RLOG | Changed row counts, anomalies, and errors for capture cycles. |
| CDC\_DIDX | Index of tables with changes in each capture cycle. |
| SNAP\_<table\_id>\_ID1 and SNAP\_<table\_id>\_ID2 | Primary-key and row-ID snapshots for comparison. |
| CDC\_CLOG\_<table\_id> | Source-column values, operation, and timestamp for each captured change. |

## Register a table

1. Run transaction /QTQVC/HRFC\_COCKPIT to open the SAP HANA RFC Endpoint Cockpit.
2. Click Register and enter the SAP table name in Table ID.
3. Select CDC Enabled.
4. Set Poll Interval (Min.), the lowest allowed change-generation interval for this table.
5. Set Retention Per (Hrs), the number of hours to keep change records before cleanup.
6. Click Save.

A registered table remains PAUSED until a data task subscribes to it. Only registered and enabled tables appear in the source table selector.

SAP pauses capture if no task requests changes for a table for a while. Capture resumes automatically when a task subscribes again.

Use Global Setting for the system-wide limits. ReBaseLine forces a fresh snapshot baseline. Coordinate a baseline reset with the data task owner before changing capture state.

Information note

The SAP admin's global settings establish the minimum polling interval, maximum retention, and parallelism ceiling. SAP applies these limits. When SAP adjusts a requested polling interval or retention value, the task log records a warning.

## Start the scheduler

Start the scheduler watchdog once. It then realigns the capture jobs to the fastest polling interval requested by active subscriptions.

1. Run transaction /QTQVC/HRFC\_COCKPIT to open the SAP HANA RFC Endpoint Cockpit.
2. Click the Schedule Job button.
3. Set Program Name to /QTQVC/CDC\_SCHEDULER.
4. Set Action to Schedule (new job).
5. Set Job Name to /QTQVC/CDC/SCHEDULER.
6. Set Period. The default is 5 minutes.
7. Click Execute.

Do not rename the watchdog job or change the capture job prefix after setup. The scheduler finds jobs by their current names. A renamed job is not realigned or cleaned up automatically.

## Schedule the housekeeping job

Schedule the housekeeping job to remove processed changelog entries from the changelog tables based on retention time.

1. Run transaction /QTQVC/HRFC\_COCKPIT to open the SAP HANA RFC Endpoint Cockpit.
2. Click the Schedule Job button.
3. Set Program Name to /QTQVC/CDC\_HOUSEKEEPING.
4. Set Action to Schedule (new job).
5. Set Job Name to /QTQVC/CDC\_HOUSEKEEPING.
6. Set Period. The default is 1440 minutes (1 day).
7. Click Execute.

For capture-job controls and job logs, see [*Schedule and manage capture jobs*](sap-hana-rfc-scheduling.htm). To investigate subscriptions, see [*Monitor and operate CDC*](sap-hana-rfc-operations.htm).
