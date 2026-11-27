---
title: "Managing big data with on-demand applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/Manage-big-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data"]
---

# Managing big data with on-demand applications

On-demand applications enable you to load and analyze big data sources in Qlik Sense Enterprise. Trying to analyze an entire big data store at one time is highly inefficient. Nevertheless, to make representative [visualizations](#glossary-1 "Glossary term"), all the data must be discoverable. Qlik Sense on-demand applications give users aggregate [views](#glossary-2 "Glossary term") of big data stores and allow them to identify and load relevant subsets of the data for detailed analysis.

On-demand applications expand the potential use cases for data discovery, enabling business users to conduct associative analysis on larger data sources. They allow users to first select data they are interested in discovering insights about and then interactively generate an on-demand application with which they can analyze the data with the full Qlik in-memory capabilities.

## On-demand application components

Qlik Sense manages the loading of big data sources with selection applications that provide aggregated views of the big data and also enable a user to zoom in and analyze finer-grained data. Embedded in each selection application are on-demand application navigation links to one or more template applications used as the basis for creating on-demand applications. Properties of the navigation links and template applications enable you to tightly control the shape and volume of data loaded into on-demand applications.

Applications can be generated repeatedly from the template application to track frequently changing data sets. While the data is filtered according to [selections](#glossary-3 "Glossary term") made in the selection application, the on-demand application content is dynamically loaded from the underlying data source. The same on-demand application can be generated multiple times to make fresh analyses of the data as they change.

Information noteOn-demand application generation is controlled by the On-demand application service. The service is disabled by default and must be enabled before selection and template applications can be linked and on-demand applications generated. The On-demand application service is managed in the Administration activity center.

For more information, see [*Enabling on-demand application generation*](../LoadData/enabling-OnDemand-app-generation.htm).

Relations between on-demand application components.

![On-demand app components.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dr_OnDemandApps2.png "Click to view full size")

## Constructing on-demand applications

Because on-demand selection and template applications require special load scripting, they are usually created by users with experience writing Qlik Sense load scripts. On-demand selection applications, for example, must load data with a modest level of [dimension](#glossary-4 "Glossary term") granularity. On-demand template applications contain load scripts with data binding expressions used to formulate the queries made on the data sources.

A selection application can be linked to multiple template applications, and a single template application can be linked to by multiple selection applications. But the template application's data binding expressions must correspond to fields in the selection applications that link to it. For that reason, selection and template applications tend to be created in conjunction with one another and often by the same experienced script writer.

Creating navigation links also requires an understanding of the fields in the selection application that have corresponding bindings in the template application. That is because each navigation link requires an expression that computes the total number of detail records. That total represents the aggregate records accessible by way of the selection state in the selection application. To create that expression requires that the user know how to compute the template application's total record count using fields available in the selection application.

For more information, see [*Building an on-demand application*](../LoadData/creating-OnDemand-app.htm).

Using selection applications to generate on-demand applications does not require a user to understand the [load script](#glossary-5 "Glossary term"). Once an on-demand application navigation link has been created, a user can drag that navigation link onto the selection application's App navigation bar to create an application navigation point. On-demand applications are then generated from the navigation point.

Navigation points become available for on-demand application generation when the maximum row calculation from the expression in the navigation link comes within the required range. At that point, the user can generate an on-demand application. The user can also make another set of selections and generate additional applications based on those different selections.

For more information, see [*On-demand apps*](../LoadData/using-OnDemand-apps.htm).

Navigation links have a limit on the number of on-demand applications that can be generated from the link. When the maximum number of applications has been generated, the user who is generating applications from the navigation point must delete one of the existing applications before generating a new on-demand application. The maximum number of generated applications applies to the on-demand application navigation link. If one on-demand application navigation point is created from the navigation link, then that navigation point would be able to create up to the maximum number. When multiple navigation points are created from the same navigation link, together those navigation points are limited to the maximum number set for the navigation link.

Navigation links also set a retention time for generated applications. On-demand applications are automatically deleted when their retention period expires.

## Sharing on-demand applications

You can share on-demand selection applications in a shared or managed space. You must first make the sheets of the
selection and template applications public. You can then add the selection application to a shared or managed space. If you are publishing to a managed space, you only need to publish the selection application.

Users with access to applications in those spaces can access the navigation points in those applications. For example, they can generate an on-demand application from the App navigation bar.

Warning note

If your applications in managed or shared spaces contain sensitive data, use on-demand applications carefully and confirm the permissions of those who have access to your selection applications.

On-demand applications are added to users' personal spaces. If users have Can contribute, Can manage, Can publish, or Owner permissions in a shared or managed space, they can share their generated on-demand applications from their personal space with other users.

Once an on-demand selection application is published to a managed space, you cannot edit the navigation link in the selection application or published application. If you need to update the navigation link, delete the published application. Next, edit the link in the selection application, and publish the application again to the managed space.

## Advantages of on-demand applications

On-demand applications help business users and IT departments derive value from big data environments in numerous ways. On-demand applications:

- Provide users with a "shopping list" experience that enables them to interactively populate their applications with a subset of data such as time period, customer segment, or geography.
- Provide full Qlik Sense functionality on a latent subset that is hosted in memory.
- Enable IT to govern how large an application can be and invoke applications based on data volume or dimensional selections.
- Provide access to non-SQL data sources such as Teradata Aster, MapR, SAP BEx, and the PLACEHOLDER function in SAP HANA.
- Allow customizable SQL and load script generation.
- Allow [section access](#glossary-6 "Glossary term") in all cases.

## Limitations

On-demand applications have the following limitations:

- The maximum amount of data that can be sent to an on-demand application is 50 MB. Any amount larger than that causes the on-demand application to fail without an error message. Set maximum row counts to ensure that users cannot create selections larger than 50 MB.
- Once an on-demand selection application is published to a managed space, you cannot edit the navigation link in the selection application or published application. If you need to update the navigation link, delete the published application. Next, edit the link in the selection application, and publish the application again to the managed space.
- If you change the script of your template application and insert a new binding variable, new on-demand application navigation links must be created to replace any existing application navigation links. If you do not, the selection for the corresponding field will not be sent for existing on-demand applications using that template application.
