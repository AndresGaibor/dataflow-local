---
title: "Best practices for asking questions in Insight Advisor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Insights/InsightAdvisorBestPractices/best-practice-ask-questions-insight-advisor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating visualizations with Insight Advisor", "Insight Advisor best practices"]
---

# Best practices for asking questions in Insight Advisor

Learn best practices for asking questions using Insight Advisor and Insight Advisor Chat.

## Understanding analysis types

When you ask a natural language question in Insight Advisor, you can describe the type of analysis you want to perform. The type of analysis is determined by the phrasing of your question and the combination of dimensions and measures in the question. For example, if you ask, Show revenue by product category and company name, you will get a breakdown rather than a fact as that is the appropriate analysis for two dimensions and one measure.

Tip noteIf you used a natural language question, you can click ![See how Insights Advisor understood the question](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) to view the filters generated from your question.

The following table lists five of the most commonly used analysis types. For a description of other analysis types, see [*Insight Advisor analysis types*](../insight-analysis-types.htm).

Commonly used analysis types

| Analysis type | Description | Dimensions | Measures |
| --- | --- | --- | --- |
| Anomaly (spike) | Identify spike anomalies by analyzing patterns in historic data. | 1 date/time dimension | 1 |
| Calculated measure (KPI) | Summarize performance in a given business segment or dimension using a key performance indicator (KPI). | 0 | 1-2 |
| Clustering (k-means) | Cluster data points aggregated by similarities from 2 measures over a dimension using a machine learning k-means algorithm. | 1 | 2 |
| Ranking | Rank dimension values by relative importance with a measure. | 1-2 | 1 |
| Relative importance | Show the size of dimension values that contribute to the whole. Can also be used to perform Pareto or 80-20 contribution analysis. | 1 | 1 |

