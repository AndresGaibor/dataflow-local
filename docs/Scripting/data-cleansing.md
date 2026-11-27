---
title: "Data cleansing"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/data-cleansing.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Next steps in scripting"]
---

# Data cleansing

There are times when the source data that you load into Qlik Sense is not necessarily how you want it in the Qlik Sense application. Qlik Sense provides a host of functions and statements that allow you to transform our data into a format that works for us.

Mapping can be used in a Qlik Sense script to replace or modify [field](#glossary-1 "Glossary term") values or names when the script is run, so mapping can be used to clean up data and make it more consistent or to replace parts or all of a field value.

When you load data from different tables, field values denoting the same thing are not always consistently named. Since this lack of consistency hinders associations, the problem needs to be solved. This can be done in an elegant way by creating a mapping table for the comparison of field values.

## Mapping tables

Tables loaded via Mapping load or Mapping select are treated differently from other tables. They are stored in a separate area of the memory and used only as mapping tables when the script is run. After the script is run these tables are automatically dropped.

### Rules:

- A mapping table must have two columns, the first one containing the comparison values and the second the desired mapping values.
- The two columns must be named, but the names have no relevance in themselves. The column names have no connection to field names in regular internal tables.

## Mapping functions and statements

The following mapping functions/statements will be addressed in this tutorial:

• Mapping prefix

• ApplyMap()

• MapSubstring()

• Map … Using statement

• Unmap statement

## Mapping prefix

The Mapping prefix is used in a script to create a mapping table. The mapping table can then be used with the ApplyMap() function, the MapSubstring() function or the Map … Using statement.

Do the following:

1. Create a new application and give it a name.
2. Add a new script section in the Data load editor.
3. Call the section Countries.
4. Enter the following script:

```
CountryMap:
MAPPING LOAD * INLINE [
Country, NewCountry
U.S.A., US
U.S., US
United States, US
United States of America, US
];
```

The CountryMap table stores two columns: Country and NewCountry. The Country column stores the various ways country has been entered in the Country field. The NewCountry column stores how the values will be mapped. This mapping table will be used to store consistent US country values in the Country field. For instance, if U.S.A. is stored in the Country field, map it to be US.

## ApplyMap() function

Use ApplyMap() to replace data in a field based on a previously created mapping table. The mapping table need to be loaded before the ApplyMap() function can be used. The data in the Data.xlsx table that you will load looks like this:

Data table

| ID | Name | Country | Code |
| --- | --- | --- | --- |
| 1 | John Black | U.S.A. | SDFGBS1DI |
| 2 | Steve Johnson | U.S. | 2ABC |
| 3 | Mary White | United States | DJY3DFE34 |
| 4 | Susan McDaniels | u | DEF5556 |
| 5 | Dean Smith | US | KSD111DKFJ1 |

Notice that the country is entered in various ways. In order to make the country field consistent, the mapping table is loaded and then the ApplyMap() function is used.

Do the following:

1. Beneath the script you entered above, select and load Data.xlsx, and then insert the script.
2. Enter the following above the newly created LOAD statement:

```
Data:
```

Your script should look like this:

```
CountryMap:
MAPPING LOAD * INLINE [
    Country, NewCountry
    U.S.A., US
    U.S., US
    United States, US
    United States of America, US
];

Data:
LOAD
    ID,
    Name,
    Country,
    Code
FROM [lib://DataFiles/Data.xlsx]
(ooxml, embedded labels, table is Sheet1);
```

3. Modify the line containing Country, as follows:

```
ApplyMap('CountryMap', Country) as Country,
```

The first parameter of the ApplyMap() function has the map name enclosed in single quotes. The second parameter is the field that has the data that is to be replaced.

4. Click Load data.

The resulting table looks like this:

Table showing data loaded using ApplyMap() function

![Table showing data loaded using ApplyMap function.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-data-cleansing-applymap.png "Click to view full size")

The various spellings of the United States have all been changed to US. There is one record that was not spelled correctly so the ApplyMap() function did not change that field value. Using the ApplyMap() function, you can use the third parameter to add a default expression if the mapping table does not have a matching value.

5. Add 'US' as the third parameter of the ApplyMap() function, to handle such cases when the country may have been entered incorrectly:

```
ApplyMap('CountryMap', Country, 'US') as Country,
```

Your script should look like this:

```
CountryMap:
MAPPING LOAD * INLINE [
    Country, NewCountry
    U.S.A., US
    U.S., US
    United States, US
    United States of America, US
];

Data:
LOAD
    ID,
    Name,
    ApplyMap('CountryMap', Country, 'US') as Country,
    Code
FROM [lib://DataFiles/Data.xlsx]
(ooxml, embedded labels, table is Sheet1);
```

6. Click Load data.

The resulting table looks like this:

Table showing data loaded using ApplyMap function

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-data-cleansing-applymap-updated.png "Click to view full size")

