---
title: "Step 3: Set up a connection to a data catalog"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/connect-data-catalog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse"]
---

# Step 3: Set up a connection to a data catalog

A data catalog is a necessary component for creating a Qlik Open Lakehouse.

When you onboard data to a Qlik Open Lakehouse, a data catalog is required to manage the metadata for your Apache Iceberg tables. Your data catalog is the target for your lakehouse project, and stores the schemas of the tables in your lakehouse, alongside pointers to the data files, for data discovery and querying.

Data catalogs enable interoperability with your Iceberg tables across different data processing engines and storage solutions. They provide centralized access to the data in your Iceberg tables and catalogs that support role-based access control (RBAC), and offer secure and compliant data access management.

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/aws-glue.png)

### [AWS Glue Data catalog](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/aws-glue-data-catalog.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/google-square.png)

### [Google Lakehouse runtime catalog](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/google-biglake-catalog.htm)
