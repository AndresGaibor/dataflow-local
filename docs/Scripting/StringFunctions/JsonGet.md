---
title: "JsonGet Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/JsonGet.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
# JsonGet Script and chart function

JsonGet() returns the path of a JSON (JavaScript Object Notation) data string. The data must be valid JSON but can contain extra spaces or newlines.

Syntax:

value JsonGet(json, path)

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| json | String containing JSON data. |
| path | The path must be specified according to [RFC 6901](https://datatracker.ietf.org/doc/html/rfc6901). This will allow lookup of properties inside JSON data without using complex substring or index functions. |

Example: Valid and invalid chart expressions

| Example | Result |
| --- | --- |
| `JsonGet( '{"a":{"xyz":"XYZ"},"b":[123,"abc","ABC"]}', '' )` | Returns `{"a":{"xyz":"XYZ"},"b":[123,"abc","ABC"]}` |
| `JsonGet( '{"a":{"xyz":"XYZ"},"b":[123,"abc","ABC"]}', '/a' )` | Returns `{"xyz":"XYZ"}` |
| `JsonGet( '{"a":{"xyz":"XYZ"},"b":[123,"abc","ABC"]}', '/a/xyz' )` | Returns `"XYZ"` |
| `JsonGet( '{"a":{"xyz":"XYZ"},"b":[123,"abc","ABC"]}', '/b' )` | Returns `[123,"abc","ABC"]` |
| `JsonGet( '{"a":{"xyz":"XYZ"},"b":[123,"abc","ABC"]}', '/b/0' )` | Returns `123` |
| `JsonGet( '{"a":{"xyz":"XYZ"},"b":[123,"abc","ABC"]}', '/b/1' )` | Returns `abc` |
| `JsonGet( '{"a":{"xyz":"XYZ"},"b":[123,"abc","ABC"]}', '/b/2' )` | Returns `ABC` |
| `JsonGet( '{"a":"b"}','/b' )` | Returns `null`. The path does not point to a valid part of the JSON data. |
| `JsonGet( '{"a"}','/a' )` | Returns `null`. The JSON data is not valid JSON (member `"a"` does not have a value). |

## Example - JsonGet fundamentals

Chart expression

Overview

You receive JSON data with order details as a text string in a single line. You want to retrieve the following information:

- price of the item and validation that the value is a number
- customer email address
- total price (price \* quantity)

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

Create the following measures:

- `IsJson( JsonGet ( OrderDetails, '/items/price' ), 'number' )`, combined with the `IsJson` function, retrieves the JSON text for `price` and validates if the value of `price` is a number.
- `JsonGet( OrderDetails, '/customer/email' )`, to retrieve the customer email address using the correct path.
- `JsonGet( OrderDetails, '/total_price' ), )`, to retrieve the total price using the correct path.

Results table

| OrderDetails | IsJson( JsonGet ( OrderDetails, '/items/price' ), 'number' ) | JsonGet( OrderDetails, '/customer/email' ) | JsonGet( OrderDetails, '/total\_price' ), ) |
| --- | --- | --- | --- |
| { "order\_id": "12345", "customer": { "name": "John Doe", "email": "john.doe@example.com"}, "items": {"product": "Laptop", "quantity": 2, "price": 1200 }, "total\_price": 2400 } | -1 (true) | john.doe@example.com | 2400 |

The first measure returns `-1 true` because the `price` key has a value of `1200`, which is a number.

The second measure returns the customer email address, `john.doe@example.com`, from `OrderDetails` using the correct path to the `email` key in the JSON string.

The third measure returns `2400`, which is the total price of the order from the `OrderDetails` field, using the correct path to the `total_price` key in the JSON string.

See also:

- [*IsJson Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/IsJson.htm)
- [*JsonSet Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/JsonSet.htm)
