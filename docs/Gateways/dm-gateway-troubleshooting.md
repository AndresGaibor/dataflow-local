---
title: "Troubleshooting Data Movement gateway"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/dm-gateway-troubleshooting.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Qlik Data Gateway - Data Movement"]
---

# Troubleshooting Data Movement gateway

This section describes various actions you can perform to troubleshoot Data Movement gateway.

## Viewing and downloading log files

The log files provide information about Data Movement gateway operations. Qlik Support might ask you to provide log files for troubleshooting purposes. You can view or download the log files in the Log viewer. Under normal circumstances, there is no reason to examine the log files, but if you experience repeated failures or other issues, the log files will often help pinpoint the cause.

Information noteViewing and downloading the logs requires the Can consume data role.

To open the Log viewer:

1. Select Administration from the launcher menu (![Launcher Menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then Data gateways.
2. Locate your Data Movement gateway. Then, from the ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu at the end of the row, select View logs.

   The Log viewer window opens.
3. From the drop-down list in the top left, choose the type of log that Qlik Support has asked you to view or download.

   The following log types are available:

   - Data Movement gateway logs (repagent) - General events related to the Data Movement gateway services
   - Replication engine logs (repsrv) - Events related to data movement
   - Source connection logs (rependsrv) - Events related to SAP Extractor and SaaS application data sources
   - SaaS application logs (ex-data-provider-agent) - Events related to SaaS applications data sources
   - ELT engine logs (qdi-db-commands-local-agent) - ELT operations on the target including data registration, storage, transformations, and data marts
   - AI local agent - Events related to the knowledge marts
4. From the adjacent drop-down list, select the log you want to view or download. The log files are ordered from the newest (the currently active log file) to the oldest. After you select a log file, you can use the ![Arrow to scroll to the top](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_up_stop.svg) and ![Arrow to scroll to the bottom](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down_stop.svg) buttons to jump to the start or end of the log file respectively.

   Tip noteThe view of the log file is not updated automatically with the latest messages. To update the view, click ![Arrow to scroll to the bottom](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down_stop.svg) to jump to the end of the log file, which will be updated with the latest messages.
5. To download the log file, click Download.

   The file will either be downloaded to your computer or you will be prompted to save it, depending on your browser settings.

## Retention policy and rollover policy for Data Movement gateway logs

The following table lists the Data Movement gateway logs that have a retention policy and a rollover policy.

Information note

- Requires Data Movement gateway 2024.11.67 or later.
- The retention policy and rollover policy are currently not configurable.

| Log | Log retention policy | Rollover policy |
| --- | --- | --- |
| Data Movement gateway (repagent) | Purge after 30 days | 100 MB |
| Replication engine logs (repsrv) | Purge after 30 days | 100 MB or 7 days (whichever occurs first) |
| Source connection logs (rependsrv) | Purge after 45 files have accumulated | 100 MB |

## Changing the logging level of the Data Movement gateway logs (repagent)

Qlik Support might ask you to change the current logging level before sending the Data Movement gateway (repagent) logs. You can view and change the current logging level by running the following commands from /opt/qlik/gateway/movement/bin:

- To view the current logging level, run:

  ./agentctl configuration getloggers
- To change the logging level to Trace, run:

  ./agentctl configuration setloggers -l Root -v DEBUG
- To change the logging level to Verbose, run:

  ./agentctl configuration setloggers -l Root –v DETAILED\_DEBUG

Information noteAfter running any of the setloggers commands, you need to restart the Data Movement gateway service as described in [*Restarting the service*](dm-gateway-managing.htm#Restarti2).

## Updating the registration key

Changing the registration key might be necessary in the unlikely event that the key becomes corrupted or if you suspect the data gateway server was accessed by an unauthorized user.

To update the registration key:

1. Generate and copy the key as described in steps 6-7 of [*Stage two: Install and set up Data Movement gateway*](dm-gateway-setting-up.htm#Stage4).
2. Select Administration from the launcher menu (![Launcher menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then Data gateways.
3. Locate your Data Movement gateway. Then, from the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu at the end of the row, select Edit.
4. Paste the key into the Key field (replacing the existing key) and save the settings.
5. Return to the Data Movement gateway server and stop and then start the Data Movement gateway service as described in [*Data Movement gateway service commands*](dm-gateway-managing.htm#Restarti).
