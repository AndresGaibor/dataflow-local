---
title: "Derived fields"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/derived-fields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures", "Fields"]
---

# Derived fields

If you have a group of fields that are related, or if fields carry information that can be broken up into smaller parts that are relevant when creating dimensions or measures, you can create field definitions that can be used to generate derived fields. One example is a date field, from which you can derive several attributes, such as year, month, week number, or day name. All these attributes can be calculated in a dimension expression using Qlik Sense date functions, but an alternative is to create a calendar definition that is common for all fields of date type. Field definitions are stored in the data load script.

Information noteDefault calendar field definitions for Qlik Sense are included in autoCalendar for date fields loaded using Data manager.For more information, see [*Automatically deriving date fields using autocalendar*](#Automati) and [*Adding data to the application from connections and new files*](../LoadData/adding-data.htm).

## Declare the calendar field definitions

You use the Declare statement to create a definition of the derived fields. This is where you define the different attributes of the [field](#glossary-0 "Glossary term") in this case date related attributes. Each field is described as <expression> As field\_name tagged tag. Setting one or more tags is optional, but it can affect the sort order of the derived field. Use $1 to reference the data field from which the derived fields should be generated.

Warning note
Unless you are creating your own autocalendar or working with the auto-configured [autoCalendar] created by Data manager, do not use autoCalendar as name for calendar field definitions. This name is reserved for auto-generated calendar templates. See [*Automatically deriving date fields using autocalendar*](#Automati).

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
DayNumberOfYear($1, first\_month\_of\_year) as DayNumberOfYear Tagged ('$numeric');

For more information, see [*Declare*](ScriptRegularStatements/Declare.htm).

## Map data fields to the calendar with Derive

The next step is to use the Derive statement to map existing data fields to the calendar. This will create the derived fields. You can do this in three alternative ways in the data load script:

- Map specific fields by field name.

  DERIVE FIELDS FROM FIELDS OrderDate,ShippingDate USING Calendar;
- Map all fields with one or more specific field tags.

  DERIVE FIELDS FROM EXPLICIT TAGS ('$date') USING Calendar;
- Map all fields that are tagged with one of the tags of the field definition ($date in the example above).

  DERIVE FIELDS FROM IMPLICIT TAG USING Calendar;

In this case, you could use any of the three examples here.

For more information, see [*Derive*](ScriptRegularStatements/Derive.htm).

## Automatically deriving date fields using autocalendar

If you use Data manager to build your application and load data, a calendar named [autoCalendar] is automatically inserted into the load script to provide default calendar definitions. These are visible in the application's [business logic](#glossary-1 "Glossary term").

For applications created using scripting which contain date fields, you can insert this [autoCalendar] code, shown below, into your script in a section after you have loaded all applicable date fields. This allows application users to use all available period-based analysis types, including those which can build smart sheets. Note that the calendar must be titled [autocalendar] for the calendar periods to be added correctly in business logic.

Modify the [My\_Date\_Field1] and [My\_Date\_Field2] field names in the line DERIVE FIELDS FROM FIELDS [My\_Date\_Field1], [My\_Date\_Field2] USING [autoCalendar] ; to link the date field with the autocalendar calculations generating the new derived date fields. If you only have one date field to link to autocalendar, remove the [My\_Date\_Field2]. Similarly, add additional date fields if you have more than two date fields to enable autocalendar for.

```
[autoCalendar]:
  DECLARE FIELD DEFINITION Tagged ('$date')
FIELDS
  Dual(Year($1), YearStart($1)) AS [Year] Tagged ('$axis', '$year'),
  Dual('Q'&Num(Ceil(Num(Month($1))/3)),Num(Ceil(NUM(Month($1))/3),00)) AS [Quarter] Tagged ('$quarter', '$cyclic'),
  Dual(Year($1)&'-Q'&Num(Ceil(Num(Month($1))/3)),QuarterStart($1)) AS [YearQuarter] Tagged ('$yearquarter', '$qualified'),
  Dual('Q'&Num(Ceil(Num(Month($1))/3)),QuarterStart($1)) AS [_YearQuarter] Tagged ('$yearquarter', '$hidden', '$simplified'),
  Month($1) AS [Month] Tagged ('$month', '$cyclic'),
  Dual(Year($1)&'-'&Month($1), monthstart($1)) AS [YearMonth] Tagged ('$axis', '$yearmonth', '$qualified'),
  Dual(Month($1), monthstart($1)) AS [_YearMonth] Tagged ('$axis', '$yearmonth', '$simplified', '$hidden'),
  Dual('W'&Num(Week($1),00), Num(Week($1),00)) AS [Week] Tagged ('$weeknumber', '$cyclic'),
  Date(Floor($1)) AS [Date] Tagged ('$axis', '$date', '$qualified'),
  Date(Floor($1), 'D') AS [_Date] Tagged ('$axis', '$date', '$hidden', '$simplified'),
  If (DayNumberOfYear($1) <= DayNumberOfYear(Today()), 1, 0) AS [InYTD] ,
  Year(Today())-Year($1) AS [YearsAgo] ,
  If (DayNumberOfQuarter($1) <= DayNumberOfQuarter(Today()),1,0) AS [InQTD] ,
  4*Year(Today())+Ceil(Month(Today())/3)-4*Year($1)-Ceil(Month($1)/3) AS [QuartersAgo] ,
  Ceil(Month(Today())/3)-Ceil(Month($1)/3) AS [QuarterRelNo] ,
  If(Day($1)<=Day(Today()),1,0) AS [InMTD] ,
  12*Year(Today())+Month(Today())-12*Year($1)-Month($1) AS [MonthsAgo] ,
  Month(Today())-Month($1) AS [MonthRelNo] ,
  If(WeekDay($1)<=WeekDay(Today()),1,0) AS [InWTD] ,
  (WeekStart(Today())-WeekStart($1))/7 AS [WeeksAgo] ,
  Week(Today())-Week($1) AS [WeekRelNo] ;

DERIVE FIELDS FROM FIELDS [My_Date_Field1], [My_Date_Field2] USING [autoCalendar] ;
```

If done correctly, a number of calendar periods will be automatically created in the application's business logic, and you will be able to use the period-based analysis types in Insight Advisor.

For more information, see [*Using smart sheets in Insight Advisor for period-based analyses*](../Insights/insight-advisor-smart-sheets.htm).

## Use the derived date fields in a visualization

Qlik Sense is prepared to recognize derived date fields if you have created a calendar definition and mapped the fields like in the example here. They are available in the Date & time fields section of the Fields asset panel. You will also find all derived fields in the expression editor and when you create or edit [dimensions](#glossary-2 "Glossary term").

For more information, see [*Date & time fields*](../Assets/date-time-fields.htm).
