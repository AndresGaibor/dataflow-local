---
title: "Example - Creating an email report using an embedded HTML template"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/HTML/html-report-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing HTML report templates"]
---

# Example - Creating an email report using an embedded HTML template

In this example, you will create and send a report by embedding an HTML report template directly into an email message.

Email report that you will create in this example.

![The resulting email report for the example](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_html-example-result.png "Click to view full size")

## Requirements

- Email provider configured for the Qlik Cloud tenant. See: [*Configuring email for reports and notifications*](../../../Admin/mc-configure-email-support.htm)
- The Private Analytics Content Creator security role, or sufficient space role for report development in a shared space. See: [*Permissions*](html-report-get-started.htm#Permissi)

## Step 1: Upload example sources

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

## Step 2: Develop the template

### Create a new template

Do the following:

1. In your application, use the drop down menu in the navigation bar and select Reporting.
2. Switch to the Templates tab.
3. In the top right, click Create new > HTML template.
4. Enter a Name for the template.

The HTML designer opens.

### Add tabular data

Next, add tabular data to the template.

Do the following:

1. Click ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) in the objects panel.
2. Click Add table. A list of available sheets appears.
3. Expand the Sales Tables sheet.
4. Click the ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the Yearly Regional Sales chart.
5. In the drop down menu, select Individual columns.
6. Under Select columns to add, select All. Click Add.

   The chart is added to the template as a table structure.
7. With the new table selected, change the following properties for the table in the objects panel:

   - Under Table settings, turn off Keep source formats.
   - Switch Display headers to Hide.
8. In the table, add a new row above the existing row definition. Add a new line below the line that contains <tbody><tr>. Paste the following:

   ```
   <th>Order year</th>
   <th>Region</th>
   <th>Sales</th>
   </tr>
   <tr>
   ```

### Style the table

Next, style the table elements by adding style definitions in the HTML head and inline styling in the table structure itself.

Do the following:

1. Add a new line below the title definition for the template.
2. Paste the following:

   ```
   <style>html { font-family: sans-serif }
   table { border: 2px solid #000000 }
   tr, th, td { border: 1px solid #000000 }
   th { font-size: large }
   td { font-size: medium }</style>
   ```
3. Locate the line in the table structure that defines the data. It should look like this:

   ```
   <td>%%OrderYear%%</td><td>%%Region%%</td><td>%%Sales%%</td>
   ```
4. Add style="text-align: center" to the opening tag of the first td element. The entire line should now look like this:

   ```
   <td style="text-align: center">%%OrderYear%%</td><td>%%Region%%</td><td>%%Sales%%</td>
   ```

   This aligns the text in the first column to be centered.

### Adding a dynamic title

Next, create an expression to store the calculation of the year range for your sales. Then, incorporate this expression into the report title so it is embedded as the email subject.

Do the following:

1. Click ![Variables and expressions](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) in the objects panel.
2. Click Add expression.
3. In the Name field, type YearRange.
4. In the Expression field, paste the following expression:

   ```
   = min(OrderYear)& ' - ' & max(OrderYear)
   ```
5. Click Create.
6. On the design surface, find the title element. Replace the entire line with the following:

   ```
   <title>Sales Report: </title>
   ```
7. On the line you just pasted, place your cursor after Sales Report:
8. In the objects panel, click Add expression tag.
9. The line should now be:

   ```
   <title>Sales Report: %YearRange%%</title>
   ```

### Add opening and closing statements

Next, add a salutation and opening statement, and finalize the report with a closing compliment.

Do the following:

1. Add a new line below the opening body tag.
2. Paste the following:

   ```
       <p>Hello,</p>
       <p>The table below outlines regional sales details for the requested years.</p>
   ```
3. Add a new line below the line containing the closing tag for the table.
4. Paste the following:

   ```
       <p>Regards,</p>
       <p>- Management</p>
   ```

### Saving and finalizing your work

Click Save template to save your work. The completed template code should look like the following.

```
<html><head>
  <title>Sales Report: %%YearRange%%</title>
<style>html { font-family: sans-serif }
table { border: 2px solid #000000 }
tr, th, td { border: 1px solid #000000 }
th { font-size: large }
td { font-size: medium }</style>
  </head>
  <body>
    <p>Hello,</p>
    <p>The table below outlines regional sales details for the requested years.</p>
    <table cellspacing="0" style="border-collapse: collapse">
    <tbody><tr>
      <th>Order year</th>
      <th>Region</th>
      <th>Sales</th>
      </tr>
      <tr>
      <td style="text-align: center">%%OrderYear%%</td><td>%%Region%%</td><td>%%Sales%%</td></tr>
    </tbody></table>
    <p>Regards,</p>
    <p>- Management</p>
</body></html>
```

## Step 3: Add a distribution list

Add a distribution list file under the Recipients or Groups tab in the application's Reporting section. Make sure you are added by email as a recipient and that the distribution list does not contain any filters or groups.

For information about distribution lists, see [*Creating a distribution list for your report*](../../Generate/cloud-in-app-reports-distribution.htm).

## Step 4: Create a report task

Do the following:

1. Open the Report tasks tab in the Reporting section of the application.
2. Click Create report task. The report task dialog opens.
3. Enter a Title for your report task.
4. Optionally, add a Description.

   In the Template dialog tab, click Add existing template. Select the template that you developed above.
5. Click Next. The dialog moves to the Output tab.
6. In the Output dialog tab, type a File name for the report output.
7. Click Next to proceed to the Distribute dialog tab.
8. Add yourself as a recipient to the report output.
9. Under Email, select HTML report. This will embed the report into the email message rather than attaching it as a file.
10. Click Next to proceed to the Schedule dialog tab.
11. Select the default scheduling settings and click Save.

## Step 5: Send the report

Do the following:

1. Stay in the Report tasks tab in the Reporting section of the application.
2. Click ![More actions](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the new report task.
3. Click ![Send](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_send_outline.svg) Send now.

When the email arrives, open it to see the result.

Resulting email report

![The resulting email report that is sent to the user, showing the embedded HTML template rendered in the email body](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_html-example-result.png "Click to view full size")
