---
title: "Hash160 Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Hash160.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# Hash160 Script and chart function

Hash160() returns
a 160-bit hash value of the combined input expression values. The result is a 27-character string. Hash values are useful for masking personal identifiable information (PII), such as customer names, social security numbers, or account numbers.

Syntax:

Hash160(expr{, expression})

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| expr | The string to evaluate. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| `Hash160( 'abc', 'xyz', '123' )` | Returns `` MA&5]6+3=:>;>G%S<U*S2I:`=X* `` |
| `Hash160( Region, Year, Month )`  Note: `Region`, `Year`, and `Month` are table fields. | Returns `G7*=6GKPJ(Z+)^KM?<$'AI.)?U$` |

## Example - Hash160 fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields which will be used to create a 160-bit hash value:

  - `Region`
  - `Year`
  - `Month`

Load script

```
Example:
Load *
inline [
Region, Year, Month
abc, xyz, 123
EU, 2022, 01
UK, 2022, 02
US, 2022, 02
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `Region`
- `Year`
- `Month`

Create the following calculated dimension:

- `=Hash160(Region, Year, Month)`, to calculate the 160-bit hash value.

Results table

| Region | Year | Month | Hash160(Region, Year, Month) |
| --- | --- | --- | --- |
| abc | xyz | 123 | MA&5]6+3=:>;>G%S<U\*S2I:`=X\* |
| EU | 2022 | 01 | B40^K&[T@!;VB'XR]<5=//\_F853 |
| UK | 2022 | 02 | O5T;+1?[B&"F&1//MA[MN!T"FWZ |
| US | 2022 | 02 | C6@#]4#\_G-(]J7EQY#KRW`@KF+W |

For each row, the hash strings for `Region`, `Year`, and `Month` are joined together, and a 27-character string is returned.

Load script

The following code shows how to use the function in a load script.

```
Hash_160:
Load *,
Hash160(Region, Year, Month) as Hash160_Region_Year_Month;
Load * inline [
Region, Year, Month
abc, xyz, 123
EU, 2022, 01
UK, 2022, 02
US, 2022, 02 ];
```

Results table

| Region | Year | Month | Hash160\_Region\_Year\_Month |
| --- | --- | --- | --- |
| abc | xyz | 123 | MA&5]6+3=:>;>G%S<U\*S2I:`=X\* |
| EU | 2022 | 01 | B40^K&[T@!;VB'XR]<5=//\_F853 |
| UK | 2022 | 02 | O5T;+1?[B&"F&1//MA[MN!T"FWZ |
| US | 2022 | 02 | C6@#]4#\_G-(]J7EQY#KRW`@KF+W |

## Example - Hash160 scenario with duplicate entries

Chart expression

Overview

This example creates a unique hash value for each product entry. The hash value serves as a unique identifier, allowing the company to detect and manage duplicates effectively.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `TransactionID`
  - `ProductID`
  - `ProductName`
  - `SupplierID`

Load script

```
Example:
Load *
inline [
TransactionID, ProductID, ProductName, SupplierID
1, 101, Widget A, S001
2, 102, Widget B, S002
3, 101, Widget A, S001
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `TransactionID`
- `ProductID`
- `ProductName`
- `SupplierID`

Create the following calculated dimension:

- ​`=Hash160(ProductID, ProductName, SupplierID)`, to calculate a 27-character key.

Results table

| TransactionID | ProductID | ProductName | SupplierID | Hash160(ProductID, ProductName, SupplierID) |
| --- | --- | --- | --- | --- |
| 1 | 101 | ​Widget A ​ ​ | S001 | ​CY`&^(N,E/#`TJT4&]/7N1Q+\*T3 |
| 2 | 102 | Widget B | S002 | O7(1;V1%MG;Z+A[/H)G5&`6RA0( |
| 3 | 101 | Widget A | S001 | ​CY`&^(N,E/#`TJT4&]/7N1Q+\*T3 |

Compare the output of the `Hash160` function. Notice that the first and third `TransactionID` records have duplicate hash values because the combination of the `ProductID`, `ProductName`, and `SupplierID` strings are the same for these rows.

## Example - Hash160 scenario to anonymize data

Chart expression

Overview

A financial services company handles sensitive customer information, such as credit card numbers, social security numbers, and customer names. To protect privacy and ensure compliance with regulations such as General Data Protection Regulation (GDPR) or Health Insurance Portability and Accountability Act (HIPAA), they need to anonymize sensitive data when generating reports for analysis. However, they also need to maintain consistency, so that they can track the same customer across different datasets without revealing the customer's identity.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `CustomerID`
  - `CustomerName`
  - `SSN`

Load script

```
Example:
Load *
inline [
CustomerID, CustomerName, SSN
101, John Doe, 123-45-6789|
102, Jane Smith, 987-65-4321
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `CustomerID`
- `CustomerName`
- `SSN`

Create the following calculated dimensions:

- `=Hash160(CustomerName)`
- `=Hash160(SSN)`

Results table

| CustomerID | CustomerName | SSN | Hash160(CustomerName) | Hash160(SSN) |
| --- | --- | --- | --- | --- |
| 101 | ​John Doe | ​123-45-6789| | ​GMD(\*B9\*!PQ&MTY2@$4A\KCL?[0 | ​N&[PSH:I$M?OF<5/9LV&N\*;`CZ(​ |
| 102 | Jane Smith | ​987-65-4321 | ​EP@9]GSI)5G\I\*,B?H,C?A$%VG: | ​HCFXMR'2=\3WF6?\_\6LN;.\*6:K?​ |

The output generates unique keys which have the following benefits:

- Data Privacy: The original sensitive data is not directly visible, but the hash value remains consistent across different records. This allows for analysis, such as aggregating customer activity, without exposing the actual identity of the customer.
- Compliance: By hashing sensitive fields, the company ensures compliance with data privacy regulations.
- Security: The hash function produces a fixed-size output that is not reversible, adding an extra layer of protection for sensitive data.
