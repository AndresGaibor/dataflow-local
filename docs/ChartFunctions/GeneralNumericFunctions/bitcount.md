---
title: "BitCount Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/bitcount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "General numeric functions"]
---

# BitCount Script and chart function

BitCount() returns how many bits in the binary equivalent of a decimal number are set to 1. That is, the function returns the number of set bits in integer\_number, where integer\_number is interpreted as a signed
32-bit integer.

Syntax:

BitCount(integer\_number)

Return data type:  integer

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| BitCount ( 3 ) | 3 is binary 11, therefore this returns 2 |
| BitCount ( -1 ) | -1 is 64 ones in binary, therefore this returns 64 |
