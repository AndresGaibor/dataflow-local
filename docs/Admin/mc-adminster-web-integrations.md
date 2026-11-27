---
title: "Managing web integrations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-adminster-web-integrations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Extending Qlik Cloud"]
---

# Managing web integrations

Web integrations allow specified domains to securely access tenant resources by verifying requests against an approved allowlist.

Use web integrations to add approved origins that can access the [tenant](#glossary-0 "Glossary term"). Each web integration includes an allowlist and is linked to an ID used in scenarios like mashups connecting to your tenant. When a request is received, Qlik Cloud checks if it originates from an allowlisted domain and either approves or denies the request.

Tenant administrators can manage web integrations in the Administration activity center.

## Creating a new web integration

Do the following:

1. In the Administration activity center, go to Web.
2. Click Create new.
3. Provide a name for the web integration.
4. Enter the origin address in the format https://domain.com.

   - For nonstandard ports, include the port number in the address (for example, https://domain.com:8080).

   Information noteQlik Cloud does not support wildcard domains for web integration origins, so make sure to specify explicit domain addresses.
5. Click Add to include the origin in the allowlist.
6. If needed, add more origins.
7. Click Create to complete the process.

## Editing a web integration

Do the following:

1. In the Administration activity center, go to Web.
2. On the web integration you want to edit, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Edit.
3. Change the options as needed.
4. Click Save.

## Deleting a web integration

Do the following:

1. In the Administration activity center, go to Web.
2. Select the web integrations you want to remove and click Delete.
3. Confirm the deletion.

## Copying a web integration ID for use in mashups

Do the following:

1. In the Administration activity center, go to Web.
2. Select the web integration you want to copy the ID for.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Copy ID.

The ID is copied to the clipboard.
