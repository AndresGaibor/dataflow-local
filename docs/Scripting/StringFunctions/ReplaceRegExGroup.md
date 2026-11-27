---
title: "ReplaceRegExGroup Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ReplaceRegExGroup.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# ReplaceRegExGroup Script and chart function

Expand/Collapse all

# ReplaceRegExGroup Script and chart function

ReplaceRegExGroup() returns a string after replacing one or more matches
between an input string and the composite regular expression pattern that is specified. The text that replaces the matching text is specified in the to\_str argument. The function works from left to right, but if you specify a negative occurrence value, the function reads from right to left.

This function performs regex operations that are case-sensitive. You can alternatively use the variant ReplaceRegExGroupI() to perform case-insensitive regex operations.

Syntax:

ReplaceRegExGroup
(text, regex, to\_str, group [, occurrence])

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The input string text that you want to replace, fully or partially, with the new text from to\_str. |
| regex | The regular expression that defines when to replace text. Matches between this argument and the text argument are replaced. |
| to\_str | The new text that you want to use to replace existing content from text. |
| group | The number of the group, in the case of a composite regular expression.  If the regular expression only contains one group, use the ReplaceRegEx() function instead. Alternatively, use ReplaceRegExGroup() with a group value of 0.  You can specify a negative group value to search for groups from right to left. |
| occurrence | The number of the match (between input text and regular expression) to replace with new text.  This is an optional argument. The default is 0 if omitted. When a value of 0 is used, or if the argument is omitted, all matches between the text and regex are replaced with to\_str.  You can specify a negative value for occurrence if you want to identify matches from right to left. |

Function examples

| Example | Result |
| --- | --- |
| ReplaceRegExGroup('abc123','([a-z])([0-9]+)','x',0) | Returns abx (replace complete match). |
| ReplaceRegExGroup('abc123','([a-z])([0-9]+)','x',1) | Returns abx123 (only replace first group in match). |
| ReplaceRegExGroup('abc123','([a-z])([0-9]+)','x',2) | Returns abcx (only replace second group in match). |
| ReplaceRegExGroup('abc123abc123','([a-z])([0-9]+)','x',1,2) | Returns abc123abx123. There are two matches between the first group of the input text and the regex pattern. However, only the second occurrence is replaced. |
| ReplaceRegExGroup('ABC123ABC123','([a-z])([0-9]+)','x',1) | Returns ABC123ABC123. In other words, no text is replaced. This is because the function is case-sensitive, and the case-insensitive variant of the function is not used. |
| ReplaceRegExGroupI('ABC123ABC123','([a-z])([0-9]+)','x',1) | Returns ABx123ABx123. In this example, text replacement happens because the case-insensitive variant of the function, ReplaceRegExGroupI(), is used. |

## When to use ReplaceRegExGroup

You can use ReplaceRegExGroup() for modifying text to meet formatting and compliance standards, especially when you need to identify complex patterns in data. The additional group argument for this function allows you to update only certain portions of a larger text pattern. For example, you can update specific parts of a URL.

If needed, you can also use this function to mask sensitive information, such as personal identifiable information (PII), so that it is not shown to users analyzing your application.

