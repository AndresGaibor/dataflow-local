---
title: "Accessing Talend account metadata"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-access-talend-metadata.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Connecting Qlik Cloud with Talend Cloud"]
---

# Accessing Talend account metadata

Access the metadata of a Talend account to collect usage metrics for Talend Cloud services.

Information noteThis topic applies if unified administration is not yet enabled for your account. Once it is enabled, Qlik Cloud and Talend Cloud are linked automatically, and these steps are no longer required.

To access account metadata, configure the Talend Cloud account connection and generate an access token in Talend Management Console. After setup, you can collect Talend usage metrics in an application. For details, see [*Monitoring detailed consumption for capacity-based subscriptions*](usage-metrics-app.htm).

## Setting up access to Talend account metadata

Do the following:

1. In the Administration activity center, go to the Settings page, then select the Talend Cloud tab.

   Talend Cloud settings for access token.

   ![Settings pane showing settings for Talend Cloud](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_settings_talend-link-with-token.png "Click to view full size")
2. Turn off the Link to Talend Cloud toggle to activate the input fields for Talend Cloud account ID and the Talend Cloud access token.
3. Enter the Talend Cloud access token that you generated in Talend Management Console under Configurations > Qlik Cloud.

   For more information about generating this secure access token, see [Generating and configuring a secure access token between Talend Management Console and Qlik Cloud](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/setting-up-capacity-based-app).

   The page refreshes automatically, and the Talend Cloud account ID field populates with your account ID.
4. Turn on the Link to Talend Cloud toggle.
