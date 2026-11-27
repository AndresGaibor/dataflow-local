---
title: "Connecting to SAP sources"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Landing/connecting-sap-sources.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources"]
---

# Connecting to SAP sources

The following SAP sources are supported in Qlik Talend Data Integration. Data moved to the target platform is kept up-to-date using CDC (Change Data Capture) technology, or with scheduled reloads of the entire source data. When working with Data Movement gateway, CDC occurs in real time. When working without Data Movement gateway, CDC occurs according to a user-defined schedule.

In certain use cases, when configuring the connection to your data source, you also need to select which Data Movement gateway to use to access the source. If your use case does require a Data Movement gateway, make sure that a Data Movement gateway has been set up for accessing the selected data source, and that the required driver is installed on the Data Movement gateway server. Note that Data Movement gateway is not supported with a Qlik Talend Cloud Starter subscription and might be optional with other subscriptions, depending on your use case and data source.

For information about when Data Movement gateway is required, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

Information noteWhen you connect to data sources, you might need to add underlying Qlik Cloud IP addresses to your allowlist. For more information, see [*Allowlisting domains and IP addresses*](../../Introduction/qlik-cloud-dns-ip.htm).

## Connecting to an SAP source

To connect to an SAP source

1. Open the Create connection dialog by doing one of the following:

   - In Create, click Data connection.
   - In Connections, click Create connection.
   - In the Select source connection screen of the onboarding wizard, click Create connection.
2. Locate the SAP source you want to connect to by doing one of the following:

   - Type SAP in the search box to show a list of SAP connectors.
   - Select Application in the Category list to show only application connectors.
   - Select from recently used connectors in the Recently used tab.
3. Click the connector name to open the connection settings.

For instructions on configuring your connector, find your connector in the list below and click the link.

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sap-square.png)

### [SAP (Application)](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-Application-DB/sap-application-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sap-square.png)

### [SAP Extractor](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-Extractor/SAP-Extractor-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sap-square.png)

### [SAP HANA (Database)](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA/SAP-HANA-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sap-square.png)

### [SAP ODP](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-ODP/sap-odp-properties.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sap-square.png)

### [SAP HANA RFC](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA-RFC/sap-hana-rfc-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/ODataConnector-square.png)

### [SAP OData](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-ODATA/sap-odata-properties.htm)

![SAP connector icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sap-square.png)

### [SAP Cloud for Customer](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-SAP-Cloud-for-customer.htm)

![SAP Cloud for Customer V2 connector icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sap-square.png)

### [SAP Cloud for Customer V2](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-SAP-Cloud-for-customerV2.htm)

![SAP Concur connector icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sap-concur-square.png)

### [SAP Concur](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-SAP-Concur.htm)

![SAP SuccessFactors connector icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sap-successfactors-square.png)

### [SAP SuccessFactors](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-SAP-SuccessFactors.htm)
