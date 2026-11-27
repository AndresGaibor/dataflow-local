---
title: "Troubleshooting semantic models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/semantic-models-troubleshooting.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Working with data products", "Semantic models in data products"]
---

# Troubleshooting semantic models

## Invalid expression in measure or dimension

**Symptom**: A measure or dimension shows a validation error.

**Cause**: The expression contains a syntax error, references a field that does not exist, or uses an unsupported function.

**Resolution**:

- Check the error message for details about the issue.
- Ensure that the referenced fields exist in the tables included in the semantic model.
- Confirm that function names are spelled correctly and use supported Qlik functions.

## Table cannot be added

**Symptom**: A table from a dataset cannot be added to the semantic model.

**Cause**: The dataset may be inaccessible, or you may not have permission to view the dataset.

**Resolution**:

- Verify that the dataset is included in the data product.
- Check that you have access to the data space containing the dataset.
- Contact the dataset owner to request access if needed.

## Changes not reflected in consuming applications

**Symptom**: Applications that consume the semantic model do not show recent changes.

**Cause**:The data product may not have been reloaded. In a published application, inherited master items remain fixed to the version of the data product used when the application was published. Reloading a published application does not create, update, or delete master items from the data product.

**Resolution**:

- For an unpublished application: Make any changes needed, and then reload the application.
- For a published application: Update the application and publish it again to use new or changed measures and dimensions.
