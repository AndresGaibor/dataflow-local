---
title: "JsonSetEx Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/JsonSetEx.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
# JsonSetEx Script and chart function

JsonSetEx() modifies strings containing JSON (JavaScript Object Notation) data. It can set or insert JSON values with the new location specified by the path. The data must be valid JSON but can contain extra spaces or newlines.

> **Note:** You can add any number of name-value pairs with JsonSetEx.

Syntax:

JsonSetEx(json, path, value, ...)

Return data type: dual

Arguments

| Argument | Description |
| --- | --- |
| json | String containing JSON data. |
| path | The path must be specified according to [RFC 6901](https://datatracker.ietf.org/doc/html/rfc6901). This allows buildup of properties inside JSON data without using complex substring or index functions and concatenation. |
| value | The new string value in JSON format. |

Example:

The following load script loads and formats data into a JSON format:

Data:
Load \*,
JsonSetEx('{"fax":123}',
'/name', Name,
'/address', Address,
'/phone', Phone,
'/fax', FaxOrNull) AS Json;
LOAD \*, If(Fax='-',Null(),Fax) AS FaxOrNull;
LOAD \* INLINE [
Id, Name, Address, Phone, Fax
1, John Doe, Oak Way, 1 234 567, 1 234 568
2, Jane Doe, Maple Way, 123456, -
3, Mr Xavier, Spruce Way, 1-800-MRX
];

This results in the following JSON data:

```
{"name":"John Doe","address":"Oak Way","phone":"1 243 567","fax":"1 234 568"}
{"name":"Jane Doe","address":"Maple Way","phone":123456}
{"fax":"","name":"Mr Xavier","address":"Spruce Way","phone":"1-800-MRX"}
```
