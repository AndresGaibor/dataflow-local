---
title: "Update run title block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/advanced/update-run-title.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Advanced blocks"]
---

# Update run title block

The update run title block sets the run title for an automation when it is executed.

Tip note

The run title is visible in the **History** view of the automation.

![Update run title block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/update-run-title-block.png)

Use the update run title block when you want your automation to have unique run titles for every execution if the automation meets a condition.

## Configuring an update run title block

Configure the block to add a run title when the automation is executed.

### Inputs

The update run title block requires a run title. This can be a field mapped value from a proceeding block or a manually entered string.

Update run title block input field

![Update run title block inputs](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/update-run-title-block-inputs.png)

When an automation is executed with an update run title block, the block adds the title to the title field. You can see the run title in the History section of the Automation overview page.

History view of an automation

![View showing updated run titles](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/run-title.png)
