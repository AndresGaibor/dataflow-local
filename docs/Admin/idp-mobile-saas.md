---
title: "Using IdPs with the Qlik Analytics mobile application"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/idp-mobile-saas.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud"]
---

# Using IdPs with the Qlik Analytics mobile application

To ensure seamless connectivity for users of the Qlik Analytics mobile application, the following identity providers (IdPs) are supported:

- Qlik Account
  (not available with Qlik Cloud Government)
- Okta
- Auth0
- Salesforce
- Microsoft Entra ID (formerly Azure AD)
- Google Identity (generic integration)
- OneLogin (generic integration)

Other IdP vendors may also support connectivity to the Qlik Analytics mobile application, but are not officially listed.

## Configuration notes for specific IdPs

- Okta:

  - While Okta supports connectivity to the Qlik Analytics mobile application, users may experience frequent re-login prompts. To resolve this, the identity provider administrator should enable the application's Refresh Token setting.
- Salesforce:

  - Salesforce connectivity works with the Qlik Analytics mobile app only if the identity provider enables offline access, which is disabled by default. Without enabling offline access, users will encounter errors, such as: "Invalid or unavailable offline\_access scope."
