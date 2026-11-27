---
title: "Qlik skills and plugins"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-skills.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik MCP server"]
---

# Qlik skills and plugins

Qlik agentic skills and plugins give compatible AI agents reusable Qlik-specific guidance for working with Qlik MCP workflows.

Agentic skills are folders of instructions, scripts, and reference material that an AI agent loads on demand. Instead of repeating the same context in every conversation, a skill packages expertise so the agent can discover and apply it when needed.

Qlik agentic skills can help AI agents use Qlik-specific APIs, tools, and workflows more consistently. They are based on the open [Agent Skills specification](https://agentskills.io/specification), so the same skill format can work with compatible AI tools.

Qlik maintains the [Qlik Agentic Skills repository](https://github.com/qlik-oss/agentic-skills) as the primary source for current skill content, installation options, contribution guidance, and compatibility details. The Qlik Agentic Skills repository contains two categories of skills:

- Official skills
- Community skills

## Official skills

The official skills folder contains skills owned and maintained by Qlik staff. These skills are reviewed by official maintainers before they are merged, and they provide Qlik-managed guidance for working with Qlik Cloud through an AI agent.

For the current list of Qlik-maintained skills, see [Official Skills](https://github.com/qlik-oss/agentic-skills/tree/main/official/skills).

## Community skills

The community skills folder contains skills and related contributions from Qlik customers, partners, and the developer community. Community skills go through automated security scanning and quality review before they are merged. Community skills are opt-in. They are never silently enabled in a Qlik environment. Tenant administrators control which community skills are available to their users.

For the current list of community contributions, see [Community Skills](https://github.com/qlik-oss/agentic-skills/tree/main/community/skills).
