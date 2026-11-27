---
title: "Cycling reports"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Generate/reports-cycles.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Configuring report generation", "Working with report tasks"]
---

# Cycling reports

With cycles, you can generate multiple versions of a report broken down by dimension, such as year or region. Cycles are added when configuring a [report task](#glossary-0 "Glossary term").

Cycles work by filtering the data included in each version of the report. The difference between a cycle and a report filter is that by adding a cycle, a single execution of the report task can generate more than one unique report for a single recipient. When you add a cycle to a report task, a unique report is generated for each unique value in the dimension you select as the cycle. If you have more than one cycle field, you will get as many reports as the combination of all cycle fields.

Cycles interact with the other types of filtering which can be applied during report generation. The order of evaluation is as follows:

1. [Section access](#glossary-1 "Glossary term"), if present
2. Task-level [report filter](#glossary-2 "Glossary term"), if present
3. Recipient-level report filter, if present
4. Cycles, if present

## Example

For example, you have a report task to send sales reports. The report task is configured with the following settings:

- File name: SalesData
- Cycle on fields Country and Year
- Timestamp format: yyyy-MM-dd\_HH-mm

Your data covers three countries and two years, so six reports are generated and sent:

- SalesData\_
  Country1
  \_
  Year1
  \_2024-11-08\_10-30.xlsx
- SalesData\_
  Country1
  \_
  Year2
  \_2024-11-08\_10-30.xlsx
- SalesData\_
  Country2
  \_
  Year1
  \_2024-11-08\_10-30.xlsx
- SalesData\_
  Country2
  \_
  Year2
  \_11-08\_10-30.xlsx
- SalesData\_
  Country3
  \_
  Year1
  \_11-08\_10-30.xlsx
- SalesData\_
  Country3
  \_
  Year2
  \_11-08\_10-30.xlsx

Once created, the output files are sent to their destination as they normally would. Report filters and section access filtering are still applied as they usually would be.

## Adding cycles to your report task

For more information about creating a report task, see [*Creating a report task*](cloud-in-app-reports-tasks.htm#Creating).

Do the following:

1. Create a report task and begin the configuration process as you usually would.
2. After completing the Template section of the dialog, you arrive at Output.
3. Under Cycle, use the drop down menu to select up to three [dimensions](#glossary-3 "Glossary term") from the application.

## Output file names

When you add a cycle, the name of the dimension value applied in the cycle is included in report file names. If a dimension value applied in the cycle contains any special characters, they are replaced with an underscore character (\_) in the file name.

Special characters include:

- \ / < > : " ' ? \*
- ASCII control characters

## Handling errors

If an error occurs for one or more reports in a cycle, an empty file is generated for each failed report. The name of each of these files has a "FAILED\_" prefix and reflects the combination of values that ended in error.

## Best practices and limitations

### Best practices

You should not start a report cycle to your report task if your report dimensions contain many values or unique value combinations. For example, if your data covers 10 years, 196 countries, and 50 products, report cycling could potentially generate up to 98,000 files (see guardrail [below](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/reports-cycles.htm#Limitations) for current unique task constraint). This could take hours or days to generate, and could consume a large volume of report generation for your Qlik Cloud subscription.

### Limitations

- You can select a maximum of three fields to cycle for a report task.
- A [report task](#glossary-4 "Glossary term") can generate a maximum of 500 unique reports. This limit is evaluated across all templates added to the task, rather than per template in the task. This limit also applies to all report tasks regardless of whether or not one or mores cycles are applied.
- You cannot set an HTML report template to generate as an embedded email message if a cycle has been applied to the report task.

For other limitations that apply to in-application reporting, see [*Qlik Reporting Service specifications and limitations*](../Reporting-service-specifications-limitations.htm#Limits2).
