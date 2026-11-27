---
title: "REGEX_NAMED_GROUPS"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/regular-expressions/regex_named_groups.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Regular Expressions"]
---

# REGEX\_NAMED\_GROUPS

Matches the regular expression on the input string. Returns the record with field names and group names.

## Syntax

```
REGEX_NAMED_GROUPS(pattern, allMatches, filterEmpty, input)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| pattern | string | Regular Expression Pattern |  |
| allMatches | Boolean | Return all the matches of the pattern, and not only the first one | false |
| filterEmpty | Boolean | Filter out empty matches | false |
| input | string |  |  |

## Examples

| pattern | allMatches | filterEmpty | input | Output |
| --- | --- | --- | --- | --- |
| '^(?:(?.*?):/)?/?(?[^:/\s]+)(?::(?\d*))?(?:(/\w+)*/)(?[\w-.]+[^#?\s]+)(?:.*)?$' | false | false | 'https://www.domain.com/page.html' | {scheme: `https`, domain: `www.domain.com`, port: null, page: `page.html`} |
| '^(?:(?.*?):/)?/?(?[^:/\s]+)(?::(?\d*))?(?:(/\w+)*/)(?[\w-.]+[^#?\s]+)(?:.*)?$' | false | false | 'http://www.domain.com:8080/page.html' | {scheme: `http`, domain: `www.domain.com`, port: `8080`, page: `page.html`} |
| '^(?\d\*)$' | false | false | '123' | {digits: `123`} |
| '^(?\d\*)$' | false | false | 'foo' | null |
| '^(?\d\*)$' | false | false | '' | {digits: ``} |
| '^(?\d\*)$' | false | true | '' | null |
| '\bwww.(?[^.]\*).com\b' | true | false | 'www.qlik.com' | {domain: `qlik`} |
| '\bwww.(?[^.]\*).com\b' | true | false | 'www.a.com www.b.com' | [{domain: `a`}, {domain: `b`}] |
| '\bwww.(?[^.]\*).com\b' | false | false | 'www.a.com www.b.com' | {domain: `a`} |