Information noteTo learn more about ApplyMap(), see this blog post in Qlik Community: [Don't join - use Applymap instead](https://community.qlik.com/t5/Qlik-Design-Blog/Don-t-join-use-Applymap-instead/ba-p/1467592)

## MapSubstring() function

The MapSubstring() function allows you to map parts of a field.

In the table created by ApplyMap() we now want the numbers to be written as text, so the MapSubstring() function will be used to replace the numeric data with text.

In order to do this a mapping table first needs to be created.

Do the following:

1. Add the following script lines after the CountryMap section, but before the Data section.

```
CodeMap:
MAPPING LOAD * INLINE [
F1, F2
1, one
2, two
3, three
4, four
5, five
11, eleven
];
```

In the CodeMap table, the numbers 1 through 5, and 11 are mapped.

2. In the Data section of the script modify the Code statement as follows:

```
MapSubString('CodeMap', Code) as Code
```

Your script should look like this:

```
CountryMap:
MAPPING LOAD * INLINE [
    Country, NewCountry
    U.S.A., US
    U.S., US
    United States, US
    United States of America, US
];

CodeMap:
MAPPING LOAD * INLINE [
    F1, F2
    1, one
    2, two
    3, three
    4, four
    5, five
    11, eleven
];

Data:
LOAD
    ID,
    Name,
    ApplyMap('CountryMap', Country, 'US') as Country,
    MapSubString('CodeMap', Code) as Code
FROM [lib://DataFiles/Data.xlsx]
(ooxml, embedded labels, table is Sheet1);
```

3. Click Load data.

The resulting table looks like this:

Table showing data loaded using MapSubString function

![Table showing data loaded using MapSubString function.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-data-cleansing-mapsubstring.png "Click to view full size")

The numeric characters were replaced with text in the Code field. If a number appears more than once as it does for ID=3, and ID=4, the text is also repeated. ID=4. Susan McDaniels had a 6 in her code. Since 6 was not mapped in the CodeMap table, it remains unchanged. ID=5, Dean Smith, had 111 in his code. This has been mapped as 'elevenone'.

Information noteTo learn more about MapSubstring(), see this blog post in Qlik Community: [Mapping … and not the geographical kind](https://community.qlik.com/t5/Qlik-Design-Blog/Mapping-and-not-the-geographical-kind/ba-p/1463192)

## Map … Using

The Map … Using statement can also be used to apply a map to a field. However, it works a little differently than ApplyMap(). While ApplyMap() handles the mapping every time the field name is encountered, Map … Using handles the mapping when the value is stored under the field name in the internal table.

Let’s take a look at an example. Assume we were loading the Country field multiple times in the script and wanted to apply a map every time the field was loaded. The ApplyMap() function could be used as illustrated earlier in this tutorial or Map … Using can be used.

If Map … Using is used then the map is applied to the field when the field is stored in the internal table. So in the example below, the map is applied to the Country field in the Data1 table but it would not be applied to the Country2 field in the Data2 table. This is because the Map … Using statement is only applied to fields named Country. When the Country2 field is stored to the internal table it is no longer named Country. If you want the map to be applied to the Country2 table then you would need to use the ApplyMap() function.

The Unmap statement ends the Map … Using statement so if Country were to be loaded after the Unmap statement, the CountryMap would not be applied.

Do the following:

1. Replace the script for the Data table with the following:

```
Map Country Using CountryMap;
Data1:
LOAD
    ID,
    Name,
    Country
FROM [lib://DataFiles/Data.xlsx]
(ooxml, embedded labels, table is Sheet1);

Data2:
LOAD
    ID,
    Country as Country2
FROM [lib://DataFiles/Data.xlsx]
(ooxml, embedded labels, table is Sheet1);
UNMAP;
```

2. Click Load data.

The resulting table looks like this:

Table showing data loaded using Map … Using function

![Table showing data loaded using Map … Using function.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-data-cleansing-mapusing.png "Click to view full size")
