---
source: https://qlik.dev/embed/foundational-knowledge/app-anatomy/data-model-paging/
last_updated: 2026-03-18T16:49:43Z
---

# Paging

Paging is a concept used in Qlik Sense to allow access to selected parts of data
tables.

The number of table rows returned by hypercubes and list objects can in many
case become large, and it will often be impractical to retrieve all cells
of the table in a single call to engine. A typical application of paging would
be to populate a list box in a GUI. The GUI can know up front how many rows it
will be able to display, and scrolling through a list box containing millions of
rows could suffer from performance problems unless a paging strategy is
implemented.

The structure `NxPage` is used to define a page. The structure contains the
properties Top, Left, Height, and Width, which together define a rectangle of
cells within a table. For instance, `NxPage` structures are provided as arguments
to the engine for methods that get data from hypercubes and list objects, and
those methods return data in the form of NxDataPage structures. The `NxDataPage`
structure contains a matrix representing the rows and columns of the data
returned as well as metadata concerning the data that was returned.

The methods provided by the engine (for instance `GenericObject.GetData`) take
lists of pages as arguments, which makes it possible to retrieve multiple pages
in one call. A typical application of this is to get both the first and the
last few rows of a table to make it possible to implement a smooth scrolling
behavior in a component that allows scrolling to wrap around to the top.

Example: Get the second and third row from the table below

NxPage to use: `{ Top = 1, Left = 0, Height = 2, Width = 3 }`

Result

| Year | Month    | Sum(Sales) |
| ---- | -------- | ---------- |
| 2014 | February | 101412     |
| 2014 | March    | 90233      |

Example: Get Month and Sales (but not Year) from the first 5 rows of the table below.

NxPage to use: `{ Top = 0, Left = 1, Height = 5, Width = 2 }`

Result

| Month    | Sum(Sales) |
| -------- | ---------- |
| January  | 101235     |
| February | 101412     |
| March    | 90233      |
| April    | 128923     |
| May      | 154321     |

Example: Get the first 2 and last 2 rows of the table below.

NxPages to use: `[{ Top = 0, Left =0, Height = 2, Width = 3 }, { Top = 14, Left =0, Height = 2, Width = 3 }]`

Result

| Year | Month    | Sum(Sales) |
| ---- | -------- | ---------- |
| 2014 | January  | 101235     |
| 2014 | February | 101412     |

Result

| Year | Month | Sum(Sales) |
| ---- | ----- | ---------- |
| 2015 | March | 112455     |
| 2015 | April | 105567     |

Example: Source data

| Dimensions | Measures  | -          |
| ---------- | --------- | ---------- |
| Year       | Month     | Sum(Sales) |
| 2014       | January   | 101235     |
| 2014       | February  | 101412     |
| 2014       | March     | 90233      |
| 2014       | April     | 128923     |
| 2014       | May       | 154321     |
| 2014       | June      | 112552     |
| 2014       | July      | 192134     |
| 2014       | August    | 90213      |
| 2014       | September | 90576      |
| 2014       | October   | 90227      |
| 2014       | November  | 106311     |
| 2014       | December  | 112394     |
| 2015       | January   | 145621     |
| 2015       | February  | 174566     |
| 2015       | March     | 112455     |
| 2015       | April     | 105567     |

See also:

.Net SDK API: [Paging of data](https://help.qlik.com/en-US/sense-developer/Subsystems/NetSDKAPI/Content/Sense_NetSDKAPI/HowTos/Net-Sdk-How-To-Paging.htm)
on Qlik Help
