---
title: "Best practices for improving performance of applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Insights/InsightAdvisorBestPractices/best-practice-improve-app-performance.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating visualizations with Insight Advisor", "Insight Advisor best practices"]
---

# Best practices for improving performance of applications

Learn how to ensure your applications are responsive and usable. You can improve the speed and overall performance of your applications by only using necessary fields, removing duplicate dimensions, and working in the published versions of applications.

Remember that Insight Advisor only uses data that is included in your data model. Creating master dimensions and measures can help when you are asking questions in Insight Advisor.

## Improving application performance with Insight Advisor

Insight Advisor can return recommendations almost immediately after you open your application by performing a profiling of the application and its data. The size of metadata available in an application can affect the amount of time it takes Insight Advisor to initially profile a new application.

If your application contains more than 500 fields, Insight Advisor is less accurate in classifying the fields beyond generic dimensions or measures.

If your application contains more than 100 master measures, or more than 100 master dimensions, Insight Advisor is less accurate in classifying the items beyond generic dimensions or measures. For example, if you have more than 100 master dimensions, master dimensions intended to be geographic dimensions could only be classified as dimensions. This threshold is defined separately for master dimensions and master measures.

As a best practice, only load relevant fields to ensure applications do not reach a size that is difficult to maintain.

To improve the performance of your applications, consider the following actions:

- Only loading the required fields for applications.
- Specifying values that can be referenced in a question with Data value lookup.
- Removing duplicate dimensions from the data model.

## Improving quality of analysis with Insight Advisor

The following are several best practices that can improve the quality of analysis in Insight Advisor.

### Avoiding adding too many dimensions to an application

It can be tempting to add as many dimensions as possible into an application. Including too many dimensions can lead to duplicates that can make it more difficult for your users to create visualizations and analyze data.

### Avoiding superlatives when naming master items

As a best practice, exclude regular expression superlatives when you name master items.

For example, Insight Advisor might recognize the following master item labeled This Week’s Sales as multiple tokens: This Weeks as a relative time filter and Sales as the name of a dimension in the data model. You can use terms like Latest Sales when naming a master item to ensure the engine recognizes the full term as the question.

### Setting data value lookup in the logical model

Data models sometimes contain multiple fields that have identical or nearly identical names. You can ensure that users are asking questions that refer to the correct fields by changing the Data value lookup value for these fields in your logical model. Customizing the Data value lookup column helps the engine recognize the correct field when a question is asked.

For example, a data model can contain two country dimensions, customer country and supplier country. If your users generally ask about the countries of their customers, then the supplier country can be removed from the Data value lookup column.

Removing a dimension from the data value lookup column

![This image shows the Fields and Groups menu in the logical model tab of Qlik Cloud. The data value lookup column is highlighted to show three similarly named dimensions and that users can choose whether dimensions can be searched using the data value lookup tool.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/InsightAdvisorbestPractices_DataValueLookup.png "Click to view full size")

See [*Defining fields and groups in Insight Advisor*](../../BusinessLogic/business-logic-fields-groups.htm) for more information on using Data value lookup.

## Working with applications in managed spaces

Insight Advisor behaves differently in applications in managed spaces. In a personal or shared space, you typically have access to all fields in the application. In a published application, you only have access to master items. Before publishing an application to a managed space, ensure you have master items created for the dimensions and measures you want available.

Natural language questions work best in applications with a limited and specific number of fields. As a result, published applications are more responsive than an application in a shared or personal space.

Information note

Insight Advisor can perform a count on a simple master dimension when the application is in personal and shared spaces. This is not possible when the application is in a managed space as users do not have access to the underlying fields.
