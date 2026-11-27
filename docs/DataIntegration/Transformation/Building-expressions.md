---
title: "Building expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Building-expressions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Managing datasets"]
---

# Building expressions

Use expressions to calculate column values or define conditions when adding columns, editing column expressions, creating transformation rules, or filtering datasets.

The expression builder lists the elements available for the current task. The movement-task references cover SaaS-managed landing, lake landing, and replication tasks. Storage, transform, and data mart expressions depend on the data platform or task engine. For CDC Storage and Streaming Transform functions, see [*Transformation functions*](../Lakehouse/transformation-functions.htm). Use the functions and syntax available in your editor.

## Creating or editing an expression

1. Open the expression builder from the column, transformation rule, or dataset filter that you are configuring.

   For a column expression, click ![Edit column expression](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression.svg) on the column.
2. Select an element, then click ![Insert selected expression element](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to insert it.

   You can also type the expression. Insert column parameters to supply values from each source row, preserving the syntax used by your editor.

   To insert an operator from the toolbar, click where it belongs in the expression, then click the operator.
3. Replace function argument placeholders with column parameters, constants, or nested expressions.

   Enclose text and date constants in single quotes, such as `'Unknown'` and `'2026-10-08'`. Represent an embedded quote with two quotes: `'O''Brien'`. Enter numbers without quotes, such as `12` or `12.5`. Use `NULL` for a missing value, not the text `'NULL'`.
4. Test the expression as described below, then click OK to save it.

## Using expression elements

- Columns: Source dataset columns supply values from the row being processed.

  For Streaming Transform tasks, this list also includes landing columns such as `hdr__kafka_partition` and `hdr__file_name`, in source order. These are separate from the `Q_H_` headers in movement-task expressions. See [*Landing tables*](../Lakehouse/lakehouse-datasets-architecture-streaming.htm#Landing).
- Functions: Calculate or convert values. Supply arguments in the order shown by the function signature. See [*Expression functions*](Expression-functions.htm).

  Information noteFor Azure Synapse Analytics expressions, `$RTRIM` and `$LTRIM` trim only spaces, regardless of the specified trim character.
- Operators: Combine values, compare them, or define conditions. Use parentheses to control evaluation order. See [*Expression operators*](Expression-operators.htm).
- Headers: Use change metadata in SaaS-managed landing, lake landing, and replication tasks. See [*Expression headers*](Expression-headers.htm) for source endpoint applicability and processing-phase values.

## Example: Combining column values

The following expression joins `first_file_name` and `first_file_title` with a colon:

```
${first_file_name} || ':' || ${first_file_title}
```

For the sample values `sales` and `Sales June 2022`, the result is `sales:Sales June 2022`.

Editing an expression

![Expression editor combining two dataset columns with a colon.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_qdi_expression_editor.png "Click to view full size")

## Testing expressions

Use sample parameter values to check the calculated result before saving. Parameter extraction identifies expression inputs; testing evaluates the expression with the values you provide.

Information noteTesting calls to the `$SOURCE_LOOKUP` and `$TARGET_LOOKUP` functions is not supported.

1. Click Extract parameters.
2. Enter a Value to test for each parameter, using values appropriate for the column data type.
3. Click Test expression and check the result.

If the expression is invalid, correct its syntax and arguments, then extract the parameters again before retesting. Repeat with representative values, including missing values where relevant. A successful sample test does not check every source row.
