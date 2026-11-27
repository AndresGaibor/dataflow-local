---
title: "Allowlisting domains and IP addresses"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qlik-cloud-dns-ip.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud"]
---

# Allowlisting domains and IP addresses

Expand/Collapse all

# Allowlisting domains and IP addresses

To ensure Qlik Cloud works correctly, you may need to allowlist certain domains and IP addresses in your firewall or proxy. This allows Qlik Cloud services, automations, connectors, and sessions to communicate reliably with your systems.

Traffic from Qlik Cloud to your systems may include:

- Connecting to your databases or other data sources
- Accessing SMTP servers
- Sending webhooks

Traffic from your systems to Qlik Cloud may include:

- Making API calls
- Using multi-cloud features
- Starting Qlik Cloud sessions

You may also need to allowlist external domains to access resources such as fonts, help pages, or integrations.

Qlik Cloud Government noteFor Qlik Cloud Government IP addresses, contact Qlik Support.

## Allowlisting traffic from Qlik Cloud

The following tables list the regional static IPv4 addresses and IPv6 CIDR blocks per tenant region that Qlik Cloud services use to communicate with customer systems.

Add the IPs for your region to your firewall or proxy allowlist to ensure reliable connectivity. You can identify your region from your tenant URL, which uses the format <tenantname>.<region-identifier>.qlikcloud.com.

Information noteDetailed information about these IP addresses is not available.

Information note

**IPv6 address allocation:** Qlik Cloud assigns unique IPv6 addresses to individual compute instances, not a single shared static address per region. The IPv6 CIDR blocks listed below represent the address ranges allocated to each region.

### Generally required static IP addresses

These static IPv4 and IPv6 addresses are used by Qlik Cloud services to communicate with customer systems. Add the IPs for your region to your firewall or proxy allowlist. You may also need to add these IPs to your tenant-level allowlist to allow inbound connections to your Qlik Cloud tenant.

Generally required static IP addresses

IP addresses per region for Qlik Cloud traffic

| Region name | Tenant URL region identifier | IPv4 addresses | IPv6 CIDR blocks |
| --- | --- | --- | --- |
| US East (North Virginia) | us | 18.205.71.36 18.232.32.199 34.237.68.254 | 2600:1f18:47d8:5a00::/64 2600:1f18:47d8:5a01::/64 2600:1f18:47d8:5a02::/64 2600:1f18:47d8:5a12::/64 2600:1f18:47d8:5a13::/64 |
| Asia Pacific (Mumbai) | in | 52.66.18.8 13.201.250.59 15.207.252.34 | 2406:da1a:b0f:8300::/64 2406:da1a:b0f:8301::/64 2406:da1a:b0f:8302::/64 2406:da1a:b0f:8312::/64 2406:da1a:b0f:8314::/64 |
| Asia Pacific (Singapore) | sg | 18.138.163.172 18.142.157.182 54.179.13.251 | 2406:da18:63c:b000::/64 2406:da18:63c:b001::/64 2406:da18:63c:b002::/64 2406:da18:63c:b012::/64 2406:da18:63c:b013::/64 |
| Asia Pacific (Sydney) | ap | 13.210.43.241 13.236.104.42 13.236.206.172 | 2406:da1c:69d:8600::/64 2406:da1c:69d:8601::/64 2406:da1c:69d:8602::/64 2406:da1c:69d:8612::/64 2406:da1c:69d:8614::/64 |
| Asia Pacific (Tokyo) | jp | 54.238.168.131 3.113.68.20 35.73.207.58 | 2406:da14:1276:b600::/64 2406:da14:1276:b601::/64 2406:da14:1276:b602::/64 2406:da14:1276:b612::/64 2406:da14:1276:b614::/64 |
| Canada (Montréal) | ca | 35.182.210.115 16.52.25.164 3.97.150.131 | 2600:1f11:445:ae00::/64 2600:1f11:445:ae01::/64 2600:1f11:445:ae02::/64 2600:1f11:445:ae12::/64 2600:1f11:445:ae14::/64 |
| Europe (Frankfurt) | de | 3.76.162.169 3.77.162.68 3.122.137.91 | 2a05:d014:2cd:7e00::/64 2a05:d014:2cd:7e01::/64 2a05:d014:2cd:7e02::/64 2a05:d014:2cd:7e13::/64 2a05:d014:2cd:7e14::/64 |
| Europe (Ireland) | eu | 34.247.21.179 52.31.212.214 54.154.95.18 | 2a05:d018:1703:a200::/64 2a05:d018:1703:a201::/64 2a05:d018:1703:a202::/64 2a05:d018:1703:a212::/64 2a05:d018:1703:a213::/64 |
| Europe (London) | uk | 13.42.141.246 18.135.245.97 35.179.0.171 | 2a05:d01c:d94:6600::/64 2a05:d01c:d94:6601::/64 2a05:d01c:d94:6602::/64 2a05:d01c:d94:6612::/64 2a05:d01c:d94:6614::/64 |
| Europe (Paris) | fr | 15.236.44.136 15.188.250.12 35.181.228.177 | 2a05:d012:535:3a00::/64 2a05:d012:535:3a01::/64 2a05:d012:535:3a02::/64 2a05:d012:535:3a12::/64 2a05:d012:535:3a14::/64 |
| Europe (Stockholm) | se | 13.51.129.105 16.170.33.251 16.170.27.83 | 2a05:d016:e4f:3200::/64 2a05:d016:e4f:3201::/64 2a05:d016:e4f:3202::/64 2a05:d016:e4f:3212::/64 2a05:d016:e4f:3214::/64 |
| Israel (Tel Aviv) | il | 51.17.198.2 51.17.227.118 51.84.30.13 | 2a05:d025:215:2b00::/64 2a05:d025:215:2b01::/64 2a05:d025:215:2b02::/64 2a05:d025:215:2b12::/64 2a05:d025:215:2b14::/64 |
| Middle East (UAE) | ae | 40.172.103.16 40.172.135.154 40.172.134.184 | 2406:da17:554:1e00::/64 2406:da17:554:1e01::/64 2406:da17:554:1e02::/64 2406:da17:554:1e12::/64 2406:da17:554:1e14::/64 |
| South America (São Paulo) | br | 56.125.3.105 18.231.207.106 54.94.46.71 | 2600:1f1e:733:df00::/64 2600:1f1e:733:df01::/64 2600:1f1e:733:df02::/64 2600:1f1e:733:df12::/64 2600:1f1e:733:df14::/64 |

