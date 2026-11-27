---
title: "Data Movement gateway system requirements"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/dm-gateway-prerequisites.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Qlik Data Gateway - Data Movement"]
---

# Data Movement gateway system requirements

This section describes the prerequisites for using Data Movement gateway as well as any limitations you should be aware of.

Data Movement gateway should be installed on a Linux machine located in the data center or in a VPC (Virtual Private Cloud) network. Do not use a machine that already has Qlik Replicate installed on it.

- Unless you are installing as root, you need sudo permission to run the Data Movement gateway RPM.
- To register a gateway on the tenant, you need tenant admin access.

Tip noteFor optimal performance, install the Data Movement gateway on a server that is as close as possible to your data source.

## Supported Linux platforms

Data Movement gateway is certified for installation on Red Hat 8.x, 9.x, and 10.x (64-bit), and Amazon Linux 2023.

Information noteAlthough Data Movement gateway is certified on Red Hat, it is also supported on corresponding and compatible Linux distributions.

Warning noteInstalling Data Movement gateway on a machine running in FIPS mode is not supported.

## Python version

Most of the supported data sources and targets require at least one driver to be installed on the Data Movement gateway machine. Installing the drivers can be done using the driver installation utility (recommended) or manually. To use the driver installation utility, Python 3.6 or later must be installed on the Data Movement gateway server.

For more information on the driver setup, see the help for the data source or target you are using.

## Ports

Port HTTPS/TCP-443 should be opened for outbound communication to <tenant-id>.<region>.qlikcloud.com.

## Recommended hardware

The recommended hardware is outlined in the table below.

Recommended hardware configurations

|  | Basic System | Large System | Extra-Large System | Notes: |
| --- | --- | --- | --- | --- |
| Processor | Quad core | Quad core base  Dual-core per task | 8-core base  Quad core per task | Additional cores are useful in any of the following situations:   - Many tasks running in parallel - Full-load performance priority - Multiple full-load processes running in parallel |
| Memory | 8 GB | 32 GB | 64 GB | More memory is useful in any of the following situations:   - Many tasks running in parallel - Long-running transactions on the source endpoint (for example, monthly batch processing) - Many active users on the source system |
| Disk requirements (SSD is recommended for optimal performance) | 320 GB | 500 GB  RAID | 500 GB  RAID | A faster disk is useful in any of the following situations:   - Long-running source transactions that may not fit into memory - Using tasks that are set up to continue processing during target outage   A larger disk is required in any of the following situations:   - Using tasks that are set up to continue processing during target outage - Very large source transactions that do not fit into memory   RAID is recommended for system recovery in case of disk failure for all configurations. |
| Network | 1 Gbps | 10 Gbps | Two 10 Gbps | - |
