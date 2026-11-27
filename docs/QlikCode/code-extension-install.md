---
title: "System requirements and installation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikCode/code-extension-install.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Qlik for VS Code"]
---

# System requirements and installation

This page outlines requirements and procedures for installing the Qlik for VS Code extension.

## Requirements

- Visual Studio Code version 1.79.0 or later.
- A Qlik Cloud tenant, and access to the spaces, applications, and scripts you want to edit.
- Tenant admin approval (see [*Qlik for VS Code Tenant Admin approval (OAuth consent)*](#OAuthConsent)).

### Qlik for VS Code Tenant Admin approval (OAuth consent)

Qlik for VS Code signs users in to Qlik Cloud using an OAuth client. Before anyone in a given Qlik Cloud [tenant](#glossary-0 "Glossary term") can sign in with Qlik for VS Code, the [tenant administrator](#glossary-1 "Glossary term") must approve this OAuth client once. This is a one-time, per-tenant step — once approved, every user in that tenant can sign in normally, with no further action needed.

There are two ways to get a tenant approved:

Method 1: Sign in as a Tenant Admin

If the person setting up Qlik for VS Code for their organization is themselves a Tenant Admin, they can simply sign in through the extension as usual. The consent is granted automatically as part of that first sign-in.

Method 2: Share a consent link with the Tenant Admin

If the person setting up Qlik for VS Code is not a Tenant Admin, their sign-in attempt will fail with an "access denied" message. In that case, Qlik for VS Code shows a link they can copy and send to their organization's Tenant Admin. The Tenant Admin opens that link in their own browser — no need to install Qlik for VS Code — and approves it from there. Once approved, the original user (and everyone else in the tenant) can sign in normally.

Error message that appears when a non-administrator tries to sign in to a tenant via Qlik for VS Code before the tenant has been approved. This error message contains a link you can send to your tenant administrator so they can complete the tenant approval.

![Error message that appears when a non-administrator tries to sign in to a tenant via Qlik for VS Code before the tenant has been approved.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qlik-code-tenant-admin-approval-needed-.png "Click to view full size")

Once approved, the Qlik for VS Code OAuth client will be visible to the Tenant Admin through the Administration [activity center](#glossary-2 "Glossary term") and can be managed like any other OAuth client. For information about managing OAuth clients in Qlik Cloud, see [*Creating and managing OAuth clients*](../Admin/mc-create-oauth-client.htm).

## Install Qlik for VS Code

Do the following:

1. In VS Code, go to the [Extension Marketplace](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace).
2. Search for "Qlik for VS Code", and select Install.

Alternatively, install from the [Marketplace website](https://marketplace.visualstudio.com/VSCode) and VS Code will prompt you to open it in the editor.

## Learn more

- [Visual Studio Code documentation](https://code.visualstudio.com/docs)
