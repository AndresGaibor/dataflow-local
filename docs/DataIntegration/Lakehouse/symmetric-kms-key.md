---
title: "Symmetric KMS key"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/symmetric-kms-key.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in AWS"]
---

# Symmetric KMS key

Create a symmetric key Qlik will use the key to encrypt and decrypt resources managed in the VPC hosting your Qlik Open Lakehouse environment.

AWS Key Management Service (KMS) enables you to create and manage cryptographic keys and control their use across AWS services and applications. One of the most commonly used key types in KMS is the symmetric encryption key.

A symmetric key uses the same cryptographic key for both encryption and decryption operations. In AWS KMS, these keys are designed for general-purpose encryption, including securing data at rest in services such as Amazon S3.

The main benefits of AWS KMS symmetric keys include:

- Managed by AWS KMS: Keys are stored in highly secure hardware security modules (HSMs) within KMS.
- Single encryption key: The same key is used to encrypt and decrypt data.
- API-integrated: Symmetric keys are used with the KMS API for encryption, decryption, and data key generation.
- Audit support: All key usage is logged in AWS CloudTrail for compliance and monitoring.

Symmetric keys are the default key type in KMS and are suitable for most use cases involving secure data encryption within AWS.

## Prerequisites

Ensure you have created the VPC and subnet and Availability Zones for hosting your Qlik Open Lakehouse.

## Creating a symmetric KMS Key

To create a symmetric KMS key for your VPC, do the following:

1. In the AWS console, go to Key Management Service.
2. In Customer-managed keys, click Create a key and configure it:

- Key type: Select Symmetric.
- Key usage: Select Encrypt and decrypt.

3. Aliases: Provide a name, for example, kms-for-qlik.
4. Click through each screen without making any further changes, then click Finish to create the key.
5. Open the key page and make a copy of the Key ARN, which includes the AWS account, Region, and key ID.
