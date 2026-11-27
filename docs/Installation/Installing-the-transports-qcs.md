---
title: "Installing the SAP transports"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Installation/Installing-the-transports-qcs.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connectors installation"]
---

# Installing the SAP transports

A SAP transport is a package which is used to transfer data from one SAP installation to another. Transports can also be used to transfer data from external applications.

Information note

There is an installation guide in PDF format available on Community. It is attached to the release notes. Go to [Release Notes](https://community.qlik.com/t5/Release-Notes/tkb-p/ReleaseNotes), click on Products, and filter on Qlik SAP Connectors. There is also a release notes summary in PDF format attached to the release notes.

## Backwards compatibility

When there is a new connector release, the SAP transports should be updated. There is backwards compatibility to the SAP code, so it is possible for a SAP connector to be added, without also installing the corresponding SAP transports.

Warning noteIf you do not update the transports, new SAP functionality dependent on changes in the connector SAP code cannot be used.

The following table shows the current backwards compatibility of the components of the connector package:

SAP connector backwards compatibility

| Connector | Client | SAP transport (data extraction) |
| --- | --- | --- |
| SQL Connector | Qlik Cloud December 2020 or later | 6.1.2 or later |
| BW Connector | Qlik Cloud February 2021 or later | 7.0.6 or later |
| Report | Qlik Cloud February 2021 or later | 8.2.0 or later |

## Downloading the transports

Do the following:

1. Go to [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).
2. Select Qlik Data Analytics, and then select Qlik Connector for use with SAP NetWeaver.
3. Use the Release filters to narrow your list of possible downloads.
4. Download the transports: [version].SAP.transports.zip

   [version] will be replaced with a number. If you are downloading version 8.7.2 of the transports, the file will be: 872.SAP.transports.zip

## Importing the transports

The transports must be imported in the correct order:

1. Data extraction transports
2. Role transports (user profile)

Information note

Note: If the Replicate endpoint SAP HANA via SAP Application Server is used together with SAP Connectors on the same SAP system, the SAP Connectors transports must be imported first. After that, import the SAP HANA App transport on top of them.

Information noteThe data extraction transports are cross-client. They should be imported to the base client (usually 000). The role transports are client-specific and must be imported into all the clients where they will be used.

For more information, see [*Importing the SAP transports*](Importing-the-transports.htm).

## Latest transports

### Transports for release 8.3.1

You can download the transports file 831 SAP transports.zip from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).

Information noteIt is recommended that the transports are imported into the SAP system by a SAP BASIS expert.

Data extraction and user profile transports are required for the following:

- SQL Connector
- BW Connector
- SAP Report connector

Warning noteYou must install SAP ERP transports before installing SAP BW transports.

### SAP ERP , Report, and BW

Transports for connector version 8.3.1 for SAP ERP, Report, and BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport |
| --- | --- | --- | --- |
| SQL | 7.31-7.40 SP07 |  |  |
| SQL | 7.40 SP08 - 7.5x |  |  |
| Runtime Object | 7.5x + ( S4HANA 2022) |  |  |

### SAP BW

Transports for connector version 8.3.1 for SAP BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport | User profile transport BW |
| --- | --- | --- | --- | --- |
| BW | 7.31 – 7.3x |  |  |  |
| BW | 7.40 – 7.5x |  |  |  |
| BW | 7.40 – 7.5x (not HANA) |  |  |  |

Do the following:

1. Import the appropriate data extraction transport into the base client, usually 000. This is client independent.
2. Import the appropriate user profile transports into every client where they will be used. This is client dependent.

### Transports for release 8.2

You can download the transports file 82 SAP transports.zip from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).

Information noteIt is recommended that the transports are imported into the SAP system by a SAP BASIS expert.

Data extraction and user profile transports are required for the following:

- SQL Connector
- BW Connector
- SAP Report connector

Warning noteYou must install SAP ERP transports before installing SAP BW transports.

### SAP ERP , Report, and BW

Transports for connector version 8.2 for SAP ERP, Report, and BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport |
| --- | --- | --- | --- |
| SQL | 7.31-7.40 SP07 | E66K900438 | E66K900154 |
| SQL | 7.40 SP08 - 7.5x | H6AK900140 | E66K900154 |
| Runtime Object | 7.5x + ( S4HANA 2022) | H6AK900140 | E66K900154 |

### SAP BW

