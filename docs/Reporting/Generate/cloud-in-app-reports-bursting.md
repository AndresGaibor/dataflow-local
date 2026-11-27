---
title: "Burst reporting using report filters"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Generate/cloud-in-app-reports-bursting.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Configuring report generation", "Working with report filters"]
---

# Burst reporting using report filters

With burst reporting, a single [report task](#glossary-0 "Glossary term") can be used to send reports to multiple recipients, with each recipient receiving a different sub-set of application data.

Employ burst reporting by creating [report filters](#glossary-1 "Glossary term") and defining them at the recipient level in your [distribution list](#glossary-2 "Glossary term").

In your distribution list file, you can reference filter names that are created in the Qlik Sense application for each recipient. These filters are created under the Filters tab in the Reporting section of the application used as the source of report generation. This allows the report data to be filtered specifically for individual recipients.

The end goal is to configure a single report task to have multiple different outputs, depending on who receives the report and which filters are applied to them as a recipient.

## Example workflow

Let’s say each manager in your company is to receive a monthly sales report, but they are not to receive the aggregated global data for the company. You only want them to receive the aggregated data for their regional division in the company. Meanwhile, a high-level executive would receive a copy of the report with the data for all divisions. You could complete the following steps:

1. Create a [template](#glossary-3 "Glossary term") that displays a level for a Division field, within which you nest the fields Manager, Sales, and any other relevant fields.
2. Create filters for each division. For each filter, restrict the data to only include one Division field value selection.
3. In the distribution list, add all managers as recipients of the application report tasks and associate each manager to their division filter. Meanwhile, executives could be added as recipients without filters.
4. Create a report task and add all managers as recipients. Each manager’s report will only include data for their division. Executives would see a separate section with all details for each division.

The following table shows how this report task could be configured:

Report task configuration for an example burst reporting scenario

| Recipient | Division | Filter name for the user | Output received |
| --- | --- | --- | --- |
| NorthManager@example.com | North America | NorthAmerica\_Dist\_Filter | Report with sales and performance for managers in North America. |
| SouthManager@example.com | South America | SouthAmerica\_Dist\_Filter | Report with sales and performance for managers in South America. |
| EUManager@example.com | Europe | Europe\_Dist\_Filter | Report with sales and performance for managers in Europe. |
| AsiaManager@example.com | Asia | Asia\_Dist\_Filter | Report with sales and performance for managers in Asia. |
| AfricaManager@example.com | Africa | Africa\_Dist\_Filter | Report with sales and performance for managers in Africa. |
| GlobalExecutive@example.com | All divisions | (No filters) | Report with sales and performance for all divisions. Each division has its own section. |

### How can I implement something like this?

To do something similar to this example, you need to configure your report filters and distribution list accordingly. See the following help topics for more information:

- [*Working with report filters*](cloud-in-app-reports-filters.htm)
- [*Creating a distribution list for your report*](cloud-in-app-reports-distribution.htm)

## Additional filtering and data security with section access

In addition to report filters, section access provides an additional layer of filtering and data security. You can use section access to control the data reduction for report recipients who are added as users in your Qlik Cloud tenant.

For more information, see [*In-application reporting and section access*](cloud-in-app-reports-section-access.htm).
