---
title: "Other functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/other-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations", "Working with formulas"]
---

# Other functions

This help topic outlines other Qlik Automate functions that don't fit into the other categories.

## If

Applies a condition on a value. If true, a value is returned. If false, a different value is returned. The syntax for an if function is:

`{if:{$.path1} operator operand, {$.path2}, 'elsevalue'}`

`{$.inputs.location}` = Canada

`{$.inputs2.location}` = Belgium

Use an if function to check if the input matches the condition `is equal to 'Canada'`.

`{if:{$.inputs.location} = 'Canada', 'Authorized', 'You must be in Canada to continue'}` = Authorized

`{if:{$.inputs2.location} = 'Canada', 'Authorized', 'You must be in Canada to continue'}` = You must be in Canada to continue

The if function supports the following operators:

```
=       (equal)
==      (equal)
!=      (not equal)
<>      (not equal)
<       (smaller than)
>       (greater than)
<=      (smaller than or equal to)
>=      (greater than or equal to)
empty
notEmpty
contain
doesntContain
inList
notInList
isText
isNotText
isNumber
isNotNumber
isObject
isNotObject
isList
isNotList
isEmail
isNotEmail
isPhone
isNotPhone
isTrue
isFalse
```

## Map

Replaces a set of values with a different set of values.

`{$.inputs.location}` = Canada

`{map: {$.inputs.location}, {"Canada":"CA"}}` = CA

## Remove Empty Properties

Removes the keys from an object, where the value is null or an empty string or a string containing only spaces.

`{$.object}` =

```
{
  "name" : "",
  "address" : null,
  "email" : "john@acme.com",
  "remarks" : "    ",
}
```

`{removeEmptyProperties:{$.object}}` =

```
{
    "email" : "john@doe.com"
}
```

Tip note

This function is useful to avoid sending empty key-value pairs to an endpoint.

## Is email

Validates an email address. Returns a Boolean {true/false}.

## Is phone

Validates a phone number. Returns a Boolean {true/flase}.

## Parse HTML

Converts HTML into an object.

`{parsehtml: {$.inputs.html}}`

## Parse label/values

Parses text in a key-value pair format.

`{$.getMail.text}` =

```
name: John Doe
email: john@doe.com
question: Hi,
I would like to receive more info.
```

`{parseLabelValues:$.getMail.text}` =

```
{
    "name":"John Doe",
    "email":"john@doe.com",
    "question":"Hi</br>I would like to receive more info."
}
```

## Hash

Creates a hash from a given string. Add the hash algorithm as a parameter.

`{$.inputs.password}` = password1234

`{hash: {$.inputs.password}, 'sha256'}` = b9c950640e1b3740e98acb93e669c65766f6670dd1609ba91ff41052ba48c6f3

The following algorithms are available:

- md4
- md5
- sha1
- sha256
- sha512

## Automation ID

Returns the unique ID of the current automation.

## Automation Name

Returns the name of the current automation.

Typically used for logging or in the block "Update Automation" to append something to the Automation name.

## Automation Description

Returns the description of the current automation.

## Automation Run ID

Returns the unique ID of the current job (Automation run).

Typically used in the block "Update Automation" to append something to the existing description, for example, details of the last run.
