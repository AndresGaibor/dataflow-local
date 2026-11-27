---
title: "Data space roles and permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataSpaces/permissions-data-space.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Working in spaces in Data Integration"]
---

# Data space roles and permissions

When you add members to a data space, you can assign them roles inside the space. Space roles are defined by a set of permissions on the data space, and the resources inside the space.

For more information about data spaces, see [*Working in spaces in Data Integration*](working-spaces.htm).

When you create a data space, you become the owner of the data space and all resources inside of that space. Space owners, tenant admins, and data admins can add members to the data space. Also, data space members who are granted the Can manage role can add other members to the space.

Warning noteIf a project is queried via the API, and you have permission to query the project, metadata for assigned objects is returned regardless of whether you have permission to access the objects directly. This includes, for example, connections, databases, and tables.

As data tasks operate in the context of the owner of the project they belong to, the following roles are required:

- The owner of a project must have the Can edit role in the space where the project resides. This allows the catalog to be updated with table metadata and ensures that storage (QVD) tasks in the project can create data files in the space.
- The owner of a project must have the Can consume data, Can edit, or Can manage role in the spaces that contain:

  - Target connections that are used in the project.
  - Source connections used in data tasks in the project.
- For any data task that uses connections through Data Movement gateway, the owner of the project must have the Can consume data, Can edit, or Can manage role in the space where the data gateway resides.

To create connections to access data through Data Movement gateway, the following roles are required for the user who creates the connection:

- Can manage on the space where you create the connection.
- Can consume data, Can edit, or Can manage on the space where the data gateway resides.

## Data space roles

Members of a data space can be assigned one or more of the following data space roles.

| Data space role | Summary |
| --- | --- |
| Is owner | This member can manage the space, all projects, data tasks and data resources inside the space, and its members. |
| Can view | This member can view projects, data tasks and data resources, but they cannot make changes. |
| Can view data | This member can view data in data tasks in the data space, for example, preview and samples of data. |
| Can consume data | This member can consume data from data tasks in the data space. |
| Can manage | This member can manage the space details and members. |
| Can operate | This member can view projects, and data tasks with basic details and perform actions, such as run, stop, and resume. |
| Can edit | This member can view and edit projects, and data tasks in this space, as well as create new data tasks. |

Information noteMembers must have the Can consume data role to use data tasks in applications. Applications that use data tasks from a data space that are shared with users who are not members of the data space can still view the application data but not the data source.

## Permissions for members of the data space

The following tables outlines what specific permissions are granted to a data space member with a particular role.

### Permissions on the data space

| Action | Is owner | Can view | Can consume data | Can manage | Can operate | Can edit |
| --- | --- | --- | --- | --- | --- | --- |
| See data space in Data Integration home | Yes | Yes | Yes | Yes | Yes | Yes |
| Change space name, description, members, and roles | Yes |  |  | Yes |  |  |
| Delete space | Yes |  |  | Yes |  |  |

### Permissions on projects

All permissions are granted on space level.

| Action | Is owner | Can view | Can consume data | Can manage | Can operate | Can edit |
| --- | --- | --- | --- | --- | --- | --- |
| List projects | Yes | Yes | Yes | Yes | Yes | Yes |
| Create project | Yes |  |  |  |  | Yes |
| Update project | Yes |  |  |  |  | Yes |
| Open project | Yes | Yes |  |  | Yes | Yes |
| Delete project | Yes |  |  |  |  | Yes |
| Operate project | Yes |  |  |  | Yes |  |
| Export project | Yes | Yes |  |  | Yes | Yes |

### Permissions on data tasks and data resources in the data space

All permissions are granted on space level.

To schedule periodical reloads for a landing data task, a member must have either the Can operate or Can edit role in the space.

| Action | Is owner | Can view | Can consume data | Can manage | Can operate | Can edit |
| --- | --- | --- | --- | --- | --- | --- |
| Create data task | Yes |  |  |  |  | Yes |
| List data tasks and information about tasks | Yes | Yes | Yes | Yes | Yes | Yes |
| Edit data task attribute | Yes |  |  |  |  | Yes |
| Open data task | Yes | Yes |  |  | Yes | Yes |
| Update data task | Yes |  |  |  |  | Yes |
| Delete data task | Yes |  |  |  |  | Yes |
| Control data task (run, stop, resume, reload, recreate, prepare) | Yes |  |  |  | Yes |  |
| List data resources (connections) | Yes | Yes | Yes | Yes | Yes | Yes |
| Add connection | Yes |  |  | Yes |  |  |
| Edit connection | Yes |  |  | Yes |  |  |
| Delete connection | Yes |  |  | Yes |  |  |
| View connection metadata | Yes | Yes |  |  |  | Yes |
| Manage connection metadata | Yes |  |  |  |  | Yes |

### Permissions on data products

All permissions are granted on space level.

| Action | Is owner | Can manage | Can edit | Can view | Can consume | Can operate |
| --- | --- | --- | --- | --- | --- | --- |
| List data product | Yes | Yes | Yes | Yes | Yes | Yes |
| Read data product | Yes | Yes | Yes | Yes | Yes | Yes |
| Create data product | Yes | No | Yes | No | No | No |
| Update data product | Yes | No | Yes | No | No | No |
| Delete data product | Yes | No | Yes | No | No | No |

## Permissions for users with security roles

The following tables outlines what specific permissions are granted to a user with a specific security role with regard to data spaces, data tasks and data resources in a data space.

### Permissions on data spaces with security roles

| Action | Tenant admin | Data admin | Data space creator |
| --- | --- | --- | --- |
| Create data space | Yes | Yes | Yes |
| See data space in Data Integration home | Yes | Yes |  |
| Change space name and description | Yes | Yes |  |
| Delete space | Yes | Yes |  |
| Change space owner | Yes | Yes |  |

### Permissions on projects with security roles

| Action | Tenant admin | Data admin |
| --- | --- | --- |
| List projects | Yes | Yes |
| Open project | Yes | Yes |
| Delete project | Yes | Yes |
| Change owner of project | Yes | Yes |

### Permissions on data tasks and data resources with security roles

| Action | Tenant admin | Data admin |
| --- | --- | --- |
| List data tasks and information about assets | Yes | Yes |
| Open data task | Yes | Yes |
| Delete data task | Yes | Yes |
| Change owner of data task | Yes | Yes |
| List data resources (connections) | Yes | Yes |
| Delete connection | Yes | Yes |
| Change owner of connection | Yes | Yes |
| Change space of connection | Yes | Yes |

### Permissions on data products with security roles

| Action | Tenant admin | Data admin |
| --- | --- | --- |
| List data products | Yes | Yes |
| Read data product | Yes | Yes |
| Create data product | No | No |
| Update data product | No | No |
| Delete data product | Yes | Yes |
