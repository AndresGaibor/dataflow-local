---
title: "Managing IP allowlists"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/manage-ip-allowlists.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Securing the system"]
---

# Managing IP allowlists

Use allowlists to control access to your Qlik Cloud tenant by only permitting specific IPv4 addresses or ranges. This helps protect your tenant from unauthorized access and reduces exposure to potential security threats.

## About allowlists

An allowlist specifies which IPv4 addresses or ranges are allowed to access your cloud tenant. When a client connects, the system checks its IP against the allowlist. If the IP is listed, the connection is allowed; if not, the connection is blocked. This provides an additional layer of security by controlling which networks can reach your tenant.

## When to allowlist Qlik Cloud IP addresses

Some Qlik Cloud capabilities work without allowlisting. Others require you to allowlist the source host or service that makes requests to the tenant. In general, allowlisting of Qlik Cloud IPs is only needed when external services or connectors make inbound calls. Activities that run fully within the tenant (for example, Qlik Automate in-tenant connectors) do not require allowlisting.

For details on which services require allowlisting and the region-specific IP addresses to allowlist, see [*Allowlisting domains and IP addresses*](../Introduction/qlik-cloud-dns-ip.htm).

## Impact on integrations

Enabling IP allowlists can cause some integrations to stop working unless their IP ranges are added to the allowlist:

- SCIM provisioning: User and group sync may fail if your identity provider’s IP ranges are not allowlisted.
- Direct Access gateway and Data Movement gateway: Connections to on-premises data sources may fail if gateway IP ranges are not allowlisted.

Check your identity provider and gateway documentation to find the IP ranges to add to the allowlist.

## Allowlist restrictions

Keep the following restrictions in mind when working with allowlists:

- Only IPv4 addresses are supported.
- Private IPv4 ranges defined in RFC 1918 are not supported:

  10.0.0.0/8
  172.16.0.0/12
  192.168.0.0/16

  These ranges are reserved for internal networks and are not routable on the public internet. External clients must use public IPv4 addresses.

## Creating an allowlist

You need to be tenant administrator to create and manage allowlists.

Create an allowlist to define which IPv4 addresses or ranges can access your tenant.

Do the following:

1. In the Administration activity center, go to Settings > IP allowlists.
2. Click Create new.
3. Enter a name for the allowlist.
4. Add one or more IPv4 addresses or ranges.

   - Each allowlist can contain one or more IPv4 addresses or ranges.
   - Only public IPv4 addresses are supported.
   - Private ranges (RFC 1918) are not allowed.
5. Click Create.

Information noteTo avoid being locked out, make sure to include your own IP address in the allowlist. In case you lose access to the tenant, contact Qlik Support.

## Enabling allowlists

Enable an allowlist to enforce its IP restrictions. You can enable more than one allowlist if you need to allow access from multiple networks.

Do the following:

1. In the Administration activity center, go to Settings > IP allowlists.
2. On the allowlist, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Enable.
3. Confirm the action.

What happens when you enable an allowlist:

- If this is the first allowlist you enable: Only the IPs in this list can access the tenant.
- If other allowlists are already enabled: Access is allowed if a client’s IP is in any enabled list.
- Ensure your current IP is included before enabling. Otherwise, you will be locked out.

## Disabling allowlists

Disable an allowlist to remove its restrictions temporarily.

Do the following:

1. In the Administration activity center, go to Settings > IP allowlists.
2. On the allowlist, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Disable.
3. Confirm the action.

What happens when you disable an allowlist:

- If it is the last enabled allowlist: Disabling removes all access restrictions.
- If other allowlists remain enabled: Only IPs in those lists can access the tenant.
- You cannot disable a list if it removes your current IP from all enabled lists. This prevents accidental lockout.

## Editing allowlists

You can rename an allowlist or add or remove IP addresses and ranges.

Do the following:

1. In the Administration activity center, go to Settings > IP allowlists.
2. On the allowlist, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Edit.
3. Edit the name.
4. Add or remove IP addresses or ranges.

   - For enabled lists, you cannot remove your current IP.
   - For disabled lists, you can edit freely.
5. Click Save.

## Deleting allowlists

Delete an allowlist to remove all its IP addresses and ranges.

Do the following:

1. In the Administration activity center, go to Settings > IP allowlists.
2. On the allowlist, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Delete.
3. Confirm the deletion.

What happens when you delete an allowlist:

- You cannot delete an enabled list if it contains your current IP. This prevents accidental lockout.
- You can delete disabled lists without restrictions.
- If you delete the only allowlist: All access restrictions are removed.

## IPv6 behavior and considerations

IP allowlists support only IPv4 addresses. This affects users on IPv6 networks as follows:

- Dual-stack IPv4/IPv6 networks:

  - If a client connects using IPv6, access is blocked even if an allowlist exists.
  - If a client connects using IPv4, access is allowed only if the IPv4 address is in an enabled allowlist.
- IPv6-only networks

  - All connections are blocked.

Information noteIf your organization uses dual-stack or IPv6-only networks, do not enable IP allowlists. Doing so will block some or all users connecting over IPv6.
