---
title: "GetSysAttr Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/GetSysAttr.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "System functions"]
---

# GetSysAttr Script and chart function

Expand/Collapse all

# GetSysAttr Script and chart function

The GetSysAttr() function is used to return information about the tenant and space in which an application is located. With the GetSysAttr() function, you can evaluate the tenant ID and name, space ID and name, and other details about the environment where the application resides. This function simplifies space and tenant identification of a Qlik Sense application that might be moved between different environments. The function makes it easy to identify the specific environment you are working in. This is particularly useful during the development, testing, acceptance and production (DTAP) stages of an application's life cycle.

This function can be used in the application's load script or chart expressions, either directly as an expression or in an expression stored as a variable.
If you anticipate your application being moved between spaces or tenants during its life cycle, use the function in a chart expression to dynamically obtain space and tenant information without reloading the application. When doing so, store the function expression in a variable outside the load script, or use the function directly in the chart expression.

Use GetSysAttr() to determine the following information about your application:

- The ID of the tenant where the application is located.
- The name of the tenant where the application is located.
- The URL of the tenant where the application is located.
- The alias URL that has been defined for the tenant containing the application.
- The region of the tenant that contains the application.
- The ID of the space where the application is located.
- The name of the space where the application is located.
- The type of the space (shared or managed) where the application is located.

