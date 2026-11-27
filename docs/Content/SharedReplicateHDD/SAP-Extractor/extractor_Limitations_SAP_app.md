---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Extractor/extractor_Limitations_SAP_app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP Extractor"]
---

# Limitations and considerations

When using SAP Extractor as a source connector in a Qlik Talend Data Integration task, the following limitations apply.

## Limitations and considerations for all data tasks

- DDLs are not supported. Should you need to change the extractor:

  1. Stop the task and remove the extractor from it.
  2. Replace the extractor and activate it.
  3. Add the extractor to the task again and resume.
- Each extractor can be associated with a single task only. Additionally, the extractor should be exclusively run by Qlik Talend Data Integration.
- Table transformations and filters may impact performance as they are not propagated to the extractors.
- Source lookup is not supported.
- Data Movement gateway supports only one instance of each extractor. Consequently, each extractor should be associated with only one Logical System.
- SAP Extractor uses the metadata extracted from the extractor's Z-table. Consequently, the target tables will be created with this table's columns and without a Primary Key/Unique Index.
- All changes are captured as INSERT operations.
- Moving data with 4-byte emoji characters is not supported.
- SAP tables with rows that exceed 8192 bytes are not supported. If you need to replicate such tables, you can work around this limitation by excluding columns until the row size is less than 8192 bytes.

## Limitations and considerations for replication and landing tasks

- The **Apply Changes** and **Store Changes** moving options cannot be enabled without the Full Load moving option.
- The "Start from timestamp" and "Start from position" options for running tasks are not supported.
- Qlik Talend Data Integration header fields are not supported.
- The [Replicate unlimited LOB columns and Optimize when LOB size is less than](../../../../Sense_Hub/DataIntegration/Replicating/replicating-settings-metadata.htm) LOB handling options are not supported.
