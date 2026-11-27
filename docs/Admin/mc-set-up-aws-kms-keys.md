---
title: "Setting up AWS KMS for customer-managed keys"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-set-up-aws-kms-keys.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Tenant encryption"]
---

# Setting up AWS KMS for customer-managed keys

Before you can use customer-managed keys (CMK), create a symmetric key in Amazon Web Services (AWS) and add a key policy that lets Qlik Cloud use the key to encrypt and decrypt your tenant data.

Complete these steps in your AWS account first. When the key is ready, add it to your tenant as a key provider. See [*Configuring customer-managed keys*](mc-configure-tenant-encryption.htm).

Warning noteAWS KMS doesn't support changing the key type after you create the key. You can't change a single-region key to a multi-region key, or the reverse. If you need to move from a single-region key to a multi-region key, see [*Moving from a single-region key to a multi-region key*](customer-managed-keys.htm#transition). If your existing key is already a multi-region key, you can modify the policy and update the replica regions.

## Before you begin

Make sure that you have:

- An AWS account. If you don't have one, go to [Amazon Web Services](https://aws.amazon.com) and create an account. Your account must be in the same region as your Qlik Cloud tenant.
- Permission in AWS to create keys and edit key policies.
- Your Qlik Cloud tenant ID. To find it, select your user profile in any activity center, and then select About. Copy the string under Tenant ID. Don't use the display name or alias hostname from the Tenant tab on the About page in the Administration activity center.
- A decision on whether you need a single-region or a multi-region key. See [*Regions and disaster recovery*](customer-managed-keys.htm#regions).

## Create an AWS KMS key

Create the key in the AWS KMS Management Console, or through the AWS KMS API using the CreateKey command. Use these settings:

AWS KMS key settings

| Setting | Value |
| --- | --- |
| Key type | Symmetric. CMK doesn't support asymmetric keys. |
| Key usage | Encrypt and decrypt |
| Key material origin | KMS |
| Region | The region where your Qlik Cloud tenant is hosted |
| Regionality | Multi-region key, or single-region key if your region requires it |

While you create the key, you can also:

- Enter a key alias.
- Define the IAM users and roles who can administer the key.
- Select the IAM users and roles who can use the key in cryptographic operations.
- Configure the key policy.

For more information, see [Create a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the AWS documentation.

## Supported regions and backup regions

Select the AWS region where your Qlik Cloud tenant is hosted. For a multi-region key, create the replica in the backup region listed below.

AWS regions

| Primary region name | Primary region code | Backup region name | Backup region code |
| --- | --- | --- | --- |
| US East (North Virginia) | us-east-1 | US East (Ohio) | us-east-2 |
| Asia Pacific (Mumbai) | ap-south-1 | Asia Pacific (Hyderabad) | ap-south-2 |
| Asia Pacific (Singapore) | ap-southeast-1 | Asia Pacific (Seoul) | ap-northeast-2 |
| Asia Pacific (Sydney) | ap-southeast-2 | Asia Pacific (Melbourne) | ap-southeast-4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | Asia Pacific (Osaka) | ap-northeast-3 |
| Canada (Montréal) | ca-central-1 | Canada (Alberta) | ca-west-1 |
| Europe (Frankfurt) | eu-central-1 | Europe (Milan) | eu-south-1 |
| Europe (Ireland) | eu-west-1 | Europe (Spain) | eu-south-2 |
| Europe (London) | eu-west-2 | Europe (Spain) | eu-south-2 |
| Europe (Paris) | eu-west-3 | N/A | N/A |
| Europe (Stockholm) | eu-north-1 | N/A | N/A |
| Israel (Tel Aviv) | il-central-1 | N/A | N/A |
| Middle East (UAE) | me-central-1 | N/A | N/A |
| South America (São Paulo) | sa-east-1 | N/A | N/A |

For more information about Qlik Cloud regions and backup locations, see [Qlik Cloud Regions](https://www.qlik.com/us/regions).

Warning noteTo set up a multi-region key correctly for use in Qlik Cloud, create the key pair according to the backup region table above.

Qlik Cloud Government noteThe Qlik Cloud Government regions (us-gov-west-1 or us-gov-east-1) don't need a replica key configuration to register a CMK.

## Create a multi-region key

Multi-region keys let you keep accessing and processing encrypted data when the primary region has an outage. You create a replica of the key in the backup region. You can decrypt data in the backup region, and data encrypted in the backup region can be decrypted in the primary region once it's restored.

Follow these steps to create a multi-region key in AWS KMS:

1. In the AWS Management Console, click on Create a key.

   ![Create a key in the AWS Management Console.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Step0CreateMultiRegionAWS-CMK_1204x570.png)
2. In Advanced options, set Key material origin to KMS. In Regionality , select Multi-region key. Click Next.

   ![Key configuration step with Multi-region key selected.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Step1CreateMultiRegionAWS-CMK_1027x814.png)
3. Enter an alias for the key. You can also add a description and tags. Click Next .

   ![Alias and description step.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Step2CreateMultiRegionAWS-CMK_1053x752.png)
4. Select the IAM users and roles who can administer the key. Click Next.

   ![Key administrators step.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Step3CreateMultiRegionAWS-CMK.png)
5. Select the IAM users and roles that can use the key. Click Next.

   ![Key usage permissions step.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Step4CreateMultiRegionAWS-CMK.png)
6. Review the configuration. Make sure that Regionality is set to Multi-region key.

   ![Review step with Multi-region key shown.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Step5CreateMultiRegionAWS-CMK.png)

## Configure the key policy

The key policy controls access to your AWS KMS key. Each key has its own policy. When you create a key in the AWS KMS Management Console, AWS KMS creates a default key policy based on your selections. This policy decides which IAM users and roles in your account can administer and use the key.

You must edit the default key policy to add the permissions and parameters that Qlik Cloud CMK needs. These are:

- Qlik proxy roles: Allow the Qlik AWS proxy accounts and required IAM roles to generate a data key, encrypt data, and decrypt data using your key. To use CMK with Qlik Automate, you must also add the separate Automations IAM roles. Both are in the code snippets below
- Your tenant ID: Qlik Cloud uses your tenant ID as the encryption context. AWS KMS uses the encryption context as additional authenticated data (AAD) to support authenticated encryption, so one tenant can't decrypt another tenant's cipher keys. If you use the same key for multiple tenants, include the tenant ID of each tenant in the key policy. See [Encryption context](https://docs.aws.amazon.com/kms/latest/cryptographic-details/basic-concepts.html) in the AWS documentation.

Do the following:

1. Check that your AWS account and your IAM users and roles are correct and included in the policy. Your policy might include other statements as well. For an example, see [*Example key policy*](#Example2).
2. Copy the code snippet below that applies to your subscription and add it to your key policy. For Qlik Cloud Government, use the Qlik Cloud Government code snippet.

   Qlik Cloud code snippet

   ```
           {
               "Sid": "Enable Qlik's proxy roles to use the Customer's AWS KMS key to encrypt and decrypt data for the Qlik cloud tenant",
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "arn:aws:iam::338144066592:role/byok-encryption-proxy-role",
                       "arn:aws:iam::634246602378:role/byok-encryption-proxy-role",
                       "arn:aws:iam::338144066592:role/byok-automations-proxy-role",
                       "arn:aws:iam::634246602378:role/byok-automations-proxy-role"
                   ]
               },
               "Action": [
                   "kms:Encrypt",
                   "kms:Decrypt",
                   "kms:GenerateDataKey"
               ],
               "Resource": "*",
               "Condition": {
                   "StringEquals": {
                       "kms:EncryptionContext:TenantId": [
                           "QLIK_TENANT_ID"
                       ]
                   }
               }
           }
   ```

   Qlik Cloud Government code snippet

   ```
   [
       {
           "Sid": "Enable Qlik's proxy roles to use the Customer's AWS KMS key to encrypt and decrypt data for the Qlik cloud tenant",
           "Effect": "Allow",
           "Principal": {
               "AWS": [
                   "arn:aws-us-gov:iam::014729015091:role/byok-encryption-proxy-role",
                   "arn:aws-us-gov:iam::014734359703:role/byok-encryption-proxy-role",
                   "arn:aws-us-gov:iam::014729015091:role/byok-automations-proxy-role",
                   "arn:aws-us-gov:iam::014734359703:role/byok-automations-proxy-role"
               ]
           },
           "Action": [
               "kms:Encrypt",
               "kms:Decrypt",
               "kms:GenerateDataKey"
           ],
           "Resource": "*",
           "Condition": {
               "StringEquals": {
                   "kms:EncryptionContext:TenantId": [
                       "QLIK_TENANT_ID"
                   ]
               }
           }
       },
       {
           "Sid": "Enable KMS Key policy for proxy account",
           "Effect": "Allow",
           "Principal": {
               "AWS": [
                   "arn:aws-us-gov:iam::014729015091:role/byok-encryption-proxy-role",
                   "arn:aws-us-gov:iam::014734359703:role/byok-encryption-proxy-role",
                   "arn:aws-us-gov:iam::014729015091:role/byok-automations-proxy-role",
                   "arn:aws-us-gov:iam::014734359703:role/byok-automations-proxy-role"
               ]
           },
           "Action": "kms:DescribeKey",
           "Resource": "*"
       }
   ]
   ```
3. In the EncryptionContext string, replace QLIK\_TENANT\_ID with your Qlik Cloud tenant ID.
4. Save the key policy.

For more information about AWS KMS key policies, see [Key policies in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the AWS documentation.

### Example key policy

The following example key policy shows the basic requirements for using an AWS KMS key with Qlik Cloud CMK.

1. Your AWS account and the IAM users and roles who can administer and use the key.
2. The Qlik accounts and IAM roles that are permitted to use the key for the cryptographic operations Encrypt, Decrypt, and GenerateDataKey.
3. The Qlik accounts and Automations IAM roles that are permitted to use the key with Qlik Automate.
4. The encryption context that identifies your tenant ID.

Selections B, C, and D are the parameters that Qlik Cloud CMK requires.

AWS KMS key policy example

![Example AWS KMS key policy with the parameters required by Qlik Cloud highlighted](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_BYOK_KeyPolicy2.png "Click to view full size")

### Example key policy for a multi-region key

The following key policy includes all the requirements for using a multi-region key with Qlik Cloud CMK, including the kms:DescribeKey action. For more information,see [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html).

{
"Version": "2012-10-17",
"Id": "key-consolepolicy-3",
"Statement": [
{
"Sid": "Enable IAM User Permissions",
"Effect": "Allow",
"Principal": {
"AWS": "arn:aws:iam::857519135519:root"
},
"Action": "kms:\*",
"Resource": "\*"
},
{
"Sid": "Enable KMS Key policy for proxy account",
"Effect": "Allow",
"Principal": {
"AWS": [
"arn:aws:iam::338144066592:role/byok-encryption-proxy-role",
"arn:aws:iam::634246602378:role/byok-automations-proxy-role",
"arn:aws:iam::634246602378:role/byok-encryption-proxy-role",
"arn:aws:iam::338144066592:role/byok-automations-proxy-role"
]
},
"Action": [
"kms:Encrypt",
"kms:Decrypt",
"kms:GenerateDataKey"
],
"Resource": "\*",
"Condition": {
"StringEquals": {
"kms:EncryptionContext:TenantId": [
"QLIK\_TENANT\_ID"
]
}
}
},
{
"Sid": "Enable KMS Key policy for proxy account",
"Effect": "Allow",
"Principal": {
"AWS": [
"arn:aws:iam::338144066592:role/byok-encryption-proxy-role",
"arn:aws:iam::634246602378:role/byok-automations-proxy-role",
"arn:aws:iam::634246602378:role/byok-encryption-proxy-role",
"arn:aws:iam::338144066592:role/byok-automations-proxy-role"
]
},
"Action": "kms:DescribeKey",
"Resource": "\*"
}
]
}

## Find your key ARN and alias ARN

An Amazon Resource Name (ARN) is a unique, fully qualified identifier for your KMS key. AWS KMS creates the ARN when you create the key.

When you add your key as a key provider in the Administration activity center, you enter the key ARN or the alias ARN. The Qlik Cloud encryption service uses it to connect to your AWS KMS key.

A) AWS KMS key ARN and B) alias ARN in AWS KMS

![Key ARN and alias ARN shown in the AWS KMS console](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AWS_KMS_Alias_ARN.png "Click to view full size")

The ARN uses this format:

arn:<partition>:kms:<region>:<account-id>:key/<key-id>

Example of a valid key ARN:

arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab

The alias ARN uses this format:

arn:<partition>:kms:<region>:<account-id>:alias/<alias-name>

Example of a valid alias ARN, where CMK-Example-Alias is the alias name:

arn:aws:kms:us-east-1:111122223333:alias/CMK-Example-Alias

For more information about finding the ARN or alias ARN of your key, see [Find the key ID and key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/find-cmk-id-arn.html) or [Find the alias name and alias ARN for a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/find-cmk-alias.html) in the AWS documentation.

## Next steps

When your key and key policy are ready, add the key to your tenant. See [*Configuring customer-managed keys*](mc-configure-tenant-encryption.htm).
