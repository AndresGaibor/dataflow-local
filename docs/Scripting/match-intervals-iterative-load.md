---
title: "Matching intervals and iterative loading"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/match-intervals-iterative-load.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Next steps in scripting", "Transforming data"]
---
# Matching intervals and iterative loading

The Intervalmatch prefix to a LOAD or SELECT statement is used to link discrete numeric values to one or more numeric intervals. This is a very powerful feature that can be used, for example, in production environments.

## Using the IntervalMatch() prefix

The most basic interval match is when you have a list of numbers or dates (events) in one table, and a list of intervals in a second table. The goal is to link the two tables. In general, this is a many to many relationship, that is, an interval can have many dates belonging to it and a date can belong to many intervals. To solve this, you need to create a bridge table between the two original tables. There are several ways to do this.

The simplest way to solve this problem in Qlik Sense is to use the IntervalMatch() prefix in front of either a LOAD or a SELECT statement. The LOAD/SELECT statement
needs to contain two fields only, the From and To fields defining the intervals. The
IntervalMatch() prefix will then generate all combinations between the loaded intervals and a previously loaded numeric [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/match-intervals-iterative-load.htm#glossary-0 "Glossary term") specified as parameter to the prefix.

Do the following:

1. Create a new application and give it a name.
2. Add a new script section in the **Data load editor**.
3. Call the sections Events.
4. Under **DataFiles** in the right menu, click **Select data**.
5. Upload and then select Events.txt.
6. In the **Select data from** window, click **Add**.
7. Upload and then select Intervals.txt.
8. In the **Select data from** window, click **Add**.
9. In the script, name the first table Events, and name the second table Intervals.
10. At the end of the script add an IntervalMatch to create a third table that bridges the two first
    tables:

```
BridgeTable:
IntervalMatch (EventDate)
LOAD distinct IntervalBegin, IntervalEnd
Resident Intervals;
```

11. Your script should look like this:

```
Events:
LOAD
    EventID,
    EventDate,
    EventAttribute
FROM [lib://DataFiles/Events.txt] 
(txt, utf8, embedded labels, delimiter is '\t', msq);
 
Intervals:
LOAD
    IntervalID,
    IntervalAttribute,
    IntervalBegin,
    IntervalEnd
FROM [lib://DataFiles/Intervals.txt] 
(txt, utf8, embedded labels, delimiter is '\t', msq);
 
BridgeTable:
IntervalMatch (EventDate)
LOAD distinct IntervalBegin, IntervalEnd
Resident Intervals;
```

12. Click **Load data**.
13. Open the **Data model viewer**. The data model looks like this:

Data model: Events, BridgeTable, Intervals, and $Syn1 tables

![Data model: Events, BridgeTable, Intervals, and $Syn1 tables.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-interval-match-prefix.png)

The data model contains a composite key (the IntervalBegin and IntervalEnd fields) which will manifest itself as a Qlik Sense [synthetic key](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/match-intervals-iterative-load.htm#glossary-1 "Glossary term").

The basic tables are:

- The Events table that contains exactly one record per event.
- The Intervals table that contains exactly one record per interval.
- The bridge table that contains exactly one record per combination of event and interval, and that links the two previous tables.

Note that an event may belong to several intervals if the intervals are overlapping. And an interval can of course have several events belonging to it.

This data model is optimal, in the sense that it is normalized and compact. The Events table and the Intervals table are both unchanged and contain the original number of records. All Qlik Sense calculations operating on these tables, for example, Count(EventID), will work and will be evaluated correctly.

> **Note:** To learn more about IntervalMatch(), see this blog post in Qlik Community: [Using IntervalMatch()](https://community.qlik.com/t5/Qlik-Design-Blog/Using-IntervalMatch/ba-p/1475510)

## Using a While loop and iterative loading IterNo()

You can achieve almost the same bridge table using a While loop and IterNo() that creates enumerable values between the lower and upper bounds of the interval.

A loop inside the LOAD statement can be created using the While clause. For example:

LOAD Date, IterNo() as Iteration From … While IterNo() <= 4;

Such a LOAD statement will loop over each input record and load this over and over as long as the expression in the While clause is true. The IterNo() function returns “1” in the first iteration, “2” in the second, and so on.

You have a primary key for the intervals, the IntervalID, so the only difference in the script will be how the bridge table is created:

Do the following:

1. Replace the existing Bridgetable statements with the following script:

```
BridgeTable:
LOAD distinct * Where Exists(EventDate);
LOAD IntervalBegin + IterNo() - 1 as EventDate, IntervalID
    Resident Intervals
    While IntervalBegin + IterNo() - 1 <= IntervalEnd;
```

2. Click **Load data**.
3. Open the **Data model viewer**. The data model looks like this:

Data model: Events, BridgeTable, and Intervals tables

![Data model: Events, BridgeTable, and Intervals tables.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_Intervalmatch2.png)

Generally, the solution with three tables is the best one, because it allows for a many to many relationship between intervals and events. But a common situation is that you know that an event can only belong to one single interval. In this case, the bridge table is really not necessary. The IntervalID can be stored directly in the event table. There are several ways to achieve this, but the most useful is to join Bridgetable with the Events table.

4. Add the following script to the end of your script:

```
Join (Events)
LOAD EventDate, IntervalID
Resident BridgeTable;
 
Drop Table BridgeTable;
```

5. Click **Load data**.
6. Open the **Data model viewer**. The data model looks like this:

Data model: Events and Intervals tables

![Data model: Events and Intervals tables.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_Intervalmatch3.png)

## Open and closed intervals

Whether an interval is open or closed is determined by the endpoints, whether these are included in the interval or not.

- If the endpoints are included, it is a closed interval:

[a,b] = {x ∈ ℝ ∣ a ≤ x ≤ b}

- If the endpoints are not included, it is an open interval:

]a,b[ = {x ∈ ℝ ∣ a < x < b}

- If one endpoint is included, it is a half-open interval:

[a,b[ = {x ∈ ℝ ∣ a ≤ x < b}

If you have a case where the intervals are overlapping and a number can belong to more than one interval, you usually need to use closed intervals.

However, in some cases you do not want overlapping intervals, you want a number to belong to one interval only. Hence, you will get a problem if one point is the end of one interval and, at the same time, the beginning of next. A number with this value will be attributed to both intervals. Hence, you want half-open intervals.

A practical solution to this problem is to subtract a very small amount from the end value of all intervals, thus creating closed, but non-overlapping intervals. If your numbers are dates, the simplest way to do this is to use the function DayEnd() which returns the last millisecond of the day:

Intervals:
LOAD…, DayEnd(IntervalEnd – 1) as IntervalEnd From Intervals;

You can also subtract a small amount manually. If you do, make sure the subtracted amount isn’t too small since the operation will be rounded to 52 significant binary digits (14 decimal digits). If you use too small of an amount, the difference will not be significant and you will be back using the original number.