### Static IP addresses required for Qlik Automate

These static IPv4 and IPv6 addresses are used by Qlik Automate to communicate with your systems. Add the IPs for your region to your firewall or proxy allowlist. You may also need to add these IPs to your tenant-level allowlist to allow inbound connections to your Qlik Cloud tenant.

Static IP addresses required for Qlik Automate

IP addresses per region for Qlik Automate

| Region name | Tenant URL region identifier | IPv4 addresses | IPv6 CIDR blocks |
| --- | --- | --- | --- |
| US East (North Virginia) | us | 18.235.133.252 3.217.244.242 18.214.8.201 | 2600:1f18:47d8:5a0c::/64 2600:1f18:47d8:5a0d::/64 2600:1f18:47d8:5a0e::/64 2600:1f18:47d8:5a0f::/64 2600:1f18:47d8:5a10::/64 2600:1f18:47d8:5a11::/64 |
| Asia Pacific (Mumbai) | in | 3.109.34.226 15.206.64.196 3.6.11.209 | 2406:da1a:b0f:830c::/64 2406:da1a:b0f:830d::/64 2406:da1a:b0f:830e::/64 2406:da1a:b0f:830f::/64 2406:da1a:b0f:8310::/64 2406:da1a:b0f:8311::/64 |
| Asia Pacific (Singapore) | sg | 54.169.84.213 13.213.173.37 13.213.113.162 | 2406:da18:63c:b00c::/64 2406:da18:63c:b00d::/64 2406:da18:63c:b00e::/64 2406:da18:63c:b00f::/64 2406:da18:63c:b010::/64 2406:da18:63c:b011::/64 |
| Asia Pacific (Sydney) | ap | 54.206.158.27 3.104.137.20 3.24.52.178 | 2406:da1c:69d:860c::/64 2406:da1c:69d:860d::/64 2406:da1c:69d:860e::/64 2406:da1c:69d:860f::/64 2406:da1c:69d:8610::/64 2406:da1c:69d:8611::/64 |
| Asia Pacific (Tokyo) | jp | 35.77.238.13 13.115.58.233 35.74.220.230 | 2406:da14:1276:b60c::/64 2406:da14:1276:b60d::/64 2406:da14:1276:b60e::/64 2406:da14:1276:b60f::/64 2406:da14:1276:b610::/64 2406:da14:1276:b611::/64 |
| Canada (Montréal) | ca | 99.79.172.236 3.96.94.72 16.54.218.81 | 2600:1f11:445:ae0c::/64 2600:1f11:445:ae0d::/64 2600:1f11:445:ae0e::/64 2600:1f11:445:ae0f::/64 2600:1f11:445:ae10::/64 2600:1f11:445:ae11::/64 |
| Europe (Frankfurt) | de | 3.69.132.138 3.69.222.86 3.72.136.160 | 2a05:d014:2cd:7e0c::/64 2a05:d014:2cd:7e0d::/64 2a05:d014:2cd:7e0e::/64 2a05:d014:2cd:7e0f::/64 2a05:d014:2cd:7e10::/64 2a05:d014:2cd:7e11::/64 |
| Europe (Ireland) | eu | 54.216.156.88 3.248.156.131 52.213.44.55 | 2a05:d018:1703:a20c::/64 2a05:d018:1703:a20d::/64 2a05:d018:1703:a20e::/64 2a05:d018:1703:a20f::/64 2a05:d018:1703:a210::/64 2a05:d018:1703:a211::/64 |
| Europe (London) | uk | 18.168.120.199 18.169.91.38 13.42.135.168 | 2a05:d01c:d94:660c::/64 2a05:d01c:d94:660d::/64 2a05:d01c:d94:660e::/64 2a05:d01c:d94:660f::/64 2a05:d01c:d94:6610::/64 2a05:d01c:d94:6611::/64 |
| Europe (Paris) | fr | 35.181.235.154 13.38.237.231 13.37.77.179 | 2a05:d012:535:3a0c::/64 2a05:d012:535:3a0d::/64 2a05:d012:535:3a0e::/64 2a05:d012:535:3a0f::/64 2a05:d012:535:3a10::/64 2a05:d012:535:3a11::/64 |
| Europe (Stockholm) | se | 13.53.211.145 13.50.63.235 13.60.101.12 | 2a05:d016:e4f:320c::/64 2a05:d016:e4f:320d::/64 2a05:d016:e4f:320e::/64 2a05:d016:e4f:320f::/64 2a05:d016:e4f:3210::/64 2a05:d016:e4f:3211::/64 |
| Israel (Tel Aviv) | il | 51.84.43.188 51.17.145.45 51.84.44.145 | 2a05:d025:215:2b0c::/64 2a05:d025:215:2b0d::/64 2a05:d025:215:2b0e::/64 2a05:d025:215:2b0f::/64 2a05:d025:215:2b10::/64 2a05:d025:215:2b11::/64 |
| Middle East (UAE) | ae | 40.172.75.127 40.172.171.244 40.172.92.216 | 2406:da17:554:1e0c::/64 2406:da17:554:1e0d::/64 2406:da17:554:1e0e::/64 2406:da17:554:1e0f::/64 2406:da17:554:1e10::/64 2406:da17:554:1e11::/64 |
| South America (São Paulo) | br | 54.207.174.200 54.207.184.180 54.94.103.110 | 2600:1f1e:733:df0c::/64 2600:1f1e:733:df0d::/64 2600:1f1e:733:df0e::/64 2600:1f1e:733:df0f::/64 2600:1f1e:733:df10::/64 2600:1f1e:733:df11::/64 |

