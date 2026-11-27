---
title: "Understanding applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/App.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data"]
---

# Understanding applications

Applications are task-specific, purpose-built applications. Applications contain data loaded from data sources that is interpreted through [visualizations](#glossary-0 "Glossary term").

Instead of deploying and managing huge business applications, you can create your own applications that you can reuse, modify and share with others. The application model helps you ask and answer the next question on your own, without having to go back to an expert for a new report or visualization.

Applications are designed to help you understand data. Data sources can be added to spaces. They are either added from within an application or created in the Create page of the Analytics [activity center](#glossary-2 "Glossary term"). Their data is then loaded into the application. Associations are made between related data tables. Using the data model, visualizations are added to [sheets](#glossary-3 "Glossary term") in the application to interpret the data. Visualizations are [charts](#glossary-4 "Glossary term"), tables, and similar representations of data. Members with access to an application can make [selections](#glossary-5 "Glossary term") in the visualizations, enabling them to explore the data for insights and discoveries.

Applications can be Qlik Sense applications or QlikView applications.

## Qlik Sense applications

A Qlik Sense application consists of one or more sheets containing visualizations. Visualizations are charts, tables, and similar representations of your data together with other information. By making selections in your visualizations you can analyze the information to make your own discoveries and gain insights about your data.

Qlik Sense applications are either created in the Analytics activity center or distributed to Qlik Cloud Analytics from a Qlik Sense Enterprise on Windows deployment.

Applications created in other Qlik Sense deployments can also be uploaded to Qlik Cloud. These applications can be edited and modified. For information about creating and managing applications, see [*Working with applications*](../Visualizations/create-apps-visualizations.htm).

If you have access to an application, you can explore the application and its sheets and [stories](#glossary-6 "Glossary term"). Applications use an associative selection model to help you discover connections between data sets. As you click, associated data values are highlighted. Selections are highlighted in green, associated data is represented in white, and excluded (unassociated) data appears in gray. This instant feedback enables you to think of new questions and continue to explore and discover.

Applications can be shared with other users in Qlik Cloud.
Applications can be added to shared spaces for collaborative development. Applications containing sensitive information can be published to managed spaces for specific users to view. For information on working collaboratively with other members, see [*Sharing and downloading application content*](../Share/share-and-download.htm).

Depending on your permissions with the application and the space it is in, you can also add your own private sheets and stories to the application and share them with other users. To learn about creating public content, see [*Granting access to sheets, sheet groups, bookmarks, and stories*](../Share/make-public-or-private.htm).

Applications can be published to Qlik Cloud Analytics from Qlik Sense Enterprise on Windows. These applications are far more limited in their capabilities within Qlik Cloud Analytics activity centers than applications created within the Create page of the Analytics activity center.

### Insight Advisor

[Insight Advisor](#glossary-7 "Glossary term") is a suite of features that assists you with Qlik Sense applications. Insight Advisor helps you create analyses, analyze data, and build an application data model. The following Insight Advisor features are available:

- [Insight Advisor Analysis Types](#glossary-8 "Glossary term")
- [Insight Advisor Search](#glossary-9 "Glossary term")
- [Insight Advisor Chat](#glossary-10 "Glossary term")
- [Associative insights](#glossary-11 "Glossary term")
- Chart suggestions
- Recommended associations

Insight Advisor Analysis Types and Insight Advisor Search help you quickly create analyses in applications. Insight Advisor Analysis Types creates charts from the analysis type and data you pick to use in the analysis. Insight Advisor Search uses search-based analysis to create charts based on your searches. As an application creator, Insight Advisor helps you create application content. As a business user using applications for analysis, Insight Advisor helps you create analyses outside of what is in the application sheets. For more information, see:

- [*Exploring analyses with Insight Advisor*](../Insights/insight-advisor-exploring-analyses.htm)
- [*Creating visualizations with Insight Advisor*](../Insights/insight-advisor-create-visualizations.htm)

Insight Advisor Chat provides a chat-based solution for conversational analytics. Insight Advisor Chat enables you to make natural language searches from activity centers to applications to which you have access. Insight Advisor Chat then returns relevant visualizations. For more information, see [*Exploring applications with conversational analytics*](../Insights/insights-chat.htm).

Associative insights helps you uncover blind spots and reveal relationships you may have missed. Associative insights compares the contributions of your selections and excluded values against your measures. For more information, see [*Discovering your data with associative insights*](../Selections/associative-insights.htm).

Chart suggestions allows you to select data fields when editing a sheet and let Insight Advisor choose the dimensions, measures, and visualization types. The suggested chart adjusts itself based on your changes. You can customize a suggested visualization with a focused set of properties. For more information, see [*Creating visualizations using Insight Advisor chart suggestions*](../Visualizations/creating-visualization-assistance.htm).

Recommended associations Insight Advisor can recommend associations between your data tables in the Associations view in Data manager. The Recommended associations panel lets you view and apply these recommendations. For more information, see [*Associating data in the table editor*](../LoadData/managing-associations-table-editor.htm).

## QlikView applications

Qlik Cloud Analytics members with access to QlikView can also add their QlikView applications to Qlik Cloud.
QlikView applications have the same purpose as Qlik Sense applications, but have a different interface. QlikView applications can be uploaded to Qlik Cloud, or they can be distributed from QlikView AccessPoint.

QlikView applications are view-only. Users can explore the visualizations in the application, but they cannot edit the application or add their own sheets to the application. QlikView applications can be shared with other users and added to spaces. QlikView applications are more restricted to what you can do with them in activity centers than Qlik Sense applications. For more information on what QlikView applications can do within Qlik Cloud Analytics, see [*QlikView applications in Qlik Cloud*](../QlikViewInCloud/using-QV-cloud-hub.htm).

For more information on QlikView applications and how to create and explore them, see [QlikView](/en-US/qlikview).

## Scripts

Scripts are purpose-built applications similar to applications, but are created for exporting data from a load script. Scripts consist only of a script editor that is used to load, transform, and export data. Scripts cannot be used to analyze or visualize the loaded data. Applications can be converted into scripts, the application load script becoming the load script of the scripts. Scripts can also be converted into applications, the script load script becoming the application load script.

To learn more about scripts, see [*Working with scripts in the catalog*](../ScriptEditor/using-the-script-editor.htm).

Related learning:

- [How do I create an application?](/lnk/How_create_app)
- [Navigating applications](/lnk/Navigating_apps)