## Example 1 – load script to update domain in URLs

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table URLs that initially contains a list of input strings in which we want to identify and update specific URLs. We want to update the domain in these URLs.
- The creation of a field, ResourceURL\_Updated, that contains modified input text with the processed URLs.
- A [variable](#glossary-0 "Glossary term") URL\_RegEx to store the regular expression being used to identify URLs to process.

Our requirements:

- Each input string contains two URLs, with the resource URL specified in the first URL. We do not want to update any URLs other than the first one listed.
- The URL to update needs to be in the format <https or https>://<domain>.com/<resource path>. The resource path is optional but is not used in this example.

Load script

```
Set URL_RegEx = '(https?):\/\/(([a-zA-Z0-9]+)\.([a-zA-Z0-9]*)\.??([a-zA-Z0-9]*))\/?((([a-zA-Z0-9]*)*)((\/?([a-zA-Z0-9]*)*))*)\/{0,1}([\.,;]+(?=\s))*?';

URLs:

Load
ReplaceRegExGroup(URLsList, '$(URL_RegEx)', 'replacement-server', 2,1) as ResourceURL_Updated;

Load * Inline `
URLsList
The resource is located at https://testserver.com/files. For more help, see: https://support.company.com.
The resource is located at https://testserver.com/files/worksheet. For more help, see: https://support.company.com.
The resource is located at https://testserver.com/files/book. For more help, see: https://support.company.com.
The resource is located at https://testserver.com/files/form. For more help, see: https://support.company.com.
The resource is located at https://testserver.com/datamodel. For more help, see: https://support.company.com.
The resource is located at https://testserver.com/resourcenew. For more help, see: https://support.company.com.
The resource is located at https://testserver.com/page. For more help, see: https://support.company.com.
The resource is located at https://testserver.com/page/overview. For more help, see: https://support.company.com.
` (delimiter is '\t');
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- ResourceURL\_Updated

Results table

| ResourceURL\_Updated |
| --- |
| The resource is located at https://replacement-server/datamodel. For more help, see: https://support.company.com. |
| The resource is located at https://replacement-server/files. For more help, see: https://support.company.com. |
| The resource is located at https://replacement-server/files/book. For more help, see: https://support.company.com. |
| The resource is located at https://replacement-server/files/form. For more help, see: https://support.company.com. |
| The resource is located at https://replacement-server/files/worksheet. For more help, see: https://support.company.com. |
| The resource is located at https://replacement-server/page. For more help, see: https://support.company.com. |
| The resource is located at https://replacement-server/page/overview. For more help, see: https://support.company.com. |
| The resource is located at https://replacement-server/resourcenew. For more help, see: https://support.company.com. |

## Example 2 – chart expression to update protocol in URLs

Chart expression and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table URLsList containing a list of input strings in which we want to identify and update specific URLs. We want to update the protocol from http to https in the links to the Support website.

Our requirements:

- Each input string contains two URLs, with the Support website link appearing as the second URL. We do not want to update any URLs other than the second URL.
- The URL to update needs to be in the format <https or https>://<domain>.com/<resource path>. The resource path is optional but is not used in this example.

Load script

```
URLs:

Load * Inline `
URLsList
The resource is located at https://testserver.com/files. For more help, see: http://support.company.com.
The resource is located at https://testserver.com/files/worksheet. For more help, see: http://support.company.com.
The resource is located at https://testserver.com/files/book. For more help, see: http://support.company.com.
The resource is located at https://testserver.com/files/form. For more help, see: http://support.company.com.
The resource is located at https://testserver.com/datamodel. For more help, see: http://support.company.com.
The resource is located at https://testserver.com/resourcenew. For more help, see: http://support.company.com.
The resource is located at https://testserver.com/page. For more help, see: http://support.company.com.
The resource is located at https://testserver.com/page/overview. For more help, see: http://support.company.com.
` (delimiter is '\t');
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- URLsList

Add this calculated dimension:

```
=ReplaceRegExGroup(URLsList, '(https?):\/\/(([a-zA-Z0-9]+)\.([a-zA-Z0-9]*)\.??([a-zA-Z0-9]*))\/?((([a-zA-Z0-9]*)*)((\/?([a-zA-Z0-9]*)*))*)\/{0,1}([\.,;]+(?=\s))*?', 'https', 1,2)
```

Results table

| URLsList | =ReplaceRegExGroup(URLsList, '(https?):\/\/(([a-zA-Z0-9]+)\.([a-zA-Z0-9]\*)\.??([a-zA-Z0-9]\*))\/?((([a-zA-Z0-9]\*)\*)((\/?([a-zA-Z0-9]\*)\*))\*)\/{0,1}([\.,;]+(?=\s))\*?', 'https', 1,2) |
| --- | --- |
| The resource is located at https://testserver.com/files. For more help, see: http://support.company.com. | The resource is located at https://testserver.com/datamodel. For more help, see: https://support.company.com. |
| The resource is located at https://testserver.com/files/worksheet. For more help, see: http://support.company.com. | The resource is located at https://testserver.com/files. For more help, see: https://support.company.com. |
| The resource is located at https://testserver.com/files/book. For more help, see: http://support.company.com. | The resource is located at https://testserver.com/files/book. For more help, see: https://support.company.com. |
| The resource is located at https://testserver.com/files/form. For more help, see: http://support.company.com. | The resource is located at https://testserver.com/files/form. For more help, see: https://support.company.com. |
| The resource is located at https://testserver.com/datamodel. For more help, see: http://support.company.com. | The resource is located at https://testserver.com/files/worksheet. For more help, see: https://support.company.com. |
| The resource is located at https://testserver.com/resourcenew. For more help, see: http://support.company.com. | The resource is located at https://testserver.com/page. For more help, see: https://support.company.com. |
| The resource is located at https://testserver.com/page. For more help, see: http://support.company.com. | The resource is located at https://testserver.com/page/overview. For more help, see: https://support.company.com. |
| The resource is located at https://testserver.com/page/overview. For more help, see: http://support.company.com. | The resource is located at https://testserver.com/resourcenew. For more help, see: https://support.company.com. |

## Learn more

- [*Working with regular expressions in load scripts and chart expressions*](../regular-expressions-qlik-analytics.htm)