### Static IP addresses required for SaaS connectors in Data Integration

These IPv4 and IPv6 addresses are used by Qlik Cloud SaaS connectors to communicate with your tenant. Add the IPs for your region to your firewall or proxy allowlist. Tenant-level allowlisting is not required for SaaS connectors.

Static IP addresses required for SaaS connectors in Data Integration

IP addresses per region for SaaS connectors in Data Integration

| Region name | Tenant URL region identifier | IPv4 addresses | IPv6 CIDR blocks |
| --- | --- | --- | --- |
| US East (North Virginia) | us | 23.21.238.161 34.232.203.146 44.212.174.31 | 2600:1f18:47d8:5a15::/64 2600:1f18:47d8:5a16::/64 2600:1f18:47d8:5a17::/64 |
| Asia Pacific (Singapore) | sg | 46.137.230.180 13.228.215.246 13.250.148.59 | 2406:da18:63c:b015::/64 2406:da18:63c:b016::/64 2406:da18:63c:b017::/64 |
| Asia Pacific (Sydney) | ap | 52.63.245.121 13.210.87.204 13.237.124.90 | 2406:da1c:69d:8615::/64 2406:da1c:69d:8616::/64 2406:da1c:69d:8617::/64 |
| Asia Pacific (Tokyo) | jp | 35.76.22.32 43.206.71.15 54.92.37.71 | 2406:da14:1276:b615::/64 2406:da14:1276:b616::/64 2406:da14:1276:b617::/64 |
| Asia Pacific (Mumbai) | in | 13.202.192.86 43.205.184.187 13.233.6.79 | 2406:da1a:b0f:8315::/64 2406:da1a:b0f:8316::/64 2406:da1a:b0f:8317::/64 |
| Canada (Montréal) | ca | 15.157.123.91 15.223.140.179 35.182.206.133 | 2600:1f11:445:ae15::/64 2600:1f11:445:ae16::/64 2600:1f11:445:ae17::/64 |
| Europe (Frankfurt) | de | 3.74.21.144 35.157.50.219 3.75.166.31/32 | 2a05:d014:2cd:7e15::/64 2a05:d014:2cd:7e16::/64 2a05:d014:2cd:7e17::/64 |
| Europe (Ireland) | eu | 52.211.180.19 52.48.201.148 54.247.165.17 | 2a05:d018:1703:a215::/64 2a05:d018:1703:a216::/64 2a05:d018:1703:a217::/64 |
| Europe (London) | uk | 13.42.85.5 18.168.59.160 13.42.139.68 | 2a05:d01c:d94:6615::/64 2a05:d01c:d94:6616::/64 2a05:d01c:d94:6617::/64 |
| Europe (Paris) | fr | 51.44.129.69 15.237.170.173 13.37.75.163 | 2a05:d012:535:3a15::/64 2a05:d012:535:3a16::/64 2a05:d012:535:3a17::/64 |
| Europe (Stockholm) | se | 51.21.123.49 13.50.254.253 51.21.139.3 | 2a05:d016:e4f:3215::/64 2a05:d016:e4f:3216::/64 2a05:d016:e4f:3217::/64 |
| Israel (Tel Aviv) | il | 51.17.142.170 51.17.144.48 51.17.177.88 | 2a05:d025:215:2b15::/64 2a05:d025:215:2b16::/64 2a05:d025:215:2b17::/64 |
| Middle East (UAE) | ae | 40.172.104.210 40.172.44.255 40.172.29.37 | 2406:da17:554:1e15::/64 2406:da17:554:1e16::/64 2406:da17:554:1e17::/64 |
| South America (São Paulo) | br | 18.231.16.63 54.232.67.215 18.231.66.252 | 2600:1f1e:733:df15::/64 2600:1f1e:733:df16::/64 2600:1f1e:733:df17::/64 |

