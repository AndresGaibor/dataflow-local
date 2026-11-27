---
title: "Connecting Qlik Cloud with Talend Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/connect-qlik-talend-tenants.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud"]
---

# Connecting Qlik Cloud with Talend Cloud

If your subscription includes Talend Cloud capabilities, your Qlik Cloud and Talend Cloud tenants must be linked. Linking enables navigation between the platforms and access to Talend usage data in Qlik Cloud.

Information noteThis topic applies if unified administration is not yet enabled for your account. Once it is enabled, Qlik Cloud and Talend Cloud are linked automatically, and these steps are no longer required.

Tip noteFor more information about subscription options, see [*Qlik Talend Cloud subscription options*](subscription-options-QTC.htm).

## Before you begin

Disable the Talend Data Stewardship and Talend Data Preparation hybrid mode in Talend Management Console.

For the full list of requirements, see [Configuring Talend Cloud with Qlik Cloud](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/configuring-talend-cloud-with-qlik-cloud).

## Link Qlik Cloud and Talend Cloud for navigation

To enable navigation between Qlik Cloud and Talend Cloud, set up the following links:

- From Qlik Cloud to Talend Cloud: Configure a direct navigation link in the Qlik Cloud Administration activity center.
- From Talend Cloud to Qlik Cloud: Link your Qlik tenant in Talend Management Console.

For detailed instructions, see:

- [*Adding a direct navigation link to Talend Cloud*](mc-administer-talend-link.htm)
- [Linking Qlik tenant in Talend Management Console](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/qlik-switch)

## Monitor Talend usage in Qlik Cloud

To monitor Talend usage metrics in Qlik Cloud, configure a secure access token.

For detailed instructions, see:

- [*Accessing Talend account metadata*](mc-administer-access-talend-metadata.htm)
- [Generating and configuring a secure access token between Talend Management Console and Qlik Cloud](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/setting-up-capacity-based-app)

## Set up secure authentication

To enable secure authentication between Qlik Cloud and Talend Cloud tenants, follow the steps in [Configuring Qlik Cloud Authentication](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/configuring-qlik-cloud-authentication).
