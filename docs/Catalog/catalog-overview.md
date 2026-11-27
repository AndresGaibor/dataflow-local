---
title: "Understanding your data with catalog tools"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/catalog-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data"]
---

# Understanding your data with catalog tools

Catalog tools in Qlik Cloud help you improve your data efficiency while maintaining security and compliance standards. Access to critical business metadata and the ability to apply user-defined tags and classifications are essential for data analysts and business groups.

Data administrators can verify the accuracy of data content and optimize data discovery by assigning and editing business metadata (names, descriptions, tags, and classifications). Business Intelligence users and application developers can configure personalized tags, apply classifications, and browse [dataset](#glossary-1 "Glossary term") samples and profile statistics to ensure that datasets are easy to find and contain the right information.

Catalog tools are particularly useful for new and existing datasets that a user has access to in their personal and [shared spaces](#glossary-2 "Glossary term"). Users have views into data files that help them to gain insights and make determinations about the data. Users can see where the comes from, what type of data it is, and how it can best be analyzed and used. This information helps to determine whether to create a new application with data or whether to load the data into an existing application.

The following Catalog options are available in the Analytics [activity center](#glossary-3 "Glossary term") for data discovery and managing business metadata:

- Dataset overview: Business and technical information about the dataset can be reviewed here. Details include the source file type, space, creation and last modified timestamps, field and row count, creator and owner, usage metrics, applied tags and common data classifications. See [*Managing dataset metadata*](managing-dataset-metadata.htm) for a complete list.
- Tagging data for improved search: Tags are filterable metatags that assist with the organization and discovery of data. Users associate tags that can be searched for quick access and identification of relevant data assets.
- Data profile views and sampling: Catalog profiles your datasets with statistics such as name, data type, sample values, most common values, and value frequency, and number of distinct values. Users select profile statistics of interest to uncover trends and anomalies in the data. See [*Managing field-level metadata and data profiling*](Profiling-data.htm) for field data visualizations and a list of available profile statistics.
- Dataset classifications: Data governance standards vary widely across regions and industries. Most data processes are impacted in some way by the need to secure data by limiting access. User-configurable classifications pertaining to regional and global data privacy and sensitivity standards and policies are provided to identify datasets with custom and sector-specific categories. See [*Managing dataset metadata*](managing-dataset-metadata.htm) to learn more.
- Create an application from your data: Qlik's data-first approach presents an option to upload data files and gain insight into your data before creating an application. This is a key element of the raw to analytics-ready workflow. See [*Creating an application from data*](../Apps/create-app-cloud-hub.htm#Creating_app_data) to create an application from data or see [*Adding data from uploaded data files*](../LoadData/adding-data-datafiles.htm) to upload data files to an existing application.
- Viewing the lineage of your data: You can view a lineage graph of your data, showing the upstream origins of your applications, datasets, and other analytics content. For more information, see [*Analyzing lineage in Analytics*](lineage.htm).
- Viewing the impact analysis of your data: You can view outputs and see the downstream impacts of applications, datasets, and other analytics content in the catalog. For more information, see [*Analyzing impact analysis in Analytics*](impact-analysis2.htm).

## Qlik Talend Cloud catalog tools

Depending on your license, the catalog may have additional tools available for your data:

- Data quality

  When looking at a dataset or a data product, you can get an idea of the quality of the data they contain, from the overall quality and freshness, to the number of empty or invalid row for each field of a dataset. For more information, see [*Assessing data quality*](../DataIntegration/DataProducts/Data-quality-and-data-discovery.htm).

  Information noteYou need one of the following subscriptions:
  - Qlik Talend Cloud Enterprise
  - Qlik Talend Cloud Premium
  - Qlik Cloud Analytics Premium
  - Qlik Cloud Analytics Enterprise
  - Qlik Sense Enterprise SaaS
- Data products

  Seamlessly access and utilize data products built and activated on the data integration side. View comprehensive details, including descriptions, purpose, and contact information for inquiries, supported by related documentation and quality metrics. For more information, see [*Creating data products*](../DataIntegration/DataProducts/Creating-data-products.htm).

  Information noteYou need one of the following subscriptions:
  - Qlik Talend Cloud Enterprise
  - Qlik Talend Cloud Premium
  - Qlik Cloud Analytics Premium
  - Qlik Cloud Analytics Enterprise
  - Qlik Sense Enterprise SaaS
- Publishing data and lineage from Talend Studio

  You can publish datasets from Data Integration Jobs in Talend Studio to Qlik Cloud including lineage, and impact analysis. You can view the lineage of your data that tracks the transformations backwards to the original source in the Catalog page of Qlik Cloud. For more information, see [Publishing datasets and lineage to Qlik Cloud](/talend/en-US/studio-user-guide/8.0-R2025-04/publishing-datasets-and-lineage-to-qlik-cloud).

  Information noteThis requires Qlik Talend Cloud Premium or Qlik Talend Cloud Enterprise.

Related learning:

- [How do I use the Data Catalog to profile data?](/lnk/How_use_datacatalog_profile_data)