## Allowlisting traffic from your systems to Qlik Cloud

The table below lists the regional static IPv4 and IPv6 addresses required for API calls, multi-cloud features, and Qlik Cloud sessions. IPs are specific to each tenant region.

Add the IPs for your region to your firewall or proxy allowlist to ensure reliable connectivity. You can identify your region from your tenant URL, which uses the format <tenantname>.<region-identifier>.qlikcloud.com.

Traffic may pass through a load balancer and use dynamic source IPs. To prevent blocked connections, allow Qlik Cloud static IPs for your region as destination addresses.

### Static IP addresses required for traffic to Qlik Cloud

Static IP addresses required for traffic to Qlik Cloud

IP addresses per region for traffic to Qlik Cloud

| Region name | Tenant URL region identifier | IPv4 addresses | IPv6 addresses |
| --- | --- | --- | --- |
| US East (North Virginia) | us | 3.233.118.242 34.234.80.90 44.215.23.130 | 2600:9000:a41a:672a:4979:e5f4:8b14:f052 2600:9000:a51a:cee6:19ae:c7e8:7915:64ff |
| Asia Pacific (Mumbai) | in | 3.108.106.180 3.6.57.94 65.1.6.215 | 2600:9000:a41a:672a:8139:7048:17c3:ecca 2600:9000:a51a:cee6:3459:1825:89f0:6d81 |
| Asia Pacific (Singapore) | sg | 3.1.207.89 18.138.83.27 52.74.26.118 | 2600:9000:a41a:672a:cc81:6b48:ae8c:674b 2600:9000:a51a:cee6:4017:b18d:6aa9:4c76 |
| Asia Pacific (Sydney) | ap | 13.54.144.196 13.55.228.248 52.64.134.232 | 2600:9000:a41a:672a:cb7f:d91c:9510:75d0 2600:9000:a51a:cee6:60dc:36c6:7b15:3986 |
| Asia Pacific (Tokyo) | jp | 13.115.5.27 18.179.235.68 52.69.157.151 | 2600:9000:a41a:672a:49c:d1c8:f0ba:a505 2600:9000:a51a:cee6:98e7:af6b:eb22:dcc6 |
| Canada (Montréal) | ca | 15.157.222.216 15.222.166.154 3.96.25.177 | 2600:9000:a419:8e3b:73e0:ff2f:9721:3c72 2600:9000:a715:7a5d:6474:15b9:5ce7:c737 |
| Europe (Frankfurt) | de | 3.67.51.47 18.193.162.245 52.58.113.105 | 2600:9000:a41a:672a:2720:d401:27c8:e5e7 2600:9000:a51a:cee6:e1d:6412:c397:d9a0 |
| Europe (Ireland) | eu | 99.81.122.190 108.128.157.152 108.129.46.246 | 2600:9000:a41a:672a:fe95:cda2:f91f:4f74 2600:9000:a51a:cee6:1df1:f6a:40b7:1f6c |
| Europe (London) | uk | 13.41.125.158 18.168.223.169 18.169.70.63 | 2600:9000:a41a:672a:1ccd:4ca5:2518:fc21 2600:9000:a51a:cee6:3c58:828d:6cd7:d541 |
| Europe (Paris) | fr | 15.188.225.140 35.180.171.215 35.181.3.153 | 2600:9000:a41a:672a:ae69:ddcd:6477:8d51 2600:9000:a51a:cee6:5ec4:878:afc4:d58b |
| Europe (Stockholm) | se | 16.171.102.151 51.20.24.0 51.20.149.100 | 2600:9000:a41a:672a:6614:b4e1:9a27:ceb 2600:9000:a51a:cee6:99f9:4d3f:8c0b:37cb |
| Israel (Tel Aviv) | il | 51.16.223.21 51.84.154.171 51.84.163.93 | 2600:9000:a41a:672a:c543:95c1:6814:b48f 2600:9000:a51a:cee6:9d6a:2bd9:77c:b63e |
| Middle East (UAE) | ae | 40.172.175.160 40.172.175.4 40.172.51.16 | 2600:9000:a41a:672a:f3c3:e0d1:1fd8:8086 2600:9000:a51a:cee6:aee7:6e62:ff46:8885 |
| South America (São Paulo) | br | 52.67.104.212 54.232.175.93 56.125.17.93 | 2600:9000:a41a:672a:b7fb:35b2:76da:7852 2600:9000:a51a:cee6:8a5b:ca12:7809:70ea |

