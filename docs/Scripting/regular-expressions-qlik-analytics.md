---
title: "Working with regular expressions in load scripts and chart expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/regular-expressions-qlik-analytics.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
# Working with regular expressions in load scripts and chart expressions

Augment your analytics and data preparation by using regular expressions (regex) in data [load scripts](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/regular-expressions-qlik-analytics.htm#glossary-0 "Glossary term") and in chart expressions. Regular expressions offer advanced, flexible, and powerful options for finding and replacing text-based data. To work with regular expressions in Qlik Sense and the Script interface, use [the available script and chart functions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/regular-expressions-qlik-analytics.htm#Available).

## How to work with regular expressions

Regular expressions (regex) offer extensive options for advanced pattern matching. Write a regular expression to specify a particular text pattern you would like to identify. For example, you might want to find occurrences of email addresses or web URLs within larger bodies of natural language.

There are many different formats in which regular expressions can be written, each with their own syntax rules. The available regular expression functions use Perl regular expression syntax.

To work with regular expressions in Qlik Sense and the Script interface, use the available regex script and chart functions. Use of these functions assumes you have a basic understanding of how regular expressions work. For more information, including examples, see [*Available functions and examples*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/regular-expressions-qlik-analytics.htm#Available).

## Use cases

You can use regular expressions for:

- Extracting and separating information from text containing multiple distinct components. For example, email addresses, phone numbers, web URLs, and more.
- Standardizing formatting of data.
- Searching and/or replacing text.

With the available regex functions, you can do the following in load scripts:

- Transform data and load it for use in analytics.
- Validate data to ensure it follows formatting and other compliance standards.
- Identify, mask, or alter personal identifiable information (PII) into a form that is appropriate for consumers of your analytics content.
- Selectively load data into applications according to whether or not it matches specific text patterns.

Use cases for regex functions in chart expressions are similar to those for load scripts. Using the functions in chart expressions also allows you to:

- Transform data on the fly, conditionally or statically, depending on user needs and interactions.
- Use the functions to define labels, color settings, and other [chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/regular-expressions-qlik-analytics.htm#glossary-1 "Glossary term")-specific properties.

## Performance considerations

The regular expression functions available in load scripts and chart expressions are best used for advanced string transformations where flexibility is a requirement. Using regex functions is more resource-intensive than the non-regex alternatives. For more simple data transformations, consider using other available script and chart functions, including string functions. For a list of available string functions, see [*String functions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/string-functions.htm).

When working with large data volumes, regex operations to search for matches of large or negative n values can cause decreased performance. In the context of the available regex functions, the n value corresponds to function arguments such as occurrence, count, and field\_no.

## Available functions and examples

- [*CountRegEx Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/CountRegEx.htm)
- [*ExtractRegEx Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ExtractRegEx.htm)
- [*ExtractRegExGroup Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ExtractRegExGroup.htm)
- [*IndexRegEx Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/IndexRegEx.htm)
- [*IndexRegExGroup Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/IndexRegExGroup.htm)
- [*IsRegEx Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/IsRegEx.htm)
- [*MatchRegEx Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/MatchRegEx.htm)
- [*ReplaceRegEx Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ReplaceRegEx.htm)
- [*ReplaceRegExGroup Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ReplaceRegExGroup.htm)
- [*SubFieldRegEx Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/SubFieldRegEx.htm)

## Learn more

- [*String functions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/string-functions.htm)
