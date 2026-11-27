---
title: "Required SAP permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Shared/Permissions_Required_for_Installing_for_SAP_Client_.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP (Application)", "Prerequisites", "Install the Replicate for SAP Client on the SAP machine"]
---

# Required SAP permissions

Replicate for SAP delivers its own authorization object: `ZR4SAP`. In addition to this authorization object, there are additional authorizations that need to be enabled for the Qlik replication software.

## SAP users for Replicate

A dialog user in SAP is required to access the Replicate for SAP Client GUI in SAP. In addition, a communication user is required to support the RFC calls from the Qlik replication software to the SAP system.

Identify existing users in SAP or create dedicated users for the Qlik replication software.

## Authorizations for the Qlik replication software.

Both the dialog and communication users will need to be assigned to a role with authorization object S\_TCODE and value ZR4SAP.

Authorization Object S\_TCODE with value ZR4SAP:

![Entering the value in SAP.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sap1.png)

The communication user will also require the following authorization objects: S\_RFC and S\_OC\_SEND and /QTQVC/RFC.

Authorization Object S\_RFC:

![The authorization object in SAP.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sap2.png)

Authorization Object S\_OC\_SEND:

![The authorization object in SAP.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sap4.png)
