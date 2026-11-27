---
title: "VPC, subnets and Availability Zones"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/vpc-subnets-azones.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in AWS"]
---

# VPC, subnets and Availability Zones

Configure your AWS VPC to integrate Qlik within your environment.

A Virtual Private Cloud (VPC) is a logically isolated network that enables you to control how AWS resources, such as databases and compute instances, connect to each other and the internet. Each VPC is created within a single AWS region.

Subnets are subdivisions of a VPC used to organize and host resources such as Amazon EC2 instances. Subnets can be:

- Public: Allows direct access to the internet via an Internet Gateway.
- Private: Restricted to internal communication within the VPC. Outbound internet access is available via a NAT Gateway..

Each subnet is created within a specific Availability Zone. For example, in the us-east-1 region, you can create subnets in us-east-1a, us-east-1b, and us-east-1c.

Availability Zones (AZs) are physically isolated data centers within a region. Distributing resources across multiple AZs improves application availability and fault tolerance.

The relationship between the VPC, subnets, and AZs, ensures that:

- A VPC is scoped to a single AWS region and spans all Availability Zones within that region.
- Subnets are bound to individual Availability Zones, providing the ability to distribute resources across zones.
- You can use this structure to deploy resources across multiple AZs within a VPC to enhance availability and resilience.

Information noteSubnets created in the VPC configuration must have a valid route that provides outbound internet access. Public subnets require a route to an Internet Gateway. Private subnets require a route to a NAT Gateway.

## Choosing between public and private subnets

Before creating your VPC, determine which subnet type is appropriate for your deployment:

| Use case | Recommended subnet type |
| --- | --- |
| Resources requiring direct internet access | Public subnet |
| Internet services only | Private subnet |
| Production workloads | Private subnet |
| Secure lakehouse deployments | Private subnet |
| Test or demo environments | Public or private subnet |

Warning noteDo not mix public and private subnet types in the same deployment unless explicitly instructed. Mixed configurations can lead to ambiguous routing and security misconfigurations.

## Creating a VPC

Create your VPC according to your network security requirements. The configurations below are provided as recommendations. Tailor them to your organization's specific needs.

Information noteWhile public subnets are supported, Qlik recommends using private subnets for all deployments to ensure a secure and production-ready environment.

### Qlik recommendations

- Availability Zones: Use 2 or more AZs to ensure high availability and fault tolerance.
- Number of subnets: Deploy at least one subnet per AZ.
- NAT Gateways: For private subnets, use one NAT Gateway per AZ for high availability.
- Subnet size: Subnets sized at /27 or smaller may cause unexpected system behavior and hinder the system's ability to scale and update reliably. Qlik recommends a minimum subnet size of /24 to ensure stable operations and room for future growth.

### Creating a VPC with private subnets

Use this option for secure deployments where resources must not be directly accessible from the internet.

1. In the AWS console, go to VPC > Your VPCs.
2. Click Create VPC.
3. Under Resources to create, select VPC and more.
4. Configure the following settings:
   - Availability Zones (AZs): 2 or more.
   - Number of public subnets: 0.
   - Number of private subnets: As required.
   - NAT gateways: As required.
5. Click Create VPC.
6. After creation, verify that each subnet:
   - Has Auto-assign public IPv4 address disabled.
   - Has a route to the NAT gateway.
   - Does not have a route to an Internet Gateway.

Information notePrivate subnets prevent direct inbound internet access while allowing outbound connectivity through the NAT Gateway. This is the recommended configuration for production workloads

## Configuration summary

After completing either option, record the following for use in subsequent configuration steps:

- VPC ID
- VPC CIDR range
- Subnets IDs
- Availability Zone for each subnet
- Subnet designation (public or private)
