---
title: "LevenshteinDist Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/LevenshteinDist.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# LevenshteinDist Script and chart function

LevenshteinDist() returns the Levenshtein distance between two strings. It is defined as the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into the other.
The function is useful for fuzzy string comparisons.

Syntax:

LevenshteinDist(text1, text2)

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| text1 | The first string. |
| text2 | The second string which will be compared to the first string in order to calculate the minimum number of single-character edits. |

Example: Chart expression

| Example | Result |
| --- | --- |
| `LevenshteinDist( 'Kitten','Sitting' )` | Returns `3` |

## Example - LevenshteinDist fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- One field in the data table called `InputText`.

Load script

```
Example:
Load * inline [
InputText
Sliver
SSiver
SSiveer
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `InputText`

Create the following measure:

- `=LevenshteinDist('Silver', InputText)`, to calculate the minimum number of single character edits required to change the string value for `InputText` to the word `Silver`.

Results table

| InputText | LevenshteinDist('Silver', InputText) |
| --- | --- |
| Sliver | 2 |
| SSiveer | 3 |
| SSiver | 2 |

The output of the `LevenshteinDist` function returns the number of changes required to change the `InputText` to the expected text, `Silver`. For example, the first row requires two changes to modify the word `Sliver` to `Silver`. The second row requires 3 changes: 1) Delete the extra character `S`. 2) Delete the extra character `e`. 3) Insert a new character `l`.

## Example - LevenshteinDist scenario

Chart expression

Overview

This example consolidates product names from different systems. The product names do not always use the same spelling due to typos, abbreviations, spacing, or other variations. Using the `LevenshteinDist` function, you can measure the similarity between two product names and identify which ones likely refer to the same product, even if the names are not identical.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `ProductA`
  - `ProductB`

Load script

```
Example:
Load * inline [
ProductA, ProductB
Coca Cola 330ml, CocaCola 330 ml
Pepsi 500 ml, Pepsi 500ml
Sprite Zero 600 ml, SpriteZero600ml
Red Bull 250ml, Redbull 250ml
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ProductA`
- `ProductB`

Create the following measure:

- `=LevenshteinDist(ProductA, ProductB)`, to calculate the minimum number of single character edits required to change the string value for `ProductB` to match `ProductA`.

Results table

| ProductA | ProductB | LevenshteinDist(ProductA, ProductB) |
| --- | --- | --- |
| Coca Cola 330ml | CocaCola 330 ml | 2 |
| Pepsi 500 ml | Pepsi 500ml | 1 |
| Red Bull 250ml | Redbull 250ml | 2 |
| Sprite Zero 600 ml | SpriteZero600ml | 3 |

The Levenshtein distance is a type of fuzzy matching that is widely used as part of spell checkers, optical character recognition, and correction systems in areas such as customer data management, inventory systems, and document processing, where slight variations in text occur frequently.

Load script

Load script

```
Example:
Load *, recno() as ID;
Load 'Silver' as String_1,* inline [
String_2
Sliver
SSiver
SSiveer ];

Example:
Load *, recno()+3 as ID;
Load 'Gold' as String_1,* inline [
String_2
Bold
Bool
Bond ];

Example:
Load *, recno()+6 as ID;
Load 'Ove' as String_1,* inline [
String_2
Ove
Uve
Üve ];

Example:
Load *, recno()+9 as ID;
Load 'ABC' as String_1,* inline [
String_2
DEFG
abc
ビビビ ];

set nullinterpret = '<NULL>';
Example:
Load *, recno()+12 as ID;
Load 'X' as String_1,* inline [
String_2
''
<NULL>
1 ];

R1:
Load
ID,
String_1,
String_2,
LevenshteinDist(String_1, String_2) as LevenshteinDistance
resident Example;

Drop table Example;
```

Results table

| ID | String\_1 | String\_2 | LevenshteinDistance |
| --- | --- | --- | --- |
| 1 | Silver | Sliver | 2 |
| 2 | Silver | SSiver | 2 |
| 3 | Silver | SSiveer | 3 |
| 4 | Gold | Bold | 1 |
| 5 | Gold | Bool | 3 |
| 6 | Gold | Bond | 2 |
| 7 | Ove | Ove | 0 |
| 8 | Ove | Uve | 1 |
| 9 | Ove | Üve | 1 |
| 10 | ABC | DEFG | 4 |
| 11 | ABC | abc | 3 |
| 12 | ABC | ビビビ | 3 |
| 13 | X |  | 1 |
| 14 | X | - | 1 |
| 15 | X | 1 | 1 |