## Tenant-level allowlisting

Tenant-level allowlisting is configured within your Qlik Cloud tenant. It controls which external services or IP addresses can directly access your tenant. This is different from allowlisting in your network firewall or proxy, which controls traffic between your systems and Qlik Cloud.

If you use Qlik Automate, toolkits, gateways, or other external services, review the next section.

For step-by-step instructions on configuring allowlists, see [*Managing IP allowlists*](../Admin/manage-ip-allowlists.htm).

### Services that require allowlisting

The following table shows which Qlik Cloud services and capabilities require tenant-level allowlisting, along with the specific requirements for each.

Services that require tenant-level allowlisting

Allowlist requirements for Qlik Cloud services

| Service or capability | Allowlisting requirement |
| --- | --- |
| Embedding | Requires allowlisting of accessing clients. If traffic is proxied through a trusted service, only the proxy must be allowlisted. |
| Data gateway | Requires allowlisting of the gateway host. |
| Data transfer | Requires allowlisting of the data transfer host. |
| Multi-cloud distribution | Requires allowlisting of client-managed distribution hosts. |
| Qlik Automate – in tenant connectors  (Qlik Cloud Services, Qlik Reporting, Qlik Predict, Qlik Cloud Data Integration, Qlik Answers, Qlik Cloud Catalog) | No allowlisting required, unless webhooks are used from the Qlik Cloud Services connector. In that case, allowlist the source region's [generally required static IPs](#Static). |
| Qlik Automate – out-tenant connectors  (for example, Qlik Platform Operations, Call URL, API key, OAuth) | Requires allowlisting of the source region's [Qlik Automate IPs](#Static3). |
| Webhooks (including webhook automations) | Requires allowlisting of the source region's [generally required static IPs](#Static). |
| Data connections (excluding Data Integration SaaS connectors) | Requires allowlisting of the source region's [generally required static IPs](#Static). |
| Data Integration SaaS connectors | Not applicable. These cannot connect to a Qlik Cloud tenant. |

Information noteIn case of a disaster recovery (DR) event, Qlik Cloud IP addresses will change. Update the tenant-level allowlist for any tenants using Qlik connector packages in the affected region. New IP addresses will be published by Qlik.

## Domain allowlisting