If you are not getting the analyses you want, you can use Insight Advisor Analysis Types. This allows you to select the analysis type and the data to use in the analysis. For more information, see [*Creating analyses by selecting analysis types*](../insight-advisor-create-visualizations.htm#Creating).

## Using filters to ask questions

You can use filters in your natural language questions. Using filters is an excellent way to analyze your data from different perspectives and generate insights. Insight Advisor supports the following types of filters:

- Category filters
- Measure filters
- Relative time filters

Insight Advisor uses a sample list of values from your data when determining filters from a question. Filters have the following limitations:

- Text fields with more than 200 characters are excluded from Insight Advisor's profiling.
- Fields that are hidden from the data model can be searched in questions.

### Category filters

You can add category filters to any question in Insight Advisor. You can refer to any dimension value in your question to either exclude or include specific items. You can include up to three values in your question.

Category filters

| Type | Sample questions | Recognized natural language phrases |
| --- | --- | --- |
| Include | What are sales for customers in London?  What are sales in London and sales in Boston?  What are sales in Boston? | On  In  For  With  Have |
| Exclude | What are sales excluding Boston?  Who are customers not in Florida? | Excluding  Not in  Not for  Are not  Have no  Without  Not from  Outside |

Category filters have the following limitations:

- Insight Advisor does not recognize contractions such as isn’t or haven’t. Use the full term instead, such as is not or have not.
- Insight Advisor does not recognize exclusion filters that are used in combination with dates, such as excluding last year.

### Measure filters

You can add measure filters to your questions. This allows you to identify items with no associated measure values and items with measure values that meet certain conditions.

Measure filters

| Type | Sample questions | Recognized natural language phrases |
| --- | --- | --- |
| Greater | Which customers had profit greater than 25%? | Greater than  Larger than |
| Less | What are the sales by customers with less than 10K in licenses? | Less than |
| Equal | Which accounts had the sales representative James? | Is  Is equal to  Equals  = |
| Between | What products are between 10 lb and 20 lb in weight? | Is between  Between |
| No | Who are reps that do not have sales? | Do not have  Have no |

Measure filters have the following limitations:

- Compound filters such as Less than or equal to (<=) and greater than or equal to (>=) are not supported. We recommend using between to show similar results. For example, use show me products with sales between 10 and 20 instead of show me products with sales greater than 10 and less than 20.
- You cannot ask show me sales > 100. Instead, ask show me sales where sales > 100.

### Relative time filters

Certain time-related terms are supported when asking questions. Relative time filters can be used to describe an analysis such as year to date or month over month.

Relative time filters

| Type | Sample questions | Recognized natural language phrases |
| --- | --- | --- |
| After | Show me all invoices with a billing date after 2019. | Since  After  Later than |
| For | What were profits for 2019? | In  For  On |
| Before | What sales are earlier than 2018? | Before  Earlier than |
| Year | What are the profits for this year? | This  Current  Previous  Last  Next n year |
| Comparison | What are sales in 2022 compared to 2021? | VS  VS.  Against  Compared  Over |
| Period over Period | Show me the last 4 periods of sales. | Last n periods  Period over period |
| Month/Quarter | How many orders did we have last month?  How many orders did we have this quarter? | This  Current  Previous  Last  Next n month  Quarter |

Relative time filters have the following limitations:

- Date filters are calculated based on the current date.
- Questions that include weeks as a time period are not supported.
- Relative time filters only work for the Gregorian calendar. Fiscal calendars are not supported. If you want to ask a question about a fiscal period, you can use a category filter. For example, show me sales where fiscal\_order\_quarter is Q1 2014.

### Asking questions with mathematical operations

Insight Advisor does not perform mathematical operations in response to natural language questions. It can perform aggregations in some limited cases, however.

For example, Insight Advisor does not allow you to add two fields together. You can count the number of items in a simple dimension, however.

Aggregations

| Type | Sample questions | Recognized natural language phrases |
| --- | --- | --- |
| Count | How many products?  What is the count of territories? | Count  Number  How many |
| Sum | What is the total cost for each product? | Sum  Total |
| Average | What is the average cost for this year? | Average  Avg |
| Minimum | What is minimum cost? | Min  Minimum  Minimal |
| Maximum | What is the territory with maximum sales? | Max  Maximum |

Questions with aggregations have the following limitations:

- You cannot ask for aggregations of a master measure. Master measures already have a defined aggregation.
- If access to the application is limited, users do not have access to fields, such as in a published application, you cannot aggregate those fields. This is consistent with application creation behavior. For example, you cannot create a KPI based on a master dimension. You can, however, create a master measure such as customer count that Insight Advisor users can use to ask questions.

## Asking questions with auto-complete

Insight Advisor recognizes inputs as they are being typed by a user. It prompts you with an auto-complete drop down for all corresponding matching fields, master items, and data values. For users with read-only permission, only master items and the values for master items appear in the auto-complete drop-down. If a master item is a drill-down dimension, there will be no match on the values.

Drop-down options by using auto-complete

![An image showing a question in the Insight Advisor search box and different drop-down options that are connected to a keyword in the question. Drop-down options include fields and data values that are connected to a key word in the question.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_InsightAdvisor_BestPractices_AutoComplete.png "Click to view full size")

## Using Insight Advisor Chat

These best practices show you how to ask questions more effectively and see different types of insights from your data with Insight Advisor Chat.

### Asking a series of questions

Insight Advisor Chat remembers certain aspects of previous questions to help you get the answer you want. For example, you ask the question show me total sales, followed by how about tobacco. You receive sales results for tobacco as Insight Advisor remembers that you are interested in sales.

Insight Advisor Chat with context-sensitive answer

![Image shows messages in Insight Advisor Chat and that Insight Advisor Chat can return answers that are context-sensitive. The user asks about total sales and then asks about a product category and Insight Advisor returns the total sales of that product category.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_InsightAdvisor_BestPractices_IAC.png "Click to view full size")

Similarly, time filters are remembered if the previous question contains a measure and a time filter. You can also ask for multiple dimension values in the context of multiple measures. For example, you can ask Show me Sales and Profit for Supplier where SupplierCountry is not Germany and Supplier is not Gal Export.

If you are asking a subsequent question and do not want Insight Advisor to apply a remembered time filter or measure, type and send clear entity context. This clears the conversation context without clearing the selected application.

## Spelling and Insight Advisor

Misspelled words are not recognized by Insight Advisor. It is critical that your questions reference existing fields and values precisely, including, but not limited to: dimensions, master items, and measures.

This includes attempts at fuzzy matching, where partial words are used to represent larger words. These would only be recognized if the specific fuzzy matching attempt was built into the application's business logic vocabulary.

Information noteIn some cases Insight Advisor cannot recognize the plural of a field name, such as how many countries. You might have to ask, how many country do I have. Another option would be to add a synonym countries for the field country using Vocabulary in Business Logic. For more information, see [*Adding synonyms to Insight Advisor*](../../BusinessLogic/business-logic-vocabulary-synonyms.htm).

## Accessibility and Insight Advisor

Insight Advisor recognizes voice inputs using voice-recognition functionality in Google Chrome. You can enable voice input by clicking the microphone ![Use microphone](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_microphone.svg) in the Insight Advisor chat.

Related learning:

- [How do I evaluate Relative importance in a Pareto chart?](/lnk/How_evaluate_Relative_importance_Pareto)
- [How do I detect anomalies in a time series?](/lnk/How_detect_anomalies_time_series)
