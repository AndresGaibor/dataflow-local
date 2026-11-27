---
title: "Math functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/math-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations", "Working with formulas"]
---

# Math functions

With the available math functions in Qlik Automate, you can apply mathematical operations to data.

## Add

Do addition.

`{$.inputs.salesCanada}` = 1000000

`{$.inputs2.salesUSA}` = 2000000

`{add: {$.inputs.salesCanada}, $.inputs2.salesUSA}` = 3000000

## Subtract

Do subtraction.

`{$.inputs.salesCanada}` = 1000000

`{$.inputs2.salesUSA}` = 2000000

`{subtract: {$.inputs2.salesUSA}, $.inputs.salesCanada}` = 1000000

## Multiply

Do multiplication.

`{$.inputs.annualSales}` = 100000

`{$.inputs2.months}` = 12

`{multiply: {$.inputs.sales}, $.inputs2.months}` = 14000

## Divide

Do division.

`{$.inputs.sales}` = 1500000

`{$.inputs2.months}` = 12

`{divide: {$.inputs.avgSalesDay}, $.inputs2.days}` = 125000

## Round

Returns the rounded number of a decimal number. The default rounding removes all decimals. Optionally add a parameter to specify the rounding places.

`{$.inputs.USDEUR}` = 0.8416

`{round: {$.inputs.USDEUR}}` = 1

`{round: {$.inputs.USDEUR}, 2}` = 0.84

## Max

Returns the maximum value from a list.

`{$.list[*].id}` = ["1","2","7","10"]

`{max:{$.list[*].id}}` = 10

## Min

Returns the minimum value from a list.

`{$.list[*].id}` = ["1","2","7","10"]

`{min:{$.list[*].id}}` = 1

## Modulo

Returns the remainder of a division.

`{$.inputs.num1}` = 25

`{$.inputs.num2}` = 4

`{mod: {$.inputs.num}, $.inputs2.num2}` = 1

## Random number

Generates a random number (integer). A parameter is required to specify the number of digits.

`{randomnumber:2}` = 14

## Mod 10

Calculates a check digit according to Mod 10.

`{modtendigit:25}` = 7

## Mod 11

Calculates a check digit according to Mod 11.

`{modelevendigit:25}` = 6
