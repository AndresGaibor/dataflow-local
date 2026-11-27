---
title: "Tenant encryption"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/tenant-encryption.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud"]
---

# Tenant encryption

Qlik Cloud encrypts all tenant data by default, and you can optionally use your own customer-managed keys (CMK) to control the encryption key.

When a [tenant](#glossary-0 "Glossary term") is created, Qlik Cloud uses multiple layers of security to protect your data. By default, each tenant is separated from other tenants by a uniquely generated set of encryption keys that are managed by the Qlik Cloud encryption service to encrypt content in the tenant. Each tenant’s keys are separate from the keys that Qlik Cloud uses to secure service-to-service communication.

## Encryption standards

Qlik Cloud uses the following encryption standards:

- In transit: TLS 1.2 encryption
- At rest: AES-256-GCM encryption
- Within the platform (after authentication with a designated IdP): Signed JSON Web Tokens (JWTs) to ensure integrity, authenticity, and non-repudiation

Information noteFor Qlik Talend Cloud Premium or Enterprise subscriptions, the encryption settings apply to both your Qlik Cloud and Talend Cloud tenants.

## Key providers

Tenant admins choose which key provider encrypts the tenant data at rest. Qlik Cloud supports the following key providers:

- Qlik Internal KMS (default): keys managed by Qlik
- AWS KMS: a customer-managed key that you create and control in your own AWS Key Management Service (AWS KMS) account

## Customer-managed keys

Use a customer-managed key (CMK) if you want control over the key that encrypts your tenant data at rest. With CMK, you are responsible for managing the key life cycle. Disabling or deleting the key affects access to your tenant.

CMK is required for tenants that process protected health information (PHI) under HIPAA. For details, see [*Customer-managed keys and HIPAA*](../Admin/customer-managed-keys.htm#hipaa).

For responsibilities, regions and disaster recovery, and limitations, see [*Customer-managed keys*](../Admin/customer-managed-keys.htm). To set it up, see [*Setting up AWS KMS for customer-managed keys*](../Admin/mc-set-up-aws-kms-keys.htm) and [*Configuring customer-managed keys*](../Admin/mc-configure-tenant-encryption.htm).
