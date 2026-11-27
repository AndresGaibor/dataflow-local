---
title: "Text functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/text-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations", "Working with formulas"]
---

# Text functions

You can manipulate strings using the available text functions in Qlik Automate.

## Upper and lowercase

Change all characters to upper or lower case.

`{$.inputs.name}` = John

`{uppercase:{$.inputs.name}}` = JOHN

`{lowercase:{$.inputs.name}}` = john

## Capitalize name

Change the first character in a name (string) to uppercase.

`{$.inputs.name}` = john doe

`{capitalizename:{$.inputs.name}}` = John Doe

## Trim

Removes spaces, line breaks, or characters. Specify which side of the string to `rtrim` (right) or `ltrim` (left). Specify an optional character trim as a parameter.

`{$.inputs.companyURL}` = www. qlik. com

`{trim:{$.inputs.companyURL}}` = www.qlik.com

`{trim:{$.inputs.companyURL}, "www."}` = qlik.com

## Regex parse

Parses a string from a given text based on a regular expression (regex). The regular expression is a required parameter. Only the first match of the regex is returned. If you want to return all the matches, use `regexparseall`.

`{$.inputs.companyURL}` = www.qlik.com/us/products

`\.com(.*)` = parses everything after ".com"

`{regexparse:{$.getCompany.url}, "\.com(.*)"}` = /us/products

See some examples of common [regular expressions](working-with-regex.htm).

## Regex parse all

Parses a string from a user-defined text based on a regular expression (regex) and returns a list with all matches. This formula supports only one capturing group in the regex. If you only want the first match, use `regexparse`.

`{$.inputs.companyURL}` = www.qlik.com/us/products, www.qlik.com/us/support, www.qlik.com/us/about

`\.com(.*)` = parses everything after ".com"

`{regexparseall:{$.getCompany.url}, "\.com(.*)"}` = /us/products, /us/support, /us/about

See some examples of common [regular expressions](working-with-regex.htm).

## Regex replace

Replaces a string based on a regular expression (regex). Each match of the regex is replaced. The new text can have a placeholder $1 to insert the text that matches a capture group from the regex, for example `(.*)`.

`{$.inputs.companyURL}` = www.qlik.ca

`{regexreplace: {$.inputs.companyURL}, '(.*)ca', '$1com'}` = www.qlik.com

See some examples of common [regular expressions](working-with-regex.htm).

## Replace

Replaces a string.

`{$.inputs.address}` = 100 Main Street

`{replace:{$.inputs.address}, "Street", "St."}` = 100 Main St.

## Remove

Removes a string.

`{$.inputs.address}` = 100 Main St., Ottawa Ontario

`{remove:{$.inputs.address}, "Ontario"}` = 100 Main St., Ottawa

## Substring

Returns part of a string based on a fixed start position and length.

`{$.inputs.postalCode}` = A1A 2B2

`{substring:{$.inputs.postalCode}, 0, 3}` = A1A

In the above example, the start position is 0 and the length of the text to return is 3 characters.

## String Position

Returns the position of the first occurrence of a specified string.

`{$.inputs.locations}` = "Ottawa\nLund\nBoston"

`{strpos: {$.inputs.locations}, 'Boston'}` = 12

Variants of `strpos`:

- `strrpos`: reverse search (right to left, finds the last occurrence of a string)
- `stripos`: case-insensitive search
- `strripos`: case-insensitive reverse search

## Text length

Returns the length of a string. Whitespaces and punctuation are counted.

`{$.inputs.postalCode}` = A1A 2B2

`{text_length:{$.inputs.postalCode}}` = 7

## toAscii

Converts a string with special characters to a plain text with ASCII characters only.

Tip note

This is useful for sending data to a platform that does not handle special characters (UTF-8).

`{$.inputs.name}` = Léo

`{toAscii:{$.inputs.name}}` = Leo

## Explode

Converts a string of items separated by either a comma or space into a list. The delimiter and a list limit can be added as parameters. If no delimiter is set, the default delimiter is a comma.

`{$.inputs.shoppingList}` = apples, oranges, pears, grapes

`{explode: {$.inputs.shoppingList}, ',', 100}` = ["apples", "oranges", "pears", "grapes"]

## Random Text

Generates random text. This formula is applied to an integer that determines the length of the random text.

`{randomText:5}` = fptun

## Line break

Inserts a line break in a string. The line break formula does not take any parameters.

`{$.inputs.name}{$.inputs.address}{$.inputs.city}` = John Doe1 Main StreetNew York

`{$.inputs.name}{linebreak}{$.inputs.address}{linebreak}{$.inputs.city}` = John Doe</br>1 Main Street</br>New York
