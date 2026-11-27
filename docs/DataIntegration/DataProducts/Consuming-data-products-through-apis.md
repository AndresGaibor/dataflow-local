---
title: "Consuming data products through APIs"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Consuming-data-products-through-apis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Working with data products"]
---

# Consuming data products through APIs

Activate API endpoints to query, filter, and consume your data across tools and ecosystems. Once the endpoints are activated, you can access your data through OData-compliant APIs.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

## Activating the API endpoints

Information noteYou need the permission to manage data products.

1. From the Data products menu, click the data product for which you want to activate API endpoints.
2. From the Overview tab, click Edit > API endpoints.

   The Edit data product window opens.
3. Select the datasets for which you want to activate API endpoints.
4. Click Save.

   You are back to the Overview tab and the API endpoints option is available in the Actions menu in the top-right corner.

   The API endpoints are created and you can configure them.

When the data product is activated on the marketplace, the API endpoints are also activated in the active version on the marketplace.

## Configuring the API endpoints

After you activated the API endpoints, you can configure the connection that must be used to consume the datasets.

File-based endpoints are consumed in the same storage as for the dataset.

1. From the Overview tab, click ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) > Use in > API endpoints.

   The API endpoints window is open.
2. If necessary, select another connection.

   Your changes are automatically saved.

## Using the APIs

Once the API endpoints are activated, you can use queries to consume your data in other tools.

The OData protocol is used. For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/odata/overview).

The format of a query in Power Query or PowerBI is:`= OData.Feed("url-of-the-dataset", null, [Headers = [Authorization = "Bearer your-api-key"]])`

You need to adapt the following to your usage:

- `url-of-the-dataset`. Replace this part by the URL from the API endpoints window.

  ![Dataset URL in the API endpoints window](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/di-endpoints-url.png)
- `your-api-key`. Replace this part by your API key.

Warning noteYou can use the APIs to read your data only, not write some.

1. Activate the API endpoints. See the procedure above.
2. Generate an API key if you do not have one already. For more information, see [Generating and managing API keys](../../Admin/mc-generate-api-keys.htm).
3. Open the tool of your choice to fetch the data. In this example, PowerBI is used.
4. Click Get Data > Blank query.
5. Enter the query.

   Here is an example of a query that you can adapt and use in Power Query or PowerBI to retrieve data from one dataset.

   `= OData.Feed("https://qcs.us.qlikcloud.com/api/data-governance/data-access/data-products/687e50d58d4773120e843007/datasets/687e508ee636a966d6a6f9e4/connections/9d0d8a52-33a8-4d46-be28-068b4fd06282", null, [Headers = [Authorization = "Bearer your-api-key"]])`
6. If you want to retrieve data from other datasets, create a query per dataset.
7. Click Close & Apply to apply your queries.
8. When the data is imported, define the relationships between the tables.
9. Click Manage relationships > New relationship.
10. Select the tables and save.
11. Create as many relationships as needed.

When the relationships are configured, you can view your data in charts.
