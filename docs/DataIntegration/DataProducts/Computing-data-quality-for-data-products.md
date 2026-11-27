---
title: "Computing data quality for data products"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Computing-data-quality-for-data-products.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Working with data products"]
---

# Computing data quality for data products

You can compute data quality for all datasets of a data product at once from the Data products page, so you can quickly assess dataset health without opening each dataset individually.

Computing quality for data products can also be performed through the corresponding [Qlik Public API](https://qlik.dev/apis/rest/data-governance/data-products/).

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

1. From Qlik Talend Data Integration > Data products, open the data product overview.
2. Click Refresh quality (top right).

   In the Quality column, each dataset shows Computing... while the computation runs.

   When the computation is complete, the Quality column displays the quality bar for each dataset.

To customize how quality is computed for an individual dataset, see [*Configuring data quality*](Configuring-data-quality.htm).
