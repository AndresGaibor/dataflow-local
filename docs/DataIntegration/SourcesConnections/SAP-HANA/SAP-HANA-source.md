---
title: "SAP HANA (Database)"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA/SAP-HANA-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources"]
---

# SAP HANA (Database)

This section explains how to set up a SAP HANA source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](prereq_saphana.htm), set up the [*Permissions*](security_req_saphana.htm), and familiarized yourself with the [*Limitations and considerations*](../../../../Global_Common/Content/SharedReplicateHDD/SAP-HANA/limitations_saphana_source.htm).

Information noteThis connector is supported with a Qlik Talend Cloud Enterprise subscription only.

## Setting connection properties

This section describes the available connection properties. All properties are required unless otherwise indicated.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the SAP HANA (Database) source connector and then provide the following settings:

### Data source

- Data gateway

  Select a Data Movement gateway to use for moving your data.

  For information on Data Movement gateway, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Server: The IP address or host name of the SAP HANA database server.

  To connect to a High Availability Cluster, specify all of the cluster nodes and port numbers in the Server field. The nodes should be separated by a comma.

  Example:

  `12.12.1.123:3033,12.12.1.124:3034`
- Instance number: The instance number of the SAP HANA database with the source tables.
- Database architecture: Select either Single tenant or Multi tenant according to your Database architecture.
- Database: The name of the source database In a Multi tenant architecture.

### Account properties

- User name: The user name required to access the SAP HANA database.
- Password: The password required to access the SAP HANA database.

### CDC properties

- Record mode: Choose one of the following:

  Information noteThe Record mode option is available from Data Movement gateway 2025.11.23.

  - Primary Key only: In this mode, for each updated record, only the Primary Key values are captured and stored. The stored Primary Keys are then used to retrieve the data from the source. This mode uses less storage, but more memory to process the data being retrieved.
  - Full record: In this mode, for each captured table, the entire data record is retrieved and stored in a "shadow" table. This mode provides a full history of changes with all values, including the before-images of each UPDATE and DELETE operation. The benefits of this mode include:

    - Improved accuracy of the latency calculation in the monitor.
    - Does not require JOIN of SELECT statements to retrieve the full data, which in turn reduces the load on the SAP HANA system.
    - Soft deletes on the target are supported, as a full history of all the data is available.

    This mode uses more storage on the SAP HANA system, but requires less memory to process the data being retrieved.

    Warning noteWhen moving large-scale data using Full record mode, we recommend partitioning the QTREP/TRAN\_LOG table to prevent it from becoming full and impacting performance.

    Information noteFull record mode has less limitations than Primary Key only mode. For more information, see [*Limitations and considerations for replication and landing data tasks*](../../../../Global_Common/Content/SharedReplicateHDD/SAP-HANA/limitations_saphana_source.htm#Limitati2).
- Create CDC table in schema: The name of the schema in the source database where you want the `attrep_cdc_changes` table to be created.
- Log cleanup interval (min): How often (in minutes) to check if Change Records need to be deleted from the attrep\_cdc\_changes table.
- Log retention period (min): How long (in minutes) to keep Change Records in the attrep\_cdc\_changes table before deleting them.
- SAP archiving users to filter: The user names of SAP application users whose DELETE operations you do not want to be captured. Users must be separated with commas.

  Information note

  Editing the user list requires you to stop and then resume the task for the changes to take affect.

Information noteThe change capture operation creates certain Qlik artifacts in the database. For more information, see [*Capturing data changes*](prereq_saphana.htm#Change)

### SSL options

- Enable SSL: Select to enable SSL and then configure the related settings.
- Crypto provider: Select your cryptographic library provider from the drop-down list.
- Keystore file: The SSL Keystore file that contains the client identity.
- Truststore file: Your SSL Truststore file that contains the server’s public certificates.
- Server host name in certificate: The name of the server host specified in the server certificate. This verifies the identity of the server, rather than the host name with which the connection was established. If you specify \* as the host name, the server host name is not validated.
- Server Name Indication: The name of the SSL server.
- Validate certificate: To validate your SSL certificate, select the check box. This step is optional, but strongly recommended for security reasons.

Information noteTo connect to SAP HANA using SSL, the client must be configured to authenticate the SSL server certificate. For more information, see [*Prerequisites*](prereq_saphana.htm).

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the source connection.
