---
title: "Troubleshooting - Administration and installation of reporting"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Troubleshooting/troubleshooting-report-administration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Troubleshooting - In-application reporting"]
---

# Troubleshooting - Administration and installation of reporting

This topic provides guidance for administrators to resolve common issues encountered during installation of Qlik reporting add-ins.

## Blank dialog shown during authentication after deployment of a Qlik add-in for Microsoft Office

When a user tries to authenticate to a reporting add-in for Microsoft Excel, Microsoft PowerPoint, or Microsoft Word, their authentication pop-up dialog might be blank. Alternatively, the user could instead see an error in the dialog (particularly, 12006).

For a user to work with a Qlik add-in for Microsoft Office, the authentication flow requires a redirect between your [tenant](#glossary-0 "Glossary term") and the identity provider hosted in a different domain. Your identity provider is setting a Cross-Origin-Opener-Policy with restrictive settings. As a result, the cross-domain communication part of the authentication flow is blocked, preventing login information to be correctly returned to the add-in.

Proposed action

The following resolution should be performed by a network administrator who is responsible for setting up identity providers.

Do the following:

- Set the response header from your IDP to your dialog to:

  Cross-Origin-Opener-Policy: unsafe-none

For more information, refer to the official Microsoft documentation: [Best practices and rules for the Office Dialog API](https://learn.microsoft.com/en-us/office/dev/add-ins/develop/dialog-best-practices)

## Learn more

- [*Troubleshooting - Working with report templates*](troubleshooting-report-templates.htm)
- [*Troubleshooting - Report tasks and generated reports*](troubleshooting-tasks-generated-reports.htm)
