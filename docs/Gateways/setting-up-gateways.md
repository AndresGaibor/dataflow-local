---
title: "Data gateways"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/setting-up-gateways.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing data governance and transfers"]
---

# Data gateways

Data gateways provide a secure means of accessing or moving firewalled data for use in Qlik Cloud. The gateway is installed behind your organization's firewall, and then registered with the Administration [activity center](#glossary-0 "Glossary term").

There are two fit for purpose data gateways: Qlik Data Gateway - Direct Access for Qlik Cloud Analytics, and Qlik Data Gateway - Data Movement for Qlik Talend Data Integration.

## [*Qlik Data Gateway - Direct Access*](direct-access-gateway.htm)

Qlik Data Gateway - Direct Access allows Qlik Cloud Analytics applications to securely access data sources that are not directly accessible from Qlik Cloud (either because they are firewalled or located in a VPC), over a strictly outbound, encrypted, and mutually authenticated connection.

## [*Qlik Data Gateway - Data Movement*](replication-gateway.htm)

Qlik Data Gateway - Data Movement facilitates data movement from SaaS applications and from enterprise data sources that are not directly accessible from Qlik Cloud (either because they are firewalled or located in a VPC) to supported targets. Data is moved over a strictly outbound, encrypted and mutually authenticated connection. By eliminating the need to open inbound firewall ports, Qlik Data Gateway - Data Movement provides a secure and trusted means of moving your enterprise data.
