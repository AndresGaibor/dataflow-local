---
title: "Managing field-level metadata and data profiling"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/Profiling-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Understanding your data with catalog tools", "Viewing and managing datasets in the catalog"]
---

# Managing field-level metadata and data profiling

Expand/Collapse all

# Managing field-level metadata and data profiling

Field-level metadata lets users apply aliases, descriptions, and classifications to fields; these features assist with identifying specific data and sensitive fields.

Data administrators access rich technical information about their datasets from profiling. Application developers use profile statistics and data sampling to gain ideas and direction for creating applications and planning [visualizations](#glossary-0 "Glossary term"). Field profiling can help data analysts and business users to gain insights faster. They can view and visualize valuable [field](#glossary-1 "Glossary term") profile metrics at-a-glance without needing to create an application first.

Information note

Qlik Cloud only profiles up to 12 million rows in a database-based [dataset](#glossary-3 "Glossary term"). If a database-based dataset exceeds 12 million rows, only the first 12 million rows are profiled. Metadata for all fields is still added, regardless of the number of rows profiled.

The profiling process has a time constraint applied to both file-based and database-based datasets, limiting the profiling to a 30 minute time window. A profile will be marked as failed if it exceeds this time limit.

## Permissions

Permissions are required to profile and sample data. You must have a role in the dataset's space that allows you to profile data sources. For more information, see [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm) or [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm).

## Managing field-level metadata

You can access and edit metadata for every field in your dataset from the Profile tab.
Select any card from the ![Tile view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_profile_tile.svg) Tile view, any row from the ![List view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_profile_list.svg) List view, or any column from the ![Data view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table2.svg) Data view to open that field's Details panel to the right of the grid. Field-level metadata fields — Field alias, Description, Tags, and Classification— are optional and can be defined and edited from this panel.

Field metadata fields

| Detail | Description |
| --- | --- |
| Field alias | Enter an optional alternate name to make field names more meaningful in the profile analysis. Alias field names only display in the profile analysis and do not impact technical column names.  Information noteThe alias cannot be identical to an existing field or alias name in the dataset. |
| Description | Enter any information that may be helpful to users viewing field metadata and profiling for the field. |
| Tags | Enter text snippets to define and categorize this field and its data. |
| Classification | Select one or more relevant classifications from the drop-down list. You can apply multiple classifications to a field. |

Information noteSelected field-level classifications appear in the Dataset overview tab and are listed by field below technical dataset metadata.

Information noteClassifications applied to fields in Excel files with multiple sheets are listed with sheet name and field name (example: Sheet1/EmpID).

Field-level metadata for an XLSX file with multiple sheets

![Select a field card in tile view to open the Details panel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_FieldLevelMetaData-rev2.png "Click to view full size")

You can also link a field to a term in your business glossary from the Details panel. For more information, see [*Linking dataset fields to business glossary terms*](BusinessGlossary/linking-dataset-fields-glossary-terms.htm).

Profiling behavior varies by data source and file size for QVD and Parquet files. For more information, see [*Limited profile view*](#Limited).

## Profiling data

Profile statistics provide column analyses that [measure](#glossary-4 "Glossary term") incidence, ranges, and values that occur within datasets. These metrics describe relationships between field values such as:

- Count of distinct values ([cardinality](#glossary-5 "Glossary term"))
- Sample values, most common values, and value frequency
- Redundancies useful in identifying default or potential duplicate values
- Counts of null, string, and numeric values
- Information about value ranges including min, max, average, sum, and standard deviation

Catalog provides three views of field profile data:

- Tile view is a card-based, visual representation of fields laid out as a grid.
- List view is a tabular summary of configurable profile statistics.
- Table view lists field column names and up to the first twenty records of the dataset.

Select the Tile ![Tile view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_profile_tile.svg), List ![List view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_profile_list.svg), or Data ![Data view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table2.svg) icon to switch between profile views.

### Tile view

Profile tile view is a visual field profile designed to display the most informative content for that type of field. The default view card type shown is determined by whether the number of numeric or text values is higher for that field. For example, for fields with both text and numeric values, Most Common Values card type displays by default if there are more text values and the Binned Frequency numeric distribution card type displays if there are more numeric values in the field. A dropdown toggle is provided so that you can switch over to the Most Common Values card type for any field that has non-unique values when ![ icon Most Common Values](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bars_horizontal.svg) is selected; or you can switch back to the numeric distribution card if Binned Frequency ![icon Binned Frequency](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_line_chart_2.svg) is selected. Note that all card types include the number of null values, if the field has null values.

Tile view: Fields are profiled by metrics that are meaningful for the type of data contained in that field (for example: text versus numeric values)

![Profile tile view of dataset](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ProfileTileView-rev2.png "Click to view full size")

#### Sample values card

The Sample values card is shown when all values are unique and text-only. It will list (up to) the first three values and the total number of additional unique values.

Tile view card: Sample Values

![Sample values tile](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SampleValuesTile.png "Click to view full size")

Sample values profile criteria: Field values are profiled with this card when cardinality is high (all distinct values). In a case where every value is text-based and unique, a few sample values provides the best initial view into this type of field's data.

Each Sample values profile card provides:

- Field name
- Cardinality (distinct values)
- Up to three sample values (fields may have less than three values)

#### Most common values frequency card

The Most common values frequency card shows the five most common values and their frequency. If there are more values than five distinct values, these are combined and displayed as Other. If any fields are missing values, the total is displayed as Null. This profile card can be applied on text, numeric, or mixed data values.

Tile view card: Most Common Values Frequency

![Tile most common values frequency](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_MostCommonValuesFreq_611x365.png "Click to view full size")

Most common values frequency criteria: Fields that have few values or a skewed distribution of values are profiled with the most common values frequency card. This profiling is only applied when there are multiple instances of the same values. Users can gain quick insight into the distribution of field values. If the field data includes both text and numeric values, and there are more text than numeric values, then the Most common values frequency card is shown. The Binned frequency toggle is provided when there are more than three numeric values in the field.

Each Most common values frequency profile card provides:

- Field name
- Cardinality (distinct values)
- Most common values and their frequency
- Other combined frequency of remaining values

#### Binned frequency card

The Binned frequency card shows distribution and profiling information that is relevant for numeric fields; including minimum, average, and maximum data values. If the field data includes both text and numeric values, and there are more numeric than text values, then the Binned frequency card is shown. The Most Common Values Frequency card type is available for all fields that have non-unique values.

Tile view card: Binned Frequency numeric distribution

![Binned frequency tile](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_BinnedFrequencyTile.png "Click to view full size")

Each Binned frequency profile card provides:

- Field name
- Cardinality (distinct values)
- Histogram showing the numeric data distribution
- Minimum value
- Average value (the sum of the numbers divided by the total number of values in the dataset)
- Maximum value

### List view

Profile list view provides a table with profile statistic options. Users check the metrics of interest that are most meaningful for the dataset under the column picker ![icon columns](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_columns.svg), which can be found by scrolling to the far-right edge of the table. The first nine statistics are preselected by default.

List view: Select profile statistics of interest from the column picker found by scrolling right on the table

![Profile list view of dataset ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ProfileListView-rev.png "Click to view full size")

Available profile statistics

Field profile statistics

| Statistic | Description |
| --- | --- |
| Name | Field name (example: CategoryID) |
| Data type | Qlik Sense registers data from many different systems, an external to internal uniform data type mapping is imposed on field (column) data for informational purposes. Supported data type values include:   - Date: A date containing month, day, year in ISO 8601 format of YYYY-MM-DD - Time: A time value containing hour, minutes, seconds in ISO 8601 format of hh.mm.ss.sss±hh:mm - Datetime: A datetime value containing Year, Month, Day, Hour, Minute, Second, and fractions in format of YYYY-MM-DDThh.mm.ss.sss - Timestamp: A timestamp value containing Year, Month, Day, Hour, Minute, Second, fractions, and timezone in the following format of YYYY-MM-DDThh.mm.ss.sssZ - String: Character data representing text - Double: A numeric data type with double-precision 64-bit IEEE 754 floating point - Decimal: An exact numeric data type defined by its precision (total number of digits) and scale (number of digits to the right of the decimal point) - Integer: Positive or negative whole numbers - Boolean: A Boolean value (TRUE/FALSE) - Binary: Categorical data that can take exactly two possible values, such as "1" and "2" - Custom: Type that is outside of the mapped system-known type |
| Distinct values | Cardinality, number of distinct values present for this field |
| Null values | Number of null values |
| Sample values | Sample values (3 sample values display) |
| Sum | Sum of all values in this field ("0" displays for string fields) |
| Min | Minimum observed value for this field (numeric fields) |
| Max | Maximum observed value for this field (numeric fields) |
| Average | Average observed value for this field |
| Median | Median (or middle) number in the array of numbers for this field |
| System Tags | File tags applied to identify the code set (ex. $ascii, $text) |
| Standard Deviation | Standard deviation for numeric fields |
| Positives | Number of positive values |
| Negatives | Number of negative values |
| Zero values | Number of "0" values |
| Empty strings | Number of empty strings |
| Min length | Lowest observed character length |
| Average length | Average observed character length |
| Max length | Highest observed character length |
| First sorted value | The first (lowest) value of sort weight (string fields) |
| Last sorted value | The last (highest) value of sort weight (string fields) |
| Numeric values | Number of numeric values |
| Text values | Number of text values |
| Most frequent values | The three most common values in the field |

### Data view

The profile data view displays your dataset as a straight data table with field column names and (up to) the first twenty values.

Data view: Dataset column names and the first twenty records display

![Profile data view of dataset](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ProfileDataView-rev.png "Click to view full size")

## Limited profile view

Some datasets display a limited profile view instead of the full profile. The limited profile shows field names, data types, distinct values, null values, and sample values. For QVD and Parquet files smaller than 1 GB in cloud storage connectors, the limited profile is displayed first. You can click Profile dataset to generate the full profile. For files that are 1 GB or larger, QVD and Parquet files show field names and data types only. Detailed profile information is not available.

The following table shows profiling behavior for cloud storage connectors by file format and file size.

| File format | File smaller than 1 GB | File 1 GB or larger |
| --- | --- | --- |
| QVD, Parquet | Limited profile view displayed first. Click Profile dataset to get the full profile. | Field names and data types only. Detailed profile information is not available. |
| Other formats | Full profile. | No profile available. The 1 GB limit applies. |

Information note

This behavior applies to cloud storage connectors including Amazon S3, Amazon S3 V2, Azure Storage, Dropbox, Google Cloud Storage, Google Drive, Office 365 SharePoint, and SFTP.

A limited profile of a QVD dataset

![Limited profile view of a QVD dataset showing field names, data types, distinct values, null values, and sample values](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_profile-limited-view.png "Click to view full size")

Available profile statistics

Limited profile statistics

| Statistic | Description |
| --- | --- |
| Name | Field name (example: CategoryID) |
| Data type | Qlik Sense registers data from many different systems, an external to internal uniform data type mapping is imposed on field (column) data for informational purposes. Supported data type values include:   - Date: A date containing month, day, year in ISO 8601 format of YYYY-MM-DD - Time: A time value containing hour, minutes, seconds in ISO 8601 format of hh.mm.ss.sss±hh:mm - Datetime: A datetime value containing Year, Month, Day, Hour, Minute, Second, and fractions in format of YYYY-MM-DDThh.mm.ss.sss - Timestamp: A timestamp value containing Year, Month, Day, Hour, Minute, Second, fractions, and timezone in the following format of YYYY-MM-DDThh.mm.ss.sssZ - String: Character data representing text - Double: A numeric data type with double-precision 64-bit IEEE 754 floating point - Decimal: An exact numeric data type defined by its precision (total number of digits) and scale (number of digits to the right of the decimal point) - Integer: Positive or negative whole numbers - Boolean: A Boolean value (TRUE/FALSE) - Binary: Categorical data that can take exactly two possible values, such as "1" and "2" - Custom: Type that is outside of the mapped system-known type |
| Distinct values | Cardinality, number of distinct values present for this field |
| Null values | Number of null values |
| Sample values | Sample values (3 sample values display) |

Related learning:

- [How do I use the Data Catalog to profile data?](/lnk/How_use_datacatalog_profile_data)
