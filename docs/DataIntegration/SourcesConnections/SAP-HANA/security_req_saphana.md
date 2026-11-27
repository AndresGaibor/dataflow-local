---
title: "Permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA/security_req_saphana.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP HANA (Database)"]
---

# Permissions

This topic lists which permissions are required for Data Movement gateway to be able to capture changes with the SAP HANA (Database) connector.

- Grant SELECT and TRIGGER on the SAP schema containing the selected source tables, to the user specified in the connector settings.
- If the [attrep\_cdc\_changes\_cts](prereq_saphana.htm#cdc_table) table is created in a schema owned by the user specified in the connector settings (the default), no further permissions are required.
- If the [attrep\_cdc\_changes\_cts](prereq_saphana.htm#cdc_table) table is created in a schema not owned by the user specified in the connector settings, grant SELECT, INSERT, UPDATE and DELETE on the attrep\_cdc\_changes\_cts table to the specified user.
