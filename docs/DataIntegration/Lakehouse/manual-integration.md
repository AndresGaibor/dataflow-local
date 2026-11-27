---
title: "Creating an AWS network integration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/manual-integration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration"]
---

# Creating an AWS network integration

A network integration allows Qlik to provision and manage resources in your AWS cloud environment. These resources process the tasks in your Qlik Open Lakehouse pipeline projects.

## Prerequisites

Before you create a network integration, ensure you have completed the instructions in [*Prerequisites in AWS*](aws-configuration.htm) and have the following configuration information available:

- AWS account ID
- VPC ID
- Availability Zones and subnets

  Alternatively, these can be created during the manual integration process
- Symmetric KMS key ARN
- S3 bucket name
- Management role ARN
- EC2 instance profile ARN

## Creating a manual network integration

To configure your network integration, do the following:

1. In the Administration activity center, go to Lakehouse clusters, and on the Network integration tab, click Create New.
2. Configure the network:

- Network integration name: Enter a name for your network integration.
- Space: Select an existing space from the list.

3. Configure the AWS account:

- AWS account: Enter the AWS account where you want to deploy Qlik.
- Region: Select the region where your VPC is located.
- VPC ID: Enter the VPC where you want to deploy Qlik. The ID must be in lower case and prefixed with vpc-.
- Provide a list of Availability Zones and Subnets where the Qlik servers should be launched. Subnets must be public or private with a NAT gateway, and prefixed with subnet-.

4. In the integration settings, create a secure link:

- Enter the Symmetric KMS key ARN.

  Provide Qlik with a key to encrypt and decrypt data and resources managed in your cloud environment. Ensure the key is symmetric, not asymmetric, and give permission to Qlik .

  For instructions on creating the necessary permissions, see [*Symmetric KMS key*](symmetric-kms-key.htm).

5. Configure the integration resources:

- S3 bucket for internal Qlik files: Enter the name of the S3 bucket for Qlik to store metadata, using the format:

  <bucket-name>

6. In the Advanced section, optionally configure proxy settings:

   Govnote-not-inNot supported in Qlik Cloud Government.

   - Use a proxy server: Route the network integration's outbound traffic through a proxy server.

     - Proxy URL: Enter the proxy server for outbound traffic, including scheme and port.

       Information noteFor a secure proxy server, use the 'https' scheme instead of 'http'.

       Example (secure proxy):

       https://proxy.example.com:3128
     - Bypass proxy for these hosts (optional): Enter an IP, hostname, domain, or wildcard domain (such as \*.internal) and click Add. Repeat to add more hosts.

       Information note

       Outbound traffic to these hosts always bypasses the proxy:

       - 127.0.0.1
       - 169.254.169.254
       - 168.63.129.16
       - metadata.google.internal
       - RFC 1918 private ranges
     - Proxy CA certificate (required if the proxy server uses a certificate): Upload the CA certificate used to trust the proxy. Required for an HTTPS proxy using a privately signed certificate, or when an HTTP proxy performs TLS inspection using a private inspection CA. Supported formats: .pem, .cer, .der, .crt (Maximum size: 1 MB).
7. Grant Qlik access to your cloud:

- In Management role, enter the ARN role created in AWS, using the format:

  arn:aws:iam::<ACCOUNT\_ID>:role/<ROLE\_NAME>

  For instructions on creating this role, see [*Management role*](management-role.htm).

8. Configure your EC2 instances:

- Security groups: Enter the security IDs for the groups to associate with the Qlik instances, prefixed with sg-.
- EC2 instances profile: Enter the profile ARN created in AWS, using the format:

  arn:aws:iam::<ACCOUNT\_ID>:instance-profile/<PROFILE\_NAME>

  For more information on creating the required permissions, see [*Security group*](security-group.htm) and [*EC2 instance profile*](ec2-instance-profile.htm).

9. Create a lakehouse cluster:

- Cluster name: Enter the name for the lakehouse cluster.
- Space: Select the space cluster will belong to. The space is not inherited from the network integration.

The lakehouse cluster is created with a single AWS Spot Instance. You can edit and manage the cluster after it has been created. For guidance, see [*Managing lakehouse clusters*](manage-clusters.htm).
