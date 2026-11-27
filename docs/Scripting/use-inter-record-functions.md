---
title: "Using inter-record functions: Peek , Previous , and Exists"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/use-inter-record-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Next steps in scripting", "Transforming data"]
---

# Using inter-record functions: Peek, Previous, and Exists

These functions are used when a value from previously loaded records
of data is needed for the evaluation of the current record.

In this part of the tutorial we will be examining the Peek(), Previous(), and Exists() functions.

## Peek()

Peek() returns the value of a field in a table for a row that has already been loaded. The row number can be specified, as can the table. If no row number is specified, the last previously loaded record will be used.

Syntax:

Peek(fieldname [ , row [ , tablename ] ] )

Row must be an integer. 0 denotes the first record, 1 the second and so on. Negative numbers indicate order from the end of the table. -1 denotes the last record read.

If no row is stated, -1 is assumed.

Tablename is a table label without the ending colon. If no tablename is stated, the current table is assumed. If used outside the LOAD statement or referring to another table, the tablename must be included.

## Previous()

Previous() finds the value of the expr expression using data from the previous input record that has not been discarded because of
a where clause. In the first record
of an internal table, the function will return NULL.

Syntax:

Previous(expression)

The Previous() function may be nested in order to access records further back. Data is fetched directly from the input source, making it possible to also refer to fields which have not been loaded into Qlik Sense, that is, even if they have not been stored in the associated database.

## Exists()

Exists() determines whether a specific field
value has already been loaded into the field in the data load script. The function returns TRUE or FALSE, so it can be used in the where clause of a LOAD statement or an IF statement.

Syntax:

Exists(field [, expression ] )

The field
must exist in the data loaded so far by the script. Expression is an expression evaluating to the field value to look for in the specified
field. If omitted, the current record’s value in the specified field
will be assumed.

## Using Peek() and Previous()

In their simplest form, Peek() and Previous() are used to identify specific values within a table. Here is a sample of the data in the Employees table that you will load in this exercise.

Sample of data from Employees table

| Date | Hired | Terminated |
| --- | --- | --- |
| 1/1/2011 | 6 | 0 |
| 2/1/2011 | 4 | 2 |
| 3/1/2011 | 6 | 1 |
| 4/1/2011 | 5 | 2 |

Currently this only collects data for month, hires and terminations, so we are going to add fields for Employee Count and Employee Var, using the Peek() and Previous() functions, to see the monthly difference in total employees.

Do the following:

1. Open the Advanced Scripting Tutorial application.
2. Add a new script section in the Data load editor.
3. Call the section Employees.
4. Under DataFiles in the right menu, click Select data.
5. Upload and then select Employees.xlsx.

Information noteUnder Field names, make sure that Embedded field names is selected to include the names of the table fields when you load the data.

6. In the Select data from window, click Add.

Your script should look like this:

