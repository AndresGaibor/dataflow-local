---
title: "Extracting data products from analytics applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/extracting-data-products.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Working with data products"]
---

# Extracting data products from analytics applications

[Feature in Preview](../../Introduction/feature-preview-program-overview.htm)

You can extract a data product from an existing analytics application. The data product is extracted with its data and corresponding semantic model (a reusable data model defining relationships, dimensions, and measures).

## Prerequisites

Prerequisites for extraction:

- The application must be in a non-managed space (shared or personal space).
- You must have Can edit data in applications permission (script editing access) in the space.

## How extraction works

When you extract a data product from an application, the following happens:

1. A script asset is created and then run.
2. This script run produces new QVD data files in the target space.
3. A new data product is created with a semantic model based on your application's structure.

Extracting a data product from an application triggers a data reload that consumes your reload quota. Each extraction run processes the application's data model, relationships, and master items, which counts toward capacity-based license consumption. Plan extractions accordingly, especially for large applications.

## Extracting a data product from an application

You can extract a data product in several ways.

### In the application

Do the following:

1. Open the analytics application that contains the data and semantic model information you want to extract.
2. Open the ... menu next to the application title and then click Details to open the application details.

   ![Opening application details](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/semantic-model-app-details.png)
3. In the Details right panel, open the ... menu next to the application title, click Manage, and then Extract and create data product.

   ![Extracting a data product](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/semantic-model-app-details_2.png)
4. Review the extraction preview, showing which assets will be created in the process.

   ![Extraction preview](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/semantic-model-extract-data-product.png)

   Note that extracting the application will trigger a data reload that consumes your reload quota. For information about how reloads impact your capacity, see [*Reloading application data*](../../Apps/reloading-apps-cloud-hub.htm).
5. Enter a name for the new data product.
6. Select the personal, shared, or data space where the data product, script, and datasets will be created.

   Extraction is not available in managed spaces due to script access restrictions. To extract a data product, move or copy the application to a shared or personal space first.
7. Click Extract.
8. When the process is finished, click the Log button to view a recap of what happened.

### In your activity center

Do the following:

1. In the Analytics or Insights [activity center](#glossary-0 "Glossary term"), find the analytics application that contains the data and semantic model information you want to extract.
2. Click ![More actions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application.
3. Select Manage > Extract and create data product.
4. In the dialogs, follow the process as described in the [*In the application*](#App) section.

## Limitations

- Extracting of data products is not supported for applications that use section access.
- Cyclic and drill-down dimensions in applications cannot be exported to a data product.
- Application with load scripts containing Exit script statements are not supported for extraction.
- Extraction is not supported for measures with Custom number formatting.
- Extraction from applications that load data via a relative data connection (for example: `lib://:DataFiles/Color.QVD`) is only supported if the data product is extracted to the same space as the application.
