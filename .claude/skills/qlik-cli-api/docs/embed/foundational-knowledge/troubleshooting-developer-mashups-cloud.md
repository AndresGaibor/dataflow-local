---
source: https://qlik.dev/embed/foundational-knowledge/troubleshooting-developer-mashups-cloud/
last_updated: 2025-11-21T14:05:39Z
---

# Troubleshoot mashups and web apps in Qlik Cloud

This section describes problems that can occur when trying to log on to the site
hosting your mashup or web app after integrating it with Qlik Cloud, as well as
suggestions for resolving them.

## Error: 401 Unauthorized

### Scenario 1

Possible cause: The web integration ID for the hosting domain is incorrect or
missing from your solution.

Proposed action: Verify the web integration ID and make sure it has been added
to your solution. See [Web Integration Examples](https://github.com/qlik-oss/web-integration-examples)
for examples of where to add your web integration ID.

### Scenario 2

Possible cause: Failed to trigger the login process for the user.

Proposed action: Make sure the login flow has been triggered before trying to
access the APIs.

## Error: Cross-origin request has been blocked by CORS policy

Possible cause: Your origin (domain) does not match the configured allowlist for
your web integration in the management console.

Proposed action: Update the allowlist configuration of the web integration
entity for your site. For more information, see [Managing web integrations](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-adminster-web-integrations.htm)
on Qlik Help.
