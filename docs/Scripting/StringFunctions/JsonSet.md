---
title: "JsonSet Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/JsonSet.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
# JsonSet Script and chart function

JsonSet() modifies a string containing JSON (JavaScript Object Notation) data. It can set or insert a JSON value with the new location specified by the path. The data must be valid JSON but can contain extra spaces or newlines.

> **Note:** You can add any number of name-value pairs with JsonSet.

Syntax:

value JsonSet(json, path, value)

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| json | String containing JSON data. |
| path | The path must be specified according to [RFC 6901](https://datatracker.ietf.org/doc/html/rfc6901). This allows buildup of properties inside JSON data without using complex substring or index functions and concatenation. |
| value | The new string value in JSON format. |

Example: Valid and invalid chart expressions

| Example | Result |
| --- | --- |
| `JsonSet( '{}','/a','"b"' )` | Returns `{"a":"b"}` |
| `JsonSet( '[]','/0','"x"' )` | Returns `["x"]` |
| `JsonSet( '"abc"','','123' )` | Returns `123` |
| `JsonSet( '"abc"','/x','123' )` | Returns `null`. The path does not point to a valid part of the JSON data. |
| `JsonSet( '{"a":{"b":"c"}}','a/b','"x"' )` | Returns `null`. The path is invalid. |
| `JsonSet( '{"a":"b"}','/a','abc' )` | Returns `null`. The value is not valid JSON. A string must be enclosed in quotes. |

## Example - JsonSet fundamentals

Chart expression

Overview

JSON data is received as a text string in a single line. You want to update the price of the item and the total price of the order accordingly.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- One field in the data table called `OrderDetails`.

Load script

```
Example:
Load  * 
INLINE [OrderDetails
'{ "order_id": "12345", "customer": { "name": "John Doe", "email": "john.doe@example.com"}, "items": {"product": "Laptop", "quantity": 2, "price": 1200 }, "total_price": 2400 }'
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `OrderDetails`

Create the following measure:

- `JsonSet(JsonSet(OrderDetails,'/items/price',1100),'/total_price',2200)`, to set the price to `1100` and the total price to `2200` using the correct path to the respective keys in the JSON string.

Results table

| OrderDetails | JsonSet(JsonSet(OrderDetails,'/items/price',1100),'/total\_price',2200) |
| --- | --- |
| { "order\_id": "12345", "customer": { "name": "John Doe", "email": "john.doe@example.com"}, "items": {"product": "Laptop", "quantity": 2, "price": 1200 }, "total\_price": 2400 } | {"order\_id":"12345","customer":{"name":"John Doe","email":"john.doe@example.com"},"items":{"product":"Laptop","quantity":2,"price":1100},"total\_price":2200} |

The out put of the measure updates the `price` and `total price` keys to `1100` and `2200` respectively.

See also:

- [*IsJson Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/IsJson.htm)
- [*JsonGet Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/JsonGet.htm)
