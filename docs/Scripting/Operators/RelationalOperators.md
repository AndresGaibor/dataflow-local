---
title: "Relational operators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Operators/RelationalOperators.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Operators"]
---
# Relational operators

All relational operators compare the values of the operands and return
True (-1) or False (0) as the result. All relational operators are binary.

Relational operators

| Operator | Description |
| --- | --- |
| < | Less than. A numeric comparison is made if both operands can be interpreted numerically. The operation returns the logical value of the evaluation of the comparison. |
| <= | Less than or equal. A numeric comparison is made if both operands can be interpreted numerically. The operation returns the logical value of the evaluation of the comparison. |
| > | Greater than. A numeric comparison is made if both operands can be interpreted numerically. The operation returns the logical value of the evaluation of the comparison. |
| >= | Greater than or equal. A numeric comparison is made if both operands can be interpreted numerically. The operation returns the logical value of the evaluation of the comparison. |
| = | Equals. A numeric comparison is made if both operands can be interpreted numerically. The operation returns the logical value of the evaluation of the comparison. |
| <> | Not equivalent to. A numeric comparison is made if both operands can be interpreted numerically. The operation returns the logical value of the evaluation of the comparison. |
| precedes | Unlike the < operator no attempt is made to make a numeric interpretation of the argument values before the comparison. The operation returns true if the value to the left of the operator has a text representation which, in string comparison, comes before the text representation of the value on the right. Example:  `'1 ' precedes ' 2'`  returns FALSE  `' 1' precedes ' 2'` returns TRUE  as the ASCII value of a space (' ') is of less value than the ASCII value of a number.  Compare this to:  `'1 ' < ' 2'` returns TRUE  `' 1' < ' 2'` returns TRUE |
| follows | Unlike the > operator no attempt is made to make a numeric interpretation of the argument values before the comparison. The operation returns true if the value to the left of the operator has a text representation which, in string comparison, comes after the text representation of the value on the right. Example:  `' 2' follows '1` ' returns FALSE  ' 2' follows ' 1' returns TRUE  as the ASCII value of a space (' ') is of less value than the ASCII value of a number.  Compare this to:  `' 2' > ' 1'` returns TRUE  `' 2' > '1 '` returns TRUE |
