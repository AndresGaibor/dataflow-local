---
title: "Creating a date interval from a single date"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/create-date-interval-from-single-date.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Best practices for data modeling"]
---
# Creating a date interval from a single date

Sometimes time intervals are not stored explicitly with a beginning and an end. Instead they are implied by only one field – the change timestamp.

It could be as in the table below where you have currency rates for multiple currencies. Each currency rate change is on its own row; each with a new conversion rate. Also, the table contains rows with empty dates corresponding to the initial conversion rate, before the first change was made.

Currency rates

| Currency | Change Date | Rate |
| --- | --- | --- |
| EUR | - | 8.59 |
| EUR | 28/01/2013 | 8.69 |
| EUR | 15/02/2013 | 8.45 |
| USD | - | 6.50 |
| USD | 10/01/2013 | 6.56 |
| USD | 03/02/2013 | 6.30 |

The table above defines a set of non-overlapping intervals, where the begin data is called Change Date and the end date is defined by the beginning of the following interval. But since the end date isn’t explicitly stored in a column of its own, we need to create such a column, so that the new table will become a list of intervals.

Do the following:

1. Create a new application and give it a name.
2. Add a new script section in the **Data load editor**.
3. Add the following inline table. Make sure that the dates in the Change Date column are in the same format as the local date format.

```
In_Rates:
LOAD * Inline [
Currency,Change Date,Rate
EUR,,8.59
EUR,28/01/2013,8.69
EUR,15/02/2013,8.45
USD,,6.50
USD,10/01/2013,6.56
USD,03/02/2013,6.30
];
```

4. Determine which time range you want to work with. The beginning of the range must be before the first date in the data and the end of the range must be after the last.

   Add the following to the top of your script:

   ```
   Let vBeginTime = Num('1/1/2013');
   Let vEndTime = Num('1/3/2013');
   Let vEpsilon = Pow(2,-27);
   ```
5. Load the source data, but change empty dates to the beginning of the range defined in the previous bullet. The change date should be loaded as "From Date".

   Sort the table first according to Currency, then according to the "From Date" descending so that you have the latest dates on top.

   Add the following after the In\_Rates table:

   ```
   Tmp_Rates:
   LOAD Currency, Rate,
       Date(If(IsNum([Change Date]), [Change Date], $(#vBeginTime))) as FromDate
   Resident In_Rates;
   ```
6. Run a second pass through data where you calculate the "To Date". If the current record has a different currency from the previous record, then it is the first record of a new currency (but its last interval), so you should use the end of the range defined in step 1. If it is the same Currency, you should take the "From Date" from the previous record, subtract a small amount of time, and use this value as "To Date" in the current record.

   Add the following after the Tmp\_Rates table:

   ```
   Rates:
   LOAD Currency, Rate, FromDate,
       Date(If( Currency=Peek('Currency'),
           Peek('FromDate') - $(#vEpsilon),
           $(#vEndTime)
           )) as ToDate
       Resident Tmp_Rates
       Order By Currency, FromDate Desc;
   					
   Drop Table Tmp_Rates;
   ```

Your script should look like this:

```
Let vBeginTime = Num('1/1/2013');
Let vEndTime = Num('1/3/2013');
Let vEpsilon = Pow(2,-27);

In_Rates:
LOAD * Inline [
Currency,Change Date,Rate
EUR,,8.59
EUR,28/01/2013,8.69
EUR,15/02/2013,8.45
USD,,6.50
USD,10/01/2013,6.56
USD,03/02/2013,6.30
];  

Tmp_Rates:
LOAD Currency, Rate,	
    Date(If(IsNum([Change Date]), [Change Date], $(#vBeginTime))) as FromDate
Resident In_Rates; 

Rates:
LOAD Currency, Rate, FromDate,	
    Date(If( Currency=Peek('Currency'),
        Peek('FromDate') - $(#vEpsilon),
        $(#vEndTime)		
        )) as ToDate	
    Resident Tmp_Rates
Order By Currency, FromDate Desc; 

Drop Table Tmp_Rates;
```

The script will update the source table in the following manner:

Updated source table

| Currency | Rate | FromDate | ToDate |
| --- | --- | --- | --- |
| EUR | 8.45 | 15/02/2013 | vEndTime |
| EUR | 8.69 | 28/01/2013 | 14/02/2013 23:59:59 |
| EUR | 8.59 | vBeginTime | 28/01/2013 23:59:99 |
| USD | 6.30 | 03/02/2013 | vEndTime |
| USD | 6.56 | 10/01/2013 | 2/02/2013 23:59:59 |
| USD | 6.50 | vBeginTime | 9/01/2013 23:59:59 |

In your application, the table appears as follows:

Preview of data

| Currency | Rate | FromDate | ToDate |
| --- | --- | --- | --- |
| EUR | 8.45 | 15/02/2013 | 01/03/2013 |
| EUR | 8.69 | 28/01/2013 | 14/02/2013 |
| EUR | 8.59 | 01/01/2013 | 28/01/2013 |
| USD | 6.30 | 03/02/2013 | 01/03/2013 |
| USD | 6.56 | 10/01/2013 | 2/02/2013 |
| USD | 6.50 | 01/01/2013 | 9/01/2013 |

This table can subsequently be used in a comparison with an existing date using the Intervalmatch method.

## Learn more

- [*Matching intervals to discrete data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/matching-intervals-to-discrete-data.htm)
