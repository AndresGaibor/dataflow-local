---
title: "Configuring customer-managed keys"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-configure-tenant-encryption.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Tenant encryption"]
---

# Configuring customer-managed keys

Configure your tenant to encrypt data at rest with your own AWS KMS key, and manage the key provider after setup.

By default, a new tenant uses Qlik Internal KMS to encrypt tenant data. Tenant admins can configure the tenant to use a customer-managed key (CMK) from AWS Key Management Service (AWS KMS) instead. You do this by creating a key provider for your AWS KMS key, and then migrating the tenant to it.

## Before you begin

Make sure that you have:

- The Tenant Admin role.
- An AWS account and an AWS KMS key that is set up for use with Qlik Cloud. The key must be in the AWS region where your tenant is hosted. See [*Supported regions and backup regions*](mc-set-up-aws-kms-keys.htm#regionality).
- The ARN or alias ARN of your key. See [*Find your key ARN and alias ARN*](mc-set-up-aws-kms-keys.htm#key).

Consider the following before you start:

- You can use CMK with new or existing tenants.
- Once you change the key provider, Qlik Cloud encrypts and decrypts all data at rest in the tenant with your key.
- Each tenant needs its own key provider configuration. You can use the same AWS KMS key for several tenants by adding each tenant ID to the key policy, but this isn’t a best practice. The encryption context keeps the data of each tenant separate.
- If you are a customer or partner who enables tenants for several end-user organizations, you must use an individual key for each end-user organization.

## Create a key provider

Create a key provider to connect your tenant to your AWS KMS key. Before you start, check that your key and key policy are configured correctly in AWS KMS. See [*Setting up AWS KMS for customer-managed keys*](mc-set-up-aws-kms-keys.htm).

Do the following:

1. In the Administration activity center, go to Settings, and then select the Security tab.
2. In the Tenant encryption section, click Manage key provider.
3. Click the Create new card.
4. Enter the following:

   - Master key provider: AWS-KMS. This is the only option available.
   - KMS key ARN: The ARN or alias ARN of your key.
   - Title: A title that identifies the key provider.
   - Description: Optional

   Create key provider card

   ![Create a master key provider](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_BYOK_CreateMasterKeyProvider.png "Click to view full size")
5. Choose whether you want to save the key provider for later use or to start the key migration now.

The key provider isn't active until you migrate the tenant to it.

Warning noteAfter you configure your tenant for CMK, tenant data can't be decrypted if you disable or delete your key. If you re-enable a disabled key, access to the data is restored. If you delete a key, access to the data is permanently lost. For more information, see [*Manage your keys in AWS KMS*](customer-managed-keys.htm#Key).

## Validate a key provider

You can validate an AWS KMS key provider at any time. Validation checks that your key and key policy meet the requirements for a key migration. Qlik Cloud also validates the key provider automatically before every migration.

Do the following:

1. In the Administration activity center, go to Settings, and then select the Security tab.
2. In the Tenant encryption section, click Manage key provider.
3. On the key provider card, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
4. Select Validate.

## Change the key provider

You can change the key provider from Qlik Internal KMS to AWS KMS, from one AWS KMS to another, or from AWS KMS back to Qlik Internal KMS. The tenant continues to work as usual during the migration, with no impact to users.

Warning noteIf a HIPAA Business Associate Agreement (BAA) is in effect and you store PHI subject to HIPAA, you can't revert to Qlik Internal KMS. To replace the AWS KMS key that you use, create a new AWS KMS key and migrate to it.

Do the following:

1. In the Administration activity center, go to Settings, and then select the Security tab.
2. In the Tenant encryption section, click Manage key provider.
3. On the card of the key provider that you want to migrate to, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
4. Select Migrate.
5. In the Change key provider dialog, select the checkbox to confirm that you want to replace the current key, and then click Change key provider.

When the migration succeeds, the new key provider becomes active.

The status of the migration updates every 15 minutes. A migration typically takes up to 24 hours, depending on the number items in the tenant, such as notes, applications, automations, alerts, and event logs. If your migration takes longer than 24 hours, submit a ticket to [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).

Information noteYou can verify the key provider change on the Events page in the Administration activity center. For the encryption event types related to migration, see [*Monitor key provider events*](#Key).

## Delete a key provider

You can delete any key provider that is inactive, except for the default Qlik Internal KMS provider.

Do the following:

1. In the Administration activity center, go to Settings, and then select the Security tab.
2. In the Tenant encryption section, click Manage key provider.
3. On the key provider card, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
4. Select Delete.

## Monitor key provider events

You can verify changes to the key provider on the Events page in the Administration activity center. The events log captures these event types:

Event types

| Event type | Description |
| --- | --- |
| com.qlik.v1.encryption.keyprovider.created | A key provider was created. |
| com.qlik.v1.encryption.keyprovider.updated | A key provider was updated. |
| com.qlik.v1.encryption.keyprovider.deleted | A key provider was deleted. |
| com.qlik.v1.encryption.keyprovider-migration.triggered | A key migration was started. |
| com.qlik.v1.encryption.keyprovider-migration.progressed | A key migration made progress. |
| com.qlik.v1.encryption.keyprovider-migration.finished | A key migration finished. |

AWS KMS logs its own events to AWS CloudTrail. In Event History, search for the event names Encrypt, GenerateDatakey, and Decrypt.

## Manage key providers with the API and Qlik Automate

In addition to the Administration activity center, you can manage key providers with:

- The encryption API: Manage key providers programmatically. See the API reference on [qlik.dev](http://qlik.dev/).
- The Amazon KMS connector in Qlik Automate: See [How to get started with the Amazon KMS connector](https://community.qlik.com/t5/Official-Support-Articles/How-to-get-started-with-the-Amazon-KMS-connector-and-Qlik-s/ta-p/2104061).
- The Qlik Platform Operations connector and the QCS connector: A no-code, Qlik-native option for managing key providers by using connector blocks in a flow. See [Qlik Platform Operations connector overview](https://qlik.dev/manage/platform-operations/no-code/overview) and [Automation connectors](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/connector-blocks/connectors-list.htm).
