---
title: "Firewall and network tags"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/gcp-firewall-network-tags.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in GCP"]
---

# Firewall and network tags

Create firewall rules in your Google Cloud project, which are required for creating a network integration.

A VPC firewall rule acts as a virtual firewall that controls inbound and outbound traffic to your resources, such as Compute Engine instances. Qlik uses a dedicated network tag, for example qlik-lakehouse, to apply the rules to the network integration instances.

The firewall rules define:

- The types of ingress traffic that is allowed to reach the instances.
- The types of egress traffic the instances can send out.

Information noteQlik does not manage firewall rules. You create and manage them.

## Prerequisites

Ensure you have:

- Created the VPC network and subnet for hosting your Qlik Open Lakehouse. For more information, see [*VPC network and subnet*](gcp-vpc-network-subnet.htm).
- The CIDR range of your subnet.

## Creating a firewall rule

To create a firewall rule, do the following:

1. In the Google Cloud console, go to the Firewall policies page.
2. Click Create firewall rule.
3. Configure the rule:

   - Name: Enter a name, for example qlik-lakehouse-allow-internal.
   - Network: Select the VPC network you created previously for running your Qlik Open Lakehouse.
   - Direction of traffic: Select Ingress.
   - Action on match: Select Allow.
   - Targets: Select Specified target tags, and in Target tags, enter a dedicated tag, for example qlik-lakehouse.
   - Source filter: Select IPv4 ranges, and in Source IPv4 ranges, enter the CIDR range of your subnet.
   - Protocols and ports: Select Specified protocols and ports, and select TCP.
4. Click Create and make a note of the network tag.
5. Ensure egress traffic is allowed for the instances.
