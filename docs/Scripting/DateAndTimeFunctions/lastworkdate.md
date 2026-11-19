---
title: "lastworkdate Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lastworkdate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# lastworkdate Script and chart function

The lastworkdate function returns
the earliest ending date to achieve no\_of\_workdays
(Monday-Friday) if starting at start\_date
taking into account any optionally listed holiday.
start\_date and holiday
should be valid dates or timestamps.

Syntax:

lastworkdate(start\_date, no\_of\_workdays {, holiday})

Return data type:  integer

A calendar that shows how the `lastworkdate()` function is used

![Diagram that shows a calendar of a month. The start date of work is set on the 10th of the month and the end date of work is set on the 26th. The days inbetween the start and end date, excluding Saturdays and Sundays, are highlighted in green.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lastworkdate-diagram1.png)

Limitations

There is no method to modify the `lastworkdate()` function for regions or scenarios that involve anything other than a work week that begins on Monday and ends on Friday.

The holiday parameter must be a string constant. It does not accept an expression.

When to use lastworkdate

The `lastworkdate()` function is commonly used as part of an expression when the user would like to calculate the proposed end date of a project or assignment, based on when the project begins and the holidays that will occur in that period.

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

Arguments

| Argument | Description |
| --- | --- |
| start\_date | The start date to evaluate. |
| no\_of\_workdays | The number of working days to achieve. |
| holiday | Holiday periods to exclude from working days. A holiday is stated as a string constant date. You can specify multiple holiday dates, separated by commas.  Example:  `'12/25/2013', '12/26/2013', '12/31/2013', '01/01/2014'` |

## Example 1 - Basic example

