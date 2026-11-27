---
title: "Kafka target"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/kafka-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to streaming targets"]
---

# Kafka target

This topic explains how to configure connectivity to a Kafka target using the Kafka target connector. Kafka can be used as a target in a replication task only.

Setting up Kafka as a target involves:

- Fulfilling the [prerequisites](#Prerequi)
- Configuring a connection to Kafka

## Setting connection properties

To configure the connector, do the following:

1. In Connections, click Create connection.
2. Select the Kafka target connector and then provide the following settings:

### Data target

#### Data gateway

Information noteThis field is not available with Qlik Talend Cloud Starter subscription as Data Movement gateway is not supported with this subscription tier.

When moving data to Amazon MSK, a Data Movement gateway is only required if Amazon MSK is not accessible from Qlik Cloud and can only be accessed using a Private Link (for instance, if it's located in a Virtual Private Cloud). In such a case, select the Data Movement gateway through which you want to access the target database. Depending on your use case, this will either be the same Data Movement gateway deployed to move data from the data source, or a different one.

If you are moving data to an Amazon MSK instance which is directly accessible from Qlik Cloud, select None.

Information note

- If you are moving data to Kafka on-premises (see Cloud provider below), you must select a Data Movement gateway, regardless of whether or not Kafka is directly accessible from Qlik Cloud.
- If you need to use Data Movement gateway, version 2025.5.40 or later is required.

For information about Data Movement gateway use cases, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top) and [*Common use cases*](../../Gateways/replication-gateway.htm#Common).

#### Cloud provider

Choose None to use Kafka on-premises or Amazon MSK to use Amazon MSK.

#### Broker servers

Specify one or more broker servers using the following format (for high availability):

`server1[:port1][,server2[:port2]]`

**Example:**

`192.168.1.100:9092,192.168.1.101:9093`

The data task will connect to the first available host. If a host is specified without a port then port 9092 will be used as the default.

Information note

When using SSL or Kerberos authentication, you must specify the broker FQDN (i.e. not the IP address).

Information note

All of the broker servers in your cluster need to be accessible from the Data Movement gateway machine. However, you do not need to specify all of the servers in the **Broker servers** field. This is because Data Movement gateway only needs to connect to one of the servers in order to retrieve the connection details for the other servers in the cluster. It is therefore best practice to specify the servers that are most likely to be available when the task is run. The servers to which the data task produces messages is determined by the topic and partitioning topic, as well as the partitioning settings.

### Account properties

#### Authentication method

Select one of the following:

- **None:** No authentication.

  Information note

  Not available when the selected Cloud provider is Amazon MSK.
- **Certificate**: If you select this option, you also need to provide the following information:

  **Note**  The public and private key files must be in PEM format.

  - **Public key file:** Browse to the public key file in PEM format. When you click Save, the file will be uploaded to Qlik Talend Cloud and deployed to the Data Movement gateway selected in the connector settings.
  - **Private key file**: Browse to the private key file in PEM format. When you click Save, the file will be uploaded to Qlik Talend Cloud and deployed to the Data Movement gateway selected in the connector settings.
  - **Private key password**: The password for the private key file.
- Kerberos (SASL/GSSAPI): Select to authenticate against the Kafka cluster using Kerberos.

  Information note

  This authentication method is not available when the selected Cloud provider is Amazon MSK.

  - Principal: The Kerberos principal used to authenticate against the broker server(s).
  - Keytab file: Browse to the keytab file. When you click Save, the file will be uploaded to Qlik Talend Cloud and deployed to the Data Movement gateway selected in the connector settings.

  Information note

  In order to use Kerberos authentication on Linux, the Kerberos client (workstation) package should be installed.
- Username and password (SASL/PLAIN): You can select this option to authenticate yourself using a user name and password (SASL/PLAIN). To prevent the password from being sent in clear text, it is strongly recommended to enable the Enable TLS option as well.

  Information note

  This authentication method is not available when the selected Cloud provider is Amazon MSK.
- Username and Password (SASL/SCRAM-SHA-256): You can select this option to authenticate yourself using a user name and password (SASL/SCRAM-SHA-256).

  Note that selecting this option also requires each broker's server.properties file to be configured with the corresponding SASL/SCRAM mechanism.

  Information note

  This authentication method is not available when the selected Cloud provider is Amazon MSK.
- Username and Password (SASL/SCRAM-SHA-512): You can select this option to authenticate yourself using a user name and password (SASL/SCRAM-SHA-512).

  Note that selecting this option also requires each broker's server.properties file to be configured with the corresponding SASL/SCRAM mechanism.

#### SSL options

Enable TLS (supports TLS 1.0, 1.1 and 1.2)

Select this option to encrypt the communication between the Qlik Talend Cloud and the broker server(s). If the brokers are configured to require SSL, then you *must* select this option.

- CA file: Browse to the CA certificate in PEM format. When you click Save, the file will be uploaded to Qlik Talend Cloud and deployed to the Data Movement gateway selected in the connector settings.

  Information note

  Not needed when the selected Cloud provider is Amazon MSK.

### Metadata message publishing

#### Schema registry will be available for metadata message publishing

From the drop-down list, select one of the following options:

- No

  When this option is selected, only the data messages will be published.

- Confluent schema registry

  If you select this option, you must also configure the Schema registry connection properties described below.

  Warning noteWhen Confluent schema registry is selected, you must set the following [internal property](#internal_prop): CsrSkipGlobalConfig=false

Information note

- The Confluent Schema registry options support Avro message format only.
- It is strongly recommended *not* to publish schema messages to the same topic as data messages.
- If the topics do not exist, configure the brokers with auto.create.topics.enable=true to enable the data task to create the topics during runtime. Otherwise, the task will fail.

#### Message format

Choose JSON or Avro as the message format. Avro will be the only available option if you selected Confluent schema registry.

### Schema registry connection properties

#### Schema registry servers

Specify one or more Schema Registry servers using the following format (for high availability):

When publishing data schemas to the Confluent Schema Registry:

server1:port1[,server2[:port2]]

Example:

192.168.1.100:8081,192.168.1.101:8081

The data task will connect to the first available host.

#### Authentication method

Select one of the following Schema Registry authentication options:

- None: No authentication.
- Certificate: Select to authenticate using a certificate.

  If you select this option, you also need to provide the following information:

- Public key file: Browse to the public key file in PEM format. When you click Save, the file will be uploaded to Qlik Talend Cloud and deployed to the Data Movement gateway selected in the connector settings.
- Private key file: Browse to the private key file in PEM format. When you click Save, the file will be uploaded to Qlik Talend Cloud and deployed to the Data Movement gateway selected in the connector settings.
- Private key password: The password for the private key file.

- User name and password: Select to authenticate with a user name and password. Then enter your login credentials in the User name and password fields.
- Certificate + User name and password: Select to authenticate using both a certificate and a user name and password.

  When this option is selected, enter the required information in the Public key file, Private key file, Private key password, User name, and Password fields described above.
- Enable TLS (supports TLS 1.0, 1.1 and 1.2): Select this option to encrypt the data between the Data Movement gateway machine and the Schema Registry server(s). If the servers are configured to require SSL, then you *must* select this option.
  - CA file: Browse to the CA certificate in PEM format. When you click Save, the file will be uploaded to Qlik Talend Cloud and deployed to the Data Movement gateway selected in the connector settings.

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the connection.

## Prerequisites

Before you can use Kafka as a target, the following prerequisites must be met:

- Open TCP ports to all the brokers from the Data Movement gateway machine
- Set permissions that will allow the data task to write to the target topics.
  One way to do this is to use the Kafka ACLs script (kafka-acls).
- Either create a topic named attrep\_apply\_exceptions before starting the data task or configure the brokers with auto.create.topics.enable=true.

  Note that if this topic does not exist, the task will always fail when it encounters a data error, regardless of the error handling policy.

  For a description of the attrep\_apply\_exceptions control table, see [*Apply exceptions*](../Replicating/apply_exceptions.htm).

## Limitations and considerations

When defining a task with Kafka as the target connector, the following limitations apply:

- Task settings that are not supported:

  - The Kafka target connector does not support unlimited LOB size. In the tasks settings, the Include LOB columns and limit column size to (KB) option will be enabled and read-only.
  - Store Changes mode is not supported.
  - Batch optimized apply mode is not supported. Kafka always works in Transactional apply mode.
  - The Ignore ALTER Apply Changes setting is not supported for changes to source data types and table renaming.
  - The Drop and Create table option of the Target Table Preparation field is not supported.
  - The Truncate before loading option of the Target Table Preparation field is not supported.
  - The Change Data Partitioning Control table is not supported.
- General limitations:
  - Kafka topic names cannot contain spaces or exceed 255 characters (249 from Kafka 0.10) and can only contain the following characters:

    a-z|A-Z|0-9|. (dot)|\_(underscore)|-(minus)

    If the source table names exceed the maximum permitted length or contain unsupported characters, you need to either modify the names before starting the task or define a global transformation.
  - Column names must begin with [A-Za-z\_] (letters or an underscore) followed by [A-Za-z0-9\_] (letters, digits, or an underscore). For example, \_Test\_ is a valid column name whereas &Test is not.

    If a source column name does not adhere to this rule, then a transformation should be used to rename the column.
  - Dropping or renaming a source table is not supported.

## Data types

The following table shows the Kafka data types that are supported when using Qlik Cloud and the default mapping from Qlik Cloud data types.

Information note

When using the JSON message format, binary values are represented as hexadecimal digits.

Kafka data mapping

| Qlik Cloud Data Types | Kafka Target Data Types in Schema Messages |
| --- | --- |
| DATE | DATE |
| TIME | TIME |
| DATETIME | DATETIME |
| BYTES | BYTES (length) |
| BLOB | BLOB |
| REAL4 | REAL4 (7) |
| REAL8 | REAL8 (14) |
| INT1 | INT1 (3) |
| INT2 | INT2 (5) |
| INT4 | INT4 (10) |
| INT8 | INT8 (19) |
| UINT1 | UINT1 (3) |
| UINT2 | UINT2 (5) |
| UINT4  Information note Values larger than 2^31-1 are not supported. | UINT4 (10) |
| UINT8  Information note Values larger than 2^63-1 are not supported. | UINT8 (20) |
| NUMERIC | NUMERIC (p,s) |
| STRING | STRING (Length) |
| WSTRING | STRING (Length) |
| CLOB | CLOB |
| NCLOB | NCLOB |
| BOOLEAN | BOOLEAN (1) |

## Mapping to JSON and Avro

Avro message format uses logical types for a more precise representation of the data type.

Qlik Cloud data types will only be mapped to supported Avro logical data types if the Use logical data types for specific data types check box is selected.

Data type mappings

| Qlik Cloud data types | JSON | Avro Logical data types |
| --- | --- | --- |
| DATE | STRING | DATE  Annotates an Avro INT. |
| TIME | STRING | TIME-MILLIS  Annotates an Avro INT. |
| TIMESTAMP | STRING | TIMESTAMP-MICROS  Annotates an Avro LONG. |
| STRING | STRING | - |
| WSTRING | STRING | - |
| CLOB | STRING | - |
| NCLOB | STRING | - |
| NUMERIC | STRING | DECIMAL (p,s)  Annotates an Avro BYTES. |
| BYTES | BYTES | - |
| BLOB | BYTES | - |
| REAL4 | FLOAT | - |
| REAL8 | DOUBLE | - |
| INT1 | INT | - |
| INT2 | INT | - |
| INT4 | INT | - |
| UINT1 | INT | - |
| UINT2 | INT | - |
| UINT4 | LONG | - |
| INT8 | LONG | - |
| UINT8 | STRING | DECIMAL (20,0)  Annotates an Avro BYTES. |
| BOOLEAN | BOOLEAN | - |
