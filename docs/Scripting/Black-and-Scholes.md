---
title: "BlackAndSchole Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Black-and-Scholes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Financial functions"]
---

# BlackAndSchole Script and chart function

The Black and Scholes model is a mathematical model for financial market derivative instruments. The formula calculates the theoretical value of an
option. In Qlik Sense, the BlackAndSchole
function returns the value according to the Black and Scholes unmodified formula (European style options).

BlackAndSchole(strike
,
time\_left , underlying\_price
,
vol , risk\_free\_rate
,
type)

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| strike | The future purchase price of the stock. |
| time\_left | The number of time periods remaining. |
| underlying\_price | The current value of the stock. |
| vol | Volatility (of the stock price) expressed as a percentage in decimal form, per time period. |
| risk\_free\_rate | The risk-free rate expressed as a percentage in decimal form, per time period. |
| call\_or\_put | The type of option:  'c', 'call' or any non-zero numeric value for call options  'p', 'put' or 0 for put options. |

Limitations:

The value of strike, time\_left, and underlying\_price must be >0.

The value of vol and risk\_free\_rate must be: <0 or >0.

Examples and results:

Scripting examples

| Example | Result |
| --- | --- |
| BlackAndSchole(130, 4, 68.5, 0.4, 0.04, 'call')  This calculates the theoretical price of an option to buy a share that is worth 68.5 today, at a value of 130 in 4 years. The formula uses a volatility of 0.4 (40%) per year and a risk-free interest rate of 0.04 ( 4%). | Returns 11.245 |
