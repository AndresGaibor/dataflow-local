---
title: "Dollar-sign expansion using parameters"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/dollar-sign-expansion-using-parameters.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures", "Dollar-sign expansions"]
---

# Dollar-sign expansion using parameters

Parameters can be used in dollar-sign expansions. This makes it possible to have a dynamic evaluation of the [variable](#glossary-0 "Glossary term").

The variable created for use in the expansion must contain formal parameters. A formal parameter is a placeholder for the input to the evaluation and is written with a dollar sign: $1, $2, $3. The number indicates the parameter number.

When using the variable, the actual parameters should be stated in a comma separated list.

## Examples: Parameters in dollar-sign expansions

If you want to define a multiplication between two numbers, you can write:

```
Set MUL= $1*$2 ;
```

This defines that $1 and $2 should be multiplied with each other. When used, this variable must be dollar expanded with values for $1 and $2 inserted into the expression:

```
Set X= $( MUL(3,7) ) ;
```

The values (3 and 7) are the actual parameters that replace $1 and $2 in the expansion. The expansion is made before the Set statement is parsed and executed, which means that the script parser sees the following:

```
Set X= 3*7 ;
```

As a result, the variable X will be assigned the string value: 3\*7.

If you use a Let instead of Set statement:

```
Let X= $( MUL(3,7) ) ;
```

The parser will see the following:

```
Let X= 3*7 ;
```

Here an evaluation will be made, and X will be assigned the numeric value 21.

## Number of parameters

If the number of formal parameters exceeds the number of actual parameters, only the formal parameters corresponding to actual parameters will be expanded. If the number of actual parameters exceeds the number of formal parameters, the superfluous actual parameters will be ignored.

### Examples: Formal parameters versus actual parameters

```
Set MUL= '$1*$2' ;
```

```
Set X= $(MUL) ;         // returns $1*$2 in X
```

```
Set X= $(MUL(10)) ;     // returns 10*$2 in X
```

```
Let X= $(MUL(5,7,8)) ;  // returns 35 in X
```

## The $0 parameter

The parameter $0 returns the number of parameters actually passed by a call.

### Example: How to introduce error handling

```
Set MUL= If($0=2, $1*$2, 'Error') ;
```

## Learn more

- [*Let*](ScriptRegularStatements/Let.htm)
- [*Set*](ScriptRegularStatements/Set.htm)
