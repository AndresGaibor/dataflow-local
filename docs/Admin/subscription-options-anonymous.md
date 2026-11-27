---
title: "Qlik Anonymous Access subscriptions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/subscription-options-anonymous.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Planning your Qlik Cloud deployment"]
---

# Qlik Anonymous Access subscriptions

Qlik Anonymous Access subscriptions allow users to develop and share Qlik Sense analytics for consumption outside of Qlik Cloud. To access applications shared through [anonymous access](#glossary-0 "Glossary term"), no login is required. Instead, tenant users share content with others by providing application links or by embedding application content directly into external web pages or applications.

With a Qlik Anonymous Access subscription, you create an anonymous access tenant in Qlik Cloud. The cloud infrastructure is hosted and managed by Qlik. In an anonymous access tenant, the user experience is very similar to other Qlik Cloud subscriptions. The main differences are assignment of user entitlement by administrators, limitations on using certain add-on capabilities, and capacities for data loading and application development.

Examples of use cases for anonymous access include sharing of non-sensitive data with external partners, or embedding analytics within a website for consumption by public audiences. For more information about anonymous access, see [*Sharing application content with anonymous access*](../Share/share-anonymous-access.htm).

## Terminology on this page

The following terminology is used in content about anonymous access:

- Anonymous users: Users who are accessing application content without signing in, either through anonymous access links to an application or by consuming embedded analytics anonymously. These users are not members of the Qlik Cloud tenant, and also do not require Qlik accounts.
- Tenant users: Users who are members of the tenant and manage the tenant or develop analytics for consumption by anonymous users. Tenant users may have administrator privileges in the tenant.

## Offerings

All Qlik Anonymous Access subscriptions provide the following:

- A Qlik Cloud tenant environment with many of the same features as other Qlik Cloud subscriptions (see full list [here](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/qcs-specs-capacity-anonymous-access.htm#Capabilities)).
- Ability for tenant users to share application content with anonymous users.
- 10 tenant users, with additional users available.
- 25 GB of Data for Analysis capacity.

For information about availability of specific capabilities, see [*Available capabilities*](../Introduction/qcs-specs-capacity-anonymous-access.htm#Capabilities).

### Purchasing options

When purchasing Qlik Anonymous Access, there are different options available to support your requirements and use case. Each option offers different consumption capacities for anonymous access value meters. For more information about what each of the value meters means, see [*Understanding the subscription value meters*](subscription-value-meters.htm).

Start by purchasing one of the following two base packs:

- The small-to-medium-sized-business (SMB) base pack includes 500 MB of Anonymous Access Capacity and 25 Anonymous Concurrent Sessions.
- The standard base pack includes 2 GB of Anonymous Access Capacity and 100 Anonymous Concurrent Sessions.

You can then purchase the individual portions of any of the base packs to add more capacity. This capacity is added to the consumption capacity of your selected base pack. For example, you can select the SMB base pack to receive 500 MB of Anonymous Access Capacity and 25 Anonymous Concurrent Sessions, and then purchase an additional 500 MB of Anonymous Access Capacity, bringing your total subscription capacity to 1 GB of Anonymous Access Capacity and 25 Anonymous Concurrent Sessions.

Some of the other included capacities and features can also be increased or added with an additional purchase. For a list of capabilities and hard limits, see [*Qlik Anonymous Access specifications and capacity limits*](../Introduction/qcs-specs-capacity-anonymous-access.htm).

## Differences between Qlik Anonymous Access and capacity-based subscriptions

Qlik Anonymous Access uses a subscription model similar to Qlik Cloud capacity-based subscriptions, but there are important differences. The sections below compare the two subscription models.

### User entitlement

User membership and access in the tenant is managed through role assignments in both subscription models.

In Anonymous Access subscriptions, two types of users are distinguished for clarity:

- Anonymous users are not members of the tenant but can view publicly shared content with restricted access.
- Tenant users are members of the tenant and can be assigned roles that grant full access to the tenant. These users may develop applications that can be shared with anonymous users.

Information noteThe terms “tenant user” and “anonymous user” are only used in the context of Qlik Anonymous Access subscriptions to differentiate the two types. In capacity-based subscriptions, all users are members of the tenant and are simply referred to as “users.”

### Value meters

Value meters for capacity-based subscriptions depend on several factors, such as how much data can be moved by and within Qlik Cloud.

For Qlik Anonymous Access subscriptions, the value is determined primarily by the tenant's capacity for anonymous users to access content. The main value metes are:

- Anonymous Access Capacity
- Anonymous Concurrent Sessions

Other metrics (for example, Data for Analysis) are still relevant but do not determine the value of the subscription purchase.

For further details, see [*Understanding the subscription value meters*](subscription-value-meters.htm).

### Overage

Capacity-based subscriptions allow overage consumption for certain resources. Qlik Anonymous Access subscriptions do not support overage. Once a capacity limit is reached, further consumption is prevented.

For Qlik Anonymous Access subscriptions, an invited user has the Requested status if no user entitlements are available. Users with this status cannot access activity centers or open applications.

For more information, see [*Adding users to a Qlik Anonymous Access tenant*](SaaS-invite-users-anonymous.htm).

### Tenant region

In capacity-based subscriptions, you may have the option to select the region where your tenant is hosted. In Qlik Anonymous Access, the tenant is only available in the Europe (Stockholm) region.

For more information, see:

- [*Creating and configuring your tenant*](../Introduction/qcs-tenant-domain.htm)
- [Qlik Cloud Regions](https://www.qlik.com/us/regions)

### Capabilities and specifications

Some capabilities that are available in capacity-based subscriptions are not available in Qlik Anonymous Access.

There are differences in the available capacities and guardrails. For example, large applications are not supported, with a maximum application size of 1 GB.

For more information, see [*Qlik Anonymous Access specifications and capacity limits*](../Introduction/qcs-specs-capacity-anonymous-access.htm).
