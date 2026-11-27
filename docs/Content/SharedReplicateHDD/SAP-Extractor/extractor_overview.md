---
title: "Overview"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Extractor/extractor_overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP Extractor"]
---

# Overview

The SAP Extractor connector leverages the SAP extractors to unload and capture SAP data directly from the SAP application, thereby eliminating the need to access the underlying database (which might not be possible due to license restrictions). Offering increased flexibility and fine-tuning options, the SAP Extractor connector facilitates effortless migration of SAP data to other environments.

The connector supports Full Load or Full Load and Apply Changes moving from standard and generic data sources.

During the moving process, Qlik Talend Data Integration does the following:

1. Executes the extractor using RFC protocol.
2. Stores the extracted data in an intermediate table corresponding to the source metadata structure.
3. Accesses the intermediate table using RFC protocol to retrieve the data.
4. Deletes the data from the intermediate table and runs the next extraction.
5. Performs INSERT operations on the target (even for source changes that were not INSERTs).

The SAP extractor connector depends on the RFC protocol to copy data retrieved by ABAP programs. As a result, the SAP extractor connector performance is not as good as the SAP (Application) connector which accesses the underlying databases directly). Therefore, if you need to Move huge amounts of data from SAP it is strongly recommended to use the SAP (Application) connector if possible.
