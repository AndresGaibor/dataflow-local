---
title: "Working in spaces in Data Integration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataSpaces/working-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections"]
---

# Working in spaces in Data Integration

Spaces are areas of Qlik Talend Data Integration that are used to create and store projects. Inside the space, you can also create new connections using connectors, and manage access to Data Movement gateways. You can use your Personal space, or governed data spaces.

For more information about Qlik Talend Data Integration, see [*Integrating data*](../Introduction/Data-services.htm).

## Personal space

Your Personal space is your own private work area. You cannot create projects in your personal space, or share resources from your personal space.

Information noteWe recommend that you do not use the personal space in data integration projects.

## Data spaces

Data spaces are governed areas that are used to create and store Qlik Talend Data Integration projects. Inside the space, you can also create new connections using connectors, and manage access to Data Movement gateways. Data spaces are indicated by ![Database icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_outline.svg).

Access to a data space is determined by membership to the space. Access to the resources inside a data space is determined by roles assigned to members of the space. This means that a user must first be a member of the data space, and second, have the required roles to create, manage, or monitor resources in a data space. Members with the roles to consume resources can also use resources from a data space when building applications in personal, shared, and managed spaces.

- Click Create data space in Data Integration Home .

### Shared data space

When you deploy a new tenant with Qlik Talend Data Integration, a shared data space named Default\_Data\_Space is created by default. All users in the tenant are members with the following roles:

- Can view
- Can consume data
- Can edit
- Can manage
- Can operate

Default\_Data\_Space is owned by the first admin created in the tenant.

### [*Managing spaces*](manage-data-space.htm)

To manage a data space, you must be a tenant admin, a data admin, or the space owner. Members of the data space who have the Can manage role can also manage the space.

### [*Data space roles and permissions*](permissions-data-space.htm)

You can add members to the data space and assign them roles inside the space. Space roles are defined by a set of permissions on the data space, and the resources inside the space.

Related learning:

- [Differentiate and manage Qlik Cloud spaces](/lnk/Differentiate_manage_spaces)
