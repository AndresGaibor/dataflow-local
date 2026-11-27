---
title: "Upgrading or Uninstalling the Replicate  SAP Extractor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Extractor/extract_UpgradeandUninstall_SAP_Client.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP Extractor", "Prerequisites", "Download the required transports to the SAP Machine"]
---

# Upgrading or Uninstalling the Replicate SAP Extractor

The following instructions explain how to upgrade and uninstall the Replicate SAP Extractor.

## Upgrading the Replicate SAP Extractor

To upgrade the Replicate SAP Extractor, apply the Install transport.

## Uninstalling the Replicate SAP Extractor

To uninstall the Replicate SAP Extractor, apply the Delete transport.

### Deleting the remaining objects

The deletion transports will remove the objects in the /QTQVC/\* namespace.

To delete the artifacts created by the Replicate for SAP Extractors, the entries described below will need to be removed. First in the Development environment, and then transported to any other systems where they might be present (assuming they were transported).

Assignment of source systems to BIW systems including IDoc type (your SLOGSYS will be different) – RSBASIDOC

This entry will be removed using function RSAP\_BIW\_DISCONNECT with the following parameters (using our example):

![Data browser showing RSBASIDOC table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image001.png)

![BIW_DISCONNECT function](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image003.png)

#### Transaction WE20

Select the Logical System created for the Replicate for SAP Extractors, and then delete.

![Window showing the logical systems created for the SAP Extractors](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image004.png)

#### Transaction WE21

Select the IDoc Port used in the partner profile in WE20, and then delete.

![Ports in IDOC processing window.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image006.png)

#### Transaction WE30

Select the IDoc Port used for message type RSSEND in the partner profile in WE20, and then delete.

![Develop IDOC types: initial screen.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image008.png)

Below are the logical system entries that need to be deleted and collected in a transport.

#### Table TBDLS

![Data browser showing TBDLS table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image009.png)

#### Table TBDLST

![Data browser showing TBDLST table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image011.png)

RFC Destination entries as well as ports and IDOC entries are listed below.

You can use R3TR TABU to manually delete the following table entries into a Customizing request

#### Table RFCDES

![Data browser showing RFCDES table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image013.png)

#### Table RFCDOC

![Data browser showing RFCDOC table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image015.png)

#### Table RFCATTRIB

![Data browser showing RFCATTRIB table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image017.png)

The following entries should be deleted with transaction WE20, but you should confirm they are removed and collected in a transport.

#### Partner Profile Table – EDPP1

![Data browser showing table EDPP1](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image019.png)

#### Outbound Parameters – EDP13

![Data browser showing table EDP13](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image020.png)

#### Inbound parameters – EDP21

![Data browser showing table EDP21](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image021.png)

The following entries should be deleted with transaction WE21, but you should confirm they are removed and collected in a transport.

#### Port Header Table - EDIPOA

![Data browser showing table EDIPOA](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image022.png)

#### Port Table – EDIPORT

![Data browser showing table EDIPORT](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image024.png)

The following entries should be deleted with transaction WE30, but you should confirm they are removed and collected in a transport.

#### IDOC Message type – EDIMSG

![Data browser showing table EDIMSG](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image025.png)

#### Deleting the ZQLIK\* Tables

Select and then delete all the entries in “Manage extractors”

![ZQLIK tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPEx/image027.png)

Collect all of the deleted ZQLIK\* TABU entries and the ZQD\* PROG program entries if you need to transport them.
