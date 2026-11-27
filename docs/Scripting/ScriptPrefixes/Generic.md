---
title: "Generic"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Generic.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---

# Generic

Expand/Collapse all

# Generic

The Generic load prefix allows for conversion of entity–attribute–value modeled data (EAV) into a traditional, normalized relational table structure. EAV modeling is alternatively referred to as "generic data modeling" or "open schema".

Example of EAV modeled data and an equivalent denormalized relational table

![Diagram showing transformation of a table with three columns and five rows into a table with four columns and two rows. The initial table has an 'Attributes' column, within which each entry gets converted to its own column in the resulting table: 'Status', 'Colour', and 'Size'.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-generic-EAV-denormalized.png "Click to view full size")

Example of EAV modeled data and an equivalent set of normalized relational tables

![Diagram showing transformation of a table with three columns and five rows into three separate tables. The initial table has an 'Attributes' column, within which each entry ('Status', 'Colour', and 'Size') gets converted into its own table. The 'Product ID' field remains constant in all tables.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-generic-EAV-normalized.png "Click to view full size")

While it is technically possible to load and analyze EAV modeled data in Qlik, it is often easier to work with an equivalent traditional relational data structure.

Syntax:

Generic( loadstatement | selectstatement
)

- For more information about using LOAD statements, see [*Load*](../ScriptRegularStatements/Load.htm).
- For more information about using SELECT statements, see [*Select*](../ScriptRegularStatements/Select.htm).

These topics may help you work with this function:

Related topics

| Topic | Description |
| --- | --- |
| [*Crosstable*](crosstable.htm) | The Crosstable load prefix transforms data that is horizontally-oriented into vertically-oriented data. From a purely functional perspective, it performs the opposite transformation to the Generic load prefix, although the prefixes typically serve entirely different use cases. |
| [*Generic databases*](../../DataSource/generic-databases.htm) | EAV structured data models are further described here. |

## Example 1 – Transforming EAV structured data with the Generic load prefix

Load script and chart expression

Overview

Open the [Data load editor](#glossary-0 "Glossary term") and add the [load script](#glossary-1 "Glossary term") below to a new tab.

The load script contains a [dataset](#glossary-2 "Glossary term") which is loaded into a table named Transactions. The dataset includes a date [field](#glossary-3 "Glossary term"). The default MonthNames definition is used.

Load script

```
Products:
Generic
Load * inline [
Product ID, Attribute, Value
13, Status, Discontinued
13, Color, Brown
20, Color, White
13, Size, 13-15
20, Size, 16-18
2, Status, Discontinued
5, Color, Brown
2, Color, White
44, Color, Brown
45, Size, 16-18
45, Color, Brown
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: Color.

Add this [measure](#glossary-4 "Glossary term"):

=Count([Product ID])

Now you can inspect the number of products by color.

Results table

| Color | =Count([Product ID]) |
| --- | --- |
| Brown | 4 |
| White | 2 |

Note the shape of the data model, where each attribute has been broken out into a separate table named according to the original target table tag Product.Each table has the attribute as a suffix. One example of this is Product.Color. The resulting Product Attribute output records are associated by the Product ID.

Data model viewer representation of the results

![Representation of the results of this example as they appear in the data model viewer. The Product ID field in each of the three tables is associated throughout the data model.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-generic-results-data-model-viewer.png "Click to view full size")

Resulting table of records: Products.Status

| Product ID | Status |
| --- | --- |
| 13 | Discontinued |
| 2 | Discontinued |

Resulting table of records: Products.Size

| Product ID | Size |
| --- | --- |
| 13 | 13-15 |
| 20 | 16-18 |
| 45 | 16-18 |

Resulting table of records: Products.Color

| Product ID | Color |
| --- | --- |
| 13 | Brown |
| 5 | Brown |
| 44 | Brown |
| 45 | Brown |
| 20 | White |
| 2 | White |

## Example 2 – Analyzing EAV structured data without the Generic load prefix

Load script and chart expression

Overview

This example shows how to analyze EAV structured data in its original form.

Open the Data load editor and add the load script below to a new tab.

The load script contains a dataset which is loaded into a table named Products in an EAV structure.

In this example, we are still counting products by color attribute. In order to analyze data structured in this way, you will need to apply expression-level filtering of products carrying the Attribute value Color.

Furthermore, individual attributes are not available to select as [dimensions](#glossary-5 "Glossary term") or fields, making it harder to determine how to build effective [visualizations](#glossary-6 "Glossary term").

Load script

```
Products:
Load * Inline
[
Product ID, Attribute, Value
13, Status, Discontinued
13, Color, Brown
20, Color, White
13, Size, 13-15
20, Size, 16-18
2, Status, Discontinued
5, Color, Brown
2, Color, White
44, Color, Brown
45, Size, 16-18
45, Color, Brown
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: Value.

Create the following measure:

=Count({<Attribute={'Color'}>} [Product ID])

Now you can inspect the number of products by color.

Resulting table of records: Products.Status

| Value | =Count({<Attribute={'Color'}>} [Product ID]) |
| --- | --- |
| Brown | 4 |
| White | 2 |

## Example 3 – Denormalizing the resulting output tables from a Generic load (advanced)

Load script and chart expression

Overview

In this example, we show how the normalised data structure produced by the Generic load prefix can be denormalised back into a consolidated Product dimension table. This is an advanced modeling technique which can be employed as part of data model performance tuning.

Open the Data load editor and add the load script below to a new tab.

Load script

```
Products:

Generic
Load * inline [
Product ID, Attribute, Value
13, Status, Discontinued
13, Color, Brown
20, Color, White
13, Size, 13-15
20, Size, 16-18
2, Status, Discontinued
5, Color, Brown
2, Color, White
44, Color, Brown
45, Size, 16-18
45, Color, Brown
];

RENAME TABLE Products.Color TO Products;

OUTER JOIN (Products)
LOAD * RESIDENT Products.Size;

OUTER JOIN (Products)
LOAD * RESIDENT Products.Status;
DROP TABLES Products.Size,Products.Status;
```

Results

Open the Data model viewer and note the shape of the resulting data model. Only one denormalized table is present. It is a combination of the three intermediary output tables: Products.Size, Products.Status, and Products.Color.

Resulting internal data model

| Products |
| --- |
| Product ID |
| Status |
| Color |
| Size |

Resulting table of records: Products

| Product ID | Status | Color | Size |
| --- | --- | --- | --- |
| 13 | Discontinued | Brown | 13-15 |
| 20 | - | White | 16-18 |
| 2 | Discontinued | White | - |
| 5 | - | Brown | - |
| 44 | - | Brown | - |
| 45 | - | Brown | 16-18 |

Load the data and open a sheet. Create a new table and add this field as a dimension: Color.

Add this measure:

=Count([Product ID])

Results table

| Color | =Count([Product ID]) |
| --- | --- |
| Brown | 4 |
| White | 2 |

## Learn more

- [*Load*](../ScriptRegularStatements/Load.htm)
- [*Select*](../ScriptRegularStatements/Select.htm)
- [*Crosstable*](crosstable.htm)
- [*Generic databases*](../../DataSource/generic-databases.htm)
