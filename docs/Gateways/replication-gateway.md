---
title: "Qlik Data Gateway - Data Movement"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/replication-gateway.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections"]
---

# Qlik Data Gateway - Data Movement

Qlik Data Gateway - Data Movement (hereafter Data Movement gateway) facilitates data movement from your enterprise data sources and SaaS applications to supported targets, over a strictly outbound, encrypted and mutually authenticated connection. By eliminating the need to open inbound firewall ports, Data Movement gateway provides a secure and trusted means of moving your enterprise data.

## When is Data Movement gateway required?

Information noteData Movement gateway is only available to customers with Standard, Premium, or Enterprise subscriptions.

Information note

If you are a customer with Qlik Talend Cloud Standard, Qlik Talend Cloud Premium, or Qlik Talend Cloud Enterprise subscriptions, the best practice is to use *Data Movement gateway* when moving data from Infor, Jira, Microsoft Dynamics 365 CRM, NetSuite, Oracle Fusion, or Salesforce.

Data Movement gateway is required in the following cases:

- Your data source or target is not directly accessible from Qlik Cloud. Examples of data sources or targets that are not directly accessible from Qlik Cloud include data sources or targets located in a VPC, or behind a firewall closed to inbound communication.

  For more information on private connections, see [*Supporting private connections in Qlik Talend Data Integration*](#Supporti) below.
- You need near real-time CDC from database sources.
- You need to access target platforms via a proxy server.
- You want to use knowledge marts.
- You have a Premium or Enterprise subscription and you need incremental loads from SaaS application sources less than every 30 minutes. When using Data Movement gateway, you can set the interval to as little as 5 minutes with Premium and Enterprise subscriptions.

  For information about minimum scheduling intervals according to data source type and subscription tier, see [*Minimum allowed scheduling intervals*](../Admin/subscription-options-QTC.htm#Minimum).
- Your data source is one of the following:
  - IBM DB2 for z/OS
  - IBM DB2 for iSeries
  - IBM DB2 for LUW
  - SAP Extractor
  - SAP (Application)
  - SAP ODP
  - SAP OData
  - SAP HANA (Database)
  - Oracle

  Information noteYou can use Data Movement gateway for any data source. The data sources above are those that require Data Movement gateway. For all other data sources Data Movement gateway can be used if you need the additional functionality it offers, but it is not a standard requirement.
- You need the added layer of security provided by Data Movement gateway, which prevents data from passing through Qlik Cloud and allows customers to control the data path. This is only relevant to RDBMS, mainframe, and SAP data sources.

In the following example, Data Movement gateway is not required as both the SaaS application source and the data warehouse target are directly accessible from Qlik Cloud:

Moving data from a SaaS application to a data warehouse target without Data Movement gateway

![Moving data from a SaaS application to a data warehouse target without Data Movement gateway](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/No-DMG-architecture.png "Click to view full size")

### Data Movement gateway deployment matrix

| Use case | Data Movement gateway deployment |
| --- | --- |
| Using a different Data Movement gateway for the source and target connectors | The data movement task always runs on the Data Movement gateway defined for the source connector. This means that the machine on which the source gateway is installed must be able to access both the data source and the target platform. The Data Movement gateway defined for the target connector allows Qlik Cloud to access the target to perform transformations and other ELT operations. |
| Moving data from a SaaS source to a target platform located in a VPC | Although Data Movement gateway is not required to access SaaS sources, it is required if the data task's target platform is located in a VPC or is otherwise inaccessible from Qlik Cloud. In such a case, the data movement task will run on the Data Movement gateway defined for the SaaS connector. |
| Defining a Data Movement gateway for a target connector | You only need to define a Data Movement gateway for the target connector if the target platform is located in a VPC or is otherwise inaccessible from Qlik Cloud. The target Data Movement gateway does not perform any data movement as that is solely the role of the source Data Movement gateway. Instead, it allows Qlik Cloud to access the target to perform transformations and other ELT operations. |

## Protecting your data

A unique key-pair is established for each Data Movement gateway server connected to the Qlik Cloud tenant. This key pair is used for authentication and for end-to-end data encryption on top of the HTTPS transport level encryption. Moreover, as communication with Qlik Cloud and data transfer is initiated via outbound ports only, you do not need to open any inbound ports to your corporate network.

Qlik Cloud Government note

For Qlik Cloud Government, verify the current platform and security requirements before installing Data Movement gateway. Installing Data Movement gateway on a machine running in FIPS mode is not supported. See [*Data Movement gateway system requirements*](dm-gateway-prerequisites.htm).

Information noteThe Data Movement gateway documentation always reflects the capabilities of the latest application version. If you’re not using the latest version, your system administrator is encouraged to upgrade immediately. For information on upgrading, see [*Upgrading and uninstalling Data Movement gateway*](dm-gateway-upgrading.htm)

## Common use cases

The following section highlights two common use cases: Moving data to a target that can only be accessed via a private connection, and moving data to targets that are directly accessible from Qlik Cloud.

Qlik Data Gateway - Data Movement plays a central role in the data movement process. The diagrams below illustrate how Data Movement gateway interacts with Qlik Cloud and your data sources to securely move data to supported targets.

Information note

The number of Data Movement gateway that need to be deployed depends on your specific environment and use case. If your data sources are in close proximity to each other and your target is directly accessible from Qlik Cloud, then a single Data Movement gateway will usually suffice. However, in the following cases, best practice is to use multiple data gateways:

- Ingesting data from data sources that are geographically distant from each other
- Moving large volumes of data from multiple data sources
- Moving data to a target that is inaccessible from Qlik Cloud (such as SQL Server in a VPC)

### Supporting private connections in Qlik Talend Data Integration

A private connection means that your data source or target is not exposed to the Internet, making it inaccessible from Qlik Cloud.

There are several types of private connection, examples of which include:

- Snowflake AWS PrivateLink where public connectivity (via port 443) has been disabled
- Microsoft SQL Server (or any other RDBMS) running in a VPC that has a private IP address only

Tip noteDeploying Data Movement gateway to access your target platform is only required if the target is not directly accessible from Qlik Cloud.

The Data Movement gateway deployed to access your target performs ELT operations, which include some or all of the following: data registration, storage, transformations, and data marts.

Note that while it is possible to use the same gateway to access both the data source and the data target, using two gateways - one accessing the source and the other accessing the target - will often provide better performance. For example, if the source database is Oracle on-premises and the target database is Snowflake AWS PrivateLink, one gateway (defined in the Oracle source connection) will be used to land data from Oracle to Snowflake, while the other gateway (defined in the Snowflake target connection) will be used to perform the ELT operations. Using two gateways is especially recommended if the source and target databases are not in close proximity to each other. In such a scenario, the landing gateway should be as close as possible to the source, while the target gateway should be as close as possible to the target. If data is being ingested from multiple data sources, it might also make sense to set up a dedicated gateway for each data source, depending on both the type and the location of the data sources. An example of this type of setup is shown in the image below.

Moving data from distributed data sources to a target in a VPC and then performing ELT operations on the target

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dmg-arch-multiplegateways-vpctarget.png "Click to view full size")

### Moving data from enterprise data sources to supported targets

The high-level communication sequence is as follows:

1. Data Movement gateway establishes a mutually authenticated and encrypted connection to Qlik Cloud, using HTTPS.
2. Qlik Cloud sends task execution instructions to the Data Movement gateway, which in turn reports the task status to Qlik Cloud.
3. Data Movement gateway retrieves the data from the data source and pushes it to the designated target.

Data Movement gateway - Moving data from enterprise data sources to supported targets

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dmg-arch-datasources-novpc.png "Click to view full size")

