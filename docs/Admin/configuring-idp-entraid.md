---
title: "Configuring Microsoft Entra ID as a SAML identity provider"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/configuring-idp-entraid.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud", "SAML for integration with identity providers"]
---

# Configuring Microsoft Entra ID as a SAML identity provider

This topic describes how to set up Microsoft Entra ID (formerly Azure AD) as an identity provider for Qlik Cloud.

## Configure a SAML application in Microsoft Entra ID

The first step is to set up a SAML application in Microsoft Entra ID to trust your Qlik Cloud tenant as a service provider (SP).

Do the following:

1. In the Microsoft Entra admin center, go to Enterprise applications > New application.
2. Click Create your own application.
3. Enter a name for the application.
4. Go to Single sign-on and select SAML as the single sign-on method.
5. On the Set up Single Sign-On with SAML page, enter the following information:

   | Setting | Value |
   | --- | --- |
   | Identifier (Entity ID) | Your original tenant hostname |
   | Reply URL (Assertion Consumer Service URL) | Your original tenant hostname with the path /login/saml appended to the end of the hostname |

   SSO settings.

   ![SAML settings pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-azuread-SAML-settings.png "Click to view full size")
6. Go to the Attributes & Claims section, and click Edit to configure the display name and groups.
7. Select Add new claim and enter the following information:

   | Setting | Value |
   | --- | --- |
   | Name | displayname |
   | Source | Attribute |
   | Source attribute | user.displayname |

   Claim settings.

   ![Claim settings pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-azuread-displayname.png "Click to view full size")
8. Click Save.
9. Select Add a group claim.

   The configuration of group claims depends on where the groups are managed.

   1. If your groups are cloud-managed:

      - Select Groups assigned to the application as associated groups.
      - For Source attribute, select Cloud-only group display names.

        Information noteYou must also assign the relevant groups to the application for them to appear in the claims.
   2. If you're using Microsoft Entra Connect:

      - Select All groups as associated groups.
      - For Source attribute, select sAMAccountName.
10. Click Save.
11. Under attributes and claims, you should now have the following claims listed:

    - displayname
    - http://schemas.microsoft.com/ws/2008/06/identity/claims/groups
    - http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress

    Save these values for later use when setting up the IdP configuration in your Qlik Cloud tenant.

    Claims mappings.

    ![Attribute and claims pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-azuread-attributes-claims.png "Click to view full size")
12. Assign users and groups.

    1. Go to Users and groups and click Add user/group.
    2. Assign the users and groups that will use the application for login.

       Assigning users to the application.

       ![Users and groups pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-azuread-add-user.png "Click to view full size")
13. Retrieve IdP metadata.

    1. Go to SAML Certificates.
    2. Download the Federation Metadata XML.
       You need this file later during the setup in Qlik Cloud.

       SAML certificates.

       ![SAML Certificates pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-azuread-metadata.png "Click to view full size")

## Create and validate an IdP configuration in Qlik Cloud

Log in to Qlik Cloud as a tenant admin to create an IdP configuration.

Do the following:

1. In the Administration activity center, go to Identity provider and click Create new.
2. For Type, select SAML.
3. For Provider, select Microsoft Entra ID (Azure AD).
4. Optionally, enter a description for the IdP configuration.
5. Select Use IdP metadata.
6. Under SAML IdP metadata, click Upload file and select the metadata file you downloaded during the Microsoft Entra ID setup.

   IdP configuration.

   ![IdP configuration pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-azuread-qcs-setup.png "Click to view full size")
7. Under Claims mapping, set name, email, and groups to the claim names from Microsoft Entra ID.

   Claims mapping in IdP configuration.

   ![Claims mapping section of the IdP configuration pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-azuread-qcs-setup-claims.png "Click to view full size")
8. Click Create.
9. In the Create interactive identity provider dialog, clear the Validate IdP checkbox, and then click Create.
   This creates the IdP configuration without immediate validation. Validation will be performed at a later stage.

   Information noteIf preferred, you can validate now. However, we recommend that you complete the next section and upload the certificate file in Microsoft Entra ID first.

## Configure SAML request signature validation

Download the Qlik Cloud SAML request signing certificate and upload it in Microsoft Entra ID.

Do the following:

1. In the Qlik Cloud Administration [activity center](#glossary-0 "Glossary term"), go to Identity providers.
2. On your SAML IdP configuration, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select View provider configuration.
3. Select Download signing certificate and then click Done.

Return to your SAML application in Microsoft Entra ID.

Do the following:

1. In Microsoft Entra ID, select your SAML application and go to Single sign-on.
2. Under Verification certificates (optional), click Edit.

   Verification certificates.

   ![Pane showing Verification certificates Edit option.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-azuread-upload-cert1.png "Click to view full size")
3. Select Require verification certificates.

   Uploading verification certificates.

   ![Verification certificates upload pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-azuread-upload-cert2.png "Click to view full size")
4. Click Upload certificate, and then locate the signing certificate file.
5. Click Save.

Microsoft Entra ID is now set up to validate SAML request signatures. Go back to Qlik Cloud to start the validation.

## Validate your identity provider in Qlik Cloud

After successfully setting up Microsoft Entra ID, you can validate the IdP configuration in Qlik Cloud.

Do the following:

1. In the Administration activity center, go to Identity providers.
2. On your SAML IdP configuration, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Validate.
3. Follow the steps in the validation wizard to perform a login as the user added to the Microsoft Entra ID application. Verify that the user profile data is correct.

   You will be presented with the options to promote the user to a Qlik Cloud tenant admin and to activate the IdP. Note that activating the IdP will deactivate any previously configured interactive identity provider in the tenant.

Related learning:

- [Microsoft Learn: Set up a SAML 2.0 provider with Microsoft Entra ID](https://learn.microsoft.com/en-us/power-pages/security/authentication/saml2-settings-azure-ad)
