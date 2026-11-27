---
title: "Managing Live Documentation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/EnablingLiveDocumentation.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API documentation"]
---

# Managing Live Documentation

## Enabling the Live Documentation

In order to share your API documentation with people who are not in your team,
you need to enable the Live Documentation feature.

Until it is enabled, it is only viewable as a preview for users who have access to the
API definition.

1. Go to the Settings page of your API by clicking Edit > Open API settings.
2. Toggle the Enabled button from Off
   to On and enter a URL.

   ![Live documentation configuration.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/enable_live_doc_02_url.png)
3. Choose the visibility. If you select Password protected,
   enter a password in the corresponding field.
4. Click Save to enable your Live Documentation.

Your Live Documentation is now available. You can click Open
to open it in a new tab.

## Disabling the Live Documentation

Disable your documentation and select whether you want to retain its
subdomain.

1. Open your API and go to Open API settings.
2. Toggle the Enabled button from On
   to Off.
3. If you want to release the documentation subdomain, clear the Retain
   Live API documentation subdomain check box.

   By default, API Contracts
   saves the subdomain you defined when you enabled the Live Documentation. This
   allows you to keep the same URL if you enable it again later. If you want to use
   this subdomain for a different API, you first need to release it.![Live documentation configuration.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/disable_live_doc.png)
4. Click Save.

Your Live Documentation is disabled. If you retained the subdomain, you can enable
it again at any time. If not, the subdomain can be used by another API and you will need
to enter a subdomain if you want to enable this documentation again.