### Moving data from SaaS applications to supported targets

The high-level communication sequence is as follows:

1. Data Movement gateway establishes a mutually authenticated and encrypted connection to Qlik Cloud, using HTTPS.
2. Qlik Cloud sends landing task execution instructions to the Data Movement gateway, which reports the task status back to Qlik Cloud.
3. When the landing task is started, Qlik Cloud pulls the data from the SaaS application and stores it (encrypted with the tenant key).
4. Data Movement gateway retrieves the SaaS application data from Qlik Cloud and pushes it to the designated target.

Tip noteIn this use case, Data Movement gateway does not have to be installed behind the firewall as neither the source (SaaS application) nor the target are located behind a firewall.

Data Movement gateway - Moving data from SaaS applications to supported targets

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dmg-arch-saas-novpc.png "Click to view full size")

### Moving data from SaaS applications and enterprise data sources to supported targets

Tip noteIn this use case, two Data Movement gateways are installed (on separate machines): one serving the enterprise data source and the other serving the SaaS application. The Data Movement gateway serving the SaaS application does not have to be installed behind the firewall as neither the source (SaaS application) nor the target are located behind a firewall.

The high-level communication sequence is a combination of the "Moving data from enterprise data sources" and "Moving data from SaaS applications" use cases described above.

Data Movement gateway - Moving data from SaaS applications and enterprise data sources to supported targets

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dmg-arch-full-novpc.png "Click to view full size")

### Moving data from SaaS applications and enterprise data sources in a VPC to targets in the VPC

The high-level communication sequence for moving data from the SaaS application is as follows:

1. Data Movement gateway establishes a mutually authenticated and encrypted connection to Qlik Cloud, using HTTPS.
2. Qlik Cloud sends landing task execution instructions to the Data Movement gateway, which reports the task status back to Qlik Cloud.
3. When the landing task is started, Qlik Cloud pulls the data from the SaaS application and stores it (encrypted with the tenant key).
4. Data Movement gateway retrieves the SaaS application data from Qlik Cloud and pushes it to the designated target.

The high-level communication sequence for moving data from the enterprise data source is as follows:

1. Data Movement gateway establishes a mutually authenticated and encrypted connection to Qlik Cloud, using HTTPS.
2. Qlik Cloud sends landing task execution instructions to the Data Movement gateway, which reports the task status back to Qlik Cloud.
3. Data Movement gateway retrieves the data from the data source and pushes it to the designated target.

Data Movement gateway - Moving data from SaaS applications and enterprise data sources in a VPC to targets in the VPC

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dmg-arch-full-vpc.png "Click to view full size")

## Learn more

- [*Data Movement gateway system requirements*](dm-gateway-prerequisites.htm)
- [*Setting up Data Movement gateway*](dm-gateway-setting-up.htm)
- [*Managing the Data Movement gateway server*](dm-gateway-managing.htm)
- [*Managing Data Movement gateway in the Administration
  activity center*](dm-gateway-managing-console.htm)
- [*Upgrading and uninstalling Data Movement gateway*](dm-gateway-upgrading.htm)
- [*Troubleshooting Data Movement gateway*](dm-gateway-troubleshooting.htm)
- [*Configuring AWS PrivateLink for Qlik Data Gateway - Data Movement*](dm-gateway-aws-privatelink.htm)
