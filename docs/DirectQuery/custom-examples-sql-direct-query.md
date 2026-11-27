---
title: "Custom SQL examples for Direct Query"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DirectQuery/custom-examples-sql-direct-query.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Accessing cloud databases directly with Direct Query", "Creating a Direct Query application with custom SQL"]
---

# Custom SQL examples for Direct Query

The following examples show some of the options when using custom SQL for Direct Query.

## Example: Adding custom SQL definitions to the Direct Query model

In this example, custom SQL definitions for tables C, R, N are added to the data model in the Direct Query application along with two inter-table relationships. The use of the Coalesce function is used to check if a field value of N\_NATIONKEY is equal to the value of C\_NATIONKEY, or if both are equal to null.

Tip note

Coalesce is the recommended way to include a check to see if a field value is equal to null. For more information, see [*coalesce Script and chart function*](../Scripting/ConditionalFunctions/coalesce.htm).

LIB CONNECT TO 'CustomSQL:Snowflake\_example.com';
Section DirectQuery;
C:
Select C\_NATIONKEY, Sum(C\_ACCTBAL) as C\_SUM from tpch1.customer group by C\_NATIONKEY;
R:
SELECT R\_REGIONKEY, R\_NAME from tpch1.region;
N:
SELECT N\_REGIONKEY, N\_NAME, N\_NATIONKEY from tpch1.nation;
Create Relationship Between R, N Matching R\_REGIONKEY With N\_REGIONKEY;
Create Relationship
Between Outer Joined N, Inner Joined C On
(coalesce([N\_NATIONKEY], -1) = coalesce([C\_NATIONKEY], -1));

## Example: Adding tables with custom SQL to a data model made with Data model manager

In this example, the Direct Query data model is first constructed with the contents in the DirectQueryModel.main object, which was created with Data model manager. Then an additional table, C with the fields C\_CUSTKEY and C\_ACCTBAL, are added to the data model. A relationship is made between the field O\_CUSTKEY in ORDERS with the field C\_CUSTKEY in C.

LIB CONNECT TO 'CustomSQL:Snowflake\_example.com';
// DMM created model portion includes Orders table.
IMPORT LIVE 'ModelName@obj://DirectQueryModel.Main';
Section DirectQuery;
C: Select C\_CUSTKEY, C\_ACCTBAL from tpch1.customer;
Create Relationship Between ORDERS, C on (O\_CUSTKEY = C\_CUSTKEY);

## Example: Constructing a Direct Query data model with a custom SQL table

In this example, the Direct Query data model is constructed with a custom SQL table, C, with the renamed fields C\_KEY and C\_BAL. Next, IMPORT LIVE adds the data model created in Data model manager from DirectQueryModel.main. This data model contains the table Orders and has an existing relationship between Orders and Customer in that model. Then, the existing relationship between Customers and Orders is dropped and a new relationship is defined between Orders and C.

LIB CONNECT TO 'CustomSQL:Snowflake\_example.com';
Section DirectQuery;
C: Select C\_CUSTKEY as C\_KEY, C\_ACCTBAL as C\_BAL from tpch1.customer;
// DMM created model portion includes Orders table.
IMPORT LIVE 'ModelName@obj://DirectQueryModel.Main';
// This relationship was defined using DMM between ORDERS and CUSTOMER, but I want to define my own.
Drop Relationship Between ORDERS, CUSTOMER;
Create Relationship Between ORDERS, C on (O\_CUSTKEY = C\_KEY);

## Example: Constructing a data model including variables

In this example, the variable MULT is defined first with a value of 100. Then, it is applied as a multiplier to the sum of PS\_Supplycost to calculate the field S.

LIB CONNECT TO 'CustomSQL:Snowflake\_example.com';
Section DirectQuery;
LET MULT=100;
T1: SELECT PS\_AVAILQTY AS C, SUM(PS\_SUPPLYCOST) \* $(MULT) AS S FROM "TPCH.01"."PARTSUPP" GROUP BY C;

## Example: Constructing a data model with Qlik expressions

In this example, both variables and expressions are used to build the data model. In the table ORDERS\_AGGREGATIONS, expressions are used to define the values in ORDERS\_GROUP\_TOTAL\_PRICE. Whenever selections are made in a sheet that would impact the values in ORDERS\_GROUP\_TOTAL\_PRICE, the expression will be re-evaluated on the data returned by the query to the database.

IMPORT LIVE 'ModelName@obj://DirectQueryModel.Main';
section DirectQuery;
let Aggr1 = 1;
let Aggr2 = 0;
[GROUPS]:
SELECT 0 as GROUP\_CODE, 'NONE' as "GROUP"
UNION ALL
SELECT 1 as GROUP\_CODE, 'ORDERSTATUS' as "GROUP"
UNION ALL
SELECT 2 as GROUP\_CODE, 'ORDERPRIORITY' as "GROUP"
;
[ORDERS\_AGGREGATIONS]:
SELECT 'BY ORDERSTATUS' as "GROUP\_NAME",
"O\_ORDERSTATUS" as "ORDERS\_GROUP",
sum("O\_TOTALPRICE") as "ORDERS\_GROUP\_TOTAL\_PRICE"
FROM "TEST1"."TPCH.01"."ORDERS"
WHERE '$(=min({<GROUP\_CODE={0,1}>}[GROUP\_CODE]))' = '1'
GROUP BY 1,2
UNION ALL
SELECT 'BY ORDERPRIORITY' as "GROUP\_NAME",
"O\_ORDERPRIORITY" as "ORDERS\_GROUP",
sum("O\_TOTALPRICE") as "ORDERS\_GROUP\_TOTAL\_PRICE"
FROM "TEST1"."TPCH.01"."ORDERS"
WHERE '$(=min({<GROUP\_CODE={0,2}>}[GROUP\_CODE]))' = '2'
GROUP BY 1,2;
;
[ORDERS\_AGGREGATIONS\_VARS]:
SELECT 'BY ORDERSTATUS' as "GROUP\_NAME\_V",
"O\_ORDERSTATUS" as "ORDERS\_GROUP\_V",
sum("O\_TOTALPRICE") as "ORDERS\_GROUP\_TOTAL\_PRICE\_V"
FROM "TEST1"."TPCH.01"."ORDERS"
WHERE $(=Aggr1) = 1
GROUP BY 1,2
UNION ALL
SELECT 'BY ORDERPRIORITY' as "GROUP\_NAME\_V",
"O\_ORDERPRIORITY" as "ORDERS\_GROUP\_V",
sum("O\_TOTALPRICE") as "ORDERS\_GROUP\_TOTAL\_PRICE\_V"
FROM "TEST1"."TPCH.01"."ORDERS"
WHERE $(=Aggr2) = 1
GROUP BY 1,2;
;

## Example: Using functions in custom SQL expressions

The following custom SQL statement demonstrates a simple use of a $(=…) Engine expression that is expanded when executed in the custom SQL. This expression retrieves remote database rows depending on the application session's user information. When a chart, query, or selection is performed by a Direct Query application session user with email address 'user1@qlik.com' then the dynamic retrieval of data rows from the remote SQL database is filtered to match only the rows where the C\_NAME field contains the value 'Customer#000000007'. Otherwise, if the Direct Query application's session user's email is not 'user1@qlik.com', only the rows where the C\_NAME field contains the value 'Customer#000000009' will be retrieved and shown.

T8: SELECT \* FROM mydb.tpch01.customer WHERE mydb.tpch01.customer.C\_NAME = '$(=if(GetUserAttr('userEmail') = 'user1@qlik.com', 'Customer#000000007','Customer#000000009'))';
