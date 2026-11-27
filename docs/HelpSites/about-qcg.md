---
title: "Qlik Cloud Government"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/HelpSites/about-qcg.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Introducing Qlik Cloud", "Qlik Cloud Government overview"]
---

# Qlik Cloud Government

Qlik Cloud Government and its product offerings are only available for the U.S. Public sector and some U.S. Department of Defense (DoD) agencies. It differes from Qlik’s commercial Qlik Cloud and Qlik Cloud Government - DoD offerings due to the security protocols required to support the U.S. Public sector. See [Qlik Cloud security, compliance, and privacy](security-compliance.htm) for a summary of compliance certifications and attestations.

Qlik keeps the Qlik Cloud Government and Qlik Cloud Government - DoD offerings in sync for product features and capabilities from Qlik Cloud wherever possible.

This topic notes feature differences between the Qlik Cloud commercial version and Qlik Cloud Government. The Qlik Cloud documentation set supports both versions, and differences are noted.

Information note

For information about new and enhanced Qlik Cloud Government features, see [What's new in Qlik Cloud](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/saas-change-log.htm). Then, filter the items that to review specific Qlik Cloud Government-related information.

## Qlik Cloud Government Subscriptions

In Qlik’s commercial cloud offerings, Qlik now offers Qlik Cloud Analytics which is a capacity based subscription model. Qlik Cloud Government remains a user-based subscription model at this time. Similarly, Qlik Talend Data Integration products have also moved to a capacity-based subscription (Qlik Talend Cloud), whereas the Qlik Cloud Data Services subscription for the Qlik Talend Data Integration capabilities of Qlik Cloud Government remain source/target based.

Qlik Cloud Analytics and Qlik Talend Cloud users and administrators can access in-product announcements, onboarding resources, in-product help, videos, interactive demos, survey and feedback options, and industry walkthroughs. They also have access to Qlik Notifications for activities such as scheduled maintenance. This content is available from the Resource Center. For more information, see [Getting started and learning options](/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/HelpSites/get-started-qlik-cloud.htm).

Qlik Cloud Government users have access to the same onboarding resources, help site documentation, in-product help, videos, and courses. Unlike the commercial cloud, Qlik Cloud Government provides only interactive demos. In-product clickthrough tours are replaced with videos and other learning resources, and survey, feedback, or industry walkthrough options are not available.

## Qlik Cloud Analytics

This section notes the Qlik Cloud Analytics feature differences between the commercial version of Qlik Cloud and the Qlik Sense Enterprise SaaS - Gov (US) version that is available on Qlik Cloud Government.

### Analytics for business users

- The Qlik Analytics mobile app for iOS and Android cannot be used with Qlik Cloud Government. If your organization deploys mobile technology, the browser-based version of Qlik Sense from an iOS or Android operating system might be available. Contact your Qlik Cloud Government tenant administrator to determine availability. For more information, see [*Qlik Analytics mobile app*](../../Sense_Hub/Mobile/qsmsaas-intro.htm) and [*System requirements and supported browsers*](../../Sense_Hub/Introduction/qcs-supported-browsers.htm).
- Alerts are used to monitor data, and to detect outliers and anomalies. All alerting functionality is available in Qlik Cloud Government except for alerting on the Qlik Analytics mobile app. For more information, see [Monitoring data with alerts](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Alerting/monitoring-changes-with-alerts.htm).
- Conversational analytics in Microsoft Teams is not supported in Qlik Cloud Government. For more information, see [Exploring application content with conversational analytics in Microsoft Teams](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Insights/insight-advisor-chat-microsoft-teams.htm).
- The Discovery Agent is not available for Qlik Cloud Government. For more information, see [Discovery Agent](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DiscoveryAgent/discovery-agent.htm).

### Qlik Answers and Qlik MCP server

- Qlik MCP server is supported in Qlik Cloud Government and Qlik Cloud Government - DoD. For more information, see [*Qlik MCP server*](../../Sense_Hub/QlikMCP/Qlik-MCP-server.htm).
- Qlik Answers is not supported in Qlik Cloud Government and Qlik Cloud Government - DoD. For more information, see [*Qlik Answers*](../../Sense_Hub/QlikAnswers/Qlik-Answers.htm).

### Creating analytics and visualizing data

- Visualization extensions enable you to extend the visualization capabilities of Qlik Sense Enterprise SaaS - Gov (US) by using standard Web technologies. Third-party extensions are supported in Qlik Cloud Government. However, the use of third-party extensions might need to be defined and approved as part of an Agency Authority to Operate, depending on the security and compliance requirements your organization follows. For more information on Extensions, see [Managing extensions](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-extensions.htm).
- Qlik Sense GeoOperations and Qlik Geocoding capabilities enable geographic calculations and functions such as calculating routes or travel areas. GeoOperations can be used with Qlik Cloud Government. Qlik Geocoding is not available in Qlik Cloud Government. For more information, see [Point to address lookup](/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/PointToAddressLookUp.htm) and [Qlik Sense GeoOperations](/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/GeoOperations.htm).
- Qlik Predict finds patterns in your data and uses them to make predictions on future data. Machine learning experiments let you collaborate with other users and integrate your predictive analytics in Qlik Sense applications. In addition to making predictions, you can do an in-depth analysis of the key features that influence the predicted outcome. Qlik Cloud Government does not support Qlik Predict. For more information, see [Machine Learning with Qlik Predict](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/home-automl.htm).
- In-application reporting is a set of features available in a Qlik Sense application, powered by the Qlik Reporting Service value-add subscription option. With in-application reporting, configure highly customizable Tabular, PixelPerfect, HTML, PowerPoint, and Word reports and distribute them to internal and external stakeholders.

  - Qlik add-ins for Microsoft Office are supported for developing report templates against applications in Qlik Cloud Government or Qlik Cloud Government - DoD tenants.
  - Qlik add-ins for Microsoft Office can be used in the following Microsoft 365 offerings:

    - Office 365 Commercial
    - Office 365 Government Community Cloud (GCC)
    - Office 365 Government Community Cloud High (GCCH)

    For more information, see [Managing installation manifests for Qlik add-ins for Microsoft Office](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-add-in.htm).
  - In Office 365 Government Community Cloud High (GCCH), Qlik add-ins for Microsoft Office can only be installed via [centralized deployment](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Install/reporting-install-add-ins.htm#Centrali). Installing via sideloading or network share is not supported.

  For more information about in-application reporting, see [In-application reporting with Qlik Cloud Analytics](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/cloud-in-app-reports-intro.htm).
- Key driver analysis is a built-in tool available within Qlik Sense applications to help you identify and visualize the underlying factors driving behaviors in your data. Key driver analysis is not available in Qlik Cloud Government. For more information, see [Uncovering the key influencers behind your data using key driver analysis](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/KeyDrivers/introduction-key-driver-analysis.htm).

### Loading and modeling analytics data

- The Qlik SAP NetWeaver Connector lets you efficiently load data into a Qlik Sense application from SAP NetWeaver. The information might be stored in several different repositories within the SAP architecture, such as SAP BI/BW, an SAP ERP, or CRM system. This connector is available with Qlik Cloud Government, and it’s available in Qlik Cloud Analytics with an additional license. For more information, see [SAP NetWeaver](/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/SAP-SQL-connector.htm).
- Qlik Cloud Government supports connectivity with Snowflake databases. However, it does not support Snowflake key pairing or the option to change the role from the default given. For more information, see [Create a Snowflake connection](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Snowflake/Create-Snowflake-connection.htm) and [Select and load data from a Snowflake database](/en-US/cloud-services/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Snowflake/Load-Snowflake-data.htm).
- Some cloud service providers may offer U.S. Government versions of their products. Depending on their implementation approach, this may result in the need of different connectors by Qlik.

  - Qlik Cloud Government supports integration to Microsoft GCC and GCC High Government clouds for our analytics and Advanced Analytics connectors. These connectors are only available in Qlik Cloud Government and Qlik Cloud Government - DoD.
  - Qlik Advanced Analytics Generative AI connectors are supported for developing ML models in Qlik Cloud Government and Qlik Cloud Government - DoD. For more information, see [*Analytics sources in Qlik Cloud Analytics*](../../Sense_Hub/LoadData/connect-analytics-sources.htm).
- Qlik for VS Code is a Visual Studio Code extension that offers script editing capabilities for analytics applications and scripts in Qlik Cloud tenants. Qlik for VS Code is not supported for Qlik Cloud Government or Qlik Cloud Government - DoD tenants.

  For more information about Qlik for VS Code, see [Qlik for VS Code](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikCode/code-extension-home.htm).

### Self-hosted software for Qlik Cloud Analytics

- Qlik DataTransfer is a lightweight Windows application that lets you upload data from on-premises data sources to Qlik Sense without firewall tunneling. Customers can choose to use Qlik DataTransfer as part of their implementation of Qlik Cloud Government. This tool supports encrypted communications but is not FIPS compliant (Federal Information Processing Standards). Qlik Cloud Government users can use it in their implementation pending their own risk review. For more information, see [Installing Qlik DataTransfer](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikDataTransfer/install-Qlik-DataTransfer.htm). Qlik DataTransfer is not available to download from Qlik Cloud Government, but it can be downloaded from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).
- Qlik Lineage Connectors are an add-on module to Qlik Cloud Analytics. These connectors extract lineage data from QlikView, QlikSense (client managed), external BI tools, and data sources. A graphical representation of the data journey can then be accessed by selecting Impact Analysis in a space defined within a Qlik Catalog Service target tenant. This feature is available in Qlik Cloud Government when configured to run in a FIPS 140-2 approved mode of operation (FIPS mode). For more information, see [Qlik Lineage Connectors](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/qlik-lineageconnectors.htm). The Qlik Lineage Connector offering is self-hosted software available to download from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).
- Qlik Cloud Government supports using Qlik Data Gateway - Direct Access only when Windows Server is configured to run in a FIPS 140-2 approved mode of operation (FIPS mode). For more information, see [System cryptography](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-setting-up.htm#System).

## Qlik Talend Data Integration

Qlik Talend Data Integration is an enterprise-scale service that automatically and continuously uploads data from on-premises systems to Qlik Cloud.

Although the Qlik Talend Data Integration interface and tooling is available in Qlik Cloud Government, it is not functional without at least one licensed RDBMS, SAP or Mainframe Source/Target Gov license of Qlik Cloud Data Services, except for the ability to create data pipelines. Qlik Cloud Data Services in Qlik Cloud Government corresponds to a Qlik Talend Cloud Enterprise subscription, with the limitations described in this section.

The Qlik Cloud Data Services subscription of Qlik Talend Data Integration in Qlik Cloud Government supports the following Data Governance capabilities that are otherwise only available as part of a Qlik Talend Cloud Enterprise subscription:

- Data catalog
- Data marketplace
- Data products
- Data quality
- Qlik Trust Score

For more information, see [Qlik Talend Data Integration](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Data-services.htm).

- Qlik Cloud Government supports using Qlik Data Gateway - Data Movement when the Linux platform where Qlik Data Gateway - Data Movement is installed is configured to run in a FIPS 140-2 approved mode of operation, also known as "FIPS mode".

  For more information, see [Qlik Data Gateway - Data Movement](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/replication-gateway.htm).
- Qlik Cloud Government does not support SaaS application connectors for Qlik Talend Data Integration.
- Qlik Cloud Government does not support SQL assistant for transformations in Qlik Talend Data Integration.
- Qlik Cloud Government does not support generating an AI-based dataset description in Qlik Talend Data Integration.
- Qlik Cloud Government does not support AI-recommended relationships when creating a data model in Qlik Talend Data Integration.
- Qlik Cloud Government does not support Talend capabilities in Qlik Talend Cloud.
- Qlik Cloud Government does not support Qlik Open Lakehouse in Qlik Talend Cloud.

## Qlik Cloud Administration

This section notes the administration difference between the commercial version and Qlik Cloud Government.

### System management

- Applications up to 5 GB in size (in-memory) are supported. With large application support, you can use larger applications. By default, Qlik Cloud Government includes 20 GB of large application capacity. Optionally, you can add packs of 20 GB and 100 GB. For more information, see [Large application support](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/large-app-support.htm).

  Information noteThe unit of measurement for Qlik Cloud capacity, usage, and limits is represented by binary gigabytes (GB), where 1 GB is 230 bytes (1,073,741,824). This is also known as a gibibyte (GiB), defined by the [International Electrotechnical Commission (IEC)](http://www.iec.ch/prefixes-binary-multiples). Similarly, 1 TB is 240 bytes (or 1,024 GBs).
- Qlik Cloud Government does not support the Qlik Account IdP (identity provider) option. For more information, see [Managing identity providers](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-create-idp-configuration.htm) and [Trust and Security at Qlik](https://www.qlik.com/us/trust).
- Qlik Cloud Government supports the JSON Web Token (JWT) authentication standard for OpenID Connect (OIDC) identity providers. For more information, see [OpenID Connect for integration with identity providers](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/OIDC-intro.htm).
- Qlik Cloud Government users can check the [Qlik Cloud services status page](https://status.qlikcloud.com/) for Qlik Cloud Government scheduled change notifications.
- Qlik Cloud Government does not support SAML for integration with identity providers. For more information, see [SAML for integration with identity providers](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SAML-intro.htm).
- When configuring Microsoft 365 as an email provider, Qlik Cloud Government and Qlik Cloud Government - DoD tenants can select a cloud region to use the correct Microsoft endpoints for authentication and email sending.

  For more information, see [Configuring email for reports and notifications](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-configure-email-support.htm).

## Qlik Automate

Qlik Automate is a no-code visual interface that lets Qlik Cloud users build automated analytics and data workflows by integrating applications and services from outside of your Qlik environment.

- Qlik Cloud Government supports a subset of Qlik-native and third-party connectors. For more information, see [Qlik Automate connectors](/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/connector-blocks/connectors-list.htm).
- The Custom Code block is not supported in Qlik Cloud Government tenants. For more information, see  [Custom Code in Qlik Automate](/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/advanced/custom-code.htm).

## Interoperability with client-managed Qlik products

- Applications can be exported from Qlik Sense Enterprise on Windows and imported by Qlik Cloud Government. For more information, see [Exporting applications](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/export-apps-cloud-hub.htm) and [Uploading applications](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/uploading-apps.htm).
- Qlik Cloud Government users cannot import applications exported from QlikView. QlikView applications cannot be used with Qlik Cloud Government. For more information, see [Exporting applications](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/export-apps-cloud-hub.htm) and [Uploading applications](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/uploading-apps.htm).

## Extending Qlik Cloud Government

- Qlik
  CLI is a command-line interface that provides access to all Qlik Cloud public APIs through a command line. Customers can choose to use QlikCLI to implement Qlik Cloud Government. This tool supports encrypted communications but is not FIPS compliant (Federal Information Processing Standards). Qlik Cloud Government users can use it in their implementation pending their own risk review. QlikCLI can be downloaded from [qlik-cli](https://qlik.dev/toolkits/qlik-cli).

## Deploying Qlik Cloud Government

- The Qlik Cloud Government subscription process differs from the Qlik Cloud process. For example, you cannot manually create your tenant or use the My Qlik portal to purchase and manage the subscription and potential customers need to be reviewed and approved to ensure they meet government criteria, prior to purchase and onboarding. For more information, contact your primary Qlik support representative.

## Qlik Cloud Government Support

- The Qlik Cloud Government customer support process is different than on Qlik's commercial cloud instances. Qlik Cloud Government customers need to initiate support via email to [government.support@qlikcloudgov.com](mailto:government.support@qlikcloudgov.com "Click to email QCG support") and cannot include government sensitive information in the email. Qlik Cloud Government support will respond and initiate the support process.

## Qlik Cloud Government Onboarding Terms

- The U.S. Government's FedRAMP and DISA authoring entities maintain a Rules of Behavior governing customers' use of Qlik Cloud Government. Please see [Qlik Cloud Government's Onboarding Terms](https://www.qlik.com/us/legal/qlik-cloud-government-onboarding-terms) for more information, including Qlik Cloud Government Terms of Service and Service Level Agreements.
