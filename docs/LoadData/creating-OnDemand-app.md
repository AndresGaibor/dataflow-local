---
title: "Building an on-demand application"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/creating-OnDemand-app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Managing big data with on-demand applications"]
---

# Building an on-demand application

An on-demand application loads a subset of the data that is loaded in aggregate form by a selection application. An on-demand application is constructed by linking an on-demand selection application to an on-demand template application. Selection applications and template applications are the fundamental building blocks of on-demand applications.

To build an on-demand application, selection and template applications that can be linked together must first be created. To be linked, selection and template applications must have data fields in common that can be bound together.

For more information, see [*Creating an on-demand selection application*](creating-OnDemand-selection-app.htm) and [*Creating an on-demand template application*](creating-OnDemand-template-app.htm).

A selection application can be linked to multiple template applications, and a single template application can be linked to by multiple selection applications. But the template application's data binding expressions must correspond to fields in the selection applications that link to it.

An on-demand application navigation link joins a selection application to a template application. On-demand application navigation links are created in selection applications. Once a navigation link has been defined, it can be added to the selection application's App navigation bar as an on-demand application navigation point. Each [sheet](#glossary-1 "Glossary term") in an application contains its own App navigation bar. Users then generate on-demand applications from the application navigation point.

Example the On-demand application building view.

![On-Demand app overview.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_OnDemandBuildComponents_saas.png "Click to view full size")

Multiple on-demand applications, each containing a different combination of selected data, can be generated from the same application navigation point.

Pointers to a single application navigation link can be added to multiple [sheets](#glossary-2 "Glossary term") in the same selection application. Also, sheets can have multiple application navigation points, created from multiple application navigation links.

When a selection application is complete with navigation links and navigation points, on-demands can be generated.

Do the following:

1. Open an on-demand selection application and select Edit.
2. Select App navigation links from the panel on the left side.
3. Click the Create new button to open the Create new On-demand app navigation link dialog.
4. Name the new on-demand application navigation link.
5. Select an On-demand template app.

   Not all the applications in the Template app drop-down list are valid template applications. You must select an application that has been constructed as a template application and whose data binding expressions correspond to fields in the selection application you are working with. Otherwise, the on-demand applications generated from the application navigation link will produce errors.

   For more information, see [*Creating an on-demand template application*](creating-OnDemand-template-app.htm).
6. Write an expression that computes the total number of detail records that are represented by the aggregate records accessible by way of the selection state in the selection application.

   The expression usually uses the SUM function to obtain a total of the records selected. The result is used to determine when the amount of data to load is within the range specified for generating the on-demand application.
7. Specify the Maximum row count.

   The Maximum row count value sets the upper limit on the number of records, computed by the function in the Expression entry, that the on-demand application can load. As long as the number of records as computed by the row estimate expression in the selection application is greater than the Maximum row count value, the on-demand application cannot be generated. The application can only be generated when the number of records computed by the row estimate expression is at or below the upper limit set by the Maximum row count value.

   To create the expression used for Maximum row count, you must know how the total record count is computed from fields available in the selection application.

   Information noteThe maximum amount of data that can be sent to an on-demand application is 50 MB. Any amount larger than that causes the on-demand application to fail without an error message. Set maximum row counts to ensure that users cannot create selections larger than 50 MB.

   For more information, see [*Creating an on-demand selection application*](creating-OnDemand-selection-app.htm).
8. Specify the Maximum number of generated apps.

   Multiple on-demand applications can be generated from the same on-demand application navigation point on the selection application's App navigation bar. The reason for generating multiple applications is that each one can contain a different selection of data. When the maximum number of applications has been generated, the user who is generating applications from the navigation point must delete one of the existing applications before generating a new on-demand application.

   The maximum number of generated applications applies to the on-demand application navigation link. If one on-demand application navigation point is created from the navigation link, then that navigation point would be able to create up to the maximum number. But if multiple navigation points are created from the same navigation link, then the total number of on-demand applications generated from those navigation points is limited to the setting for Maximum number of generated apps.

   Information note

   On the on-demand application navigation link, you can select:

   - Overwrite generated app and if it has reached the maximum number of generated applications, users will not be able to generate new applications. Add a button to the sheet set to navigate to the on-demand application navigation link or delete one or more of the generated applications.
   - Keep script in generated apps. Users with access to the application will be able to generate applications with the script of the template application included. Additionally, if you have create-edit permission in your personal space, you will be able to see and edit the script of the generated application. For QSEoW, you decide which stream to publish your generated application to.
9. Enter a numeric value in the Retention time field for the length of time applications generated from the navigation link will be retained before they are deleted.
10. In the drop-down menu to the right of the Retention time field, select the unit of time for the retention period.

    The options for retention time are hours, days, or Never expires.

    All on-demand applications generated from the navigation link will be retained according to this setting. The age of a generated on-demand application is the difference between the current time and the time of the last data load. This calculation of an on-demand application's age is the same for published and unpublished applications. And if an on-demand application is published manually after it has been generated, the age calculation remains the same: it is based on the last data load of the generated application.
11. In the Default view when opened drop-down menu, select the sheet to display first when the applications generated from the navigation link are opened.

    You can select App overview or one of the sheets in the selection application from which the navigation link is created.
12. Click Create and the new on-demand application navigation link will appear in the list of App navigation links.
13. Drag the application navigation link to the App navigation bar on the selection application.

    Dragging the application navigation link onto the selection application creates an on-demand application navigation point. The [properties](#glossary-3 "Glossary term") of the new on-demand application navigation point are displayed in the panel on the right side. You can change the name of the navigation point there if you wish.
14. Click Done in the sheet editor.

    The on-demand selection application is now ready to use or publish. Users of the selection application will be able to generate on-demand applications from the navigation points on the App navigation bar in the selection application.

You can share on-demand selection applications in a shared or managed space. You must first make the sheets of the
selection and template applications public. You can then add the selection application to a shared or managed space. If you are publishing to a managed space, you only need to publish the selection application.

Users with access to applications in those spaces can access the navigation points in those applications. For example, they can generate an on-demand application from the App navigation bar.

Warning note

If your applications in managed or shared spaces contain sensitive data, use on-demand applications carefully and confirm the permissions of those who have access to your selection applications.

On-demand applications are added to users' personal spaces. If users have Can contribute, Can manage, Can publish, or Owner permissions in a shared or managed space, they can share their generated on-demand applications from their personal space with other users.

Once an on-demand selection application is published to a managed space, you cannot edit the navigation link in the selection application or published application. If you need to update the navigation link, delete the published application. Next, edit the link in the selection application, and publish the application again to the managed space.
