---
title: "GetUserAttr Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/GetUserAttr.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "System functions", "sheet"]
---
Expand/Collapse all

# GetUserAttr Script and chart function

The GetUserAttr() function returns the following information for the user accessing an application:

- Email address
- Subject
- Groups the user belongs to, such as Identity provider (IdP) groups and custom groups
- Preferred language
- Time zone

Use the GetUserAttr() function directly in the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/GetUserAttr.htm#glossary-0 "Glossary term") or in a chart expression. In either case, you can use the function to store attributes in a variable, or directly without a variable. If you use this function in Qlik Sense Client-Managed, it returns only empty data values. Therefore, you can use the function to develop scripts in Qlik Sense Client-Managed without encountering errors, with the intention of later uploading the applications to Qlik Cloud.

Syntax:

GetUserAttr(name)

Return data type: dual

Arguments

| Argument | Description |
| --- | --- |
| name | The name of the attribute to return. Enter as a string value in the expression. The string value entered is case-sensitive. |

Use the function to load user attributes into your application. The function can return the following attributes:

User attributes that can be returned by the GetUserAttr() function

| Attribute | Description | Example of load script variable | Example of chart expression (no variable) | Example of chart expression results |
| --- | --- | --- | --- | --- |
| userEmail | The email of the current user. | `Let vUserEmail = GetUserAttr('userEmail')` | `=GetUserAttr('userEmail')` | `john.doe@company.com` |
| userSubject | The subject of the current user. | `Let vUserSubject = GetUserAttr('userSubject')` | `=GetUserAttr('userSubject')` | `00uss7ra3dk9doJln0x7` |
| userGroups | The groups (IdP, custom, or both) to which the current user belongs. Returns a comma-separated list of groups in a string. By default, `GetUserAttr` returns IdP groups unless the `QlikCloudGroupMode` system variable is set in a load script statement. [*QlikCloudGroupMode*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/QlikCloudGroupMode.htm). | `Let vUserGroups = GetUserAttr('userGroups')` | `=GetUserAttr('userGroups')` | `Sales,Product-Lead,OKTA-Github-RnD` |
| userLocale | The preferred language of the user, which is set in the user's **Settings**. [*Managing your personal settings*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/profile-settings.htm) | `Let vUserLocale = GetUserAttr('userLocale')` | `=GetUserAttr('userLocale')` | `en` |
| userZoneinfo | The time zone of the user, which is set in the user's **Settings**. [*Managing your personal settings*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/profile-settings.htm) | `Let vUserLanguage = GetUserAttr('userZoneinfo')` | `=GetUserAttr('userZoneinfo')` | `Europe/London` |

## When to use GetUserAttr

This function returns user properties and groups for the current user of the application. This allows you to build solutions that customize the content that appears for your users. For example, in a global sales application, you can show product-specific sheets to only those sales representatives who are responsible for a particular product group. Use the function in load statements in the application's load script or in chart expressions, either directly as an expression or in an expression stored as a variable.

