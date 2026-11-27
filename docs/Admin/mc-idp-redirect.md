---
title: "Using post logout redirect URI"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-idp-redirect.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud", "Configuring an identity provider (IdP)"]
---

# Using post logout redirect URI

Configure a post logout redirect URI in your identity provider settings to direct users to a specific URI after logging out.

In your identity provider (IdP) configuration, there is an advanced section with the setting Post logout redirect URI. By using the post logout setting, you can redirect a user who is logging out from the IdP to a URI of your choice. Without a post logout redirect, a user who logs out normally ends up on the home page of the identity provider.

In the following procedure, it is assumed that you are editing an existing IdP configuration.

Do the following:

1. In the Administration activity center, open the section Identity provider.
2. Select your identity provider and click Edit.

   The page for editing the IdP configuration opens.
3. Scroll down to the bottom and open the section Advanced options.
4. For Post logout redirect URI, enter the URI to which you want to redirect the user after they have logged out from the IdP.
5. Add the logout URI in your identity provider to the allowlist. The name may be Allowed Logout URLs, Logout redirect URIs, or something similar.

Information noteNot all IdPs support a logout redirect capability. Consult your identity provider for more information.
