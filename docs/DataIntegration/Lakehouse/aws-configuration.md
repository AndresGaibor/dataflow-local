---
title: "Prerequisites in AWS"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/aws-configuration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration"]
---

# Prerequisites in AWS

Configure the entities in your cloud environment needed to create a network integration.

To create a network integration, you must first configure the required entities in AWS. We recommend you follow the instructions below, saving the relevant details for each entity to a file. When all entities are created, use the information to configure a manual network integration for your Qlik Open Lakehouse pipeline projects.

Follow the instructions for creating each entity below. Complete them in order, making a note of each setting. When you have finished, follow the instructions for creating a [*Creating an AWS network integration*](manual-integration.htm).

## [*VPC, subnets and Availability Zones*](vpc-subnets-azones.htm)

Configure a VPC to integrate Qlik with your private cloud environment. The VPC allows data tasks to run Qlik Open Lakehouse pipeline projects.

## [*Symmetric KMS key*](symmetric-kms-key.htm)

Generate a symmetric key to enable Qlik to encrypt and decrypt data managed in your cloud environment.

## [*S3 bucket*](s3-bucket.htm)

Create an Amazon S3 bucket to store metadata object definitions, configurations, and intermediate data.

## [*Security group*](security-group.htm)

Define a security group to control inbound and outbound traffic to your EC2 instances.

## [*Management role*](management-role.htm)

Create a management role that grants Qlik the permissions it needs to manage AWS resources and run tasks in your Qlik Open Lakehouse pipeline projects.

## [*EC2 instance profile*](ec2-instance-profile.htm)

Configure an instance profile to enable Qlik to securely access your AWS resources without the need to store credentials on the instance.

## [*AMI requirements*](ami-requirements.htm)

Configure the image requirements for running Qlik Open Lakehouse in your AWS environment.