[Video: https://share.vidyard.com/watch/bozy96G13YU5YrBjnqNNDF]

## Example – Storing user attributes as variables in the script

Load script variables and chart expressions

This example defines a set of script [variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/GetUserAttr.htm#glossary-2 "Glossary term") that can be used in the application content you create. Each time the application is reloaded, the attributes are evaluated and added to the application.

Do the following:

1. Create a new Qlik Sense application.
2. Open the Data load editor and add the load script below to a new section. The load script contains:

   - A new table, called `Transactions`, with sample transaction data. This could be replaced with any data, and is added as a placeholder.
   - A script statement that sets the `QlikCloudGroupMode` system variable to `2`. The `userGroups` attribute will return both the IdP and custom groups to which the user belongs.
   - A series of script variable definitions for the available attributes that the GetUserAttr function can return.

   ```
   Set QlikCloudGroupMode = 2;
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
   Let vUserEmail = GetUserAttr('userEmail');
   Let vUserSubject = GetUserAttr('userSubject');
   Let vUserGroups = GetUserAttr('userGroups');
   Let vUserLocale = GetUserAttr('userLocale');
   Let vUserZoneinfo = GetUserAttr('userZoneinfo');
   ```
3. Load the data and open a new [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/GetUserAttr.htm#glossary-3 "Glossary term") in advanced edit mode.
4. Create a table and add the following expressions as [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/GetUserAttr.htm#glossary-4 "Glossary term"):

- `=vUserEmail`
- `=vUserSubject`
- `=vUserGroups`, this returns a comma-separated list in a string
- `=vUserLocale`
- `=vUserZoneinfo`

> **Tip:** You can add a dimension label, such as User Email, for improved readability when you create the dimension.

The output in the table dynamically displays the available user attributes. The following table shows an example of results returned using the `GetUserAttr` function.

Results table

| =vUserEmail | =vUserSubject | =vUserGroups | =vUserLocale | =vUserZoneinfo |
| --- | --- | --- | --- | --- |
| john.doe@company.com | 00uss7ra3dk9doJln0x7 | Sales,Product-Lead,OKTA-Github-RnD | en | America/Toronto |

## Example – Storing user attributes as variables and using them in chart expressions

Variables and chart expressions

In this example, instead of defining variables in the load script, variables are defined in the application. Once defined, variables can be used in chart expressions in the application. The main benefit of using the function in chart expressions is that the attributes will automatically refresh without having to reload the application. This enables smoother movement of applications between users as part of the application life cycle.

Do the following:

1. Create a new Qlik Sense application.
2. Open a new sheet in advanced edit mode.
3. Open the variables dialog.
4. Select **Create new**, and then do the following:

   - Under **Name**, enter vUserEmail.
   - Under **Definition**, enter =GetUserAttr('userEmail').
   - Select **Create**.

An application variable is created to display the email address of the user. Repeat this step to create a variable for the remaining attributes using the following parameters:

- User Subject

  - **Name**: vUserSubject
  - **Definition**: =GetUserAttr('userSubject')
- User Groups

  - **Name**: vUserGroups
  - **Definition**: =GetUserAttr('userGroups')
- User Locale

  - **Name**: vUserLocale
  - **Definition**: =GetUserAttr('userLocale')
- User Zoneinfo

  - **Name**: vUserZoneinfo
  - **Definition**: =GetUserAttr('userZoneinfo')

5. Create a table and add the following expressions as dimensions:

- `=vUserEmail`
- `=vUserSubject`
- `=vUserGroups` (returns a comma-separated list in a string)
- `=vUserLocale`
- `=vUserZoneinfo`

> **Tip:** You can add a dimension label, such as User Email, for improved readability when you create the dimension.

The output in the new table dynamically displays the available user attributes. The following table shows an example of results returned from the `GetUserAttr` function.

Results table

| =vUserEmail | =vUserSubject | =vUserGroups | =vUserLocale | =vUserZoneinfo |
| --- | --- | --- | --- | --- |
| john.doe@company.com | 00uss7ra3dk9doJln0x7 | Sales,Product-Lead,OKTA-Github-RnD | en | America/Toronto |

> **Note:** By default, the `GetUserAttr('userGroups')` function returns the IdP groups for the user. You can choose which groups are returned by setting the `QlikCloudGroupMode` system variable in a script statement, for example `Set QlikCloudGroupMode = 2` returns both IdP and custom groups. For more information, see [*QlikCloudGroupMode*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/QlikCloudGroupMode.htm).

## Example – Using the GetUserAttr function in the load script

Load script

You can also use the function in your applications without a variable. This example demonstrates how to load a table with each attribute as an individual [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/GetUserAttr.htm#glossary-5 "Glossary term"). From here, you can create [visualizations](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/GetUserAttr.htm#glossary-6 "Glossary term") in the application to display these details.

Do the following:

1. Create a new Qlik Sense application.
2. Open the Data load editor and add the load script below to a new section. The load script contains:

   - A new table called `Attributes`, that contains each attribute as a field.
   - A script statement that sets the `QlikCloudGroupMode` system variable to `1` for custom groups. The `userGroups` attribute will return only the custom groups to which the user belongs.

   ```
   Set QlikCloudGroupMode = 1;
   Attributes:
   Load RowNo() as Key,
   GetUserAttr('userEmail') as UserEmail,
   GetUserAttr('userSubject') as UserSubject,
   GetUserAttr('userLocale') as UserLocale,
   GetUserAttr('userZoneinfo') as UserZoneinfo,
   GetUserAttr('userGroups') as UserGroups autogenerate 1;
   ```
3. Load the data. A table is created in the data model that displays each of the attributes in individual fields.

You can now use the attribute fields in visualizations such as tables or text & image objects.

## Example – Using the GetUserAttr function in chart expressions

Chart expressions

You can enter the function directly into chart expressions without using a variable. The user attributes will refresh without having to reload the application. This enables smoother movement of applications between users as part of the application life cycle.

Do the following:

1. Create a new Qlik Sense application.
2. Open a new sheet in advanced edit mode.
3. Drag a Text & image object onto the sheet.
4. Click inside the blank chart and enter the following label:

   User Email:
5. In the [properties](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/GetUserAttr.htm#glossary-7 "Glossary term") panel, select **Add measure**.
6. Enter the following expression:

   - =GetUserAttr('userEmail')
7. Add labels and measures for the other attributes on new lines. Use the following expressions for each attribute:

   - =GetUserAttr('userSubject'), for User Subject
   - =GetUserAttr('userGroups'), for User Groups
   - =GetUserAttr('userLocale'), for User Locale
   - =GetUserAttr('userZoneinfo'), for User Zone info​

> **Note:** By default, the `GetUserAttr('userGroups')` function returns the IdP groups for the user. You can choose which groups are returned by setting the `QlikCloudGroupMode` system variable in a script statement, for example `Set QlikCloudGroupMode = 2` returns both IdP and custom groups. For more information, see [*QlikCloudGroupMode*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/QlikCloudGroupMode.htm).

## Example – Conditionally hide a column using a chart expression

Chart expressions

Overview

This example shows or hides a column from a table based on the domain of the user's email address.

Do the following:

1. Create a new Qlik Sense application.
2. Open the Data load editor and add the load script below to a new section. The load script contains:

   - A dataset which is loaded into a table called `Transactions`.
   - The following fields in the data table:

     - `ID`
     - `Date`
     - `Amount`

     Load script

     ```
     Transactions:
     Load * inline [
     ID, Date, Amount
     1, 1/1/2023, 500.67
     2, 1/2/2023, 458.91
     3, 1/3/2023, 12.34
     ];
     ```
3. Load the data and open a sheet. Create a new table and add these fields as dimensions:

   - `ID`
   - `Date`
   - `Amount`

   Add the following expression as a calculated dimension:

   - `=WildMatch(GetUserAttr('userEmail'),'*@qlik.com')>0`, to check whether the user’s email domain matches `@qlik.com`.
4. In the properties panel of the `Amount` dimension, under **Show column if**, add the following expression:

   - `=WildMatch(GetUserAttr('userEmail'),'*@qlik.com')>0`, to display the Amount column if the user's email matches the `qlik.com` domain.

   The expression will display the `Amount` column for only those users whose email address domain contains `@qlik.com`. The column will be hidden for users with other domain names.

Results table 1 - User with email address: `user@qlik.com`

| ID | Date | Amount | WildMatch(GetUserAttr('userEmail'),'\*@qlik.com')>0 |
| --- | --- | --- | --- |
| 1 | 1/1/2023 | 500.67 | -1 |
| 2 | 1/2/2023 | 458.91 | -1 |
| 3 | 1/3/2023 | 12.34 | -1 |

Results table 2 - User with email address: `user@gmail.com`

| ID | Date | WildMatch(GetUserAttr('userEmail'),'\*@qlik.com')>0 |
| --- | --- | --- |
| 1 | 1/1/2023 | 0 |
| 2 | 1/2/2023 | 0 |
| 3 | 1/3/2023 | 0 |

In this example, you can see how the `GetUserAttr` function is used to conditionally hide or show a particular column. The `Amount` column is showing in the first table because the email address for the user viewing the application contains the domain `@qlik.com`, and the dimension expression in column 4 returns `-1`. The `Amount` column is hidden from the results in the second table because the user does not have an email address with the `qlik.com` domain.
