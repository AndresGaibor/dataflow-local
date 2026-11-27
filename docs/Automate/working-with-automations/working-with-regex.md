---
title: "Working with regular expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-regex.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations"]
---

# Working with regular expressions

Regular expression can be used with the [regex functions](text-functions.htm#anchor-4). This section contains example of some useful expressions.

## General expressions

This example removes special characters from a string. Special characters are everything that is not a-z or 1-9.

`{ regexReplace: {$.getCompany.URL}, "[^\w\s\-_]", "" }`

This example removes special characters from a string but keeps characters with accents.

`{ regex_replace: {$.companyname}, "[^A-Za-zÀ-ÖØ-öø-ÿ ]" , "" }`

This example replaces a special character—the German "ß"—with a double "s".

`{ regex_replace: {$.companyname}, "ß" , "ss"}`

## Names

These examples parse the first and last name from a full name, where the name format is "FirstName" "LastName".

Get first name:

`{ regexparse:{$.fullname}, '^([^\s]*)' }`

Get last name:

`{ regexparse:{$.fullname}, '^[^\s]*\s(.*)' }`

## Addresses

This example parses the house number from a street address, where the format is "StreetName" "HouseNumber".

Get the house number:

`{regexparse: 'Grauwpoort 1A-5, 9000 Gent', '([0-9]+[^ ,\n]*)'}`

## Phone numbers

This example removes all special characters from a phone number.

`{regex_replace: {$.phone}, "([^\S]|[^0-9+])",""}`

## URLs and domain names

This example parses the path from a full URL, where the URL has a *.com* domain.

`{ regexparse:{$.getCompany.url}, "\.com(.*)" }`

Get the filename part of a URL:

`{regexparse: {$.url}, '(?:.+\/)(.+)'}`
