---
title: "Creating and configuring your tenant"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qcs-tenant-domain.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud"]
---

# Creating and configuring your tenant

This topic walks the service account owner (SAO) through creating a Qlik Cloud [tenant](#glossary-0 "Glossary term"): activating your account, choosing a region, and getting ready to invite users. You need the welcome email from Qlik, or access to My Qlik.

## Before you begin

Check the following before you start, as they affect how you set up your tenant.

- Region: The region you choose becomes part of your tenant URL, and you cannot change it after setup. A default is suggested based on your location. See [*Regions reference*](#Regions) to compare options. If you later need to move your tenant, contact [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport) to discuss available options. For more information, see [How to move a Qlik Cloud Tenant to a different Region](https://community.qlik.com/t5/Official-Support-Articles/How-to-move-a-Qlik-Cloud-Tenant-to-a-different-Region/ta-p/1816598).
- Anonymous access: Anonymous access tenants let people view shared or embedded Qlik analytics content without logging in. They require a Qlik Anonymous Access subscription and the Europe (Stockholm) region, which is available only for anonymous access tenants. For more information, see [*Qlik Anonymous Access subscriptions*](../Admin/subscription-options-anonymous.htm). If you don't plan to share analytics with the public or external users, see [*Planning your Qlik Cloud deployment*](planning-deployment.htm) for other subscription options.
- OEM or external customers: For OEM and Enterprise external use deployments, deploy each end customer in their own Qlik Cloud tenant.

  Warning noteUsing a single tenant for all end customers may result in a user having access to visibility of all other users within the same tenant. Such visibility may include, but is not limited to, user names, email addresses and the user's subject, which is a unique string used to identify the user that is provided to Qlik Cloud by the configured identity provider.

There is a maximum number of tenants that you can create in a region. Contact Qlik Sales to manage your user account.

Qlik Talend Cloud subscriptions automatically create and link the Qlik Cloud and Talend Cloud tenants during setup.

## Key concepts

- Tenant: a unit within Qlik Cloud that holds your organization's data, apps, users, and spaces. Each tenant is tied to one subscription.
- Service account owner (SAO): the first user to access the [tenant](#glossary-1 "Glossary term"), who creates it and becomes its initial tenant admin. The SAO and other tenant admins can manage the tenant, but only the SAO can manage the subscription.

  Information note

  To change the service account owner, contact [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport) or create a support case from the [Support Case Portal](https://community.qlik.com/t5/forums/postpage/board-id/@support). For more information, see [Qlik Cloud Services: Service Account Owner and Tenant Admin FAQ](https://community.qlik.com/t5/Knowledge/Qlik-Cloud-Services-Service-Account-Owner-and-Tenant-Admin-FAQ/ta-p/1799811).

## Create your tenant

Do the following:

1. Activate your account.

   1. In the welcome email from Qlik, click Let's get started.
   2. On the Set up your account page, enter a password in Create password.
   3. Select the checkbox to agree to the Qlik terms and conditions, then click Next.
2. Choose your region.

   1. On the Almost finished page, select your region.
   2. Click Finish.
3. Check your tenant URL. Your tenant is created at <tenantname>.<region-identifier>.qlikcloud.com, where the region identifier comes from the table in [*Regions reference*](#Regions). You are now the first tenant admin.

Tip note

No welcome email? Log in to My Qlik from the [My Qlik portal](https://account.myqlik.qlik.com/), or go to [Qlik.com](http://www.qlik.com/) and select Log In > Qlik Cloud, and create the tenant there. For more information, see [How to create your Qlik Cloud tenant](https://community.qlik.com/t5/Support-Knowledge-Base/How-to-receive-the-Tenant-On-boarding-email-from-My-Qlik-portal/ta-p/1711273?_ga=2.65234792.770940907.1602083441-123334668.1522775250).

## Regions reference

Tenant URLs use the format <tenantname>.<region-identifier>.qlikcloud.com.

Tenant regions and their backup regions

| Region name | Region code | Tenant URL region identifier | Backup region name | Backup region code |
| --- | --- | --- | --- | --- |
| US East (North Virginia) | us-east-1 | us | US East (Ohio) | us-east-2 |
| Asia Pacific (Mumbai) | ap-south-1 | in | Asia Pacific (Hyderabad) | ap-south-2 |
| Asia Pacific (Singapore) | ap-southeast-1 | sg | Asia Pacific (Seoul) | ap-northeast-2 |
| Asia Pacific (Sydney) | ap-southeast-2 | ap | Asia Pacific (Melbourne) | ap-southeast-4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | jp | Asia Pacific (Osaka) | ap-northeast-3 |
| Canada (Montréal) | ca-central-1 | ca | Canada (Alberta) | ca-west-1 |
| Europe (Frankfurt) | eu-central-1 | de | Europe (Milan) | eu-south-1 |
| Europe (Ireland) | eu-west-1 | eu | Europe (Spain) | eu-south-2 |
| Europe (London) | eu-west-2 | uk | Europe (Spain) | eu-south-2 |
| Europe (Paris) | eu-west-3 | fr | N/A | N/A |
| Europe (Stockholm) | eu-north-1 | se | N/A | N/A |
| Israel (Tel Aviv) | il-central-1 | il | N/A | N/A |
| Middle East (UAE) | me-central-1 | ae | N/A | N/A |
| South America (São Paulo) | sa-east-1 | br | N/A | N/A |

Choose the region closest to your data for the best performance. For more information about Qlik Cloud regions and backup locations, see [Qlik Cloud Regions](https://www.qlik.com/us/regions).

## After tenant creation

As the SAO, you are the first [tenant admin](#glossary-2 "Glossary term"). Next, invite users and assign other users as tenant admins. You can manage users with a corporate identity provider (IdP) or with Qlik Account.

For more information about user management, see:

- [*Identity providers in Qlik Cloud*](../Admin/mc-create-idp-configuration.htm)
- [*Managing users - Capacity-based subscriptions*](../Admin/SaaS-user-management-capacity-model.htm)
- [*Managing users - User-based subscriptions*](../Admin/SaaS-user-management.htm)
- [*Managing users - Qlik Anonymous Access subscriptions*](../Admin/SaaS-user-management-anonymous.htm)

Information note

If several tenants share one license, connect them all to the same IdP. Otherwise, license assignments can be duplicated.

### Additional configuration

- Encryption: Qlik Cloud encrypts tenant data by default using keys that Qlik manages. Tenant admins can instead use a customer-managed key (CMK) from AWS Key Management Service. For more information, see [*Tenant encryption*](tenant-encryption.htm).
- Firewalls: If your data sources sit behind a firewall, add the underlying IP addresses for your region in your firewall allowlist so that Qlik Cloud can request data through it. For more information, see [*Allowlisting domains and IP addresses*](qlik-cloud-dns-ip.htm).
- Customization: Tailor your Qlik Cloud environment to better meet your user's needs. For more information, see [*Customizing your system*](system-customization.htm).

Related learning:

- [Getting Started with Qlik Cloud](/lnk/Getting_started_Qlik_Cloud)
