---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-ODATA/sap-odata-limitations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP OData"]
---

# Limitations and considerations

When using SAP OData as a source, the following limitations apply:

- The SAP OData connector supports services generated with SAP Gateway Service Builder for Extracting ODP Data via OData. Other types of service should meet the requirements for services generated with SAP Gateway Service Builder for Extracting ODP Data via OData.

  For more information, see [Generating a Service for Extracting ODP Data via OData](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/11/853413cf124dde91925284133c007d/frameset.htm).
- OData Version 2.0 (V2) is supported only.
- An OData service with a single entity is supported. DeltaLinksOf<EntitySet> is supported for a delta enabled service.
- Service version 1.0 is supported only.
- Metadata changes are not supported. Any changes to the service metadata requires reloading the task.
- Each ODP subscription in the SAP system can be used for a unique service name and username. In other words, it is not possible to have multiple subscriptions for the same service and username. Any new task for the service and username will cancel the existing subscription and start a new one.
- Current data is the only supported mode, when the actual change operation (INSERT, UPDATE, or DELETE) is performed on the target.

  Information note
  - Changes operations are determined by the ODP source. Some operations might not be supported by the target.
  - We recommend manually setting a Primary Key for ODP sources that do not use the default Primary Key.
  - Applicable to replication projects only: Some INSERTs are received as UPDATEs. Therefore, to prevent conflicts on the target, set the No record found for applying an UPDATE Apply Conflicts handling policy to INSERT the missing target record.
- GZIP compression requires HTTP 1.1 or later (HTTP/1.1)
- HTTPS is only supported with a host name. If there is no DNS name, add the IP address and host name to the local hosts file.
- For currency and unit of measure, the SAP NetWeaver Gateway framework always uses the type conversions (methods for outbound and inbound flow of CL\_GDT\_CONVERSION). Unit of measure and currency conversion always use the ISO code, as opposed to the desired unit or currency.For more information, see SAP notes 1893788 and 3082462.
- Due to the OData specification, each entity must have at least one primary key. If the source ODP entity has no primary keys, all columns in the service model will be generated as primary keys.
- The Tables are already loaded. Start processing changes from options for running tasks are not supported.
- The Do not limit LOB column size option in the task settings is not supported.
- Source lookup is not supported.
- The SAP OData endpoint uses the metadata of the OData service. Therefore, the target tables will be created with ODP-provided columns.
- Hierarchy objects and columns are not supported.

## SAP notes

If you encounter any of the issues listed below, make sure to upgrade your system to the SAP version that resolves the issue.

| SAP note | SAP\_BW |
| --- | --- |
| 3118751 - ODP OData V2: MaxPageSize higher than 50000 not taken | 750-756 |
| 3023446 - ODP with OData V2: odata.maxpagesize is ignored for delta request | 750-755 |
| 3094347 - OData query from a data source having a field of type RAW 16 shows incorrect value | 750-757 |
| 3389181 - Metadata of timestamp fields in ODP OData V2 | 750, 754-757 |
| 3396326 - Mapping INT8 to Edm.Int64 instead Edm.String | 750-758 |
| 3355345 - Helper report to maintain value in ODQADMIN table | 750-758 |
| 3250756 - Floating type fields in the source are rounded off in the Operational Data provider access | 750-757 |
| 062232 - ODP OData V2 - Last skiptoken for a pointer provides no deltatoken | 750-755 |
| 3335039 - OData V2: UNCAUGHT\_EXCEPTION short dump in SEGW for ABAP CDS ODP ending with $E | 754-757 |
| 3197913 - XML transformation error during extraction | 731-757 |
| 3315021 - ODP OData V2: type DATS cannot be converted to Edm.Datetime | all |
| 2219781 - ODP\_ODATA: DeltaLinksOf<EntitySet> | 750 |
| 3305193 - Handling of initial date and time values in DB, when read via OData service | 752-757 |
| 2787992 - New data types | 750-754 |
| 3569859 - Overflow possible if integer type INT8 used in ODP source of ODATA v2 model | SAP\_BW: 750-758  SAP BW/4HANA 2.0 , 2021, 2023 |
| 3790740 – Error: Metadata cache on hub system for current model is outdated | Check the SAP Note for release and support package level. |
| 3566255 – Cache refresh on empty srv\_tech\_name | Check the SAP Note for release and support package level. |
| 3618997 – Backend Cache timestamp issue when extended model with overwrite is used | Check the SAP Note for release and support package level. |
| 3244392 – ODATA ODP V2: Delta not possible if latest delta request in source system deleted | Check the SAP Note for release and support package level. |
| 3294213 - ODATA V2: Convert $filter expressions to filter select options | Check the SAP Note for release and support package level. |
| 3564384 - Exception Handling on Response Serialization via Simple Transformation in OData V2 | Check the SAP Note for release and support package level. |
| 3778892 - "Transformation error on serialization" error observed upon fetching data via OData service | Check the SAP Note for release and support package level. |
