---
title: "Viewing and managing datasets in the catalog"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/managing-datasets-catalog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Understanding your data with catalog tools"]
---

# Viewing and managing datasets in the catalog

Depending on your permissions in the space containing the datasets, you can view and manage datasets in the catalog. You can:

- Upload datasets and manage their file formatting

  Add datasets to Qlik Cloud. Edit their formatting setting to resolve anomalies or fix formatting issues.

  [*Uploading datasets and editing file format settings*](file-format-settings.htm)
- Manage metadata on the dataset level

  Profile and refresh dataset metadata. Apply tags and classifications.

  [*Managing dataset metadata*](managing-dataset-metadata.htm)
- Manage metadata on the field level

  View profiled field metadata. Add field aliases. Apply tags and classifications.

  [*Managing field-level metadata and data profiling*](Profiling-data.htm)

Viewing and managing datasets in different spaces requires different space permissions.

## Permissions for viewing and managing datasets

You can view and manage datasets in your personal space. To interact with datasets in shared and managed spaces, you require specific permissions in those spaces.

Information noteThis section only lists permissions for actions that are possible via the user interface. It does not list permissions for actions that are possible via API only.

### Viewing datasets and metadata

Space permissions are required in a space to view datasets and dataset metadata. Your permissions in the space must allow you to List and use data source in the space. In shared spaces, the following user roles allow you to view datasets and metadata:

- Owner
- Can manage
- Can edit
- Can edit data in applications
- Can consume data

In managed spaces, the following user roles allow you to view datasets and metadata:

- Owner
- Can manage
- Can consume data
- Can operate

For more information, see [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm) or [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm).

Information noteTenant and analytics admins can view datasets and [dataset](#glossary-0 "Glossary term") metadata belonging to other spaces (personal, shared, or managed), but they cannot apply classifications, use Create app from data, or Profile the datasets.

### Profiling and sampling datasets

Permissions are required to profile and sample data, as well as managing field-level metadata. You must have a role in the dataset's space that allows you to profile data sources.

In shared spaces, the following user roles allow you to apply classifications and tags to datasets:

- Owner
- Can manage
- Can edit
- Can edit data in applications

In managed spaces, the following user roles allow you to apply classifications and tags to datasets:

- Owner
- Can manage
- Can consume data
- Can operate

For more information, see [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm) or [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm).

### Applying classifications, regulations, and tags to datasets

Permissions are required to:

- Apply classifications to dataset fields, and to edit them.
- Apply and edit regulations to datasets, and to edit them.
- Apply tags to datasets, and to edit them.

Look for the permission Edit and apply properties to data source in the space for details in these topics: [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm) or [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm).

In shared spaces, the following user roles allow you to apply classifications and tags to datasets:

- Owner
- Can manage
- Can edit
- Can edit data in applications

In managed spaces, the following user roles allow you to apply classifications and tags to datasets:

- Owner
- Can manage
- Can operate
