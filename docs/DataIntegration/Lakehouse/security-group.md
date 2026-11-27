---
title: "Security group"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/security-group.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in AWS"]
---

# Security group

Create a security group in your AWS account, which is required for creating a network integration.

A security group acts as a virtual firewall that controls inbound and outbound traffic to your resources, such as EC2 instances. It defines rules that specify what traffic is allowed in and out based on IP addresses, protocols, and ports.

The security group defines:

- The types of inbound traffic, for example SSH, or HTTP, that is allowed to reach the instance.
- The types of outbound traffic the instance can send out.

When you launch an instance, such as an EC2 server, you associate it with one or more security groups. If you don't specify a group, AWS applies the default security group for the VPC. Security groups are applied directly to instances, not to subnets. If two instances are in the same subnet, they can have different security groups with different traffic rules. For example, you can allow SSH (port 22) only from your local IP address while blocking all other traffic.

## Prerequisites

Ensure you have:

- Created the VPC and subnet and Availability Zones for hosting your Qlik Open Lakehouse.
- The CIDR range of your VPC.

## Creating a security group

To create a security group, do the following:

1. In the AWS console, go to EC2.
2. In the side menu, under Network & Security, select Security Groups.
3. On the Security Groups page, click Create security group.
4. Configure the Basic details:

- Security group name: Enter a name for your security group.
- Description: Optionally, add a meaningful label to describe the purpose of the security group.
- VPC: From the list, select the ID of the VPC you created previously for running your Qlik Open Lakehouse.

5. In Inbound rules, click Add rule and create it as follows:

- Type: Ensure this is set to All TCP.
- Source: Select Custom and enter the CIDR range of the VPC you created.

6. In Outbound rules, ensure Type is set to All Traffic.
7. Click Create security group and make a note of the Security group ID, which will be prefixed with sg-.
