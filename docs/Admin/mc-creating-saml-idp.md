---
title: "Configuring an interactive SAML IdP"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-creating-saml-idp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud", "Configuring an identity provider (IdP)"]
---

# Configuring an interactive SAML IdP

This topic describes how to configure the identity provider settings in Qlik Cloud.

## Configuration on the identity provider side

In addition to the configuration in Qlik Cloud, you also need to make configurations on the identity provider side. For a walk-through of those configurations, refer to the following topics:

- [*Configuring Active Directory Federation Services as a SAML identity provider*](configuring-idp-adfs.htm)
- [*Configuring Microsoft Entra ID as a SAML identity provider*](configuring-idp-entraid.htm)
- [*Configuring Okta as a SAML identity provider*](configuring-idp-okta.htm)

## Configuration in Qlik Cloud

Tenant administrators can create new IdP configurations.

Information noteYou can only have one single interactive IdP at a time. If you already have an active one, you need to first deactivate it before you can activate the new one. For more information, see [*Changing corporate identity providers*](mc-change-corporate-idp.htm).

Do the following:

1. In the Administration activity center, go to Identity provider and click Create new.
2. For Type, select SAML.
3. For Provider, select an identity provider from the list, or choose Generic if your specific provider is not listed.
4. Optionally, enter a description for the IdP configuration.
5. Under Configuration, you have the option to either upload the SAML XML metadata from your identity provider or manually enter individual values.

   Do one of the following:

   1. Select Use IdP metadata.
   2. Click Upload file under SAML IdP metadata and choose the file containing metadata from your identity provider. Alternatively, if your identity provider metadata isn't available as a file, you can copy and paste the metadata directly in the IdP metadata field.

   or

   1. Click Upload file under Signing certificates to upload the certificate file.
      This is the certificate used by the identity provider to sign the SAML assertions sent to Qlik Cloud.
   2. Enter the Entity ID of your identity provider.
   3. Enter the Single sign-on URL.

      This is the endpoint where the SAML authentication requests are sent. It is the URL to which the user is redirected for authentication.
   4. Select a Name ID format.

   Configuration using metadata and manual configuration.

   ![Configuration panes shown with and without using IdP metadata](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_idp_config_options.png "Click to view full size")
6. Optionally, select Enable IdP-initiated login.

   The default login flow is that the user first goes to Qlik Cloud and is then redirected to the IdP for authentication. Enable IdP-initiated login if you want the user to first login to the identity provider and then be redirected to Qlik Cloud.
7. Modify the fields under Claims mapping or keep the default values.

   Claims mappings define how user attributes from your identity provider are associated with fields in the Qlik Cloud user model. Mappings are available for sub, name, email, groups, and picture. Adjust the values to fit your organization's needs and the attributes from your identity provider.

   Information note
   - You can enter multiple lookup values, separated by a comma, in the input fields. The first non-null value found will be used.
   - The groups claim is needed to receive groups. Note that nested groups are not supported in Microsoft Entra ID.
8. Optionally, configure Post logout redirect URI under Advanced options.

   This it used to redirect a user to a defined URI after logout. For an example of how to use post logout redirect URI, see [*Using post logout redirect URI*](mc-idp-redirect.htm).
9. Click Create.

   A confirmation dialog appears with the option to validate the IdP configuration.

   The SAML service provider metadata and signing certificate are available only after creating the IdP configuration. If you need this information to set up the identity provider, you can create the IdP without validation initially, and validate once the configuration at your identity provider is completed.

   - To validate now, select Validate IdP and click Create. This will initiate the validation process. Follow the steps in the validation wizard to perform a login and confirm that the user profile data is valid.
   - If you prefer to create the configuration now but validate it later, clear the Validate IdP checkbox and click Create. You can validate later by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on your IdP configuration and selecting Validate.

   Validating and creating the IdP configuration.

   ![Confirmation dialog with Validate IdP option selected](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_idp_confirm_validation.png "Click to view full size")

## Uploading the service provider metadata to your identity provider

Do the following:

1. In the Administration activity center, on your newly created IdP configuration, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select View provider configuration.

   A dialog shows the service provider metadata and the URL to the metadata endpoint.

   Service provider metadata.

   ![Confirmation dialog with Validate IdP option selected](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_idp_sp_metadata.png "Click to view full size")
2. Depending on the setup at your identity provider, either download the metadata file or copy the URL and save it for later use. Download the signing certificate file, if needed. Click Done.
3. At your identity provider, enter the service provider metadata. Ensure to configure the following required settings:

   - Assertion Consumer Service (ACS) URL. This is where the identity provider sends the SAML assertions after authentication.
   - Entity ID of the service provider.
   - The certificate for validating authentication requests. This is used by the identity provider to verify the authenticity of the service provider.
4. Once the configuration at your identity provider is complete, you can validate your IdP configuration in the Administration activity center.
   Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on your configuration and select Validate. Follow the steps in the validation wizard to perform a login and verify that the user profile data is correct.

## Advanced options

The advanced options provide additional capabilities for certain identity providers.

### Post logout redirect URI

Use this field to specify a URI to which users will be redirected after logging out. For detailed instructions, see [*Using post logout redirect URI*](mc-idp-redirect.htm).

### Assertion signature verification and decryption

Generate key pairs to verify signatures and decrypt encrypted JSON Web Tokens (JWT). For detailed instructions, see  [*Managing key pairs for signed and encrypted ID assertion (SAML)*](mc-idp-token-decryption-saml.htm).
