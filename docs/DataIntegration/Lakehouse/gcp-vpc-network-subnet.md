---
title: "VPC network and subnet"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/gcp-vpc-network-subnet.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in GCP"]
---

# VPC network and subnet

Configure your Google Cloud VPC network and subnet to integrate Qlik within your environment.

A Virtual Private Cloud (VPC) network is a global, logically isolated network in Google Cloud that spans all regions. It controls how Google Cloud resources, such as Compute Engine instances, connect to each other and to the internet.

Subnets are regional subdivisions of a VPC network, used to organize and host resources such as Compute Engine instances. Each subnet has a primary IP range and is created in a specific region.

Qlik-managed instances do not have external IP addresses. For the cluster to start, the subnet must provide:

- Outbound internet access through Cloud NAT in the region of the subnet.
- Access to Google APIs through Private Google Access enabled on the subnet.

## Creating a VPC network and subnet

Create your VPC network according to your network security requirements. The configurations below are provided as recommendations. Tailor them to your organization's specific needs.

### Qlik recommendations

- Region: Create the subnet in the region where you plan to deploy the resources.
- Subnet size: Use a subnet with sufficient free IP addresses for cluster growth and rolling updates. Subnets sized at /27 or smaller can limit scaling and updates. Qlik recommends a minimum subnet size of /24.

### Creating a VPC network with a subnet

1. In the Google Cloud console, go to the VPC networks page.
2. Click Create VPC network.
3. Enter a Name, for example qlik-lakehouse-vpc.
4. For Subnet creation mode, select Custom.
5. In the New subnet section, configure the subnet:

   - Name: Enter a name, for example qlik-lakehouse-subnet.
   - Region: Select the region where you will deploy.
   - IP address range: Enter a CIDR range of /24 or larger, for example 10.10.0.0/24.
   - Private Google Access: Select On.
6. Click Done, and then click Create.

### Creating a Cloud NAT gateway

1. In the Google Cloud console, go to the Cloud NAT page.
2. Click Get started if this is your first Cloud NAT gateway, or Create Cloud NAT gateway otherwise.
3. In Gateway name, enter a name for the gateway.
4. For NAT type, select Public.
5. In the Select Cloud Router section, configure the following:

   - Network: Select the VPC network you created.
   - Region: Select the region of your subnet.
   - Cloud Router: Select an existing Cloud Router in the region, or create a new one.
6. In the Cloud NAT mapping section, make sure Source endpoint type is set to VM instances, GKE nodes, Serverless.
7. For Source IP version, select IPv4 subnet ranges, and then in Source subnets select the ranges that include your subnet, for example Primary IP ranges for all subnets.
8. In Cloud NAT IP addresses, select Automatic (recommended).
9. Click Create.

## Configuration summary

After completing the steps above, record the following for use in subsequent configuration steps:

- Project ID
- VPC network name
- Subnet name
- Region
- Subnet CIDR range
