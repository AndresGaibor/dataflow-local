---
title: "Creating analytics with Qlik Sense"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/working-with-apps-hub.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data"]
---

# Creating analytics with Qlik Sense

You create analytics by creating a Qlik Sense application, adding data, and then visualizing it in [sheets](#glossary-1 "Glossary term") within the application.

Applications can be added from the Create page of the Analytics [activity center](#glossary-2 "Glossary term"). In user-based subscriptions, creating applications requires a Professional user entitlement. Users can view and interact with applications in spaces where they are members. If they have permission in a space, they can also add content such as sheets and [stories](#glossary-3 "Glossary term").

Information note

Applications made in Qlik Sense Enterprise on Windows and published to Qlik Cloud Analytics cannot be edited or shared within the activity centers. If you want to edit these applications, you should export the applications from the QMC and import them into Qlik Cloud Analytics.

There are different ways of developing applications and sharing them. Here is a sample application lifecycle:

1. Create your application

   Create a new application and develop it in the Analytics activity center. If you want to develop the application collaboratively, you can add the application to a shared space.

   [*Creating applications and adding data*](create-app-cloud-hub.htm)

   [*Working in spaces*](../Spaces/Spaces.htm)

   If you own an application that you want to use as a template, you can duplicate that application and then edit the copy.

   [*Duplicating applications*](duplicating-app-cloud-hub.htm)

   You can also import an application, such as one exported from another deployment of Qlik Sense.

   [*Uploading applications*](uploading-apps.htm)
2. Add data

   If you created a new application, you can add new data sources or use existing data sources from your personal or shared spaces and build your data model.

   [*Loading and modeling analytics data*](../LoadData/loading-and-modeling-analytics-data.htm)

   If you copied an application, you can change the data sources, revise the data model, and then edit the sheets and stories. If you duplicate an application containing data sources you do not own, you will need to add those sources.

   If you uploaded an application, you need to add the original data sources to the application again. You can also add new data sources and change the content.

   You can build your data model collaboratively with other members of shared spaces. For more information, see [*Collaboratively developing data load scripts in shared spaces*](../LoadData/script-codevelopment.htm).
3. Develop your application

   Once you have added your data, you can start creating sheets and visualizations. Visualizations are charts and other objects that visualize your data. Application users can make selections in the visualizations to change the data displayed in your application. You use sheets to present related visualizations within an application, such as a dashboard.

   [*Working with sheets*](../Sheets/working-with-sheets.htm)

   [*Working with visualizations*](../Visualizations/working-with-visualizations.htm)

   After you add your sheets and visualizations, you can optionally add stories and bookmarks to your application. Stories collect snapshots from your application so you can share insights you have discovered with other users.

   [*Sharing insights with data storytelling*](../StoryTelling/use-data-storytelling.htm)

   Bookmarks allow you to save your current analytic selections of data in your application. These can be shared with other users so they can quickly apply useful selections to sheets in your application.

   [*Bookmarking selections*](../Bookmarks/keep-track-of-important-data.htm)
4. Make your sheets and stories public

   Your sheets and stories are private until you make them public. If you are sharing your application with other users, make sure you make them public.

   [*Granting access to sheets, sheet groups, bookmarks, and stories*](../Share/make-public-or-private.htm)
5. Create a data reload schedule

   You can create scheduled reloads of your data to make sure your visualizations reflect the most up to date information.

   [*Reloading application data*](reloading-apps-cloud-hub.htm)
6. Share your application with other members

   You can share your personal application with other users by moving the application to a shared space. You can also publish the application to a managed space.

   [*Working in shared spaces*](../Spaces/working-in-shared-spaces.htm)

   [*Working in managed spaces*](../Spaces/working-in-managed-spaces.htm)
7. Update your application

   As application owner, you may receive feedback from your application users. A shared application can be updated at any time. You can make sheets and stories private again to work on them further. You can make changes to the data model.
8. Retire the application

   When the application is no longer required, you can delete it.

   [*Deleting applications*](delete-app-cloud-hub.htm)

Related learning:

- [Getting Started with Qlik Cloud](/lnk/Getting_started_Qlik_Cloud)
