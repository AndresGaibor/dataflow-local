---
title: "Workday"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Workday.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# Workday

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual.

Workday is a cloud-based software that specializes in human capital management applications. You can land Human Resources data from Workday as a data source when landing or replicating data.

Tip noteIf you want to land Workday custom reports, see [*Workday Reports*](Connecting-Workday-Reports.htm).

- For more information about connecting to SaaS applications, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).
- For more information about Lite connectors, see [*SaaS application Lite connectors*](../Landing/connecting-web-applications.htm#SaaS2)
- Depending on your use case, you might need to install Data Movement gateway to move data from SaaS applications. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You need access to a Workday Integrated System User (ISU). To create an ISU you need to be logged into Workday as a user with administrative access.

1. Use the search bar to find Create Integration System User and select it.
2. Add the newly created user to the list of System Users.
3. Search for Create Security Group, and create a new User-Based Security Group.
4. Add the user you created to the group you created.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Fill in the required connection properties.
2. Provide a name for the connection in Connection name.
3. Select Open connection metadata to define metadata for the connection when it has been created.
4. Click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Tenant Name | Name of the Workday tenant. |
| Username | ISU user name. |
| Password | Password for the ISU. |
| Hostname | Host name. To find your host name:   1. In Workday, search for Public Web Services and open the report. 2. Open the menu for Human Resources. 3. Click Web Service, and then View WDSL. 4. Scroll to the bottom of the WDSL page to find the hostname, for example https://wd5-impl-services1.workday.com. |
| Version | Enter the version of your application. A version is given as a format example.  Example: v43.0. |
| Report Date | Date to start journal reports, in YYYY-MM-DD format. |
