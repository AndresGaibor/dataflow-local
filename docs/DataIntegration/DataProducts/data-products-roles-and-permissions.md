---
title: "Data products roles and permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/data-products-roles-and-permissions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Working with data products"]
---

# Data products roles and permissions

The access to datasets in data products depend on roles, permissions and spaces. The following sections help you configure your data products to share your data properly.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

## Best practices

To simplify the usage of the data products, here is a few best practices:

- Document the roles and spaces: Explain in the documentation of the data product what each space role enables for the features of the data product.
- Use a simple configuration: In most use cases, the combination data space + shared space + managed space is sufficient.
- Create user groups: Assign users to groups with the space access required for their role.

## Understanding data product access across spaces

Data product may include datasets and metadata from multiple spaces. As each feature of a data product depends on where the resources are stored, the access depends on your role in each space, not only by your role in the managed space.

Dataset profiling and quality computation require that you have permissions both on the data space, which let you see the dataset, and the shared space, which lets you run or view profiling and quality jobs.

The following table summarizes the expected behavior when you deploy data products that span multiple spaces.

| Capability | Space | Space role required | Action |
| --- | --- | --- | --- |
| View data product in the marketplace | Managed space | Can consume data | Allows listing and previewing the data product, seeing descriptions and documentation |
| Consume data product in the application or using an API | Managed space | Can consume data | Allows application usage or endpoint access |
| Consume semantic model from data product | Managed space (or space containing data product) | Can consume data or Can view | Allows loading semantic models via Data Catalog and using inherited master items |
| View dataset metadata and lineage | Data space | Can view | Shows dataset metadata, lineage and impact included in the data product |
| View dataset trust score | Data space | Can view | Shows trust score for datasets |
| View dataset quality metrics | Shared space (for the connection) | Can consume data | Displays quality dashboards and metrics for dataset profiles and quality |
| Compute/Refresh quality | Shared space (for the connection) | Can consume data | Allows triggering quality refresh jobs |
| View dataset profile | Data space and shared space | Can consume data in both spaces | Profiles require dataset access in the data space combined with connection access in the shared space |

## Deploying data products with access for all

This procedure lets you share data products with all users to let them:

- See the data product in the marketplace.
- Browse lineage and metadata.
- View data quality and profile information.

1. In one data space, create the datasets.
2. In one shared space, create connections used for data quality and profiling.
3. Assign the Can consume data space role to the users in all spaces: the managed space, the data space, and the shared space.

## Deploying data products with restricted access

This procedure lets you control the access of datasets with different sensitivity or audience requirements.

1. Store the sensitive datasets in separate data spaces with restricted audience.
2. Use shared spaces for connections that compute data quality, trust scores, and profiles.
3. Assign roles per space depending on the access policy:
   - For general users: Can view in the data spaces.
   - For advanced users: Can consume data in the other spaces.

When a user does not have access to some datasets in a data product, a message indicates that restricted content exists but cannot be opened.

## Authorized actions depending on your roles

The following tables describe what actions you can take with data products, depending on your permissions. "Consuming" a data product means you can either create an application from it, or use its data access endpoints.

To edit, delete, deactivate, or activate a data product, you need an edit role for the relevant space. For deactivating, or activating a data product in a managed space, you also need a publish role on that space.

For more details about the permissions required for data product users and administrators, see [*Default permissions and custom roles*](../../Admin/permissions-scopes-capacity-model.htm).

### I open a data product on a managed space

| Action | User allowed to manage data products | User allowed to consume data products |
| --- | --- | --- |
| View a data product | Yes | Yes |
| Consume a data product | Yes | Yes |
| Edit a data product | No | No |
| Delete a data product | No | No |
| Deactivate a data product | Yes | No |
| Activate a data product | No | No |
| Update the marketplace | Yes | No |

### I open a data product on a personal/shared/data space

| Action | User allowed to manage data products | User allowed to consume data products |
| --- | --- | --- |
| View a data product | Yes | Yes |
| Consume a data product | Yes | Yes |
| Edit a data product | Yes | No |
| Delete a data product | Yes | No |
| Deactivate a data product | Yes | No |
| Activate a data product | Yes | No |
