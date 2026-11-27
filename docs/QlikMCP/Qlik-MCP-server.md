---
title: "Qlik MCP server"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data"]
---

# Qlik MCP server

Add the analytics capabilities of Qlik Cloud into your own LLM projects and AI tools and services.

Qlik Model Context Protocol (MCP) server integrates Qlik Cloud into your LLM workflow, allowing you to work with Qlik Cloud using your LLM without having to leave your LLM.

Once connected to your tenant, your LLM can access your Qlik Cloud resources through the Qlik MCP server. Your natural language questions and requests are interpreted by your LLM. The LLM then selects the corresponding MCP tools from the tools available and passes the request through to Qlik MCP server. Qlik MCP server then uses Qlik APIs to perform the requested actions and prepares a response back to your MCP client.

The Qlik MCP server allows you to perform activities in your MCP client such as:

- Searching for information from your available apps, data products, and datasets.
- Asking natural language questions without navigating to apps and sheets.
- Understanding expressions and scripts in apps.
- Creating and editing dashboards, sheets, and visualizations using prompts.
- Generating business glossaries
- Training, deploying, and creating predictions with machine learning models using Qlik Predict.

Before beginning to use Qlik MCP server, administrators should review [*Deploying and administering Qlik MCP server*](Administering-Qlik-MCP.htm).

Warning note

Data sharing

By clicking Approve when connecting your MCP client to the Qlik MCP server, you will enable the Qlik Server to share your Qlik Cloud data ("Content") with a third-party system (like an AI tool). That system is not managed by Qlik, and your Content will be located, stored and processed under the third party’s control.

Warning note

Qlik MCP server connects with generative artificial intelligence ("GenAI") products and services. It is the user's responsibility to review and verify any GenAI output before using or sharing it, and to evaluate whether the use of Qlik's MCP server is appropriate for any particular use case and whether it complies with applicable laws.

Information note

The use of the Qlik MCP server is subject to the terms of the Qlik API policy. For more information on the terms and limitations of the API policy, see [API policy](https://qlik.dev/apis/api-policy/).

## Integrating Qlik MCP into your workflows

Qlik MCP server allows you to work with Qlik Cloud from your MCP client, offering a broad range of actions in Qlik Cloud. To view specific tools, see [*Qlik MCP tools*](Qlik-MCP-server-tools.htm).

Consider integrating the following kinds of activities into your LLM workflows:

- Data exploration and analysis: Use your MCP clients to navigate and explore applications like an analyst. Query chart data, search fields, apply selections, and analyze the results.
- Build applications: From your MCP client, create, duplicate, and edit sheets, add and update charts and containers, and create master dimensions and measures.
- Create business glossaries: Get your MCP client to look at your applications and data to build corresponding business glossaries for you.
- Finding and using data products: Use your LLM to explore available data products, check their quality, review their documentation, and create load scripts for applications.

## Getting started with Qlik MCP server

Setting up Qlik MCP for your tenant involves the following steps:

1. Allow access to Qlik MCP

   The tenant administrator allows user access to Qlik MCP, either for all users in the tenant or through a custom role for selected users.

   [*Deploying and administering Qlik MCP server*](Administering-Qlik-MCP.htm)
2. Choose the OAuth client creation method

   The tenant administrator chooses how OAuth clients are created for the MCP clients that users connect with.

   [*Deploying and administering Qlik MCP server*](Administering-Qlik-MCP.htm)
3. Authorize MCP clients for Qlik MCP

   The tenant administrator authorizes MCP clients for Qlik MCP.

   [*Deploying and administering Qlik MCP server*](Administering-Qlik-MCP.htm)

   [*Connecting to the Qlik MCP server*](Connecting-Qlik-MCP-server.htm)
4. Connect MCP clients to Qlik MCP

   Users connect their MCP clients to Qlik MCP and use Qlik MCP tools and skills.

   [*Connecting to the Qlik MCP server*](Connecting-Qlik-MCP-server.htm)

   [*Qlik MCP tools*](Qlik-MCP-server-tools.htm)

   [*Qlik skills and plugins*](Qlik-MCP-skills.htm)