Some Qlik Cloud resources are hosted on external domains and CDNs. Allowlisting these domains ensures full functionality, including fonts, help pages, and integrations.

Domains to allowlist

Allowlist domains for Qlik Cloud services

| Category | Domain | Purpose |
| --- | --- | --- |
| General | \*.qlikcloud.com | Required for core user experience and API calls from all user interfaces. |
| Authentication | cdn.auth0.com | Required for users authenticating via Qlik Account. |
| Authentication | cdn.myqlik.qlik.com | Required for users authenticating via Qlik Account. |
| Authentication | login.qlik.com | Required for users authenticating via Qlik Account. |
| Authentication | myqlik.qlik.com | Required for users authenticating via Qlik Account. |
| Authentication | qlikidp-prod.guardian.auth0.com | Required for users authenticating via Qlik Account and using MFA. |
| Authentication | unpkg.com | Required for users authenticating via Qlik Account. |
| User interface | cdnjs.cloudflare.com | Serves resources and frameworks for the user interface. |
| User interface | fonts.googleapis.com | Serves fonts for the user interface. |
| User interface | fonts.gstatic.com | Serves fonts for the user interface. |
| User interface | gravatar.com | Serves the profile icon for the logged-in user. |
| Resource center & notifications | \*.ada.support | Required for serving the Qlik help bot on the tenant. |
| Resource center & notifications | cdn.pendo.io | Required for serving notification content such as What's new, Learn, Help, support chats, and some other feature and deprecation related UI notifications. |
| Resource center & notifications | help.qlik.com | Required for serving notification content such as What's new, Learn, Help, support chats, and some other feature and deprecation related UI notifications. |
| Resource center & notifications | i.ytimg.com | Required for serving notification content such as What's new, Learn, Help, support chats, and some other feature and deprecation related UI notifications. |
| Resource center & notifications | pendo-static-5763789454311424.storage.googleapis.com | Required for serving notification content such as What's new, Learn, Help, support chats, and some other feature and deprecation related UI notifications. |
| Resource center & notifications | play.vidyard.com | Required for serving video content used in Qlik Help pages and notifications. |
| Resource center & notifications | www.qlik.com | Required for serving notification content such as What's new, Learn, Help, support chats, and some other feature and deprecation related UI notifications. |
| Resource center & notifications | www.youtube-nocookie.com | Required for serving notification content such as What's new, Learn, Help, support chats, and some other feature and deprecation related UI notifications. |
| Account management | www.zuora.com | Required for digital purchase subscriptions. |
| Features & telemetry | api.qlikdataengineering.com | Provides Qlik with telemetry used for feature development, anomaly detection, and issue detection. |
| Features & telemetry | app.launchdarkly.com | Required for feature enablement and telemetry on the tenant. |
| Features & telemetry | clientsdk.launchdarkly.com | Required for feature enablement and telemetry on the tenant. |
| Features & telemetry | events.launchdarkly.com | Required for feature enablement and telemetry on the tenant. |
| Features & telemetry | \*.sentry.io | Provides Qlik with telemetry used for application error tracking and crash reporting. |
| Features & telemetry | sqs.us-east-1.amazonaws.com | Provides Qlik with telemetry used by data engineering to capture UI events. |
| Features & telemetry | www.google-analytics.com | Provides Qlik with telemetry used for feature development, anomaly detection, and issue detection. |

Copy-paste list (all domains above, one per line):

```
*.qlikcloud.com
cdn.auth0.com
cdn.myqlik.qlik.com
login.qlik.com
myqlik.qlik.com
qlikidp-prod.guardian.auth0.com
unpkg.com
cdnjs.cloudflare.com
fonts.googleapis.com
fonts.gstatic.com
gravatar.com
*.ada.support
cdn.pendo.io
help.qlik.com
i.ytimg.com
pendo-static-5763789454311424.storage.googleapis.com
play.vidyard.com
www.qlik.com
www.youtube-nocookie.com
www.zuora.com
api.qlikdataengineering.com
app.launchdarkly.com
clientsdk.launchdarkly.com
events.launchdarkly.com
*.sentry.io
sqs.us-east-1.amazonaws.com
www.google-analytics.com
```

### Network Integration domains for AWS

These domains are required in addition to the domains above for customers running Network Integration on AWS. No IP address changes are needed, because the existing regional static IP addresses already cover Network Integration. Replace `<aws_region>` with your AWS region and `<your_s3_bucket>` with your own bucket name.

Domains to allowlist for Network Integration on AWS

Domains to allowlist for Network Integration on AWS

