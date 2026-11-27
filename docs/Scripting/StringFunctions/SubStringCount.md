---
title: "SubStringCount Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/SubStringCount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# SubStringCount Script and chart function

Expand/Collapse all

# SubStringCount Script and chart function

SubStringCount() returns
the number of occurrences of the specified substring in the input string text.
If there is no match, 0 is returned.

Syntax:

SubStringCount(text,
sub\_string)

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. |
| sub\_string | A string which may occur one or more times within the input string text. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| SubStringCount( 'abcdefgcdxyz', 'cd' ) | Returns 2 |
| SubStringCount( 'abcdefgcdxyz', 'dc' ) | Returns 0 |

## Example - SubStringCount fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called FruitSentence.

Load script

```
Example:
Load * inline [
FruitSentence
"I love eating an apple every day.Apple juice is great too!"
"Apple pie is my favorite dessert. I also enjoy apple jam."
"There is an apple and a banana on the table."
"I don't like apples as much as oranges."
"An apple a day keeps the doctor away, but two apples are even better!"
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- FruitSentence

Create the following calculated dimension:

- =SubStringCount(FruitSentence, 'apple'), to calculate how many times the word apple occurs in FruitSentence.

Results table

| FruitSentence | SubStringCount(FruitSentence, 'apple') |
| --- | --- |
| An apple a day keeps the doctor away, but two apples are even better! | 2 |
| Apple pie is my favorite dessert. I also enjoy apple jam. | 1 |
| I don't like apples as much as oranges. | 1 |
| I love eating an apple every day. Apple juice is great too! | 1 |
| There is an apple and a banana on the table. | 1 |

The table is sorted on the dimension FruitSentence in ascending order. The SubStringCount function returns the number of times the word apple occurs in each sentence. For example, the first sentence returns 2, because the word occurs twice in the sentence. In the second and fourth sentences, the function ignores the word Apple because it does not match the case of the search term apple.

Tip noteTo do a case-insensitive search, you can convert your input string to upper or lowercase characters first, and then use the SubStringCount function on the result. For example, to search for all occurrences of the word apple, regardless of case, use the following measure expression: =SubStringCount(Upper(FruitSentence),'APPLE').The expression uses the SubStringCount function with the Upper function to convert the whole string to uppercase characters, and then searches for the word APPLE.

Load script

The following code shows how to use the function in a load script. This example includes a preceding load that uses the SubStringCount function with the Upper function to convert the whole string to uppercase characters, and then searches for the word APPLE.

```
Example:
Load *,
SubStringCount(Upper(FruitSentence),'APPLE') as SubStringCount_APPLE;
Load * inline [
FruitSentence
"I love eating an apple every day. Apple juice is great too!"
"Apple pie is my favorite dessert. I also enjoy apple jam."
"There is an apple and a banana on the table."
"I don't like apples as much as oranges."
"An apple a day keeps the doctor away, but two apples are even better!"
];
```

Results table

| FruitSentence | SubStringCount\_APPLE |
| --- | --- |
| I love eating an apple every day. Apple juice is great too! | 2 |
| Apple pie is my favorite dessert. I also enjoy apple jam. | 2 |
| There is an apple and a banana on the table. | 1 |
| I don't like apples as much as oranges. | 1 |
| An apple a day keeps the doctor away, but two apples are even better! | 2 |

## Example - SubStringCount scenario

Chart expression

Overview

A dataset of fruit products contains a field with product descriptions. This example calculates the number of times the following fruit names occur in each description: apple, banana, or orange.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called ProductDescription.

Load script

```
Example:
Load * inline [
ProductDescription
"Fresh apple and banana smoothie."
"Organic apple, banana, and orange juice. Great for breakfast."
"A refreshing orange soda made with real orange juice."
"Banana chips with apple and cinnamon flavor."
"Delicious apple pie with a hint of cinnamon and vanilla."
"Tropical banana and orange mix for smoothies."
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- ProductDescription

Create the following calculated dimensions:

- =SubStringCount(ProductDescription, 'apple'), to calculate the number of occurrences of the word apple in the string ProductDescription.
- =SubStringCount(ProductDescription, 'banana'), to calculate the number of occurrences of the word banana in the string ProductDescription.
- =SubStringCount(ProductDescription, 'orange'), to calculate the number of occurrences of the word orange in the string ProductDescription.

Results table

| ProductDescription | SubStringCount(ProductDescription, 'apple') | SubStringCount(ProductDescription, 'banana') | SubStringCount(ProductDescription, 'orange') |
| --- | --- | --- | --- |
| A refreshing orange soda made with real orange juice. | 0 | 0 | 2 |
| Banana chips with apple and cinnamon flavor. | 1 | 0 | 0 |
| Delicious apple pie with a hint of cinnamon and vanilla. | 1 | 0 | 0 |
| Fresh apple and banana smoothie. | 1 | 1 | 0 |
| Organic apple, banana, and orange juice. Great for breakfast. | 1 | 1 | 1 |
| Tropical banana and orange mix for smoothies. | 0 | 1 | 1 |

The output of the SubStringCount function successfully returns the number of instances that each substring (apple, banana, orange) occurs in the product description. For example, in the first description, the function returns 2 because there are two instances of the word orange. The sub\_string argument is case-sensitive, so in the second description, the function does not count the word Banana because it does not match the substring banana in the measure expression.

Tip noteTo do a case-insensitive search, you can convert your input string to upper or lowercase characters first, and then use the SubStringCount function on the result. For example, to search for all occurrences of the word apple, regardless of case, use the following measure expression: =SubStringCount(Upper(ProductDescription),'APPLE').The expression uses the SubStringCount function with the Upper function to convert the whole string to uppercase characters, and then searches for the word APPLE.

## Example - SubStringCount scenario parsing nested data

Chart expression

Overview

A dataset of IT records contains a list of change ID numbers and categories. In the data table, the Categories field is derived from a multi-level hierarchy that lists the top parent category followed by all sub categories, for example Software > Program > Patch. This scenario demonstrates how to pick out the last value, or leaf value, from this ragged category hierarchy using a combination of the SubStringCount and the SubField functions.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - ChangeID contains the original change ID to be processed.
  - Categories contains a list of change categories. Categories are separated by semi-colons and listed in hierarchical order from left to right, starting from the top parent category to the most detailed sub-category.

Load script

```
Example:
Load * inline [
ChangeID,Categories
CHG00100,Software;Program;Patch
CHG00101,Hardware;Server
CHG00102,Hardware;Network;Router
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- ChangeID
- Categories

Create the following calculated dimensions:

- =SubStringCount(Categories,';')+1, to calculate the number of category levels in the change hierarchy.
- =SubField(Categories, ';' ,SubStringCount(Categories,';')+1), to extract the rightmost category in the change hierarchy.

Results table

| ChangeID | Categories | ​SubStringCount(Categories,';')+1 | SubField(Categories, ';' ,SubStringCount(Categories,';')+1) |
| --- | --- | --- | --- |
| CHG00100 | Software;Program;Patch | 3 | Patch |
| CHG00101 | Hardware;Server | 2 | Server |
| CHG00102 | Hardware;Network;Router | 3 | Router |

In this example, the SubStringCount function is nested within the SubField function. The first calculated dimension, SubStringCount(), calculates the number of nested values in the Categories field. This is determined by counting the number of semi-colons ';' and adding 1 to the result. This output is then injected as the third parameter of the SubField function to extract the rightmost category nested in the Categories field.

For example, review the results for the ChangeID entry CHG00100. In the first calculated dimension, the SubStringCount is 2. The expression then adds 1 to that result to determine that the Categories field has three nested category values, Software, Program, and Patch. The SubField function, in the second calculated dimension, then uses this result to extract the third category, Patch.
