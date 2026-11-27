---
title: "Required permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA-RFC/sap-hana-rfc-permissions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP HANA RFC"]
---

# Required permissions

Authorize the SAP user specified in the source connection to consume every registered table selected for a data task.

## Authorize the connection user

- Grant the /QTQVC/CDC authorization object with activity CONSUME and the registered table ID.
- Grant the S\_RFC authorization object with Execute activity, restricted to function group /QTQVC/CDC\_RFC.

Missing add-on authorization causes a fatal authorization error. If the connection user is authorized for only some selected tables, subscriptions fail for the other tables. Grant the missing permissions before restarting the data task.

## Authorize the SAP admin

The SAP admin needs S\_TCODE authorization for transaction /QTQVC/HRFC\_COCKPIT to access the SAP HANA RFC Endpoint Cockpit.

These are permissions on the SAP system. They do not replace the permissions required to create connections and run data tasks in Qlik Talend Data Integration.