The GetSysAttr() function can be used directly in the [load script](#glossary-0 "Glossary term") or in a chart expression. In either case, you can use the function to store attributes in a variable, or directly without a variable.

If you use this function in Qlik Sense Client-Managed, it only returns empty data values. Therefore, you can use the function to develop scripts in Qlik Sense Client-Managed without encountering errors, with the intention of later uploading the applications to Qlik Cloud.

Syntax:

GetSysAttr(name)

Return data type: dual

Arguments

| Argument | Description |
| --- | --- |
| name | The name of the attribute to return. Enter as a string value in the expression. The string value entered is case-sensitive. |

You can use the function to load environment attributes into your application. The function can return the following attributes:

Environment attributes that can be returned by the GetSysAttr() function

| Attribute | Description | Example of load script variable | Example of chart expression (no variable) |
| --- | --- | --- | --- |
| tenantId | The [tenant](#glossary-2 "Glossary term") ID. | Let vTenantID = GetSysAttr('tenantId') | =GetSysAttr('tenantId') |
| tenantName | The name of the tenant. | Let vTenantName = GetSysAttr('tenantName') | =GetSysAttr('tenantName') |
| tenantUrl | The default URL for the tenant. | Let vTenantUrl = GetSysAttr('tenantUrl') | =GetSysAttr('tenantUrl') |
| tenantUrlAlias | The alias URL that has been defined for the tenant. | Let vTenantUrlAlias = GetSysAttr('tenantUrlAlias') | =GetSysAttr('tenantUrlAlias') |
| tenantRegion | The region in which the tenant resides. | Let vTenantRegion = GetSysAttr('tenantRegion') | =GetSysAttr('tenantRegion') |
| spaceId | The space ID. This is only defined for an application in a [shared](#glossary-3 "Glossary term") or [managed space](#glossary-4 "Glossary term").  Information note If the GetSysAttr() function returns an empty spaceId value in Qlik Cloud, this indicates that the application is located in a [personal space](#glossary-5 "Glossary term").  The GetSysAttr() function always returns an empty spaceId value when used in Qlik Sense Client-Managed. | Let vSpaceId = GetSysAttr('spaceId') | =GetSysAttr('spaceId') |
| spaceName | The name of the space. This is only defined for an application in a shared or managed space.  Information note If the GetSysAttr() function returns an empty spaceName value in Qlik Cloud, this indicates that the application is located in a personal space.  The GetSysAttr() function always returns an empty spaceName value when used in Qlik Sense Client-Managed. | Let vSpaceName = GetSysAttr('spaceName') | =GetSysAttr('spaceName') |
| spaceType | The type of space in which the application is located. This is only defined for an application in a shared or managed space.  Information note If the GetSysAttr() function returns an empty spaceType value in Qlik Cloud, this indicates that the application is located in a personal space.  The GetSysAttr() function always returns an empty spaceType value when used in Qlik Sense Client-Managed. | Let vSpaceType = GetSysAttr('spaceType') | =GetSysAttr('spaceType') |

## Example 1 – Storing environment attributes as load script variables

Load script and variables

In this example, we define a set of script [variables](#glossary-6 "Glossary term") that can be used in the application content you create. Each time the application is reloaded, the attributes are evaluated and added to the application.

Do the following:

1. Create a new Qlik Sense application in a shared space.
2. Open the Data load editor.
3. Paste the following load script into a new tab:

   ```
   Transactions:

   Load * inline [
   id,date,amount
   1,1/1/2023,500.67
   2,1/2/2023,458.91
   3,1/3/2023,12.34
   4,1/4/2023,90.90
   5,1/5/2023,256.30
   6,1/6/2023,789.16
   7,1/7/2023,501.25
   8,1/8/2023,87.01
   9,1/9/2023,161.16
   10,1/10/2023,300.06
   ];

   Let vTenantId = GetSysAttr('tenantId');
   Let vTenantName = GetSysAttr('tenantName');
   Let vTenantUrl = GetSysAttr('tenantUrl');
   Let vTenantUrlAlias = GetSysAttr('tenantUrlAlias');
   Let vTenantRegion = GetSysAttr('tenantRegion');
   Let vSpaceId = GetSysAttr('spaceId');
   Let vSpaceName = GetSysAttr('spaceName');
   Let vSpaceType = GetSysAttr('spaceType');
   ```

This load script contains the following:

- A new table, called Transactions, contains sample transaction data. This could be replaced with any data, and is added as a placeholder.
- A series of script variable definitions, for the available attributes that can be fetched by GetSysAttr().

Load the data and open a new [sheet](#glossary-7 "Glossary term") in advanced edit mode.

Create a table and add the following expressions as [dimensions](#glossary-8 "Glossary term"), along with their respective labels:

- =vTenantId, with label Tenant ID
- =vTenantName, with label Tenant Name
- =vTenantUrl, with label Tenant URL (Default)
- =vTenantUrlAlias, with label Tenant URL (Alias)
- =vTenantRegion, with label Tenant Region
- =vSpaceId, with label Space ID
- =vSpaceName, with label Space Name
- =vSpaceType, with label Space Type

You now have a table in your application that dynamically displays each of the available environment attributes. Exporting the application and uploading it to a different tenant and space would give you these attributes for the newly uploaded version of the application.

## Example 2 – Storing environment attributes as variables and using them in chart expressions

Chart expressions and results

In this example, rather than defining variables in the script, we define several variables using the dialog in advanced edit mode. The variables can then be used in chart expressions in the application.

Do the following:

1. Create a new Qlik Sense application in a shared space.
2. Open a new sheet in advanced edit mode.
3. Click ![Variables](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) to open the variables dialog.
4. Click Create new.
5. Under Name, enter vTenantId.
6. Under Definition, enter =GetSysAttr('tenantId').
7. Click Create.

This creates an application variable to display the ID of the tenant. Repeat steps 3 to 6 to create a variable for each of the remaining attributes. Use the following parameters:

- Tenant Name

  - Name: vTenantName
  - Definition: =GetSysAttr('tenantName')
- Tenant URL

  - Name: vTenantUrl
  - Definition: =GetSysAttr('tenantUrl')
- Tenant URL Alias

  - Name: vTenantUrlAlias
  - Definition: =GetSysAttr('tenantUrlAlias')
- Tenant Region

  - Name: vTenantRegion
  - Definition: =GetSysAttr('tenantRegion')
- Space ID

  - Name: vSpaceId
  - Definition: =GetSysAttr('spaceId')
- Space Name

  - Name: vSpaceName
  - Definition: =GetSysAttr('spaceName')
- Space Type

  - Name: vSpaceType
  - Definition: =GetSysAttr('spaceType')

Create a table and add each of following expressions as dimensions, along with their respective labels:

- =vTenantId, with label Tenant ID
- =vTenantName, with label Tenant Name
- =vTenantUrl, with label Tenant URL (Default)
- =vTenantUrlAlias, with label Tenant URL (Alias)
- =vTenantRegion, with label Tenant Region
- =vSpaceId, with label Space ID
- =vSpaceName, with label Space Name
- =vSpaceType, with label Space Type

You now have a table in your application, dynamically displaying each of the available environment attributes. Exporting the application and uploading it to a different tenant and space would give you these attributes for the newly uploaded version of the application.

The main benefit of using the function in chart expressions is that the application does not need to be reloaded for these attributes to be refreshed. This enables smoother movement of applications between tenants and spaces as part of the application life cycle.

## Example 3 – Using the function directly in the load script

Load script and results

You can also use the function in your applications without a variable. This example demonstrates how to load a table with each attribute as an individual [field](#glossary-9 "Glossary term"). From here, you can create [visualizations](#glossary-10 "Glossary term") in the application to display these details.

Do the following:

1. Create a new Qlik Sense application in a shared space.
2. Open the Data load editor.
3. Paste the following load script into a new tab:

   ```
   Attributes:

   Load RowNo() as Key,
   GetSysAttr('tenantId') as TenantID,
   GetSysAttr('tenantName') as TenantName,
   GetSysAttr('tenantUrl') as TenantUrl,
   GetSysAttr('tenantUrlAlias') as TenantUrlAlias,
   GetSysAttr('tenantRegion') as TenantRegion,
   GetSysAttr('spaceId') as SpaceID,
   GetSysAttr('spaceName') as SpaceName,
   GetSysAttr('spaceType') as SpaceType autogenerate 1;
   ```

Load the data. A table is created in the data model, displaying each of the attributes in individual fields.

Now you can use the attribute fields in visualizations, such as tables or text & image objects.

## Example 4 – Using the function directly in chart expressions

Load script and chart expression

You can enter the function directly into chart expressions without using a variable.

The main benefit of using the function in chart expressions is that the application does not need to be reloaded to refresh these attributes. This enables smoother movement of applications between tenants and spaces as part of the application life cycle.

Do the following:

1. Create a new Qlik Sense application in a shared space.
2. Open a new sheet in advanced edit mode.
3. Drag a Text & image object onto the sheet.
4. Click inside the blank chart to add text, and type:

   Tenant ID:
5. In the [properties](#glossary-11 "Glossary term") panel, click Add measure.
6. Enter the following expression:

   =GetSysAttr('tenantId')
7. Repeat these steps for the other attributes on new lines, using the expressions presented in the attributes table in the introduction of this help topic.
