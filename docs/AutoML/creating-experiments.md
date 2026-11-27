---
title: "Creating experiments"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/creating-experiments.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments"]
---

# Creating experiments

You can create new experiments in personal spaces or shared spaces for collaboration.

## Requirements and permissions

To learn more about the user requirements for working with ML experiments, see [*Working with experiments*](working-with-experiments.htm).

## Creating experiments

You create experiments from the Analytics [activity center](#glossary-0 "Glossary term").

Do the following:

1. Go to the Create page of the Analytics activity center and select ML experiment.

   Tip note

   Other ways to create ML experiments:

   - Go to Predict and select ML experiment. Alternatively, in Catalog, click Create new > ML experiment.
   - In the Analytics activity center, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a data product and select Use in > ML experiment.
2. Enter a name and space, and, optionally, a description and tags.
3. Click Create.

   The Open experiment checkbox is selected by default. If you deselect this checkbox, you must open the experiment manually before proceeding to the next step.
4. Select a dataset to use in your experiment. You can choose from:

   - Datasets: Select a dataset in any space you can access. See [*Tips and guidelines for uploading and selecting datasets*](#Tips).
   - Data products: Select a dataset from an active data product you can access. For more information about data products, see [*Creating data products*](../DataIntegration/DataProducts/Creating-data-products.htm).

The next step in the process is to configure the experiment. See [*Configuring experiments*](configuring-experiments.htm).

### Tips and guidelines for uploading and selecting datasets

- Datasets can be uploaded via the Create page in the Analytics activity center, and are visible in the catalog.
  You can also upload a new dataset directly into the catalog from the experiment's dataset selection page. To do so, click Upload file and choose the file to upload.
- Any flat file that can be uploaded and profiled in Qlik Cloud is supported for use in Qlik Predict.

  For multi-table files such as Microsoft Excel files with multiple sheets, only the first table will be imported. If data profiling fails for a table (for example, if it is empty), the file is not supported.

## Editing experiment name and other details

You can change the titles and descriptions of your ML experiments. You can also change the tags used with the ML experiments. Tags are used to group ML experiments with related content. When adding new tags to an ML experiment, users can view all tags that exist in the tenant.

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) by the experiment name.
2. Click ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit details.
3. Edit the name or other details.

## Sharing experiments

You can share an experiment by inviting a user, group, or everyone in your tenant to the space where it is stored.

Do the following:

1. In the catalog, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the item to be shared and select Share > Invite.
2. Search for users or groups by name or email address.
3. Select space permissions for the users or groups.
4. Or, select permissions for Anyone at <your tenant name> from the dropdown list.
5. Click Done.

The users receive access to the shared item and all other content in the space.

## Deleting experiments

You can delete an experiment from the catalog.

Related learning:

- [Introduction to Qlik Predict](/lnk/Introduction_Qlik_AutoML)

## Learn more

- [*Qlik Predict limitations and capacities*](ml-limitations-capacities.htm)
- [Introduction to Qlik Predict](/lnk/Introduction_Qlik_AutoML)
