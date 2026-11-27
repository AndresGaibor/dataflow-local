---
title: "Qlik Data Gateway - Direct Access"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data"]
---

# Qlik Data Gateway - Direct Access

Businesses commonly enforce strict firewall policies that block external access to their data sources. This presents a challenge when such businesses need to access their data from the cloud for analytics. Qlik Data Gateway - Direct Access overcomes this challenge by eliminating the need to open inbound firewall ports. Operating behind your organization’s firewall, the Direct Access gateway allows Qlik Sense SaaS applications to securely access behind-the-firewall data, over a strictly outbound, encrypted, and mutually authenticated connection.

Information noteThe Direct Access gateway documentation always reflects the capabilities of the latest application version. If you’re not using the latest version, your system administrator is encouraged to upgrade immediately. For more information, see [*Qlik Data Gateway - Direct Access version history*](direct-access-gateway-upgrading.htm#version).

Qlik Cloud Government noteQlik Cloud Government supports using Qlik Data Gateway - Direct Access when the Windows platform where Qlik Data Gateway - Direct Access is installed is configured to run in a FIPS 140-2 approved mode of operation, also known as "FIPS mode". For more information, see [*Setting up Qlik Data Gateway - Direct Access*](direct-access-gateway-setting-up.htm#System).

Qlik Data Gateway - Direct Access architecture

![Direct Access Gateway architecture diagram](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/direct-access-gateway_architecture1.png "Click to view full size")

The high-level communication sequence is as follows:

1. The Direct Access gateway establishes a mutually authenticated and encrypted connection to Qlik Cloud, using HTTPS.
2. Qlik Cloud sends a load statement (query) to the Direct Access gateway.
3. The Direct Access gateway relays the query to the relevant data source.
4. The data is then pushed (streamed) directly from the data source to Qlik Cloud over WSS.

Information noteData is always in transit and never physically resides on the Direct Access gateway server. A unique key-pair is established for each Direct Access gateway server connected to the Qlik Cloud tenant. This key pair is used for authentication and for end-to-end data encryption on top of the HTTPS transport level encryption.

## Learn more

- [*Setting up Qlik Data Gateway - Direct Access*](direct-access-gateway-setting-up.htm)
- [*Managing the Qlik Data Gateway - Direct Access server*](direct-access-gateway-managing.htm)
- [*Managing Qlik Data Gateway - Direct Access in Administration*](direct-access-gateway-managing-console.htm)
- [*Viewing and running benchmark tests*](direct-access-gateway-managing-console.htm#ViewingBenchmarks)
- [*Upgrading and uninstalling Qlik Data Gateway - Direct Access*](direct-access-gateway-upgrading.htm)
- [*Configuring AWS PrivateLink for Qlik Data Gateway - Direct Access*](direct-access-gateway-aws-privatelink.htm)
