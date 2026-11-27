---
title: "Bit operators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Operators/BitOperators.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Operators"]
---

# Bit operators

All bit operators convert (truncate) the operands to signed integers (32 bit) and
return the result in the same way. All operations are performed bit by
bit. If an operand cannot be interpreted as a number, the operation will return NULL.

Bit operators

| Operator | Full name | Description |
| --- | --- | --- |
| bitnot | Bit inverse. | Unary operator. The operation returns the logical inverse of the operand performed bit by bit.  Example:  bitnot 17 returns -18 |
| bitand | Bit and. | The operation returns the logical AND of the operands performed bit by bit.  Example:  17 bitand 7 returns 1 |
| bitor | Bit or. | The operation returns the logical OR of the operands performed bit by bit.  Example:  17 bitor 7 returns 23 |
| bitxor | Bit exclusive or. | The operation returns the logical exclusive or of the operands performed bit by bit.  Example:  17 bitxor 7 returns 22 |
| >> | Bit right shift. | The operation returns the first operand shifted to the right. The number of steps is defined in the second operand.  Example:  8 >> 2 returns 2 |
| << | Bit left shift. | The operation returns the first operand shifted to the left. The number of steps is defined in the second operand.  Example:  8 << 2 returns 32 |
