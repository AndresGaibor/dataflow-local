---
title: "Required SAP permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Extractor/Extractor_Permissions_Required_for_Installing_for_SAP_Client_.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP Extractor", "Prerequisites", "Download the required transports to the SAP Machine"]
---

# Required SAP permissions

Replicate for SAP delivers its own authorization object: `ZR4SAP`. In addition to this authorization object, there are additional authorizations that need to be enabled for the Qlik Talend Data Integration software.

## SAP users for Qlik Talend Data Integration for SAP Extractors

A dialog user in SAP is required to access the Qlik Talend Data Integration for SAP Extractor GUI in SAP. In addition, a communication user is required to support the RFC calls from the Qlik Talend Data Integration software to the SAP system.

Identify existing users in SAP or create dedicated users for the Qlik Talend Data Integration software.

Qlik Talend Data Integration for SAP delivers its own authorization object: /QTQVC/RAO.

The authorization object /QTQVC/RAO can be turned on to enable/disable specific authorizations below according to the needs of the Qlik Talend Data Integration user:

![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sapextractor_permissions_replicate.png)

## Authorizations for Qlik Talend Data Integration for SAP Extractors

The SAP system needs to be open to create the logical system. This is done using SAP Transaction /nSCC4.

Make sure the Changes and Transports for Client-Specific Objects for the Source Client is set to Automatic Recording of Changes or Changes without Automatic Recording.

![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sapextractor_permissions_1.png)

All clients need to be opened for Cross-Client Object Changes. Creating a Logical Client is a cross-client change that cannot be captured in a transport. It only needs to be open for a minute when the target logical system is created.

![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sapextractor_permissions_2.png)

Make sure the Transaction /nSE06 System Change Option > Global Setting is set to Modifiable (During Logical System creation and activation of Extractors).

![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sapextractor_permissions_3.png)

### Administration User

SAP Authorizations for Administrator Role for initial setup of the logical system and activation of the extractors within /QTQVC/EXTREP.

Authorizations required for Administrator:

Creating the RFC.

Instead of \*, RFCDEST can have the name of the logical system, which is completely configurable to the customer’s preference.

![SAP interface, showing RFC creation permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions.png)

Creating the IDocs for sending to Replicate.

![SAP interface, showing IDoc creation permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions2.png)

Creating the ZQLIK\* programs and tables during activation of the extractors.

![SAP interface, showing ZQLIK creation permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions3.png)

Maintaining table information during activation and table updates.

![SAP interface, showing table maintenance permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions4.png)

Access to tables to check data and update as needed.

![SAP interface, showing table access permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions5.png)

Adding ZQLIK\*-created tables to a transport.

![SAP interface, showing ZQLIK to transport permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions6.png)

Administering transports.

![SAP interface, showing administer transport permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions7.png)

### RFC Communications User

This user is needed to be used when setting up the SAP for Extractors endpoint in Replicate. It can be set as a COM user as there is no need for dialog access. Optionally you can create one dialog user ID with both the Communication user and Administration user access.

Authorizations required for RFC Communications User and Administration User:

Sending and receiving of IDocs via RFC connection to Replicate.

![SAP interface, showing IDoc sending permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions8.png)

Access to the RFC communication protocol for the connection to Replicate.

![SAP interface, showing communication protocol acces permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions9.png)

Access to the main QTQVC transactions and security checks.

![SAP interface, showing QTQVC transaction permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions10.png)

Access for trace features for the SQL functionality.

![SAP interface, showing SQL tracing permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions11.png)

Executing the datasources during run time to extract the data from SAP.

![SAP interface, showing datasource execution permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions12.png)

Administrating jobs in the background as scheduled by Replicate.

![SAP interface, showing scheduled job administration permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions13.png)

Processing jobs in the background as scheduled by Replicate.

![SAP interface, showing background job processing permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions14.png)

Sending internal SAP messages during the extract process.

![SAP interface, showing sending internal messages permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions15.png)

Executing functions inside the /QTQVC/\* namespace to support the SQL functionality.

![SAP interface, showing permission to execute functions inside QTQVC.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions16.png)

Viewing tables inside the /QTQVC/\* namespace to support the SQL functionality.

![SAP interface, showing permission to view tables inside QTQVC.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions17.png)

Program authorization for Qlik programs.

![SAP interface, showing Qlik program permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/SAPExPerm/ui_SAPExPermissions18.png)

![SAP interface, showing Qlik program permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/SAP-perm3.png)

Access to tables to check data and update as needed.

![SAP interface, showing Qlik program permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/SAP-perm1.png)

Maintaining table information during activation and table updates.

![SAP interface, showing Qlik program permission.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/SAP-perm2.png)

### SQL Connector Authorizations

Qlik provides two roles that contain the necessary authorizations. You can assign different roles to different users, depending on need, or both roles can be assigned to one user.

- The QTQVCADMIN role is required for users who perform Qlik transactions in the SAP GUI.
- The QTQVCACCESS role is used by a connector back-end user who performs extraction jobs from Qlik.

For information on adding and testing these permissions, see [SAP SQL Connector user configuration](/en-US/connectors/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Configuration/SAP-SQL-user-configuration.htm).
