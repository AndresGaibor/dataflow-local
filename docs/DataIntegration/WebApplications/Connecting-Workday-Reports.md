---
title: "Workday Reports"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Workday-Reports.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# Workday Reports

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual.

The Workday Reports connector, unlike the general Workday connector, is specifically designed for use with Workday Report as a Service (RaaS). It is a feature that exposes reports as web services. To use the Workday Reports connector, you need your custom reports URLs to integrate your reports data that is mainly aggregated data to the destinations. The Workday Reports connector must be used only when you have set up the Workday RaaS and want to integrate your custom reports data to destinations. In other cases, it is recommended to use the general [*Workday*](Connecting-Workday.htm) connector.

Some datasets are supported, see [List of supported datasets.](#List)

- For more information about connecting to SaaS applications, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).
- For more information about Lite connectors, see [*SaaS application Lite connectors*](../Landing/connecting-web-applications.htm#SaaS2)
- Depending on your use case, you might need to install Data Movement gateway to move data from SaaS applications. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

## Preparing for authentication

To access your Workday Reports data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You need access to a Workday Integrated System User (ISU). To create an ISU you need to be logged into Workday as a user with administrative access.

1. Use the search bar to find Create Integration System User and select it.
2. Add the newly created user to the list of System Users.
3. Search for Create Security Group, and create a new User-Based Security Group.
4. Add the user you created to the group you created.

Information noteWorkday does not allow to sync the reports whose size exceed 2 GB.

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
| Username | ISU user name. |
| Password | Password for the ISU. |
| Report URLs | List of report URLs, each separated by a space character. Example:  https://services1.myworkday.com/ccx/service/customreport2/vhr\_xyz/QW/HC\_Report\_-\_Published https://services1.myworkday.com/ccx/service/customreport2/vhr\_xyz/QW/HC\_Different\_Report |
| Start Date | Start date for reports that accept date filtering, in the format `YYYY-MM-DD`. Example: 2024-07-26 |

## List of supported datasets

- Financial Management Cost Centers: [Get Cost Centers](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Cost_Centers.html), CDC is not supported
- Financial Management Customer Categories: [Get Customer Categories](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Customer_Categories.html), CDC is not supported
- Financial Management Fund Hierarchies: [Get Fund Hierarchies](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Fund_Hierarchies.html), CDC is not supported
- Financial Management Fund Types: [Get Fund Types](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Fund_Types.html), CDC is not supported
- Financial Management Funding Sources: [Get Funding Sources](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Funding_Sources.html), CDC is not supported
- Financial Management Funds: [Get Funds](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Funds.html), CDC is not supported
- Financial Management Journal Sources: [Get Journal Sources](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Journal_Sources.html), CDC is not supported
- Financial Management Journals: [Get\_Journals](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Journals.html)
- Financial Management Ledger Account Summaries: [Get Ledger Account Summaries](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Ledger_Account_Summaries.html), CDC is not supported
- Financial Management Ledgers: [Get Ledgers](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Ledgers.html), CDC is not supported
- Financial Management Organizations: [Get Organizations](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Organizations.html), CDC is not supported
- Financial Management Position Budgets: [Get Position Budgets](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Position_Budgets.html), CDC is not supported
- Financial Management Program Hierarchies: [Get Program Hierarchies](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Program_Hierarchies.html), CDC is not supported
- Financial Management Programs: [Get Programs](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Programs.html), CDC is not supported
- Financial Management Revenue Categories: [Get Revenue Categories](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Revenue_Categories.html), CDC is not supported
- Financial Management Revenue Category Hierarchies: [Get Revenue Category Hierarchies](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Revenue_Category_Hierarchies.html), CDC is not supported
- Financial Management Spend Category Hierarchies: [Get Spend Category Hierarchies](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Spend_Category_Hierarchies.html), CDC is not supported
- Financial Management Supplier Categories: [Get Supplier Categories](https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Get_Supplier_Categories.html), CDC is not supported
- Human Resources Job Categories: [Get Job Categories](https://community.workday.com/sites/default/files/file-hosting/productionapi/Human_Resources/v38.2/Get_Job_Categories.html), CDC is not supported
- Human Resources Job Family Groups: [Get Job Family Groups](https://community.workday.com/sites/default/files/file-hosting/productionapi/Human_Resources/v38.2/Get_Job_Family_Groups.html), CDC is not supported
- Human Resources Job Profiles: [Get Job Profiles](https://community.workday.com/sites/default/files/file-hosting/productionapi/Human_Resources/v38.2/Get_Job_Profiles.html), CDC is not supported
- Human Resources Locations: [Get Locations](https://community.workday.com/sites/default/files/file-hosting/productionapi/Human_Resources/v38.2/Get_Locations.html), CDC is not supported
- Human Resources Workers: [Get\_Workers](https://community.workday.com/sites/default/files/file-hosting/productionapi/Human_Resources/v38.2/Get_Workers.html), CDC is not supported
- Staffing Organizations: [Get\_Organizations](https://community.workday.com/sites/default/files/file-hosting/productionapi/Staffing/v38.2/Get_Organizations.html), CDC is not supported
