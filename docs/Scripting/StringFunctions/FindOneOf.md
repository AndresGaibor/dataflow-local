---
title: "FindOneOf Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/FindOneOf.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# FindOneOf Script and chart function

Expand/Collapse all

# FindOneOf Script and chart function

FindOneOf() searches a string to find the position of the occurrence of any character from a set of provided characters. The position of the Nth occurrence of any character from the search set is returned where N is the optional third parameter of the function. If no third parameter is supplied, the first occurrence is returned. If no match is found,
0 is returned.

Syntax:

FindOneOf(text, char\_set[, count])

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. |
| char\_set | A set of characters to search for in text. |
| count | Defines which occurrence of any of the characters to search for. For example, a value of 2 searches for the second occurrence. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| FindOneOf( 'my example text string', 'et%s' ) | Returns 4 because e is the fourth character in the example string. |
| FindOneOf( 'my example text string', 'et%s', 3 ) | Returns 12 because the search is for any of the characters e, t, % or s, and t is the third occurrence in position 12 of the example string. |
| FindOneOf( 'my example text string', '¤%&' ) | Returns 0 because none of the characters ¤, %, or & are found in the example string. |

## Example - FindOneOf fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called Phrase, which contains the original text strings to be processed.

Load script

```
Example:
Load *
Inline
[Phrase
Many tiny beads
For a very long time
Has the potential for growth
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Phrase

Create the following calculated dimensions:

- =FindOneOf(Phrase, 'e', 1)
- =FindOneOf(Phrase, 'y', 1)
- =FindOneOf(Phrase, 'ey', 1)
- =FindOneOf(Phrase, 'e', 2)
- =FindOneOf(Phrase, 'y', 2)
- =FindOneOf(Phrase, 'ey', 2)

Results table

| Phrase | FindOneOf(Phrase, 'e', 1) | FindOneOf(Phrase, 'y', 1) | FindOneOf(Phrase, 'ey', 1) | FindOneOf(Phrase, 'e', 2) | FindOneOf(Phrase, 'y', 2) | FindOneOf(Phrase, 'ey', 2) |
| --- | --- | --- | --- | --- | --- | --- |
| For a very long time | 8 | 10 | 8 | 20 | 0 | 10 |
| Has the potential for growth | 7 | 0 | 7 | 12 | 0 | 12 |
| Many tiny beads | 12 | 4 | 4 | 0 | 9 | 9 |

For each calculated dimension, the output returns the position of the occurrence of the characters from the search set for each phrase. For example, the first occurrence of the letter e is found at position 8, 7, and 12 for each phrase respectively. The second occurrence of the letter e in each phrase is found at position 20, 12, and 0 (not found). Similarly, the first occurrence of the letters 'e or y' is found at position 8, 7, and 4, for each phrase respectively. Notice that in the phrase For a very long time, the first occurrence of 'e or y' is found at position 8, an e, and the second occurrence at position 10, a y.

Load script

The following code shows how to use the function in a load script.

```
Example:
Load *, FindOneOf(InputText, SearchFor, Occurrence) AS FindOneOf_Matches
Inline
InputText, SearchFor, Occurrence
my example text string, et%s,1
my example text string, et%s,3
my example text string, ¤%&,1
];
```

Results table

| InputText | SearchFor | Occurrence | FindOneOf\_Matches |
| --- | --- | --- | --- |
| my example text string | et%s | 1 | 4 |
| my example text string | et%s | 3 | 12 |
| my example text string | ¤%& | 1 | 0 |

## Example - FindOneOf scenario

Chart expression

Overview

This example uses the FindOneOf function to analyze customer comments in a dataset of customer orders and identify orders that may require action. Each order has a CustomerComment field where customers can leave notes or comments about their orders. By analyzing the comments, you can identify specific keywords or characters, such as '!', '@', '#', that might indicate urgency or special requests.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - TicketID the identity number of the ticket
  - CustomerComment the original text string

Load script

```
Example:
Load * inline [
TicketID, CustomerComment
1, I need this order ASAP!
2, Please confirm my order @12345.
3, Can you update my order?
4, I have a question about #discount.
5, Thank you!
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- TicketID
- CustomerComment

Create the following calculated dimensions:

- =FindOneOf(CustomerComment, '!,@,#')
- =If(FindOneOf(CustomerComment, '!,@,#')>0,'High Priority','Normal Priority')

Results table

| TicketID | CustomerComment | FindOneOf(CustomerComment, '!,@,#') | If(FindOneOf(CustomerComment, '!,@,#')>0,'High Priority','Normal Priority') |
| --- | --- | --- | --- |
| 1 | I need this order ASAP! | 23 | High Priority |
| 2 | Please confirm my order @12345. | 25 | High Priority |
| 3 | Can you update my order? | 0 | Normal Priority |
| 4 | I have a question about #discount. | 25 | High Priority |
| 5 | Thank you! | 10 | High Priority |

Compare the output of the FindOneOf function to the original CustomerComment string values that loaded in the script. Using the values !,@,#, the function successfully returned the position where those characters occur in the comment string. The final measure uses a conditional If statement to identify records that include any of the search characters and assign these as High Priority. If none of the search characters !,@,# are found, for example row 3, then the ticket is classified as Normal Priority.