Load script and results 

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lastworkdate.htm#glossary-0 "Glossary term") containing project IDs, project start dates, and the estimated effort, in days, required for the projects. The dataset is loaded into a table called ‘`Projects`’.
- A [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lastworkdate.htm#glossary-1 "Glossary term") which contains the `lastworkdate()` function which is set as the [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lastworkdate.htm#glossary-2 "Glossary term") ‘`end_date`’ and identifies when each project is scheduled to end.

Load script

```
SET DateFormat='MM/DD/YYYY'; 

Projects: 
    Load 
       *, 
       LastWorkDate(start_date,effort) as end_date 
       ; 
Load 
id, 
start_date, 
effort 
Inline  
[	 
id,start_date,effort 
1,01/01/2022,14 
2,02/10/2022,17 
3,05/17/2022,5 
4,06/01/2022,12 
5,08/10/2022,26 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- start\_date
- effort
- end\_date

Results table

| id | start\_date | effort | end\_date |
| --- | --- | --- | --- |
| 1 | 01/01/2022 | 14 | 01/20/2022 |
| 2 | 02/10/2022 | 17 | 03/04/2022 |
| 3 | 05/17/2022 | 5 | 05/23/2022 |
| 4 | 06/01/2022 | 12 | 06/16/2022 |
| 5 | 08/10/2022 | 26 | 09/14/2022 |

Because there are no scheduled holidays, the function adds the defined number of working days, Monday to Friday, to the start date to find the earliest possible end date.

The following calendar shows the start and end date for project 3, with the working days highlighted in green.

A calendar that shows the start and end date of project 3

![Diagram that shows the start date of project 3 as May 17 and the last work date as May 23, for a total of five working days.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lastworkdate-example1-diagram.png)

## Example 2 - Single holiday

Load script and results 

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing project IDs, project start dates, and the estimated effort, in days, required for the projects. The dataset is loaded into a table called ‘`Projects`’.
- A preceding load which contains the `lastworkdate()` function which is set as the field ‘`end_date`’ and identifies when each project is scheduled to end.

However, there is one holiday scheduled on May 18, 2022. The `lastworkdate()` function in the preceding load includes the holiday in its third argument to identify when each project is scheduled to end.

Load script

```
SET DateFormat='MM/DD/YYYY'; 

Projects: 
    Load 
       *, 
       LastWorkDate(start_date,effort, '05/18/2022') as end_date 
       ; 
Load 
id, 
start_date, 
effort 
Inline  
[	 
id,start_date,effort 
1,01/01/2022,14 
2,02/10/2022,17 
3,05/17/2022,5 
4,06/01/2022,12 
5,08/10/2022,26 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- start\_date
- effort
- end\_date

Results table

| id | start\_date | effort | end\_date |
| --- | --- | --- | --- |
| 1 | 01/01/2022 | 14 | 01/20/2022 |
| 2 | 02/10/2022 | 17 | 03/04/2022 |
| 3 | 05/17/2022 | 5 | 05/24/2022 |
| 4 | 06/01/2022 | 12 | 06/16/2022 |
| 5 | 08/10/2022 | 26 | 09/14/2022 |

The single scheduled holiday is entered as the third argument in the `lastworkdate()` function. As a result, the end date for project 3 is shifted one day later because the holiday takes place on one of the working days before the end date.

The following calendar shows the start and end date for project 3 and shows that the holiday changes the end date of the project by one day.

A calendar that shows the start and end date of project 3 with a holiday on May 18

![Diagram that shows the start date of project 3 as May 17 with a holiday on May 18. The last work date of the project moves to May 24.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lastworkdate-example2-diagram.png)

## Example 3 - Multiple holidays

Load script and results 

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing project IDs, project start dates, and the estimated effort, in days, required for the projects. The dataset is loaded into a table called ‘`Projects`’.
- A preceding load which contains the `lastworkdate()` function which is set as the field ‘`end_date`’ and identifies when each project is scheduled to end.

However, there are three holidays scheduled for May 19, 20, 21, and 22. The `lastworkdate()` function in the preceding load includes each of the holidays in its third argument to identify when each project is scheduled to end.

Load script

```
SET DateFormat='MM/DD/YYYY'; 

Projects: 
    Load 
       *, 
       LastWorkDate(start_date,effort, '05/19/2022','05/20/2022','05/21/2022','05/22/2022') as end_date 
       ; 
Load 
id, 
start_date, 
effort 
Inline  
[	 
id,start_date,effort 
1,01/01/2022,14 
2,02/10/2022,17 
3,05/17/2022,5 
4,06/01/2022,12 
5,08/10/2022,26 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- start\_date
- effort
- end\_date

Results table

| id | start\_date | effort | end\_date |
| --- | --- | --- | --- |
| 1 | 01/01/2022 | 14 | 01/20/2022 |
| 2 | 02/10/2022 | 17 | 03/04/2022 |
| 3 | 05/17/2022 | 5 | 05/25/2022 |
| 4 | 06/01/2022 | 12 | 06/16/2022 |
| 5 | 08/10/2022 | 26 | 09/14/2022 |

The four holidays are entered as a list of arguments in the `lastworkdate()` function after the start date and number of working days.

The following calendar shows the start and end date for project 3 and shows that the holidays change the end date of the project by three days.

A calendar that shows the start and end date of project 3 with holidays from May 19 to 22

![Diagram that shows the start date of project 3 as May 17 and the last work date as May 25, with four extra holidays moving the last work date back by three days - with two of the holidays falling on Saturday and Sunday.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lastworkdate-example3-diagram.png)

## Example 4 - Single holiday (chart)

Load script and chart expression

Overview

The same dataset and scenario as the first example are used.

However, in this example, the dataset is unchanged and loaded into the application. The `end_date` field is calculated as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lastworkdate.htm#glossary-4 "Glossary term") in a chart.

Load script

```
SET DateFormat='MM/DD/YYYY'; 

Projects: 
Load 
id, 
start_date, 
effort 
Inline  
[	 
id,start_date,effort 
1,01/01/2022,14 
2,02/10/2022,17 
3,05/17/2022,5 
4,06/01/2022,12 
5,08/10/2022,26 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- start\_date
- effort

To calculate the end\_date, create the following measure:

- `=LastWorkDate(start_date,effort,'05/18/2022')`

Results table

| id | start\_date | effort | =LastWorkDate(start\_date,effort,'05/18/2022') |
| --- | --- | --- | --- |
| 1 | 01/01/2022 | 14 | 01/20/2022 |
| 2 | 02/10/2022 | 17 | 03/04/2022 |
| 3 | 05/17/2022 | 5 | 05/23/2022 |
| 4 | 06/01/2022 | 12 | 06/16/2022 |
| 5 | 08/10/2022 | 26 | 09/14/2022 |

The single scheduled holiday is entered as a measure in the chart. As a result, the end date for project 3 is shifted one day later because the holiday takes place on one of the working days before the end date.

The following calendar shows the start and end date for project 3 and shows that the holiday changes the end date of the project by one day.

A calendar that shows the start and end date of project 3 with a holiday on May 18

![Diagram that shows the start date of project 3 as May 17 with a holiday on May 18. The last work date of the project moves to May 24.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lastworkdate-example2-diagram.png)
