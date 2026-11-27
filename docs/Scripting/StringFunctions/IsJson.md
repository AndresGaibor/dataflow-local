---
title: "IsJson Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/IsJson.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# IsJson Script and chart function

Expand/Collapse all

# IsJson Script and chart function

IsJson() tests whether a specified string contains valid JSON (JavaScript Object Notation) data. You can also validate a specific JSON data type.

Syntax:

value IsJson(json [, type])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| json | String to test. It can contain extra spaces or newlines. |
| type | Optional argument that specifies the JSON data type to test for.   - 'value' (default) - 'object' - 'array' - 'string' - 'number' - 'Boolean' - 'null' |

Example: Valid and invalid chart expressions

| Example | Result |
| --- | --- |
| IsJson( 'null' ) | Returns -1 (true) |
| IsJson( '"abc"', 'value' ) | Returns -1 (true) |
| IsJson( '"abc"', 'string' ) | Returns -1 (true) |
| IsJson( 123, 'number' ) | Returns -1 (true) |
| IsJson( 'text' ) | Returns 0 (false), 'text' is not a valid JSON value |
| IsJson( '"text"', 'number' ) | Returns 0 (false), '"text"' is not a valid JSON number |
| IsJson( '"text"', 'text' ) | Returns  0 (false), 'text' is not a valid JSON type |

## Example - IsJson fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called API\_Response.
- A derived field called ID. This field uses the Rec() function to enumerate the input records.

Load script

```
Example:
Load
Recno() AS ID, API_Response
inline [
API_Response
'{"id": 1, "name": "Alice"}'
'{"id": 2, "name": "Bob"}'
'{invalid json string}'
'{"id": 4, "name": "Charlie"}'
'{"id": 5, name: "David"}'
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- ID
- API\_Response

Create the following calculated dimension:

- =IsJson(API\_Response), to calculate if the values in API\_Response are valid JSON.

Results table

| ID | API\_Response | IsJson(API\_Response) |
| --- | --- | --- |
| 1 | {"id": 1, "name": "Alice"} | -1 (true) |
| 2 | {"id": 2, "name": "Bob"} | -1 (true) |
| 3 | {invalid json string} | 0 (false) |
| 4 | {"id": 4, "name": "Charlie"} | -1 (true) |
| 5 | {"id": 5, name: "David"} | 0 (false) |

The output returns -1, or true, for those values with valid JSON syntax.

The output returns 0, or false, for the following ID records (3 and 5) with invalid JSON:

- {invalid json string} —The text string does not represent a valid JSON response structure.
- {"id": 5, name: "David"} —The second key-value pair is missing quotation marks around the key "name".

## Example - IsJson scenario

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called OrderDetails.

Load script

```
Example:
Load *
INLINE [OrderDetails
'{ "order_id": "12345", "customer": { "name": "John Doe", "email": "john.doe@example.com"}, "items": {"product": "Laptop", "quantity": 2, "price": 1200 }, "total_price": 2400 }'
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- OrderDetails

Create the following measures:

- IsJson( OrderDetails), to calculate if the values in OrderDetails are valid JSON.
- IsJson( JsonGet ( OrderDetails, '/items/price' ), 'number' ), using the function JsonGet, it retrieves the JSON text for the price key and validates that the value of price is a number.

Results table

| OrderDetails | IsJson(OrderDetails) | IsJson( JsonGet ( OrderDetails, '/items/price' ), 'number' ) |
| --- | --- | --- |
| { "order\_id": "12345", "customer": { "name": "John Doe", "email": "john.doe@example.com"}, "items": {"product": "Laptop", "quantity": 2, "price": 1200 }, "total\_price": 2400 } | -1 (true) | -1 (true) |

The first measure returns -1 (true) because OrderDetails contains valid JSON syntax.

The second measure returns -1 (true) because the value of the price key is a valid number, 1200.

See also:

- [*JsonGet Script and chart function*](JsonGet.htm)
- [*JsonSet Script and chart function*](JsonSet.htm)
