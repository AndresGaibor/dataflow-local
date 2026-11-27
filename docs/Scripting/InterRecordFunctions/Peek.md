---
title: "Peek Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterRecordFunctions/Peek.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# Peek Script function

Peek() returns the value of a field in a table for a row that has already been loaded. The row number can be specified, as can the table. If no row number is specified, the last previously loaded record will be used.

The Peek() function is most often used to find the relevant boundaries in a previously loaded table, that is, the first value or last value of a specific [field](#glossary-0 "Glossary term"). In most cases, this value is stored in a [variable](#glossary-1 "Glossary term") for later use, for example, as a condition in a do-while loop.

Syntax:

Peek(

field\_name

[, row\_no[, table\_name ] ])

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_name | Name of the field for which the return value is required.Input value must be given as a string (for example, quoted literals). |
| row\_no | The row in the table that specifies the field required. Can be an expression, but must resolve to an integer. 0 denotes the first record, 1 the second, and so on. Negative numbers indicate order from the end of the table. -1 denotes the last record read.  If no row\_no is stated, -1 is assumed. |
| table\_name | A table label without the ending colon. If no table\_name is stated, the current table is assumed. If used outside the LOAD statement or referring to another table, the table\_name must be included. |

Limitations:

The function can only return values from already loaded records. This means that in the first record of a table, a call using -1 as row\_no will return NULL.

Examples and results:

## Example 1

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

EmployeeDates:
Load \* Inline [
EmployeeCode|StartDate|EndDate
101|02/11/2010|23/06/2012
102|01/11/2011|30/11/2013
103|02/01/2012|
104|02/01/2012|31/03/2012
105|01/04/2012|31/01/2013
106|02/11/2013|
] (delimiter is '|');
First\_last\_Employee:
Load
EmployeeCode,
Peek('EmployeeCode',0,'EmployeeDates') As FirstCode,
Peek('EmployeeCode',-1,'EmployeeDates') As LastCode
Resident EmployeeDates;

Resulting table

| Employee code | StartDate | EndDate | FirstCode | LastCode |
| --- | --- | --- | --- | --- |
| 101 | 02/11/2010 | 23/06/2012 | 101 | 106 |
| 102 | 01/11/2011 | 30/11/2013 | 101 | 106 |
| 103 | 02/01/2012 |  | 101 | 106 |
| 104 | 02/01/2012 | 31/03/2012 | 101 | 106 |
| 105 | 01/04/2012 | 31/01/2013 | 101 | 106 |
| 106 | 02/11/2013 |  | 101 | 106 |

FirstCode = 101 because Peek('EmployeeCode',0, 'EmployeeDates') returns the first value of EmployeeCode in the table EmployeeDates.

LastCode = 106 because Peek('EmployeeCode',-1, 'EmployeeDates') returns the last value of EmployeeCode in the table EmployeeDates.

Substituting the value of the argument row\_no returns the values of other rows in the table, as follows:

Peek('EmployeeCode',2, 'EmployeeDates') returns the third value, 103, in the table as the FirstCode.

However, note that without specifying the table as the third argument table\_name in these examples, the function references the current (in this case, internal) table.

## Example 2

If you want to access data further down in a table, you need to do it in two steps: first, load the entire table into a temporary table, and then re-sort it when using Peek().

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

T1:
LOAD \* inline [
ID|Value
1|3
1|4
1|6
3|7
3|8
2|1
2|11
5|2
5|78
5|13
] (delimiter is '|');
T2:
LOAD \*,
IF(ID=Peek('ID'), Peek('List')&','&Value,Value) AS List
RESIDENT T1
ORDER BY ID ASC;
DROP TABLE T1;

Create a table in a [sheet](#glossary-2 "Glossary term") in your application with ID, List, and Value as the [dimensions](#glossary-4 "Glossary term").

Resulting table

| ID | List | Value |
| --- | --- | --- |
| 1 | 3,4 | 4 |
| 1 | 3,4,6 | 6 |
| 1 | 3 | 3 |
| 2 | 1,11 | 11 |
| 2 | 1 | 1 |
| 3 | 7,8 | 8 |
| 3 | 7 | 7 |
| 5 | 2,78 | 78 |
| 5 | 2,78,13 | 13 |
| 5 | 2 | 2 |

The IF() statement is built from the temporary table T1.
Peek('ID') references the field ID in the previous row in the current table T2.
Peek('List') references the field List in the previous row in the table T2, currently being built as the expression is evaluated.

The statement is evaluated as follows:
If the current value of ID is the same as the previous value of ID, then write the value of Peek('List') concatenated with the current value of Value. Otherwise, write the current value of Value only.

If Peek('List') already contains a concatenated result, the new result of Peek('List') will be concatenated to it.

Information noteNote the Order by clause. This specifies how the table is ordered (by ID in ascending order). Without this, the Peek() function will use whatever arbitrary ordering the internal table has, which can lead to unpredictable results.

## Example 3

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

Amounts:
Load
Date#(Month,'YYYY-MM') as Month,
Amount,
Peek(Amount) as AmountMonthBefore
Inline
[Month,Amount
2022-01,2
2022-02,3
2022-03,7
2022-04,9
2022-05,4
2022-06,1];

Resulting table

| Amount | AmountMonthBefore | Month |
| --- | --- | --- |
| 1 | 4 | 2022-06 |
| 2 | - | 2022-01 |
| 3 | 2 | 2022-02 |
| 4 | 9 | 2022-05 |
| 7 | 3 | 2022-03 |
| 9 | 7 | 2022-04 |

The field AmountMonthBefore will hold the amount from the previous month.

Here, the row\_no and table\_name parameters are omitted, so the default values are used. In this example, the following three function calls are equivalent:

- Peek(Amount)
- Peek(Amount,-1)
- Peek(Amount,-1,'Amounts')

Using -1 as row\_no means that the value from previous row will be used. By substituting this value, values of other rows in the table can be fetched:

Peek(Amount,2) returns the third value in the table: 7.

## Example 4

Data needs to be correctly sorted in order to get the correct results but, unfortunately, this is not always the case. Furthermore, the Peek() function cannot be used to reference data that has not yet been loaded. By using temporary tables and running multiple passes through the data, such problems can be avoided.

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

```
tmp1Amounts:
Load * Inline
[Month,Product,Amount
2022-01,B,3
2022-01,A,8
2022-02,B,4
2022-02,A,6
2022-03,B,1
2022-03,A,6
2022-04,A,5
2022-04,B,5
2022-05,B,6
2022-05,A,7
2022-06,A,4
2022-06,B,8];

tmp2Amounts:
Load *,
If(Product=Peek(Product),Peek(Amount)) as AmountMonthBefore
Resident tmp1Amounts
Order By Product, Month Asc;
Drop Table tmp1Amounts;

Amounts:
Load *,
If(Product=Peek(Product),Peek(Amount)) as AmountMonthAfter
Resident tmp2Amounts
Order By Product, Month Desc;
Drop Table tmp2Amounts;
```

Explanation

The initial table is sorted according to month, which means that the peek() function would in many cases return the amount for the wrong product. Hence, this table needs to be re-sorted. This is done by running a second pass through the data creating a new table tmp2Amounts. Note the Order By clause. It orders the records first by product, then by month in ascending order.

The If() function is needed since the AmountMonthBefore only should be calculated if the previous row contains the data for the same product but for the previous month. By comparing the product on the current row with the product on the previous row, this condition can be validated.

When the second table is created, the first table tmp1Amounts is dropped using a Drop Table statement.

Finally, a third pass is made through the data, but now with the months sorted in reverse order. This way, AmountMonthAfter can also be calculated.

Information noteOrder by clauses specify how the table is ordered; without these, the Peek() function will use whatever arbitrary ordering the internal table has, which can lead to unpredictable results.

Result

Resulting table

| Month | Product | Amount | AmountMonthBefore | AmountMonthAfter |
| --- | --- | --- | --- | --- |
| 2022-01 | A | 8 | - | 6 |
| 2022-02 | B | 3 | - | 4 |
| 2022-03 | A | 6 | 8 | 6 |
| 2022-04 | B | 4 | 3 | 1 |
| 2022-05 | A | 6 | 6 | 5 |
| 2022-06 | B | 1 | 4 | 5 |
| 2022-01 | A | 5 | 6 | 7 |
| 2022-02 | B | 5 | 1 | 6 |
| 2022-03 | A | 7 | 5 | 4 |
| 2022-04 | B | 6 | 5 | 8 |
| 2022-05 | A | 4 | 7 | - |
| 2022-06 | B | 8 | 6 | - |

## Example 5

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

T1:
Load \* inline [
Quarter, Value
2003q1, 10000
2003q1, 25000
2003q1, 30000
2003q2, 1250
2003q2, 55000
2003q2, 76200
2003q3, 9240
2003q3, 33150
2003q3, 89450
2003q4, 1000
2003q4, 3000
2003q4, 5000
2004q1, 1000
2004q1, 1250
2004q1, 3000
2004q2, 5000
2004q2, 9240
2004q2, 10000
2004q3, 25000
2004q3, 30000
2004q3, 33150
2004q4, 55000
2004q4, 76200
2004q4, 89450 ];
T2:
Load \*, rangesum(SumVal,peek('AccSumVal')) as AccSumVal;
Load Quarter, sum(Value) as SumVal resident T1 group by Quarter;

Result

Resulting table

| Quarter | SumVal | AccSumVal |
| --- | --- | --- |
| 2003q1 | 65000 | 65000 |
| 2003q2 | 132450 | 197450 |
| 2003q3 | 131840 | 329290 |
| 2003q4 | 9000 | 338290 |
| 2004q1 | 5250 | 343540 |
| 2004q2 | 24240 | 367780 |
| 2004q3 | 88150 | 455930 |
| 2004q4 | 220650 | 676580 |

Explanation

The load statement
Load \*, rangesum(SumVal,peek('AccSumVal')) as AccSumVal includes a recursive call where the previous values are added to the current value. This operation is used to calculate an accumulation of values in the script.

## Learn more

- [*Table labels*](../table-labels.htm)
- [*Previous Script function*](Previous.htm)
