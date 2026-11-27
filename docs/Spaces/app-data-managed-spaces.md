---
title: "Data sources for applications in managed spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/app-data-managed-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces", "Working in managed spaces"]
---

# Data sources for applications in managed spaces

Managed spaces provide governed access to applications in Qlik Cloud Analytics.
Applications published to a [managed space](#glossary-0 "Glossary term") keep the data loaded in the application, but do not include their data files or data connections. This enables the use of mock data in application development that is replaced with real data when the application is published without changing the [load script](#glossary-2 "Glossary term").

Information noteManaged spaces are not available in Qlik Cloud Analytics Starter or Qlik Sense Business.

Applications do not include their data sources when they are published to a managed space. The application load script remains unchanged, however. By using space-aware data sources in your load script, development data sources in personal or [shared spaces](#glossary-3 "Glossary term") can be replaced with the final data sources when the application is added to the managed space. This helps keep strict data governance for applications and their users in managed spaces.

Space-aware data sources syntax enables you to specify in the load script that the data sources exist in the current space, rather than in a specific space. The application will always look in the current space for the data sources. By using mock data sets and real data sets with the same name, published applications can seamlessly switch to the final data sources.

## Space-aware data source syntax examples

This example loads the file orders.csv from the current space. If the application is moved to another space, for example, it will use the file orders.csv in the new space.

```
LOAD * FROM [lib://:DataFiles/orders.csv];
```

This example loads the table Sales\_data from the DataSource [data connection](#glossary-4 "Glossary term") in the current space.

```
LIB CONNECT TO ':DataSource';
LOAD *;
SQL SELECT * FROM `Sales_data`;
```

For more information using space-aware data sources, see:

- [*Connect to data sources in load scripts*](../LoadData/connect-data-sources-data-load-editor.htm)
- [*Adding data from uploaded data files*](../LoadData/adding-data-datafiles.htm)
- [*Loading data from files*](../DataSource/load-data-from-files.htm)

## Best practice workflow for governed applications and data

The following is an example best practice workflow for governed applications and data sources in managed spaces.

Mock data sources are created that share the same names as the real data sources that will be used in the managed space. These mock data sources are added to a shared space where application developers have Can manage, Can edit, or Can edit data in applications [permissions](#glossary-5 "Glossary term"). Developers reference these data sources in the load script so that the load script looks for the data sources in the current space. When the applications are ready, the application is published to the managed space, where the managed space administrator adds the real data sources. This populates the applications with sensitive data while preventing the application developers from seeing any sensitive information.

This workflow involves three primary users:

- [Tenant administrator](#glossary-6 "Glossary term"): The tenant administrator creates the managed space and then assigns users and roles to the managed space.
- Governed Manager: The user in charge of managing access to sensitive data and administering the managed spaces
- Developer: The user in change of developing applications for the managed space and publishing them to the space.

Information noteAnalytic administrators and users with the Managed Space Creator role can also create managed spaces.

This workflow occurs in four steps:

1. Create the spaces.
2. Add mock data and develop the application.
3. Publish applications to managed space containing real data.
4. Adding application consumers to the managed space.

### Creating managed space and shared spaces

First, the spaces are created and then users are added to them.

Do the following:

1. The tenant administrator creates a managed space, Secure Apps, as the destination for published governed applications.
2. The tenant administrator adds two members to Secure Apps:

   - The lead application developer, Developer, is added with Can publish permission.
   - The owner of the governed applications, Governed Manager, is made the space owner.
3. Developer creates the Develop Apps shared space for the development of the governed applications. Optionally, additional developers are added with Can edit and Can edit data in applications roles.

### Developing applications with mock data

Next, mock data is added and the application is developed.

Do the following:

1. Developer adds mock testing data to the Develop Apps space. This data can be used once or in continuous deployment scenarios.

   Data can be made available to a space by adding an application and then adding the data source to the application. Once a data source has been added to an application in the space, it is available to all users with Can edit and Can edit data in applications roles in the space.

   Information noteUsers with Can consume data can also view the data sources, and they can consume the data where they have permission to create applications. They cannot add, edit, or delete data sources. They have no permissions to view, add, edit, or delete applications.
2. Developer develops applications in the Develop Apps space. These applications use space-aware scripting to always look for the data sources in the current space.

   For space-aware connection syntax in Data load editor, see [*Connect to data sources in load scripts*](../LoadData/connect-data-sources-data-load-editor.htm).

   If Developer uses Data manager, they unlock the load script for editing and update the data source references to use space-aware connection syntax.

### Publishing applications and adding final data

The application is published to the managed space. The real data sources are added to the managed space.

Do the following:

1. When the application is ready for release, Governed Manager adds production data to the Secure Apps space.
2. Developer publishes the application from Develop Apps to Secure Apps.
3. Governed Manager schedules reloads for the application and confirms the application can reload data without errors.

### Adding application consumers to the managed space

Finally, the application consumers are added to the managed space.

Do the following:

1. Governed Manager adds Can view members to the Secure Apps managed space. These users will be able to open and create private [bookmarks](#glossary-7 "Glossary term"), [snapshots](#glossary-8 "Glossary term") and [stories](#glossary-9 "Glossary term").
2. Governed Manager adds Can contribute members to the Secure Apps managed space. These users will be able to additionally create community [sheets](#glossary-10 "Glossary term"), stories & bookmarks, and publish community [sheets](#glossary-11 "Glossary term") in the published application.
