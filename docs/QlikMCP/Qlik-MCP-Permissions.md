---
title: "Qlik MCP server access and permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-Permissions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik MCP server", "Deploying and administering Qlik MCP server"]
---

# Qlik MCP server access and permissions

Access to Qlik MCP server is controlled by your user role and space permissions.

After authenticating to use Qlik MCP server, the Qlik MCP tools acts as that user with the same permissions and access rights.

## User permissions

User role permissions are set by administrators in the Administration activity center. To use Qlik MCP server, users need the following permission under Features and actions > Agentic AI:

- MCP: Allowed

To give all users in the Qlik Cloud tenant access, allow this permission in the default permissions. For more information, see [*Providing permission through user default*](Administering-Qlik-MCP.htm#Providin).

To limit access to specific users or groups, create a custom role with this permission and assign the role to those users or groups. For more information, see [*Providing permission through a custom role*](Administering-Qlik-MCP.htm#Providin2).

## Space permissions and Qlik MCP server

Your user role permissions give you access to Qlik MCP server, but your space roles control what the Qlik MCP tools can access with your MCP client from different spaces. When using Qlik MCP server, your MCP client will use your user roles and your space permissions to determine what it can do in the Qlik Cloud tenant and what content it can access.

## Section access and Qlik MCP tools

Qlik MCP tools support apps using Section Access and respects the Section Access rules of the application. When accessing applications, Qlik MCP tools use the permissions of the user. They can only access content from a Section Access application to which the user has permission to access and cannot expand the scope through natural language questions about other data in the application.
