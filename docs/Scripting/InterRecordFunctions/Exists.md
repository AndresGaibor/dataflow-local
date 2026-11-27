---
title: "Exists Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterRecordFunctions/Exists.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# Exists Script function

Exists() determines whether a specific field
value has already been loaded into the field in the data load script. The function returns TRUE or FALSE, so it can be used in the where clause of a LOAD statement or an IF statement.

Information noteYou can also use Not Exists() to determine if a [field](#glossary-0 "Glossary term") value has not been loaded, but caution is recommended if you use Not Exists() in a where clause. The Exists() function tests both previously loaded tables and previously loaded values in the current table. So, only the first occurrence will be loaded. When the second occurrence is encountered, the value is already loaded. See the examples for more information.

Syntax:

Exists(field\_name
[, expr])

Return data type:  Boolean

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_name | The name of the field where you want to search for a value. You can use an explicit field name without quotes.  The field must already be loaded by the script. That means, you cannot refer to a field that is loaded in a clause further down in the script. |
| expr | The value that you want to check if it exists. You can use an explicit value or an expression that refers to one or several fields in the current load statement.  Information noteYou cannot refer to fields that are not included in the current load statement.  This argument is optional. If you omit it, the function will check if the value of field\_name in the current record already exists. |

Examples and results:

Example 1

Exists
(Employee)

Returns -1 (True) if the value of the field Employee in the current record
already exists in any previously read record containing that field.

The statements Exists (Employee, Employee) and Exists (Employee) are equivalent.

Example 2

Exists(Employee,
'Bill')

Returns -1 (True) if the field value 'Bill' is found in the current content of the field Employee.

Example 3

Employees:
LOAD \* inline [
Employee|ID|Salary
Bill|001|20000
John|002|30000
Steve|003|35000
] (delimiter is '|');
Citizens:
Load \* inline [
Employee|Address
Bill|New York
Mary|London
Steve|Chicago
Lucy|Madrid
Lucy|Paris
John|Miami
] (delimiter is '|') where Exists (Employee);
Drop Tables Employees;

This results in a table that you can use in a table [visualization](#glossary-1 "Glossary term") using the [dimensions](#glossary-2 "Glossary term") Employee and Address.

The where clause, where Exists (Employee), means only the names from the table Citizens that are also in Employees are loaded into the new table. The Drop statement removes the table Employees to avoid confusion.

Results

|  |  |
| --- | --- |
| Employee | Address |
| Bill | New York |
| John | Miami |
| Steve | Chicago |

Example 4

Employees:
Load \* inline [
Employee|ID|Salary
Bill|001|20000
John|002|30000
Steve|003|35000
] (delimiter is '|');
 
Citizens:
Load \* inline [
Employee|Address
Bill|New York
Mary|London
Steve|Chicago
Lucy|Madrid
Lucy|Paris
John|Miami
] (delimiter is '|') where not Exists (Employee);
 
Drop Tables Employees;

The where clause includes not: where not Exists (Employee).

This means that only the names from the table Citizens that are not in Employees are loaded into the new table.

Note that there are two values for Lucy in the Citizens table, but only one is included in the result table. When you load the first row with the value Lucy, it is included in the Employee field. Hence, when the second line is checked, the value already exists.

Results

| Employee | Address |
| --- | --- |
| Mary | London |
| Lucy | Madrid |

Example 5

This example shows how to load all values.

Employees:
Load Employee As Name;
LOAD \* inline [
Employee|ID|Salary
Bill|001|20000
John|002|30000
Steve|003|35000
] (delimiter is '|');
 
Citizens:
Load \* inline [
Employee|Address
Bill|New York
Mary|London
Steve|Chicago
Lucy|Madrid
Lucy|Paris
John|Miami
] (delimiter is '|') where not Exists (Name, Employee);
 
Drop Tables Employees;

To be able to get all values for Lucy, two things were changed:

- A [preceding load](#glossary-3 "Glossary term") to the Employees table was inserted where Employee was renamed to Name.

  Load Employee As Name;
- The Where condition in Citizens was changed to:

  not Exists (Name, Employee).

This creates fields for Name and Employee. When the second row with Lucy is checked, it still does not exist in Name.

Results

| Employee | Address |
| --- | --- |
| Mary | London |
| Lucy | Madrid |
| Lucy | Paris |
