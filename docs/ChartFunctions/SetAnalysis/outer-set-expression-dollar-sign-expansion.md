---
title: "Outer set expressions and dollar-sign expansions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/outer-set-expression-dollar-sign-expansion.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis"]
---

# Outer set expressions and dollar-sign expansions

When one (or more) dollar-sign expansions are used in a larger expression, every dollar-sign expansion will be evaluated in isolation before the result is inserted into the rest of the expression. One implication of this evaluation method is that set expressions outside of a dollar-sign expanded expression will not affect the result. This creates an effect in which there is a double evaluation of information within an expression.

## Example – How expressions containing outer set expression and dollar-sign expansions are evaluated

Suppose you have this example expression:

{<Year={2024}>} $(=Sum(Sales))

Within the expression above, there is a set expression to select Year values of 2024: {<Year={2024}>}. When the entire example expression is evaluated, this set expression is not applied.

Instead, the dollar-sign expression $(=Sum(Sales)) is evaluated first.

For this example, suppose that Sum(Sales) evaluates to a result of 1500311. When evaluating the expression {<Year={2024}>} $(=Sum(Sales)), this number is inserted into the surrounding expression. This evaluation order results in the following partially evaluated configuration (note that this is not a useful Qlik Sense expression, and is shown only to demonstrate the order of evaluation):

{<Year={2024}>} 1500311

Next, the expression {<Year={2024}>} 1500311 is evaluated as a whole. The set expression {<Year={2024}>} does have not any effect because the expression to the right of it is simply a number, not any type of aggregated expression.

Therefore, using the Sum(Sales) value given above in the example, the evaluated result for the entire expression {<Year={2024}>} $(=Sum(Sales)) would be 1500311.

## Building an expression from parts

Using dollar-sign expansions in an expression results in a double-evaluation effect. You can benefit from this double-evaluation effect by building an expression using parts.

### Example

Suppose you have this example expression:

{<Year={2024}>} $(='Sum(' & 'Sales' & ')')

In the first round of evaluation, the dollar-sign expansion $(='Sum(' & 'Sales' & ')') is evaluated. In this step, the three strings are combined into a single string 'Sum(Sales)'. Since this is a string and not an expression, the expression inside is not evaluated at this time.

At this stage in the evaluation, the expression is set to be interpreted by Qlik Sense as follows:

{<Year={2024}>} Sum(Sales)

In this case, the outer set analysis expression will be applied to the Sum aggregation since we now have produced a normal expression, rather than just a number (as was the case in [the first example](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/outer-set-expression-dollar-sign-expansion.htm#Example1)). Note that the quotation characters consumed the first round of evaluation so that the expression was preserved (and concatenated using &) for the second evaluation round.

## Variable lookup

When using a variable dollar-sign expansion to do a variable lookup, the content of the variable is inserted into the surrounding expression before that content is evaluated.

### Example

Suppose you have this example expression:

{<Year={2024}>} $(Var1)

In this example, the content of the [variable](#glossary-0 "Glossary term") Var1 will be inserted into the surrounding expression before that content is evaluated.

#### Outcome A – Variable definition without equal sign

If Var1 is defined as Sum(Sales), it would look like this after expansion (note that the configuration below is a partially evaluated expression):

{<Year={2024}>} Sum(Sales)

Variables dialog showing definition and value of variable Var1, when an equal sign is not placed at the start of the variable definition.

![Variables dialog showing definition and value of variable Var1, when an equal sign is not placed at the start of the variable definition (which is Sum Sales). As a result, the variable's evaluated value is Sum(Sales)](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_variable-def-no-equal-sign.png "Click to view full size")

So, for this example, the outer set expression {<Year={2024}>} will be applied.

#### Outcome B – Variable definition with equal sign

On the other hand, if the definition in Var1 starts with an equal sign – that is, =Sum(Sales) – the outer set expression is not applied. This is because the equal sign causes the variable expression to be calculated ahead of time, and in isolation. This leads to a result similar to [the first example](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/outer-set-expression-dollar-sign-expansion.htm#Example1), in which there is an outer set expression to be evaluated alongside a number, which does not return a useful result.

Variables dialog showing definition and value of variable Var1, when an equal sign is placed at the start of the variable definition.

![Variables dialog showing definition and value of variable Var1, when an equal sign is placed at the start of the variable definition (which is Sum Sales). As a result, the variable's evaluated value is the calculated value of the expression Sum(Sales), which in this case is 1500311](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_variable-def-with-equal-sign.png "Click to view full size")

## Learn more

- [*Inner and outer set expressions*](set-expressions-inner-and-outer.htm)
- [*Dollar-sign expansions*](../../Scripting/dollar-sign-expansions.htm)
- [*Creating a variable*](../../Variables/create-variable-using-dialog.htm)
- [*Variables dialog*](../../Sheets/variables-dialog.htm)
