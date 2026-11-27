---
title: "Importing the SAP transports"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Installation/Importing-the-transports.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connectors installation"]
---

# Importing the SAP transports

It is recommended that the transports are imported into the SAP system by SAP BASIS experts.

There is normally no need to delete the Qlik objects from a previous release before import because the objects from the latest transport overwrites the previous transport.

Depending on the SAP BASIS, it might be necessary to select the following options in transaction STMS:

![Import transport request dialog](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_gen_SAP-import-transport-request4.png)

After import, check the transport log:

![Transport log output](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_gen_SAP-import-queue2.png)

Mark the transport and press the Logs button ![Logs icon](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_gen_SAP-Logs-button.png).

The log example below illustrates a successful import. Warnings normally do not indicate a problem, but if the log lists errors, they must be corrected.

![Overview of transport logs](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_gen_Transport-logs2.png)

## Learn more

- [*SAP Connector configuration*](../Configuration/Connector-configuration.htm)