Transports for connector version 8.2 for SAP BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport | User profile transport BW |
| --- | --- | --- | --- | --- |
| BW | 7.31 – 7.3x | B7DK900299 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x | H7TK900384 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x (not HANA) | SM7K900129 | E66K900154 | H7TK900185 |

Do the following:

1. Import the appropriate data extraction transport into the base client, usually 000. This is client independent.
2. Import the appropriate user profile transports into every client where they will be used. This is client dependent.

## Transport history

### Transports for release 8.2

You can download the transports file 82 SAP transports.zip from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).

Information noteIt is recommended that the transports are imported into the SAP system by a SAP BASIS expert.

Data extraction and user profile transports are required for the following:

- SQL Connector
- BW Connector
- SAP Report connector

Warning noteYou must install SAP ERP transports before installing SAP BW transports.

### SAP ERP , Report, and BW

Transports for connector version 8.2 for SAP ERP, Report, and BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport |
| --- | --- | --- | --- |
| SQL | 7.31-7.40 SP07 | E66K900438 | E66K900154 |
| SQL | 7.40 SP08 - 7.5x | H6AK900140 | E66K900154 |
| Runtime Object | 7.5x + ( S4HANA 2022) | H6AK900140 | E66K900154 |

### SAP BW

Transports for connector version 8.2 for SAP BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport | User profile transport BW |
| --- | --- | --- | --- | --- |
| BW | 7.31 – 7.3x | B7DK900299 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x | H7TK900384 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x (not HANA) | SM7K900129 | E66K900154 | H7TK900185 |

Do the following:

1. Import the appropriate data extraction transport into the base client, usually 000. This is client independent.
2. Import the appropriate user profile transports into every client where they will be used. This is client dependent.

### Transports for release 8.1

You can download the transports file 81 SAP transports.zip from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).

Information noteIt is recommended that the transports are imported into the SAP system by a SAP BASIS expert.

Data extraction and user profile transports are required for the following:

- SQL Connector
- BW Connector

Warning noteYou must install SAP ERP transports before installing SAP BW transports.

### SAP ERP and BW

Transports for connector version 8.1 for SAP ERP and BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport |
| --- | --- | --- | --- |
| SQL | 7.31 – 7.40 SP07 | E66K900414 | E66K900154 |
| SQL | 7.40 SP08 – 7.5x | H6AK900131 | E66K900154 |
| Runtime Object | 7.5x + (S4HANA 2022) | S4HK903414 | E66K900154 |

### SAP BW

Transports for connector version 8.1 for SAP BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport | User profile transport BW |
| --- | --- | --- | --- | --- |
| BW | 7.31 – 7.3x | B7DK900298 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x | H7TK900370 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x (not HANA) | SM7K900128 | E66K900154 | H7TK900185 |

Do the following:

1. Import the appropriate data extraction transport into the base client, usually 000. This is client independent.
2. Import the appropriate user profile transports into every client where they will be used. This is client dependent.

### Transports for release 8.0.3

You can download the transports file 803 SAP transports.zip from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).

Information noteIt is recommended that the transports are imported into the SAP system by a SAP BASIS expert.

Data extraction and user profile transports are required for the following:

- SQL Connector
- BW Connector

Warning noteYou must install SAP ERP transports before installing SAP BW transports.

### SAP ERP and BW

Transports for connector version 8.0.3 for SAP ERP and BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport |
| --- | --- | --- | --- |
| SQL | 7.31 – 7.40 SP07 | E66K900383 | E66K900154 |
| SQL | 7.40 SP08 – 7.5x | H6AK900126 | E66K900154 |
| Runtime Object | 7.5x + (S4HANA 2022) | S4HK903913 | E66K900154 |

### SAP BW

Transports for connector version 8.0.3 for SAP BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport | User profile transport BW |
| --- | --- | --- | --- | --- |
| BW | 7.31 – 7.3x | B7DK900290 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x | H7TK900351 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x (not HANA) | SM7K900122 | E66K900154 | H7TK900185 |

Do the following:

1. Import the appropriate data extraction transport into the base client, usually 000. This is client independent.
2. Import the appropriate user profile transports into every client where they will be used. This is client dependent.

### Transports for release 8.0.2

You can download the transports file 802 SAP transports.zip from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).

Information noteIt is recommended that the transports are imported into the SAP system by a SAP BASIS expert.

Data extraction and user profile transports are required for the following:

- SQL Connector
- BW Connector

Warning noteYou must install SAP ERP transports before installing SAP BW transports.

### SAP ERP and BW

