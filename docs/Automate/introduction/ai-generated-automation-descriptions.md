---
title: "AI-generated automation descriptions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/ai-generated-automation-descriptions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Getting started"]
---

# AI-generated automation descriptions

You can use the AI Generate button in Automation settings to generate a description for an automation from its workspace structure. This makes the automation easier to discover for AI agents and MCP integrations that cannot access the workspace directly.

To generate a description, your tenant must have cross-region inference enabled. For details, see [*Enabling cross-region inference*](../../Sense_Hub/Admin/cross-region-data-processing.htm).

Prerequisites:

- Your tenant must have the `catalogGovernanceGenAI` entitlement.
- You must be the owner of the automation.

If cross-region inference is turned off, the AI Generate button is not shown. In Automation settings, the Description field still shows descriptions that were generated before cross-region inference was turned off.

Qlik Cloud Government noteAI generation of automation descriptions is not supported in Qlik Cloud Government or Qlik Cloud Government - DoD.

## Regional restrictions

AI-generated automation descriptions are currently not available for tenants in the `il-central-1` (Israel) region.

## Generate an automation description

Do the following:

1. Open the automation in the editor.
2. Click the More menu and select Automation settings.
3. Next to the Description field, click AI Generate.
4. Review the generated description. Edit it if needed.
5. Click Save.

## What the generator uses

- Connector blocks and their descriptions.
- Built-in blocks, such as loops and conditions.
- Comments on each block.

Warning note

Block comments and connector and block names are sent to an LLM to generate the description. Do not include personal data or sensitive information in block comments.
