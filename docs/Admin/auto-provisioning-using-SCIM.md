---
title: "Provisioning users and groups using SCIM"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/auto-provisioning-using-SCIM.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud"]
---

# Provisioning users and groups using SCIM

SCIM (System for Cross-Identity Management) is an open standard for automating the exchange of user identity information between identity providers and enterprise applications. It aims to simplify user management by providing a common API for creating, updating, and deleting user accounts across different systems.

## What SCIM does

SCIM provides a standardized way for IT systems to communicate and exchange user identity data. With SCIM, you can:

- Create a new user in one system and automatically provision the same user in another system.
- Update user information in one system and reflect that change in all other systems.
- Delete a user in one system and automatically deprovision the user in all other systems.

By standardizing the user management process, SCIM makes managing users across different IT systems easier and reduces the likelihood of errors or discrepancies in user information.

## How SCIM works

SCIM defines a set of REST APIs that can be used to exchange user identity information. These APIs support standard CRUD (Create, Read, Update, Delete) operations, making it possible to manage users consistently across different systems.

SCIM also defines a standard data model for representing user identity information, including basic information such as name and email address, and more complex data such as groups.

## Custom groups and SCIM

SCIM synchronization manages only Identity Provider (IdP) managed groups. Custom groups that are created in Qlik Cloud are not available through SCIM group endpoints.

SCIM group endpoints return and manage only IdP-managed groups. Custom groups are excluded from SCIM group list, get, delete, and patch operations.

Users can belong to both IdP-managed groups and custom groups at the same time. If SCIM updates a user's IdP-managed group memberships, the user's custom group memberships are not changed.

## Why use SCIM?

SCIM provides several benefits for organizations managing user identities across multiple systems:

- Simplified user management: SCIM makes it easier to manage users by providing a common API for creating, updating, and deleting users across different systems.
- Consistent user data: SCIM ensures that user information is consistent across all systems, reducing the likelihood of errors or discrepancies.
- Improved security: By automating the exchange of user identity information, SCIM reduces the need for manual processes that might be prone to errors or security breaches.
- Better user experience: SCIM makes it easier for users to access the resources they need by providing a consistent experience across different systems.

## SCIM versions compatible with Qlik Cloud

Qlik Cloud is compatible with SCIM 2.0.

## SCIM connectors that work with Qlik Cloud

Qlik Cloud supports Microsoft Entra ID (formerly Azure AD).

Wf-note**Get started by following these steps**

This section of the help features a step-by-step flow, that shows you how to get started with Provisioning users and groups using SCIM.

[See the steps](/en-US/cloud-services/wf/Subsystems/Hub/Content/Sense_Hub/Admin/auto-provisioning-using-SCIM.htm)

## Resources

For more information about SCIM and Microsoft Entra ID SCIM, see:

- [System for Cross-Domain Identity Management](https://www.simplecloud.info/)
- [SCIM synchronization with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/architecture/sync-scim)
