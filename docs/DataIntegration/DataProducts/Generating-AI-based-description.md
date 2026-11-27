---
title: "Generating an AI-based description"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Generating-AI-based-description.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Understanding your data with the catalog"]
---

# Generating an AI-based description

You can generate an AI-based description to quickly get a precise description of a data product, a dataset and the dataset fields. The description is based on:

- For a data product containing less than 10 datasets: The name of each dataset and the schema.
- For a data product containing 10 or more datasets: The name of each dataset.
- For a dataset: The name of the dataset and the name of the fields.
- For a dataset field: The original name of the field and the native type.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

Once the description has been generated, you can still edit it.

Information note

After a description has been generated, it remains available in the system, even if you later turn off Enable cross-region inference, or no longer have permission to generate AI-based descriptions. The latest generated description, whether or not it has since been edited, stays accessible.

Text prompt and dataset information are sent to a third party generative AI (GenAI) model. The information is treated as customer data and will not be used to train Qlik Cloud or the GenAI model. For more information, see [*Information that is shared*](#shared-information).

Warning noteThis feature uses generative artificial intelligence (“GenAI”). It is the user’s responsibility to review and verify any GenAI output before using or sharing it, and to evaluate whether the use of it is appropriate for any particular use case and whether it complies with applicable laws.

Information noteThis feature is offered and supported in the English language only but it does not depend on the language of your data or of Qlik Talend Cloud. When the name of the dataset and the name of the fields are in English, the description is generated in English.

Qlik Cloud Government note

Generative AI-based description assistant is not available in Qlik Cloud Government.

## Activating the option

Before generating a description using AI, you must activate the option. Only a Tenant Admin can activate it.

To generate AI-based descriptions, turn on the toggle Enable cross-region inference. For more information about processing locations, see [*Enabling cross-region inference*](../../Admin/cross-region-data-processing.htm).

## Generating the description of a data product

You can generate the description when you create the dataset or data product, or edit it later.

As the description is based on the names of the datasets, the data product must contain at least one dataset. Otherwise, you cannot generate the description.

1. From the Catalog or Data products menu, open a data product.
2. Click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png), and Edit.
3. Click Generate description.
4. When the description is generated, review it.
5. If needed, edit the description.
6. Rate the description. It helps enhance the quality of the generated descriptions.
7. Click Save to apply the description.

When a data product is activated on the Data marketplace, the description is also updated and visible by other users of the data marketplace. For more information, see [*Activating data products to the data marketplace*](../Marketplace/Consuming-in-data-marketplace.htm).

## Generating the description of a dataset and the dataset fields

All descriptions are generated at the same time. You cannot generate a description for a dataset or a dataset field only.

You can generate the descriptions when you create the dataset, or edit them later.

1. From the Catalog or Data products menu, open a dataset.
2. Click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png), and Edit.
3. On the top right, click Generate all.
4. When the descriptions are generated, review them.

   When a description has already been manually entered or generated, the AI-based description will not overwrite it. To generate all descriptions using AI, clear all descriptions and generate them again.
5. If needed, edit the description and click Generate all to apply your changes.
6. Rate the description of the dataset. It helps enhance the quality of the generated descriptions.
7. Click Save to apply the descriptions.

Tip noteYou can also edit the field description from the Profile and Data preview tabs.

## Information that is shared

The following information is shared with the Generative AI model to generate the description:

- For datasets: The dataset name and the field names.
- For dataset fields: The original name of the fields and the native types.
- For data products: The name of each dataset and the schema.

## Usage limitations

Timeout error: When the generation takes more than one minute, it fails. Remove some fields from the dataset and try again.