LOAD
"Date",
Hired,
Terminated
FROM [lib://DataFiles/Employees.xlsx]
(ooxml, embedded labels, table is Sheet1);

7. Modify the script so that it now looks like this:

   ```
   [Employees Init]:
   LOAD
       rowno() as Row,
       Date(Date) as Date,
       Hired,
       Terminated,
       If(rowno()=1, Hired-Terminated,  peek([Employee Count], -1)+(Hired-Terminated)) as [Employee Count]
   FROM [lib://DataFiles/Employees.xlsx]
   (ooxml, embedded labels, table is Sheet1);
   ```

The dates in the Date field in the Excel [sheet](#glossary-0 "Glossary term") are in the format MM/DD/YYYY. To ensure dates are interpreted correctly using the format from the system [variables](#glossary-1 "Glossary term") the Date function is applied to the Date field.

The Peek() function lets you identify any value loaded for a defined field. In the expression, we first look to see if the rowno() is equal to 1. If it is equal to 1, no Employee Count will exist, so we populate the field with the difference of Hired minus Terminated.

If the rowno() is greater than 1, we look at last month’s Employee Count and use that number to add to the difference of that month’s Hired minus Terminated employees.

Notice too that in the Peek() function we use a (-1). This tells Qlik Sense to look at the record above the current record. If the (-1) is not specified, Qlik Sense will assume that you want to look at the previous record.

8. Add the following to the end of your script:

```
[Employee Count]:
LOAD
	Row,
	Date,
	Hired,
	Terminated,
	[Employee Count],
	If(rowno()=1,0,[Employee Count]-Previous([Employee Count])) as [Employee Var]
Resident [Employees Init] Order By Row asc;
Drop Table [Employees Init];
```

The Previous() function lets you identify the last value loaded for a defined field. In the expression we first look to see if the rowno() is equal to 1. If it is equal to 1, we know that there will be no Employee Var because there is no record for the previous month’s Employee Count. So we simply enter 0 for the value.

If the rowno() is greater than 1, we know that there will be an Employee Var so we look at last month’s Employee Count and subtract that number from the current month’s Employee Count to create the value in the Employee Var field.

Your script should look like this:

```
[Employees Init]:
LOAD
    rowno() as Row,
    Date(Date) as Date,
    Hired,
    Terminated,
    If(rowno()=1, Hired-Terminated,  peek([Employee Count], -1)+(Hired-Terminated)) as [Employee Count]
FROM [lib://DataFiles/Employees.xlsx]
(ooxml, embedded labels, table is Sheet1);

[Employee Count]:
LOAD
    Row,
    Date,
    Hired,
    Terminated,
    [Employee Count],
    If(rowno()=1,0,[Employee Count]-Previous([Employee Count])) as [Employee Var]
Resident [Employees Init] Order By Row asc;
Drop Table [Employees Init];
```

9. Click Load data.

In a new sheet in the application overview, create a table using Date, Hired, Terminated, Employee Count and Employee Var as the columns of the table. The resulting table should look like this:

Table following use of Peek and Previous in script

![Table following use of Peek and Previous in script.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-peek-previous-table.png "Click to view full size")

Peek() and Previous() allow you to target defined rows within a table. The biggest difference between the two functions is that the Peek() function allows the user to look into a field that was not previously loaded into the script whereas the Previous() function can only look into a previously loaded field. Previous() operates on the input to the LOAD statement, whereas Peek() operates on the output of the LOAD statement. (Same as the difference between RecNo() and RowNo().) This means that the two functions will behave differently if you have a Where-clause.

So the Previous() function would be better when you need to show the current value versus the previous value. In the example we calculated the employee variance from month to month.

The Peek() function would be better when you are targeting a field that has not been previously loaded into the table, or when youo need to target a specific row. This was shown in the example where we calculated the Employee Count by peeking into the previous month’s Employee Count, and then added the difference between the hired and terminated employees for the current month. Remember that Employee Count was not a field in the original file

Information noteTo learn more about when to use Peek() and Previous(), see this blog post in Qlik Community: [Peek() vs Previous() – When to Use Each](https://community.qlik.com/t5/Qlik-Design-Blog/Peek-vs-Previous-When-to-Use-Each/ba-p/1475913).
The behaviors are discussed in the context of QlikView. However, the logic applies equally to Qlik Sense.

## Using Exists()

The Exists() function is often used with the Where clause in the script in order to load data if related data has already been loaded in the data model.

In the following example we also use the Dual() function to assign numeric values to strings.

Do the following:

1. Create a new application and give it a name.
2. Add a new script section in the Data load editor.
3. Call the section People.
4. Enter the following script:

```
//Add dummy people data
PeopleTemp:
LOAD * INLINE [
PersonID, Person
1, Jane
2, Joe
3, Shawn
4, Sue
5, Frank
6, Mike
7, Gloria
8, Mary
9, Steven,
10, Bill
];
 
//Add dummy age data
AgeTemp:
LOAD * INLINE [
PersonID, Age
1, 23
2, 45
3, 43
4, 30
5, 40
6, 32
7, 45
8, 54
9,
10, 61
11, 21
12, 39
];
 
//LOAD new table with people
People:
NoConcatenate LOAD
    PersonID,
    Person
Resident PeopleTemp;
 
Drop Table PeopleTemp;
 
//Add age and age bucket fields to the People table
Left Join (People)
LOAD
    PersonID,
    Age,
	If(IsNull(Age) or Age='', Dual('No age', 5),
	 If(Age<25, Dual('Under 25', 1),
	  If(Age>=25 and Age <35, Dual('25-34', 2),
	   If(Age>=35 and Age<50, Dual('35-49' , 3),
	    If(Age>=50, Dual('50 or over', 4)
	     ))))) as AgeBucket
Resident AgeTemp
Where Exists(PersonID);
 
DROP Table AgeTemp;
```

5. Click Load data.

In the script, the Age and AgeBucket fields are loaded only if the PersonID has already been loaded in the data model.

Notice in the AgeTemp table that there are ages listed for PersonID 11 and 12 but since those IDs were not loaded in the data model (in the People table), they are excluded by the Where Exists(PersonID) clause. This clause can also be written like this: Where Exists(PersonID, PersonID).

The output of the script look like this:

Table following use of Exists in script

![Table following use of Exists in script.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-exists-table.png "Click to view full size")

If none of the PersonIDs in the AgeTemp table had been loaded into the data model, then the Age and AgeBucket fields would not have been joined to the People table. Using the Exists() function can help to prevent orphan records/data in the data model, that is, Age and AgeBucket fields that do not have any associated people.

6. Create a new sheet and give it a name.
7. Open the new sheet and click Edit sheet.
8. Add a standard table to the sheet with the dimension AgeBucket and name the visualization Age Groups.
9. Add a bar chart to the sheet with the dimension AgeBucket, and the measure Count([AgeBucket]). Name the visualization Number of people in each age group.
10. Adjust the properties of the table and bar chart to your preference and then click Done.

    Your sheet should look similar to this:

    Sheet with groupings by age

    ![Sheet with groupings by age.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-exists-chart.png "Click to view full size")

The Dual() function is useful in the script, or in a chart expression, when there is the need to assign a numeric value to a string.

In the script above you have an application that loads ages, and you have decided to put those ages in buckets so that you can create [visualizations](#glossary-2 "Glossary term") based on the age buckets versus the actual ages. There is a bucket for people under 25, between 25 and 35, and so on. By using the Dual() function, the age buckets can be assigned a numeric value that can later be used to sort the age buckets in a list box or in a chart. So, as in the application sheet, the sort puts "No age" at the end of the list.

Information noteTo learn more about Exists() and Dual(), see this blog post in Qlik Community: [Dual & Exists – Useful Functions](https://community.qlik.com/t5/Qlik-Design-Blog/Dual-Exists-Useful-Functions/ba-p/1465290)
