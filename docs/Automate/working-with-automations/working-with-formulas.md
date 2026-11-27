---
title: "Working with formulas"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-formulas.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations"]
---

# Working with formulas

This section shows you how to use formulas in input fields.

The input fields for most blocks automatically show possible field mapped values from preceding blocks. You also have the option to add formulas. Formulas generically refers to all of the available functions.

Data to output field

![inputs showing field mapped value and formula option](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/formula.png)

When you select Add formula, you have many types of functions that can be applied. Each formula is described in this section.

Formula selection pane

![The formula options window showing all functions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/formula-options.png)

## Basic formula syntax

When you add a field mapped value, you are creating a placeholder for data coming from elsewhere in the automation. A formula manipulates the data of that placeholder. When you add a formula to an input field, it is applied to the result of the placeholder.

For example, the placeholder `{$.inputs.name}` references the `name` field of the inputs block. You can apply a formula to that data by adding it to the front of the placeholder. Formula parameters are placed after the placeholder.

- Example of a formula applied to a placeholder: `{formula-name: {$.inputs.name}}`
- Example of a formula applied to a placeholder with parameters: `{formula-name: {$.inputs.name}, parameter1, parameter2}`

You can use multiple formulas for a single placeholder. Each formula is wrapped by curly braces. The inner formula is applied first.

- Example of nested formulas: `{ outer-formula: { inner-formula: {$.inputs.name}, inner-parameters }, outer-parameters }`

## Adding formulas to input fields

To apply a formula, first add the formula, then select the formula type, then select the placeholder and parameters. The options are slightly different for each formula.

Formula in data to output field

![adding a formula with formula parsing](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/formula-input-on.png)

When you toggle formula parsing, you see the underlying JSON object.

Raw formula in data to output field

![adding a formula with formula parsing](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/formula-input-off.png)
