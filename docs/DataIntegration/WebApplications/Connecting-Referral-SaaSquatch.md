---
title: "Referral SaaSquatch"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Referral-SaaSquatch.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Referral SaaSquatch

Referral SaaSquatch is a cloud-based loyalty, referral and rewards marketing platform.

Referral SaaSquatch integration replicates data using the [Referral SaaSquatch REST API](https://docs.referralsaasquatch.com/api/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You must have the Full Access role in your Referral SaaSquatch admin portal.

To retrieve your API key and tenant alias:

1. Log into your [Referral SaaSquatch](https://auth.saasquatch.com/login?state=hKFo2SAzVGlmTUZPcEpmY282NzBrcWMtZlZpVTE3Tng2dHpRZqFupWxvZ2luo3RpZNkgSDMtYVV4bzFuczhkVzdUcy0ySFZLYW5CWUxVUURHR2ujY2lk2SBCVTF0QkZzd3Q5bGVSS09JeDBtUmwzZThEM3FDMEJXcg&client=BU1tBFswt9leRKOIx0mRl3e8D3qC0BWr&protocol=oauth2&redirect_uri=https%3A%2F%2Fapp.referralsaasquatch.com%2Fauth0%2Fcallback&response_type=code&scope=openid%20email) account.
2. Choose your tenant from the tenant selection dropdown.
3. Go to Settings > General.
4. In the Tenant details section, click the eye icon to reveal the API key and locate the Tenant Alias field.
5. Copy and paste your API key and tenant alias into a secured file.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Fill in the required connection properties.
2. Provide a name for the connection in Connection name.
3. Select Open connection metadata to define metadata for the connection when it has been created.
4. Click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| API Key | API key. |
| Tenant Alias | Tenant alias. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### referrals

The `referrals` table contains info about all of the referrals in your Referral SaaSquatch tenant.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Referral SaaSquatch documentation](https://docs.referralsaasquatch.com/api/methods/#open_list_referrals)  [Referral SaaSquatch API method](https://docs.referralsaasquatch.com/api/methods/#list_referrals "Opens in new tab: Referral SaaSquatch API method") |

referrals table foreign keys

| Join referrals with | on |
| --- | --- |
| [reward\_balances](#reward-balances) | ``` referrals.referredUser = reward_balances.userId ```  ``` referrals.referrerUser = reward_balances.userId ```  ``` referrals.referredAccount = reward_balances.accountId ```  ``` referrals.referrerAccount = reward_balances.accountId ``` |
| [users](#users) | ``` referrals.referredUser = users.id ```  ``` referrals.referrerUser = users.id ```  ``` referrals.referredAccount = users.accountId ```  ``` referrals.referrerAccount = users.accountId ``` |

referrals table schema

|  |
| --- |
| **dateConverted**  DATE-TIME |
| **dateModerated**  DATE-TIME |
| **dateReferralEnded**  DATE-TIME |
| **dateReferralPaid**  DATE-TIME |
| **dateReferralStarted**  DATE-TIME |
| **id**  OBJECT This is a nested data structure. |
| **programId**  STRING |
| **referredAccount**  STRING |
| **referredModerationStatus**  STRING |
| **referredReward**  STRING |
| **referredUser**  STRING |
| **referrerAccount**  STRING |
| **referrerModerationStatus**  STRING |
| **referrerReward**  STRING |
| **referrerUser**  STRING |

### reward\_balances

The `reward_balances` table contains info about the balances for all rewards.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | userId  accountId |
| **Useful links** | [Referral SaaSquatch API method](https://docs.referralsaasquatch.com/api/methods#list_balances "Opens in new tab: Referral SaaSquatch API method") |

reward\_balances table foreign keys

| Join reward\_balances with | on |
| --- | --- |
| [referrals](#referrals) | ``` reward_balances.userId = referrals.referredUser ```  ``` reward_balances.userId = referrals.referrerUser ```  ``` reward_balances.accountId = referrals.referredAccount ```  ``` reward_balances.accountId = referrals.referrerAccount ``` |
| [users](#users) | ``` reward_balances.userId = users.id ```  ``` reward_balances.accountId = users.accountId ``` |

reward\_balances table schema

|  |
| --- |
| **accountId**  OBJECT This is a nested data structure. |
| **amount**  INTEGER |
| **type**  STRING |
| **unit**  STRING |
| **userId**  OBJECT This is a nested data structure. |

### users

The `users` table contains info about the users in your Referral SaaSquatch tenant.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  accountId |
| **Useful links** | [Referral SaaSquatch API method](https://docs.referralsaasquatch.com/api/methods#list_users "Opens in new tab: Referral SaaSquatch API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [referrals](#referrals) | ``` users.id = referrals.referredUser ```  ``` users.id = referrals.referrerUser ```  ``` users.accountId = referrals.referredAccount ```  ``` users.accountId = referrals.referrerAccount ``` |
| [reward\_balances](#reward-balances) | ``` users.id = reward_balances.userId ```  ``` users.accountId = reward_balances.accountId ``` |

users table schema

|  |
| --- |
| **accountId**  OBJECT This is a nested data structure. |
| **dateCreated**  DATE-TIME |
| **email**  STRING |
| **emailHash**  STRING |
| **emailShareLink**  STRING |
| **facebookShareLink**  STRING |
| **firstName**  STRING |
| **firstSeenIP**  STRING |
| **id**  OBJECT This is a nested data structure. |
| **imageUrl**  STRING |
| **lastName**  STRING |
| **lastSeenIP**  STRING |
| **linkedinShareLink**  STRING |
| **locale**  STRING |
| **referralSource**  STRING |
| **shareLink**  STRING |
| **twitterShareLink**  STRING |
