---
title: "Custom code block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/advanced/custom-code.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Advanced blocks"]
---

# Custom code block

The custom code block lets you use custom code in your automation. Because the output of this block is used as the input for other blocks, the script must use a JSON-encoded print/echo or equivalent.

Qlik Cloud Government noteDue to U.S. Government specific control requirements, the Custom Code block is not supported by Qlik Cloud Government or Qlik Cloud Government - DoD. Using a Custom Code block in US Government tenants will generate an error message (Custom code block not allowed).

![custom code block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/custom-code-block.png)

A custom code block is commonly used in the following situation:

- When you want to customize your automation beyond what is available with blocks.

## Configuring a custom code block

Configure the custom code block to execute custom code.

### Inputs

The custom code block requires that you specify the code language and provide the custom code. You can add variables if needed.

This block supports PHP, Node.js, and Python.

Custom code block input fields

![custom code block showing language and code snippet](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/custom-code-block-inputs.png)

## Limitations

Because the custom code block is optimized for security, it cannot access the internet, leverage third-party modules and packages, or make direct external calls. Since version upgrades may occasionally break customer code we recommend using native blocks and functions where possible.