Transports for connector version 8.0.2 for SAP ERP and BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport |
| --- | --- | --- | --- |
| SQL | 7.31 – 7.40 SP07 | E66K900351 | E66K900154 |
| SQL | 7.40 SP08 – 7.5x | H6AK900114 | E66K900154 |

### SAP BW

Transports for connector version 8.0.2 for SAP BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport | User profile transport BW |
| --- | --- | --- | --- | --- |
| BW | 7.31 – 7.3x | B7DK900279 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x | H7TK900321 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x (not HANA) | SM7K900111 | E66K900154 | H7TK900185 |

Do the following:

1. Import the appropriate data extraction transport into the base client, usually 000. This is client independent.
2. Import the appropriate user profile transports into every client where they will be used. This is client dependent.

### Transports for release 8.0.1

You can download the transports file 801 SAP transports.zip from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).

Information noteIt is recommended that the transports are imported into the SAP system by a SAP BASIS expert.

Data extraction and user profile transports are required for the following:

- SQL Connector
- BW Connector

Warning noteYou must install SAP ERP transports before installing SAP BW transports.

### SAP ERP and BW

Transports for connector version 8.0.1 for SAP ERP and BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport |
| --- | --- | --- | --- |
| SQL | 7.31 – 7.40 SP07 | E66K900289 | E66K900154 |
| SQL | 7.40 SP08 – 7.5x | H6AK900107 | E66K900154 |

### SAP BW

Transports for connector version 8.0.1 for SAP BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport | User profile transport BW |
| --- | --- | --- | --- | --- |
| BW | 7.31 – 7.3x | B7DK900274 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x | H7TK900314 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x (not HANA) | SM7K900108 | E66K900154 | H7TK900185 |

Do the following:

1. Import the appropriate data extraction transport into the base client, usually 000. This is client independent.
2. Import the appropriate user profile transports into every client where they will be used. This is client dependent.

### Transports for release 8.0.0

Information noteIt is recommended that the transports are imported into the SAP system by a SAP BASIS expert.

Data extraction and user profile transports are required for the following:

- SQL Connector
- BW Connector

You must install the SAP ERP and BW transports before installing SAP BW transports.

Information noteOnly the SQL connector from those transports can be used in Qlik Cloud.

### SAP ERP and BW

Transports for connector version 8.0.0 for SAP ERP and BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport |
| --- | --- | --- | --- |
| SQL | 7.31 – 7.40 SP07 | E66K900212 | E66K900154 |
| SQL | 7.40 SP08 – 7.5x | H6AK900092 | E66K900154 |

### SAP BW

Transports for connector version 8.0.0 for SAP BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport | User profile transport BW |
| --- | --- | --- | --- | --- |
| BW | 7.31 – 7.3x | B7DK900257 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x | H7TK900299 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x (not HANA) | SM7K900095 | E66K900154 | H7TK900185 |

Do the following:

1. Import the appropriate data extraction transport into the base client. This is client independent.
2. Import the appropriate user profile transports into every client where they will be used. This is client dependent.

### Transports for release 7.0.6 and 7.0.7

Information noteIt is recommended that the transports are imported into the SAP system by a SAP BASIS expert.

Data extraction and user profile transports are required for the following:

- SQL Connector
- BW Connector

You must install the SAP ERP and BW transports before installing SAP BW transports.

Information noteOnly the SQL connector from those transports can be used in Qlik Cloud.

### SAP ERP and BW

Transports for connector version 7.0.6 and 7.0.7 for SAP ERP and BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport |
| --- | --- | --- | --- |
| SQL | 7.00 – 7.1x | E6DK901087 | E6DK901010 |
| SQL | 7.20 – 7.40 SP07 | E66K900205 | E66K900154 |
| SQL | 7.40 SP08 – 7.5x | H6AK900083 | E66K900154 |

### SAP BW

Transports for connector version 7.0.6 and 7.0.7 for SAP BW

| Connector | SAP BASIS system | Data extraction transport | User profile transport | User profile transport BW |
| --- | --- | --- | --- | --- |
| BW | 7.00 – 7.2x | B7TK900180 | E6DK901010 or E66K900154 | E66K900076 |
| BW | 7.30 – 7.3x | B7DK900254 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x | H7TK900296 | E66K900154 | H7TK900185 |
| BW | 7.40 – 7.5x (not HANA) | SM7K900092 | E66K900154 | H7TK900185 |

Do the following:

1. Import the appropriate data extraction transport into the base client. This is client independent.
2. Import the appropriate user profile transports into every client where they will be used. This is client dependent.
