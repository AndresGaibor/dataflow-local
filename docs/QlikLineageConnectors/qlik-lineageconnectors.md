---
title: "Extracting lineage data with Qlik Lineage Connectors"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/qlik-lineageconnectors.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics"]
---

# Extracting lineage data with Qlik Lineage Connectors

Qlik Lineage Connectors
 is an add-on module to Qlik Cloud that helps users to visualize, understand, and scale data environments in an intuitive way.
The connectors extract lineage and metadata from Qlik on-premises offerings, external BI tools, and data sources.

Source-specific connectors within this utility extract lineage data from Qlik on-premises, external BI tools, and data sources; mapping information and usage between these systems. Source lineage and the data journey displays in your Qlik Cloud tenant. This information assists analysts, database administrators, and data consumers to visualize, understand, and scale data environments in an intuitive way. The mapped information and usage between systems can be displayed by selecting its link in a space you have defined and then drilling in to view Lineage.

Qlik Lineage Connectors are available with Qlik Sense Enterprise SaaS, Qlik Cloud Analytics Premium, and Qlik Cloud Enterprise subscriptions.

Qlik Cloud Government noteQlik Cloud Government supports using Qlik Lineage Connectors when the Windows platform where Qlik Lineage Connectors is installed is configured to run in a FIPS 140-2 approved mode of operation, also known as "FIPS mode". For more information, see [*System cryptography*](qlik-lineageconnectors-install.htm#System_Cryptography).

Information noteWhich Qlik Lineage Connectors that are available to you depends on your license. Connectors that link to Qlik on-premises sources (Qlik Sense Client-managed, QlikView, Qlik NPrinting) are included with the Qlik Sense Enterprise SaaS, Qlik Cloud Analytics Premium, and Qlik Cloud Enterprise licenses. Clients who have purchased the Qlik Lineage Connectors premium license have access to all available lineage connectors. If you do not have the Qlik Lineage Connectors premium license, some connectors are not available.

## How do Qlik Lineage Connectors work?

Qlik Lineage Connectors
 automatically gather metadata and lineage information from each targeted system. Each connector has its own configuration. Clients configure source-specific fields per connector type and define rules for each connector that tell Qlik Lineage Connectors what to include for mapped lineage in the specified tenant space. Users define how connectors behave and schedule how often to reload the metadata and lineage information.

## Qlik Lineage Connectors workflow

To prepare for connection and extraction of lineage metadata from on-premises BI tools and database applications to your Qlik Cloud tenant, refer to the following high-level workflow:

### Prerequisites

- You must be assigned the Analytics Admin role and the Manage API keys permission in the target tenant.
- Download and Install Qlik Lineage Connectors. See [*Installing Qlik Lineage Connectors*](qlik-lineageconnectors-install.htm)
- Obtain an API key (JWT token) from your tenant: Click your user profile menu and select Settings. In the API Keys section, generate a new key, then copy and save it somewhere easily accessible.
- Create and name an empty [managed space](#glossary-0 "Glossary term") in your tenant.
- Open your tenant and Qlik Lineage Connectors utility.

### Qlik Lineage Connectors configuration steps

- Project: Add and name a new project.
- Qlik Cloud Target: Define, validate, and save the Qlik Cloud Target.
- Connectors: Define and save a connector.
- Rules: Add at least one rule to each connector in connector settings.

  Information noteFor the QlikView and Qlik Sense connectors, check the box next to Create Link in Qlik Cloud to ensure the assets pulled in by this rule populate as links in Qlik Catalog.
- Scheduler: Select ![icon play](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_gen_ForwardIcon.png)or schedule a job. Once the job completes, navigate to the created space in your tenant to view the imported lineage.

### Accessing data lineage in the target tenant

Once the job defined by your connectors populates into Qlik Catalog, navigate to the managed space in your tenant.
Extracted lineage sourced by Qlik Lineage Connectors displays with an Open link label when you hover over the tile. Open the lineage graph by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the app, and then selecting Lineage. You can also access the lineage graph from the Details section.

Details provide you with information around ownership and recent activity of this source. On the left side of the panel, IDs display for the job and the connector.

Details display in Qlik Catalog

![Link details display in Qlik Catalog Service](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_QlikLineageConnector_LinkDetails.png "Click to view full size")

[Impact analysis](#glossary-2 "Glossary term") provides a graphical representation of the data lineage across various platforms as well as inputs and dependencies available from the extracted metadata. For example, a QlikView app displays the QVDs and data sources that have produced the resulting QlikView application. When the node is selected in the graph, it displays any outputs that are generated from that QlikView [dataset](#glossary-3 "Glossary term") onward, even after it populates in Qlik Cloud.

Lineage in Qlik Catalog

![View Impact Analysis in Qlik Catalog Service](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_QlikLineageConnector_ImpactAnalysis.png "Click to view full size")

For more information, see [Analyzing the lineage of data](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/lineage.htm).