| Domain | Purpose |
| --- | --- |
| metrics.gateway.qlikcloud.com | Sends metrics to Qlik Cloud. Already covered if you allowlist `*.qlikcloud.com`. |
| rolesanywhere.amazonaws.com | IAM Roles Anywhere: credential helper binary. |
| rolesanywhere.us-east-1.amazonaws.com | IAM Roles Anywhere: credentials. |
| api.ecr.us-east-1.amazonaws.com | ECR API, authentication. |
| 433987883887.dkr.ecr.us-east-1.amazonaws.com | ECR Docker registry (NI containers). |
| prod-us-east-1-starport-layer-bucket.s3.us-east-1.amazonaws.com | Container image layers. |
| <your\_s3\_bucket>.s3.amazonaws.com  <your\_s3\_bucket>.s3.<aws\_region>.amazonaws.com  <your\_s3\_bucket>.s3.us-east-1.amazonaws.com | Customer's own S3 bucket used in the integration. |
| qlik-upsolver-data-plane-config-us-east-1.s3.amazonaws.com  qlik-upsolver-data-plane-config-us-east-1.s3.<aws\_region>.amazonaws.com  qlik-upsolver-data-plane-config-us-east-1.s3.us-east-1.amazonaws.com | Configuration bucket. |
| qlik-upsolver-prod-fluentd-log-us-east-1.s3.amazonaws.com  qlik-upsolver-prod-fluentd-log-us-east-1.s3.<aws\_region>.amazonaws.com  qlik-upsolver-prod-fluentd-log-us-east-1.s3.us-east-1.amazonaws.com | Logs bucket. |
| qlik-upsolver-prod-tasks-cache-us-east-1.s3.amazonaws.com  qlik-upsolver-prod-tasks-cache-us-east-1.s3.<aws\_region>.amazonaws.com  qlik-upsolver-prod-tasks-cache-us-east-1.s3.us-east-1.amazonaws.com | Tasks cache bucket. |
| qlik-upsolver-prod-thread-dumps-us-east-1.s3.amazonaws.com  qlik-upsolver-prod-thread-dumps-us-east-1.s3.<aws\_region>.amazonaws.com  qlik-upsolver-prod-thread-dumps-us-east-1.s3.us-east-1.amazonaws.com | Thread dumps bucket. |
| upsolver-prod-file-reporter-us-east-1.s3.amazonaws.com  upsolver-prod-file-reporter-us-east-1.s3.<aws\_region>.amazonaws.com  upsolver-prod-file-reporter-us-east-1.s3.us-east-1.amazonaws.com | File reporter bucket. |
| upsolver-prod-task-run-events-us-east-1.s3.amazonaws.com  upsolver-prod-task-run-events-us-east-1.s3.<aws\_region>.amazonaws.com  upsolver-prod-task-run-events-us-east-1.s3.us-east-1.amazonaws.com | Task run events bucket. |
| kinesis.us-east-1.amazonaws.com | Metrics sent to Kinesis. |
| autoscaling.<aws\_region>.amazonaws.com | Autoscaling. |
| glue.<aws\_region>.amazonaws.com | Glue data catalog. |
| kms.<aws\_region>.amazonaws.com | Key management. |
| monitoring.<aws\_region>.amazonaws.com | Monitoring. |
| ssm.<aws\_region>.amazonaws.com | Systems Manager. |
| sts.<aws\_region>.amazonaws.com | Security Token Service. |

Copy-paste list (one per line):

