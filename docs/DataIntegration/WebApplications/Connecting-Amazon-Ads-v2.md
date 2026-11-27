---
title: "Amazon Ads"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Amazon-Ads-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Amazon Ads

Amazon Ads is an advertising service that allows online merchants to present products on the Amazon platform.

Amazon Ads integration replicates data using the [Amazon Ads API](https://advertising.amazon.com/API/docs/en-us/reference/amazon-ads/overview).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your credentials:

1. Log into your Amazon Developer console.
2. Select Login with Amazon.
3. Click Create a New Security Profile.

   You are required to provide several information to create a new profile. For more information, see [Create an LWA security profile](https://developer.amazon.com/fr/docs/amazon-data-portability/lwa-profile.html).
4. From the Login with Amazon page, select Show Client ID and Client Secret.
5. Copy and paste your client ID and client secret into a secured file.
6. From the Security Profile Management page, copy and paste your security profile into a secured file.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Click Authenticate when you have filled in the required connection settings.

   You may be asked to log in to the source application.

   A window is displayed with an authentication code.
2. Copy the code to the clipboard and return to the connection dialog.
3. Paste the code in Complete authentication with the code provided by the source and click Verify.

   Tip noteYou may need to scroll down to see this field.

   When status is Verified, the authentication is verified.
4. Provide a name for the connection in Connection name.
5. Select Open connection metadata to define metadata for the connection when it has been created.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Profiles | Profile associated with the Login with Amazon account. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### invoices

The `invoices` table contains info about the invoices in your Amazon Ads account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | invoiceDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/billing#tag/invoice/operation/getAdvertiserInvoices) |

### portfolios

The `portfolios` table contains info about the portfolios in your Amazon Ads account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | invoiceDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/reference/portfolios#tag/Portfolios/operation/ListPortfolios) |

### profiles

The `profiles` table contains info about the profiles in your Amazon Ads account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | profileId |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/reference/portfolios#tag/Portfolios/operation/ListPortfolios) |

### sponsored\_brands\_ad\_creatives

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | adId |
| **Replication Keys** | lastUpdateTime |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Ad-creatives/operation/ListCreatives) |

### sponsored\_brands\_ad\_groups

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | adGroupId |
| **Replication Keys** | extendedData.lastUpdateDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Ad-groups/operation/ListSponsoredBrandsAdGroups) |

### sponsored\_brands\_ads

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | adId |
| **Replication Keys** | extendedData.lastUpdateDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Ads/operation/ListSponsoredBrandsAds) |

### sponsored\_brands\_bid\_recommendations

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | recommendationId |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Bid-recommendations/operation/getBidsRecommendations) |

### sponsored\_brands\_budget\_rules\_campaigns

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | campaignId |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Budget-rules/operation/GetCampaignsAssociatedWithSBBudgetRule) |

### sponsored\_brands\_budget\_rules

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ruleId |
| **Replication Keys** | lastUpdatedDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Budget-rules/operation/GetSBBudgetRulesForAdvertiser) |

### sponsored\_brands\_campaigns\_budget\_rules

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ruleId |
| **Replication Keys** | lastUpdatedDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Budget-rules/operation/ListAssociatedBudgetRulesForSBCampaigns) |

### sponsored\_brands\_campaigns

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | campaignId |
| **Replication Keys** | extendedData.lastUpdateDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Campaigns/operation/ListSponsoredBrandsCampaigns) |

### sponsored\_brands\_keywords

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | keywordId |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Keywords/operation/listKeywords) |

### sponsored\_brands\_negative\_keywords

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | keywordId |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Negative-keywords/operation/listNegativeKeywords) |

### sponsored\_brands\_negative\_targets

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | targetId |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Negative-product-targeting/operation/listNegativeTargets) |

### sponsored\_brands\_product\_targets

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | targetId |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Product-targeting/operation/listTargets) |

### sponsored\_brands\_store\_assets

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | assetID |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Stores/operation/listAssets) |

### sponsored\_display\_ad\_groups

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | adGroupId |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi#tag/Ad-Groups/operation/listAdGroupsEx) |

### sponsored\_display\_brand\_safety\_list

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | requestId |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi#tag/Brand-Safety-List/operation/listRequestStatus) |

### sponsored\_display\_budget\_rules\_campaigns

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | campaignId |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi#tag/Budget-Rules/operation/GetCampaignsAssociatedWithSDBudgetRule) |

### sponsored\_display\_budget\_rules

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ruleId |
| **Replication Key** | lastUpdatedDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi#tag/Budget-Rules/operation/GetSDBudgetRulesForAdvertiser) |

### sponsored\_display\_campaigns\_budget\_rules

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ruleId |
| **Replication Key** | lastUpdatedDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi#tag/Budget-rules/operation/DisassociateAssociatedBudgetRuleForSBCampaigns) |

### sponsored\_display\_campaigns

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | campaignId |
| **Replication Key** | lastUpdatedDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi#tag/Campaigns/operation/listCampaignsEx) |

### sponsored\_display\_creatives

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | creativeId |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi#tag/Creatives/operation/listCreatives) |

### sponsored\_display\_negative\_targeting\_clauses

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | targetId |
| **Replication Key** | lastUpdatedDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi#tag/Negative-Targeting/operation/listNegativeTargetingClausesEx) |

### sponsored\_display\_product\_ads

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | adId |
| **Replication Key** | lastUpdatedDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi#tag/Product-Ads/operation/listProductAdsEx) |

### sponsored\_display\_targetings

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | targetId |
| **Replication Key** | lastUpdatedDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi#tag/Targeting/operation/listTargetingClausesEx) |

### sponsored\_products\_ad\_groups

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | adGroupId |
| **Replication Key** | extendedData.lastUpdateDateTime |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#tag/Ad-groups/operation/ListSponsoredProductsAdGroups) |

### sponsored\_products\_ads

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | adId |
| **Replication Key** | extendedData.lastUpdateDateTime |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#tag/Product-ads/operation/ListSponsoredProductsProductAds) |

### sponsored\_products\_budget\_rules

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ruleId |
| **Replication Key** | lastUpdatedDate |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#tag/BudgetRules/operation/GetSPBudgetRulesForAdvertiser) |

### sponsored\_products\_campaigns

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | campaignId |
| **Replication Key** | extendedData.lastUpdateDateTime |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#tag/Campaigns/operation/ListSponsoredProductsCampaigns) |

### sponsored\_products\_keywords

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | keywordId |
| **Replication Key** | extendedData.lastUpdateDateTime |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#tag/Keywords/operation/ListSponsoredProductsKeywords) |

### sponsored\_products\_negative\_keywords

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | keywordId |
| **Replication Key** | extendedData.lastUpdateDateTime |
| **Useful links** | [Amazon Ads documentation](https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#tag/Negative-keywords/operation/ListSponsoredProductsNegativeKeywords) |
