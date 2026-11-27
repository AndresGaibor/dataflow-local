---
title: "JsonObject Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/JsonObject.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# JsonObject Script and chart function

JsonObject is used to build JSON objects.

Information noteYou can add any number of name-value pairs with JsonObject.

Syntax:

JsonObject(name, value [name, value, ...])

Return data type: dual

Arguments

| Argument | Description |
| --- | --- |
| json | String containing JSON data. |
| name | The name of the field in JSON format. |
| value | The string value in JSON format. |

Example:

The following load script loads and sets data as a JSON object.

Data:
Load \*,
JsonObject('id', Id,
'name', Name,
'address', Address,
'phone', Phone,
'fax', FaxOrNull) AS Json;
LOAD \*, If(Fax='-',Null(),Fax) AS FaxOrNull;
LOAD \* INLINE [
Id, Name, Address, Phone, Fax
1, John Doe, Oak Way, 1 234 567, 1 234 568
2, Jane Doe, Maple Way, 123456, -
3, Mr Xavier, Spruce Way, 1-800-MRX
];

This results in the following JSON data:

```
{"id":1,"name":"John Doe","address":"Oak Way","phone":"1 234 567","fax":"1 234 568"}
{"id":2,"name":"Jane Doe","address":"Maple Way","phone":123456}
{"id":3,"name":"Mr Xavier","address":"Spruce Way","phone":"1-800-MRX","fax":""}
```
