---
title: "Setting up Qlik Data Gateway - Data Movement for knowledge marts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/gateways-for-knowledge-mart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections for knowledge marts"]
---

# Setting up Qlik Data Gateway - Data Movement for knowledge marts

To use knowledge marts, you need to connect to vector databases and LLM connections which requires a specific installation.

Information noteBefore installing the gateway, read the [Data Movement gateway system requirements](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/dm-gateway-prerequisites.htm). The recommended configurations are the ones for large and extra-large systems.

1. On the Qlik Data Gateway - Data Movement machine, change the directory to:

   `/opt/qlik/gateway/movement/drivers/bin`
2. Run the command:

   `./install ai-local-agent`
3. Restart the gateway.
4. Follow all steps from Stage Three of  [*Setting up Data Movement gateway*](dm-gateway-setting-up.htm).

When the installation is completed, you can start using knowledge marts. For more information, see [*Creating knowledge marts*](../DataIntegration/KnowledgeMart/Creating-knowledge-marts.htm).

## Updating the service

1. On the Qlik Data Gateway - Data Movement machine, change the directory to:

   `/opt/qlik/gateway/movement/drivers/bin`
2. Run the command:

   `./update ai-local-agent`
3. Restart the gateway.

## Uninstalling the service

1. Stop all tasks.
2. On the Qlik Data Gateway - Data Movement machine, change the directory to:

   `/opt/qlik/gateway/movement/drivers/bin`
3. Run the command:

   `./uninstall ai-local-agent`
