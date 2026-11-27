---
title: "Configuring editable columns"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/editable-column.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating write tables", "Configuring write tables"]
---

# Configuring editable columns

An editable column is a special type of column that is only available in a [write table](#glossary-0 "Glossary term").

## What is an editable column?

In a write table, editable columns allow users to enter data on the fly during analysis. By saving changes to an editable column, a user writes changes to a [change store](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/change-store.htm), from which they can be retrieved by application developers and integrators.

## Adding an editable column

Do the following:

1. Create a new write table and add dimension and measure columns.

   [*Creating write tables*](create.htm)
2. In the properties panel, expand Data.
3. Click ![Add editable columns](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_user_outline.svg), and then select one of the following:

   - Create new editable column: Create a new, blank editable column.
   - Add existing editable columns: Use existing editable columns that match the [primary keys](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/primary-key.htm) defined for your write table.

After adding the editable column, you can configure its appearance and how users can interact with it. See [*Configuring editable columns*](#ConfigureEditable).

## Configuring editable columns

Do the following:

1. In the properties panel, under Data, click the editable column.

   The column properties open.
2. You can change any of the following properties:

   - Title: Change the default column title.
   - Show content: Change how users can edit data in the table. You can choose between:

     - Manual user input: Users edit data by typing text manually into cells.

       [*Manual entry*](../Analyze/write-table.htm#Manual)
     - Single selection: Specify a set of values that users can select for each cell when editing. For example, you could add two values for orders statuses: On Track and Late. Users can then select between these values when they comment on data records.

       For single selection, you can use either fixed or dynamic values:

       - Fixed: Define values manually by typing them into the entry box. These values are static and do not change with application data.
       - Dynamic: Use expressions to define input values that can change depending on the value of an expression. For example, you can link values to a data model field, or to application [variables](#glossary-1 "Glossary term"). You can specify values and labels, or just values.

         For more information about using expressions in visualizations, see [*Using expressions in visualizations*](../../../ChartFunctions/use-expressions-in-visualizations.htm).

         Tip note

         Syntax:

         Use | to separate values and ~ to separate value and label, like this: value1|value2 or value1~label1|value2~label2.

         Information note

         Up to 1000 values are supported. Values exceeding the limit will be ignored.

         Examples

         ```
         =Concat(Country, '|')
         ```

         ```
         =Concat(DISTINCT City & '~' & Upper(City), '|')
         ```

         ```
         ='Product A|Product B|Product C'
         ```

         ```
         ='$(vMyVariable)'
         ```

         ```
         ='ProductA-value~ProductA-label|ProductB-value~ProductB-label'
         ```

       [*Single selection*](../Analyze/write-table.htm#SingleSelect)
     - Date picker: Users select a date for each cell when editing.

       Information noteIn the user interface, dates entered by users are displayed in the date format defined by the application load script (see [*DateFormat*](../../../Scripting/NumberInterpretationVariables/DateFormat.htm)). These dates are stored in the change store in ISO 8601 format.

       [*Date picker*](../Analyze/write-table.htm#DatePicker)
   - Show column: Toggle whether the column is visible or hidden.
   - Column width: Set the width of the column.

## Styling editable columns

For information about styling the appearance of editable columns, see [*Styling editable columns*](style.htm#StyleEditable).

## Learn more

- [*Creating write tables*](create.htm)
- [*Write table*](../Analyze/write-table.htm)
- [*Working with change stores*](change-store.htm)
- [*Primary keys in write tables*](primary-key.htm)
- [How to extract changes from the Change Store (Write Table) and store them in a database using Qlik Automate](https://community.qlik.com/t5/Official-Support-Articles/How-to-extract-changes-from-the-Change-Store-Write-Table-and/ta-p/2537848)
