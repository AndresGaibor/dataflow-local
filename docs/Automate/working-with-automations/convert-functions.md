---
title: "Convert functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/convert-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations", "Working with formulas"]
---

# Convert functions

This help topic outlines the available convert functions in Qlik Automate. Convert functions can change the data in a placeholder from one type to another.

## Boolean

Converts data from an unspecified data type to Boolean data type.

`{$.inputs.currentAddress}` = true

`{boolean:{$.inputs.currentAddress}}` = true

## Country to ISO

Converts a country name (English) to its two-letter ISO code.

`{$.inputs.country}` = Canada

`{countrytoiso:{$.inputs.country}}` = CA

## ISO to country

Converts a two-letter ISO code to the corresponding country name (English).

`{$.inputs.ISO}` = CA

`{isotocountry:{$.inputs.ISO}}` = Canada

## Domain

Extracts the domain name from the website URL.

`{$inputs.website}` = <https://help.qlik.com/>

`{domain:{$inputs.website}}` = qlik.com

## Flatten

Flattens an object with nested properties to a new object without nested properties.

`{$userInfo}` =

```
{
  "name": "John",
  "address": {
    "city": "Paris"
  },
  "orders": [
    {"id": 55},
    {"id": 66}
  ]
}
```

`{flatten:$.userInfo}` =

```
{
  "name": "John",
  "address.city": "Paris",
  "orders.0.id": 55,
  "orders.1.id": 66
}
```

## Host

Extracts the host name from the website URL.

`{$inputs.website}` = <https://help.qlik.com/>

`{host:{$inputs.website}}` = help.qlik.com

## National Phone

Normalizes a phone number into a national format by removing the international code.

`{$inputs.phone}` = +1 (529) 866–7788

`{nationalphone:{$.inputs.phone}}` = 5298667788

## Phone

Normalizes a phone number into an international format. A two-character ISO country code parameter is required.

`{$inputs.phone}` = 498667788

`{phone:{$.inputs.phone}, 'FR'}` = +33 4 98 66 77 88

## Number

Converts data from an unspecified data type to number data type.

`{$.inputs.age}` = 55

`{number:{$.inputs.age}}` = 55

## Object

Converts data from an unspecified data type to object data type.

`{$.inputs.age}` = 55

`{object:{$.inputs.age}}` =

```
{
    "age" : "55"
}
```

## List

Converts data from an unspecified data type to list data type.

`{$.inputs.age}` = 55, 65, 75

`{list:{$.inputs.age}}` = ["55","65","75"]

## JSON

Converts an object into JSON text.

`{$.inputs.age}` = 55, 65, 75

`{list:{$.inputs.age}}` = ["55","65","75"]

When the $.path value is a list with three items, for example, the result will be text such as "[ "one", "two", "three" ]"

`{$.path}` is a variable of type list or a list that is returned by a certain block.

`{json: {$.path}}` = [ "one", "two", "three" ]

## CSV

Converts a flat JSON object with key-value pairs into a single CSV line. You can optionally enter the columns and delimiter as parameters.

Information note

The CSV convert function will not work properly if the JSON object has nested properties. If you have a nested JSON object, use the flatten convert function first.

`{$.inputs.userName}` = {"name": "John Doe","location": "New York"}

`{csv: {$.inputs.userName}, 'name, location', ','}` = "John Doe","New York"

The CSV convert function preserves the order of columns in the CSV file for multiple objects.

`{$.myObject1}` =

```
{
  "key3": "val 003",
  "key1": "val 001"
}
```

`{$.myObject2}` =

```
{
  "key1": "val 011",
  "key2": "val 022",
  "key3": "val 033"
}
```

`{$.myObject3}` =

```
{
  "key1": "val 111",
  "key2": "val 222"
}
```

`{$.columns}` = [ "key1", "key2", "key3" ]

Apply the following CSV formulas:

`{csv: $.myObject1, $.columns} {csv: $.myObject2, $.columns} {csv: $.myObject3, $.columns}`

The CSV convert function returns the following table:

```
"val 001",         ,"val 003"
"val 011","val 022","val 033"
"val 111","val 222"
```

## Base64 encode

Encodes a string to base64.

`{$.inputs.userName}` = John Doe

`{base64encode: {$.inputs.userName}}` = Sm9obiBEb2U=

## Base64 decode

Decodes a string from base64.

`{$.inputs.userName}` = Sm9obiBEb2U=

`{base64decode: {$.inputs.userName}}` = John Doe
