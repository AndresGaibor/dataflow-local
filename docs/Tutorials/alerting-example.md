---
title: "Tutorial - Alerts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Tutorials/alerting-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Monitoring data with alerts"]
---

# Tutorial - Alerts

You can monitor critical data without opening your Qlik Sense applications. Qlik Cloud lets users set conditions based on [measures](#glossary-1 "Glossary term") or [dimensions](#glossary-2 "Glossary term"), and receive alerts when they are met. Alerts can be evaluated whenever the data changes or based on a time-based schedule. You can share alerts with any user that has read [permissions](#glossary-3 "Glossary term") for the application.

## What you will learn

This step-by-step guide will show you how to:

1. Create a simple alert.
2. Create a complex alert.
3. Manage an alert's life cycle.

## Who should complete this tutorial

This tutorial is for users who are comfortable working in the Analytics [activity center](#glossary-4 "Glossary term").

Information noteIf alerts are not working, contact a Qlik Sense administrator. They might need to turn on alerts.

## What you need to do before you start

### Download tutorial application and data

Download the CreatingAlertsFiles.zip file. It contains the application and data files needed to complete this tutorial:

[Creating alerts files](/en-US/cloud-services/tutorials/CreatingAlertsFiles.zip)

### Upload the tutorial application

You need to unzip the folder and upload the application and data files to a space in Qlik Sense. The application is similar to the application from [*Tutorial - Beginning with the Basics*](introduction-beginning-with-basics.htm), except a script was added to keep the dates current.

Do the following:

1. Unzip the CreatingAlertsFiles file.
2. Open Qlik Cloud.
3. Go to the Create page of the Analytics activity center and select Upload. A dialog box opens.
4. Select App.
5. Drag and drop the Creating alerts.qvf file.
6. Select a space, such as Personal, and click Upload.

   You can pick a different space if you want other users to be able to access this application and data files.
7. Go to the Create page of the Analytics activity center and select Dataset. A dialog box opens.
8. Click Upload data file.
9. Drag and drop the five Microsoft Excel files onto the dialogue box. Click Upload.

### Create dynamic bookmarks

Qlik Sense applications often include data over multiple years. Alerts are usually set for the current time period (current week, month, or quarter). To imitate a realistic scenario, you need to create dynamic [bookmarks](#glossary-5 "Glossary term").

Do the following:

1. Open the application and open any [sheet](#glossary-6 "Glossary term").
2. Click ![Selections tool](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_tool.svg) .
3. The [selections](#glossary-7 "Glossary term") screen will appear. The App dimensions are at the bottom of the screen. Make sure that the Show fields check box is selected.
4. In the search box on the right-hand side, type *YearMonth*.
5. Find the *Date.autoCalendar.YearMonth* dimension and click ![Search in listbox](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search.svg).
6. In the search list box, type the following function *=Date.autoCalendar.YearMonth=Monthstart(Now())*. Press Enter. The current month is selected.
7. Close the selections tool by clicking ![Selections tool](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_tool.svg).
8. Click ![Bookmark](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bookmark.svg) Bookmark.
9. Click Create a new bookmark. Under Title, type *Current month*.

Using the same procedure, create the following bookmarks. Ensure you clear the previous selections before you make new ones:

- Last Month: *=Date.autoCalendar.YearMonth=Monthstart(Now(),-1)*
- Current Quarter: *=Date.autoCalendar.YearMonth>=Quarterstart(Now(),-1) and Date.autoCalendar.YearMonth<Quarterstart(Now())*
- Last Quarter: *=Date.autoCalendar.YearMonth>=Quarterstart(Now(),-2) and Date.autoCalendar.YearMonth<Quarterstart(Now(),-1)*

For additional general information about creatin dynamic bookmarks, see [*Creating bookmarks*](../Bookmarks/create-bookmark.htm).

## Enabling notifications

You can customize [notifications](#glossary-8 "Glossary term") in your personal settings.

Do the following:

1. In the Analytics activity center, in the navigation bar, open Settings.
2. Click on Notifications.
3. Under Alerts, you can choose to receive alerts via Web, Push, or Email.

For more information, see [*Managing your alerts*](../Alerting/managing-your-alerts.htm)

## Creating a simple alert

You will create an alert that monitors the profit margin rate and sends a notification when it becomes less than 40 percent.

### Creating a new alert

Do the following:

1. Open the application. Open the Dashboard sheet in Analyze view.
2. Right-click the Profit Margin gauge in the top-right corner.
3. From the menu, select Alerts > Create new alert.

   A dialog box opens.
4. In the detail section, insert:
   1. Title: Profit Margin Rate
   2. Description: Profit Margin should never fall below 40%
5. The measure of the gauge is already added: (Sum(Sales) - Sum(Cost)) / Sum(Sales).

   Click Add additional measure and select Margin (%) under Master measures.
6. From the Selections dropdown, select Current Month as the bookmark to apply to the data.

   Data preview shows the current measure value, taking into account the bookmark applied.
7. Click Next.
8. Under Condition 1, set the following:
   1. Measure: Margin (%)
   2. Operator: Less than
   3. Compare with: Value
   4. Value: 40
9. Click Next.

   This dialog box shows alert scheduling. Keep the default settings.
10. Click Create.

### Testing the alert

This alert evaluates when the application data changes.

Do the following:

1. In the Analytics activity center, click Alerts on the left-hand panel.
2. Find the Profit Margin Rate alert you created and click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg). Click Details.
3. Notice that this alert has never been evaluated. This is because the profit margins have not changed. We need to change the data to trigger the alert.
4. From the context menu, click Edit alert in app. The Alert dialog box will open.
5. Raise the Margin (%) value to 43 (or higher than the actual value).
6. Go back to the Analytics activity center. Find the application and click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg). From the context menu, click Reload.

You will see a notification on the top menu. Click the alert. A dialog box opens showing that profit margins are below 43 %.

Your inbox may also contain an email from Qlik Sense, depending on your notification settings.

## Creating a complex alert

We will create a monthly alert that monitors the last quartile product type margin rate in a specific sales range.

### Creating a new alert

Do the following:

1. Open the application in Qlik Sense. Open the Customer Details sheet in Analyze view.
2. Find the pivot table labeled "Customer KPIs" at the bottom of the page. Right-click it.
3. From the context menu, select Alerts > Create new alert.

   A dialog box opens.
4. In the detail section, insert:
   1. Title: Low margin products last month
   2. Description: Monthly products that need margin improvements
5. The measures used in the chart are automatically added.
6. Select Product type in Show by dimension.
7. From the Selections dropdown, select Last Month as the bookmark to apply to the data.
8. Data preview shows the product type by sales and margin percent, taking into account the bookmark applied.
9. Click Next.
10. Under Condition 1 set:

    1. Measure or dimension: Sales
    2. Operator: Greater than
    3. Compare with: Value
    4. Value: 50000
11. Click Add additional condition.
12. Under Condition 2 set:
    1. Measure or dimension: Sales
    2. Operator: Less than
    3. Compare with: Value
    4. Value: 100000
    5. Ensure that there is an And operator between the two conditions.

       ![AND operator between Condition 1 and Condition 2](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_Alerting_create_alert_AND.png)
13. Click Add additional condition.
14. Under Condition 3 set:
    1. Measure or dimension: Margin (%)
    2. Operator: Less than
    3. Compare with: ValueCurrent set
    4. Aggregation: Percentile
    5. Percentile: 25 (this means the last quartile)

       ![Dialogue window showing all three conditions that were made](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_Alerting_create_alert_conditions2.png)
    6. Click the ![linked](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) between Condition 2 and Condition 3 to ungroup them. Ensure that there is a Then operator between the last two conditions.

       ![THEN operator between Condition 1 and Condition 2](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_Alerting_create_alert_THEN.png)
15. Preview alert might be blank. If this is the case, increase the percentile value.
16. Click Next.
17. Set Evaluate the alert to Monthly.
18. Click Create.

### Testing the alert

This alert is set to evaluate once a month. However, if you own an alert, you can evaluate it at any time.

Do the following:

1. In the Analytics activity center, click Alerts on the left-hand panel.
2. Find the Low margin products last month alert and click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
3. From the context menu, click Evaluate now.

You will see a notification on the top menu.

## Alert life cycle

This section explains how to manage alerts after they are created.

### Turn alerts on and off

Alerts are created based on [visualizations](#glossary-9 "Glossary term") but they are not linked to them. Deleting [charts](#glossary-10 "Glossary term") does not delete associated alerts. Only administrators and alert owners can turn alerts on and off.

#### Manage alerts as owner

Do the following:

1. In the Analytics activity center, click Alerts on the left-hand panel.
2. For each alert, the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) opens the context menu. From here you can disable and delete alerts.

### Viewing alert details

Do the following:

You can check alert details, conditions, and execution history.

1. In the Analytics activity center, click Alerts on the left-hand panel.
2. Find the Low margin products last month alert.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
4. From the context menu, click Details.
5. The left-hand side menu shows: Details, Data & conditions, History, Recipients, and Notifications.

   These sections cannot be edited.
6. From the Details section, click View to display the most recent alert.

### Modifying an alert

Do the following:

1. In the Analytics activity center, click Alerts on the left-hand panel.
2. Find the Low margin products last month alert.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
4. From the context menu, click on Edit alert in app. The Alert dialog box will open.
5. Leave the Details & data section as is. Click Next .
6. Leave the Conditions section as is. Click Next.
7. In the Distribution section, change Snooze notifications and set Off.
8. Click Save.
