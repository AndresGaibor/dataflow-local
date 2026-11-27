---
title: "Enabling API mocks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/EnablingApiMock.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API mocks"]
---

# Enabling API mocks

Every API Contracts API
version comes with an integrated API mock.
Each version of an API has a
unique mock endpoint. When you create a new version from an existing version with a mock
enabled, the mock is disabled in the new version. You can enable it to get a new
endpoint.

1. Go to the Settings page of your API version.
2. Scroll down to the Mock section, then toggle the
   Enabled button to On.
3. Click Save.

   ![Mock section.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/activatemock.png)

When you activate an API mock, the mock endpoint is added to your API.

This endpoint is also visible in API documentation that you publish from API Contracts.

Information noteNote: The first endpoint in the list of endpoints is selected when you use
features like exporting OAS. You can reorder endpoints at any time via the general information panel.