```
metrics.gateway.qlikcloud.com
rolesanywhere.amazonaws.com
rolesanywhere.us-east-1.amazonaws.com
api.ecr.us-east-1.amazonaws.com
433987883887.dkr.ecr.us-east-1.amazonaws.com
prod-us-east-1-starport-layer-bucket.s3.us-east-1.amazonaws.com
<your_s3_bucket>.s3.amazonaws.com
<your_s3_bucket>.s3.<aws_region>.amazonaws.com
<your_s3_bucket>.s3.us-east-1.amazonaws.com
qlik-upsolver-data-plane-config-us-east-1.s3.amazonaws.com
qlik-upsolver-data-plane-config-us-east-1.s3.<aws_region>.amazonaws.com
qlik-upsolver-data-plane-config-us-east-1.s3.us-east-1.amazonaws.com
qlik-upsolver-prod-fluentd-log-us-east-1.s3.amazonaws.com
qlik-upsolver-prod-fluentd-log-us-east-1.s3.<aws_region>.amazonaws.com
qlik-upsolver-prod-fluentd-log-us-east-1.s3.us-east-1.amazonaws.com
qlik-upsolver-prod-tasks-cache-us-east-1.s3.amazonaws.com
qlik-upsolver-prod-tasks-cache-us-east-1.s3.<aws_region>.amazonaws.com
qlik-upsolver-prod-tasks-cache-us-east-1.s3.us-east-1.amazonaws.com
qlik-upsolver-prod-thread-dumps-us-east-1.s3.amazonaws.com
qlik-upsolver-prod-thread-dumps-us-east-1.s3.<aws_region>.amazonaws.com
qlik-upsolver-prod-thread-dumps-us-east-1.s3.us-east-1.amazonaws.com
upsolver-prod-file-reporter-us-east-1.s3.amazonaws.com
upsolver-prod-file-reporter-us-east-1.s3.<aws_region>.amazonaws.com
upsolver-prod-file-reporter-us-east-1.s3.us-east-1.amazonaws.com
upsolver-prod-task-run-events-us-east-1.s3.amazonaws.com
upsolver-prod-task-run-events-us-east-1.s3.<aws_region>.amazonaws.com
upsolver-prod-task-run-events-us-east-1.s3.us-east-1.amazonaws.com
kinesis.us-east-1.amazonaws.com
autoscaling.<aws_region>.amazonaws.com
glue.<aws_region>.amazonaws.com
kms.<aws_region>.amazonaws.com
monitoring.<aws_region>.amazonaws.com
ssm.<aws_region>.amazonaws.com
sts.<aws_region>.amazonaws.com
```

### Network Integration domains for GCP

These domains are required in addition to the domains above for customers running Network Integration on GCP. No IP address changes are needed, because the existing regional static IP addresses already cover Network Integration.

Domains to allowlist for Network Integration on GCP

Domains to allowlist for Network Integration on GCP

| Domain | Purpose |
| --- | --- |
| monitoring.googleapis.com | Monitoring. |
| secretmanager.googleapis.com | Roles Anywhere secret. |
| storage.googleapis.com | GCS buckets. |
| metrics.gateway.qlikcloud.com | Telegraf metrics to Qlik Cloud. Already covered if you allowlist `*.qlikcloud.com`. |
| rolesanywhere.amazonaws.com | Credential helper binary. |
| rolesanywhere.us-east-1.amazonaws.com | Credentials. |
| api.ecr.us-east-1.amazonaws.com | ECR API, authentication. |
| 433987883887.dkr.ecr.us-east-1.amazonaws.com | ECR Docker registry (NI containers). |
| prod-us-east-1-starport-layer-bucket.s3.us-east-1.amazonaws.com | Container image layers. |
| qlik-upsolver-data-plane-config-us-east-1.s3.amazonaws.com | Configuration bucket. |
| qlik-upsolver-prod-fluentd-log-us-east-1.s3.us-east-1.amazonaws.com | Logs bucket. |
| qlik-upsolver-prod-tasks-cache-us-east-1.s3.us-east-1.amazonaws.com | Tasks cache bucket. |
| qlik-upsolver-prod-thread-dumps-us-east-1.s3.us-east-1.amazonaws.com | Thread dumps bucket. |
| upsolver-prod-file-reporter-us-east-1.s3.us-east-1.amazonaws.com | File reporter bucket. |
| upsolver-prod-task-run-events-us-east-1.s3.us-east-1.amazonaws.com | Task run events bucket. |
| kinesis.us-east-1.amazonaws.com | Metrics sent to Kinesis. |

Copy-paste list (one per line):

```
monitoring.googleapis.com
secretmanager.googleapis.com
storage.googleapis.com
metrics.gateway.qlikcloud.com
rolesanywhere.amazonaws.com
rolesanywhere.us-east-1.amazonaws.com
api.ecr.us-east-1.amazonaws.com
433987883887.dkr.ecr.us-east-1.amazonaws.com
prod-us-east-1-starport-layer-bucket.s3.us-east-1.amazonaws.com
qlik-upsolver-data-plane-config-us-east-1.s3.amazonaws.com
qlik-upsolver-prod-fluentd-log-us-east-1.s3.us-east-1.amazonaws.com
qlik-upsolver-prod-tasks-cache-us-east-1.s3.us-east-1.amazonaws.com
qlik-upsolver-prod-thread-dumps-us-east-1.s3.us-east-1.amazonaws.com
upsolver-prod-file-reporter-us-east-1.s3.us-east-1.amazonaws.com
upsolver-prod-task-run-events-us-east-1.s3.us-east-1.amazonaws.com
kinesis.us-east-1.amazonaws.com
```
