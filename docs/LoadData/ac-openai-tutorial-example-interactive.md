---
title: "OpenAI analytics connector  – Interactive example"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-openai-tutorial-example-interactive.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "OpenAI analytics source", "Tutorial – Using the OpenAI analytics connector in Qlik Cloud"]
---

# OpenAI analytics connector – Interactive example

This example allows you to import a pre-configured application into Qlik Cloud, where you can learn how to create chart expressions to control usage of OpenAI data, and to generate responses as users make application selections.

Warning noteBe aware that using the OpenAI platform requires you to enter into a commercial relationship with OpenAI. While the free trial allotment of data you can use might allow you to complete these exercises, it is important to remember that completing the exercises will require you to consume some amount of data from OpenAI.

In this example, it is assumed you have a basic understanding of analytics connectors in Qlik Cloud. For clarification on any of the key concepts, refer to the earlier tutorial examples and the remaining OpenAI connector documentation.

This example uses the OpenAI Chat Completions API configuration of the connector.

## Before you start

### Considerations

OpenAI applies rate limits to use of its APIs. This means that depending on the connector configuration and OpenAI model that you use, you might be restricted in how many requests you can make within certain time intervals (for example, a minute). For this reason, each chart expression has been commented out until you need to use it, and only one chart expression can likely be evaluated at a time. Refer to OpenAI's documentation on rate limits for more information.

[Rate limits](https://platform.openai.com/docs/guides/rate-limits)

### Preparations

Before you can complete this example, you need to complete the following steps:

- Create an OpenAI platform account
- Obtain an OpenAI API key
- Enable analytic connection functionality in Qlik Cloud
- Create a separate connection for this example (OpenAI\_Example\_InteractiveApp)

For full details, see: [*Getting started with the OpenAI platform*](ac-openai-overview.htm#Getting) and [*Create the connections*](ac-openai-tutorial.htm#Create).

## Download and upload the application

Download the example application here:

[OpenAI Demo App - Complaints Analysis and Handling](/en-US/cloud-services/tutorials/TutorialExampleOpenAIConnector.zip)

Upload the application into the Analytics [activity center](#glossary-0 "Glossary term").

Interactive Qlik Sense application for using generative AI in responses to complaints and technical issues

![Interactive Qlik Sense app for using OpenAI to interact with app data.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_openai_interactive_app.png "Click to view full size")

### What's in the application?

The application contains a small inline dataset with customer comments on a website for a company offering various products. The comments have been reviewed manually prior to application development to ensure they do not contain any PII or other sensitive information.

We will use OpenAI to generate sample responses and severity analysis based on which customer comment we select in the application.

Information noteThe responses provided by OpenAI are not to be used to completely replace the act of responding to unique customer concerns, but might help generate ideas on where to start addressing their problems.

## Chart expression exercises

After you have uploaded the application, open it and enable editing of its sheets if needed. You might need to make the sheets private.

The example sheets use the Server side extensions syntax to use analytics connectors in chart expressions. The chart expressions reference fields called ComplaintText and ProductDescription, which appear in the data model.

The goal of these exercise is to show how you can use if statements, in an interactive setting where the chart references fields in your data model, to control how often the chart is calculated. This reduces the costs you incur from OpenAI, since in this case the charts are only calculated when a single selection in a single field is made.

These examples are set up so that only one chart expression can be evaluated at a time. This is due to possible rate limits that might apply to your OpenAI services, preventing evaluation of more than one chart expression simultaneously.

### Example 1

The first sheet, Example 1, contains a basic layout of charts showing metrics of a series of customer complaints. The source data includes individual customer complaints, along with dimensions such as the type of product they are complaining about, and a severity score out of 5. There are chart objects to show a selected complaint from the table, and for displaying OpenAI's response to how a customer service department could help the customer with their issue.

Do the following:

1. Open the first sheet, Example 1.
2. In the advanced options edit mode, select the yellow Text & image chart titled OpenAI Possible Starting Points.
3. In the properties panel, under Data, click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) under Expression to open the expression editor.
4. Remove the // from the start of the expression. This uncomments the expression, allowing the expression to be evaluated. The expression should now be:

   ```
   if( count(distinct [ComplaintText]) = 1, endpoints.ScriptAggrStr('{"RequestType":"endpoint", "endpoint":{"connectionname":"OpenAI_Example_InteractiveApp","column":"choices.message.content"}}', 'draft generic starting points for ways a customer can fix an issue reported with '& [ProductDescription]))
   ```
5. Exit edit mode.
6. In the table titled Complaints - Reference Table, select a single cell value in the ComplaintText column.

The OpenAI chart now calculates the response to the selected complaint.

Example 1 sheet highlighting the selected customer complaint, along with OpenAI's suggestions on how to address the comment

![Interactive Qlik Sense app for using OpenAI to interact with app data. A single selection is made in the app, which triggers the OpenAI chart expression to be evaluated and provide a reponse on how to address the selected customer comment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_openai_example1_w_selection.png "Click to view full size")

Clear the selection and try selecting another complaint. The chart will refresh with OpenAI's response to the new selection.

Information noteWhen you are ready to move to Example 2, add the // back to the expression you uncommented above. This prevents the expression from being evaluated when you use the second sheet.

### Example 2

The second sheet, Example 2, contains similar charts as Example 1. The OpenAI object is now configured to provide general impression analysis of the comment that a user selects. This provides general details on how severe the complaint is, and might be helpful in identifying how to prioritize or start addressing the feedback.

Do the following:

1. If you haven't already done so, add the // back to the expression for the OpenAI object in the Example 1 sheet.
2. Open the second sheet, Example 2.
3. In the advanced options edit mode, select the yellow Text & image chart titled OpenAI Initial Impression.
4. In the properties panel, under Data, click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) under Expression to open the expression editor.
5. Remove the // from the start of the expression. This uncomments the expression, allowing the expression to be evaluated. The expression should now be:

   ```
   if( count(distinct [ComplaintText]) = 1, endpoints.ScriptAggrStr('{"RequestType":"endpoint", "endpoint":{"connectionname":"OpenAI_Example_InteractiveApp","column":"choices.message.content"}}', 'provide a short description of how severe the following customer complaint is: ' & [ComplaintText]))
   ```
6. Exit edit mode.
7. In the table titled Complaints - Reference Table, select a single cell value in the ComplaintText column.

The OpenAI chart now calculates the response to the selected complaint.

Example 2 sheet highlighting the selected customer complaint, along with OpenAI's impression of the complaint's severity

![Interactive Qlik Sense app for using OpenAI to interact with app data. A single selection is made in the app, which triggers the OpenAI chart expression to be evaluated and provide a reponse on the general severity of the selected customer comment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_openai_example2_w_selection.png "Click to view full size")

Clear the selection and try selecting another complaint. The chart will refresh with OpenAI's response to the new selection.

## Learn more

- [*Server side extensions syntax*](sse-syntax.htm)
