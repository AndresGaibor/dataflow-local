---
title: "Troubleshooting - Working with others in Qlik Cloud Analytics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Troubleshooting/troubleshooting-cloud-hub-collab.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users"]
---

# Troubleshooting - Working with others in Qlik Cloud Analytics

This section describes problems that can occur when working with others in Qlik Cloud Analytics.

## I cannot change with whom I shared my application

I shared an application with other users from my [personal space](#glossary-1 "Glossary term") using the Share option. I wanted to change who has access to this application, but cannot find the Share option.

Possible cause

The Share option for sharing applications from a personal space was deprecated as of the March 2020 release of Qlik Sense Enterprise SaaS. Applications are now shared only from shared spaces.

If the Share option was not toggled off before the deprecation of the Share option, you will not be able to change who your application is shared with.

Proposed action

Duplicate the application and then delete the original application. Duplicating an application does not duplicate the access you gave to other users.

Do the following:

1. Go to your personal space.
2. Right-click a shared application and select Manage > Duplicate.

   A duplicate of the application is created.
3. Delete the shared application.
