---
title: "Dollar-sign expansion using a variable"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/dollar-sign-expansion-using-variable.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures", "Dollar-sign expansions"]
---

# Dollar-sign expansion using a variable

Expand/Collapse all

# Dollar-sign expansion using a variable

In the [load script](#glossary-0 "Glossary term") or a chart expression, use a [variable](#glossary-1 "Glossary term") in a dollar-sign expansion to:

- Reference text
- Reference a numeric value

## Text variable

When using a variable for text replacement in the script or in an expression,
the following syntax is used:

$(variablename)

$(variablename)
 expands to the value in the variable. If variablename does not exist, the expansion will result in an empty string.

## Examples: Text variable load scripts

Example 1: Load script

Load script

Load the following data as an inline load in the data load editor:

```
Set x = 'red';  	// Assign the value "red" to variable x
Set y = 'blue'; 	 // Assign the value "blue" to variable y
Set z = '$(x) $(y)';    // Expands x and y, returns "red blue" in variable z

// Expand x and y, return "red green blue" in variable MyString

Let MyString='$(x)'&' green '&'$(y)';

// Create table MyTable, load variable values for x, y, z into fields X, Y, Z
// Concatenate with variable MyString into field NewString

MyTable:
Load '$(x)' as X, '$(y)' as Y, '$(z)' as Z, '$(MyString)' as NewString autogenerate 1;
```

For more information about using inline loads, see [*Using inline loads to load data*](inline-loads-qs.htm).

Explanation

This example demonstrates:

- How to expand a variable in variable assignments.
- How to expand variables combined with a textual operations.

This is a useful setup for creating dynamic labels and general text strings that combine a variable content with static strings.

Output

Create the following table in Qlik Sense:

Table - Output from load script

| X | Y | Z | NewString |
| --- | --- | --- | --- |
| red | blue | red blue | red green blue |

Example 2: Load script

Load script

Load the following data as an inline load in the data load editor:

```
Set vFunction = 'upper';  // Assign the string “upper” to variable vFunction
Set vField = 'String';    // Assign the string "String" to variable vField
Let vEvaluate = '$(vFunction)'&'('&'$(vField)'&')';

// The variable vEvaluate returns the value "upper(string)"

MyTable: // Create table called MyTable
Load *, $(vEvaluate) as Upper;          // vEvaluate expanded as a dynamic expression
Load *, '$(vEvaluate)' as Expression;   // vEvaluate expanded as string
Load * inline [
ID, String
1, abc
2, def
3, ghi
4, jkl ];
```

Explanation

The Set and Letstatements are used to assign values to variables in the load script. The difference between the two is that the Setstatement assigns a string to the variable, while the Letstatement evaluates the content of the string before assigning the resultant value to the variable. The load inline table in this example is supplemented with two [preceding load](#glossary-2 "Glossary term") statements that are used to visualize different evaluations of the variable vEvaluate both as a text string and as the corresponding expression.

Output

Create the following table in Qlik Sense:

Table - Output from load script

| ID | String | Expression | Upper |
| --- | --- | --- | --- |
| 1 | abc | upper(String) | ABC |
| 2 | def | upper(String) | DEF |
| 3 | ghi | upper(String) | GHI |
| 4 | jkl | upper(String) | JKL |

## Example: Text variable chart expression

Example: Load script

Load script

Load the following data as an inline load in the data load editor:

```
// Create table SalesByCountry
SalesByCountry:
Load * Inline [
Country, Year, Sales
Argentina, 2014, 66295.03
Argentina, 2015, 140037.89
Austria, 2014, 54166.09
Austria, 2015, 182739.87
Belgium, 2014, 182766.87
Belgium, 2015, 178042.33
Brazil, 2014, 174492.67
Brazil, 2015, 2104.22
Canada, 2014, 101801.33
Canada, 2015, 40288.25
Denmark, 2014, 45273.25
Denmark, 2015, 106938.41
Finland, 2014, 107565.55
Finland, 2015, 30583.44
France, 2014, 115644.26
France, 2015, 30696.98
Germany, 2014, 8775.18
Germany, 2015, 77185.68
];
```

Variables

In a [sheet](#glossary-3 "Glossary term") in edit mode, open the Variables dialog from the Assets panel.

Open variables dialog

![KPIs using set modifiers.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_dollar_open_variable_dialog.png "Click to view full size")

Create the following variables:

Variable to create

| Name | Definition |
| --- | --- |
| vSales | Sum(Sales) |
| vSales2014 | Sum({<Year={2014}>}Sales) |
| vSales2015 | Sum({<Year={2015}>} Sales) |
| vSalesAllYears | $(vSales2014) +$(vSales2015) |
| vSalesDifference | $(vSales2015)/$(vSales2014) - 1 |

Variables

![KPIs using set modifiers.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_dollar_variables_window_new.png "Click to view full size")

Create KPI charts to see the expansions.

KPIs using dollar sign expansions

![KPIs using dollar sign expansions.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_dollar_kpis.png "Click to view full size")

## Numeric variable expansion

For numeric variable expansions, the following syntax is used:

(#variablename)

The expansion always yields a valid decimal-point representation of the numeric value of the variable, possibly with exponential notation (for very large or small numbers). If variablename does not exist or does not contain a numeric value, it will be expanded to 0 instead of NULL.

## Examples: Numeric variable load scripts

Example 1: Load script

Load script

Load the following data as an inline load in the data load editor:

```
Set DecimalSep = ',';  // Set decimal comma as separator for this example.
Let X = 7/2;           // Assign the expression 7/2 to variable X.

MyTable:   // Create an inline table labeled “MyTable”
Load 1 as ID, * inline [
DecimalComma	DecimalPoint
$(X)	$(#X) ]
(delimiter is '\t');
```

Explanation

The #vVariable expansion always yields a valid decimal-point representation of the numeric value of the variable. This is useful when comma, rather than point is used as decimal separator and there is a risk of a conflict with comma separated lists.

The main reason for expanding these variables in a load-inline table is that no additional quoting of $(X) is required.

Output

Create the following table in Qlik Sense:

Table - Output from load script

| DecimalComma | DecimalPoint |
| --- | --- |
| 3,5 | 3.5 |

Example 2: Load script

Load script

Load the following data as an inline load in the data load editor:

```
// The three Set statements below are required to mimic and initialize
// Format specifiers that are relevant to this particular example

Set ThousandSep=' '; 		// Set example thousand separator
Set DecimalSep=','; 		// Set example decimal separator
Set TimestampFormat='YYYY-MM-DD hh:mm:ss';	 // Set example date format
Let vRaw = today()-1/1440;  		 // Timestamp minus one minute
Let vFormat = timestamp($(#vRaw));	 // Formatted as timestamp

// Create MyTable as an inline table to expand variables as field values

MyTable:
Load * inline [
DecimalComma	DecimalPoint	FormattedNumber
$(vRaw)	$(#vRaw)	$(vFormat) ] (delimiter is '\t');
```

Explanation

The #vVariable expansion always yields a valid decimal-point representation of the numeric value of the variable. This is useful when comma, rather than point is used as decimal separator and there is a risk of a conflict with comma separated lists. It is also important to note that the numerical precision will be affected due to the decimal part being truncated when variables are expanded without correct decimal separator.

The main reason for expanding these variables in a load-inline table is that no additional quoting of $(X) is required.

Output

Create the following table in Qlik Sense:

Table - Output from load script

| DecimalComma | DecimalPoint | FormattedNumber |
| --- | --- | --- |
| 44 470,00 | 44469.999305556 | 2021-09-18 23:59:00 |

Example 3: Load script

Load script

Load the following data as an inline load in the data load editor:

```
// The three Set statements below are required to mimic and initialize
// format specifiers that are relevant to this particular example

Set ThousandSep=' '; 		// Set example thousand separator
Set DecimalSep=','; 		// Set example decimal separator
Set TimestampFormat='YYYY-MM-DD hh:mm:ss';	// Set example date format

// Assign a numerical value and a valid format specifier to vStart

Let vStart = timestamp#('2021-03-23 12:34:56','$(TimestampFormat)');

// Calculate timestamp (vStart + 3 hours) with valid decimal separator: "."

Let vStop = timestamp($(#vStart)+1/8,'YYYY-MM-DD hh:mm:ss');

// Create MyTable as an inline table to expand variables as field values

MyTable:
Load * inline [
StartTime	StopTime
$(vStart)	$(vStop) ] (delimiter is '\t');

// This is a tab delimited inline table
// Tab delimited tables are useful for avoiding conflicting list separators
```

Explanation

The #vVariable expansion always yields a valid decimal-point representation of the numeric value of the variable. This is useful when comma, rather than point is used as decimal separator and there is a risk of a conflict with comma separated lists. It is also important to note that the numerical precision will be affected due to the decimal part being truncated when variables are expanded without correct decimal separator.

The main reason for expanding these variables in a load-inline table is that no additional quoting of $(X) is required.

Output

Create the following table in Qlik Sense:

Table - Output from load script

| StartTime | StopTime |  |
| --- | --- | --- |
| 2021-03-23 12:34:56 | 2021-03-23 15:34:56 |  |

## Expanding variables referencing alternate states

The variable has only one value, and this is used in all alternate states. When you expand a variable the value is also the same, independent of where it is made, and the state of the object.

If the variable is a calculated variable, that is, the definition starts with an equals sign, the calculation is made in the default state, unless you specify an alternate state in the variable definition.

For example, if you have a state named MyState, and a variable named vMyVar:

```
vMyvar: =only({MyState}MyField)
```

The variable definition content, with an explicit reference to the alternate state name, determines in which state the variable content will be evaluated.

## Interaction between variables and outer set expressions

When you reference a variable in a dollar-sign expansion that also contains an outer set expression, a specific order of evaluation applies. For details, see [*Variable lookup*](../ChartFunctions/SetAnalysis/outer-set-expression-dollar-sign-expansion.htm#Variable).

## Learn more

- [*Let*](ScriptRegularStatements/Let.htm)
- [*Set*](ScriptRegularStatements/Set.htm)
- [*Working with variables in the data load editor*](work-with-variables-in-data-load-editor.htm)
