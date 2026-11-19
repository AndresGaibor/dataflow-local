---
title: "Declare"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Declare.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Declare

The Declare statement is used to create field definitions, where you can define relations between fields or functions. A set of field definitions can be used to automatically generate derived fields, which can be used as dimensions. For example, you can create a calendar definition, and use that to generate related dimensions, such as year, month, week and day, from a date field.

You can use Declare to either set up a new [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Declare.htm#glossary-0 "Glossary term") definition, or to create a field definition based on an already existing definition.

## Setting up a new field definition

Syntax:

definition\_name:

Declare [Field[s]] Definition [Tagged tag\_list ]

[Parameters parameter\_list ]

Fields field\_list

Arguments:

| Argument | Description |
| --- | --- |
| definition\_name | Name of the field definition, ended with a colon.  **Warning:** Do not use autoCalendar as name for field definitions, as this name is reserved for auto-generated calendar templates.  Example:  `Calendar:` |
| tag\_list | A comma separated list of tags to apply to fields derived from the field definition. Applying tags is optional, but if you do not apply tags that are used to specify sort order, such as $date, $numeric or $text, the derived field will be sorted by load order as default.  Example:  `'$date'Thank you for bringing this to our attention, and apologies for the inconvenience.`  [*Field tags*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/field-tags.htm) |
| parameter\_list | A comma separated list of parameters. A parameter is defined in the form `name=value` and is assigned a start value, which can be overridden when a field definition is re-used. Optional.  Example:  `first_month_of_year = 1` |
| field\_list | A comma separated list of fields to generate when the field definition is used. A field is defined in the form `<expression> As field_name tagged tag`. Use `$1` to reference the data field from which the derived fields should be generated.  Example:  `Year($1) As Year tagged ('$numeric')` |

Example:

Calendar:
DECLARE FIELD DEFINITION TAGGED '$date'
Parameters
first\_month\_of\_year = 1
Fields

Year($1) As Year Tagged ('$numeric'),
Month($1) as Month Tagged ('$numeric'),
Date($1) as Date Tagged ('$date'),
Week($1) as Week Tagged ('$numeric'),
Weekday($1) as Weekday Tagged ('$numeric'),
DayNumberOfYear($1, first\_month\_of\_year) as DayNumberOfYear Tagged ('$numeric')
;

The calendar is now defined, and you can apply it to the date fields that have been loaded, in this case OrderDate and ShippingDate, using a Derive clause.

[*Derived fields*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/derived-fields.htm) (full example)

## Re-using an existing field definition

Syntax:

<definition name>:

Declare [Field][s] Definition

Using <existing\_definition>

[With <parameter\_assignment> ]

Arguments:

| Argument | Description |
| --- | --- |
| definition\_name | Name of the field definition, ended with a colon.  Example:  `MyCalendar:` |
| existing\_definition | The field definition to re-use when creating the new field definition. The new field definition will function the same way as the definition it is based on, with the exception if you use parameter\_assignment to change a value used in the field expressions.  Example:  `Using Calendar` |
| parameter\_assignment | A comma separated list of parameter assignments. A parameter assignment is defined in the form `name=value` and overrides the parameter value that is set in the base field definition. Optional.  Example:  `first_month_of_year = 4` |

Example:

In this example we re-use the calendar definition that was created in the previous example. In this case we want to use a fiscal year that starts in April. This is achieved by assigning the value 4 to the first\_month\_of\_year parameter, which will affect the DayNumberOfYear field that is defined.

The example assumes that you use the sample data and field definition from the previous example.

MyCalendar:
DECLARE FIELD DEFINITION USING Calendar WITH first\_month\_of\_year=4;

DERIVE FIELDS FROM FIELDS OrderDate,ShippingDate USING MyCalendar;

When you have reloaded the data script, the generated fields are available in the sheet editor, with names OrderDate.MyCalendar.\* and ShippingDate.MyCalendar.\*.

## Learn more

- [*Derive*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Derive.htm)
