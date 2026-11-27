---
title: "Configuring Okta as a SAML identity provider"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/configuring-idp-okta.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud", "SAML for integration with identity providers"]
---

# Configuring Okta as a SAML identity provider

This topic describes how to set up Okta as an identity provider for Qlik Cloud.

## Configure a SAML application in Okta

The first step is to set up a SAML application in Okta to trust your Qlik Cloud tenant as a service provider (SP).

Do the following:

1. In Okta's Admin Console, go to Applications > Applications.
2. Click Create App Integration.
3. For Sign-in method,
   select SAML 2.0 and click Next.
4. Fill out the general information for the integration as desired, then click Next.
5. Under SAML Settings, enter the following information:

   | Setting | Value |
   | --- | --- |
   | Single-sign on URL | Your original tenant hostname with the path /login/saml appended to the end of the hostname |
   | Audience URI (SP Entity ID) | Your original tenant hostname (without any path appended and no trailing slash) |
   | Name ID format | Unspecified |

   SAML settings.

   ![SAML settings pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-okta-SAML-settings.png "Click to view full size")
6. Under Attribute Statements, add attribute statements for name and email.
   Enter the following information:

   | Name | Name format | Value |
   | --- | --- | --- |
   | name | Unspecified | ${user.firstName} ${user.lastName} |
   | email | Unspecified | user.email |

   Tip noteOkta supports expressions in string formatting to integrate multiple values into a single attribute. The value suggested here will combine the first name and last name into the name attribute.

   Attribute statements.

   ![Attribute statements pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-okta-attributes.png "Click to view full size")
7. Under Group Attribute Statements, add an attribute statement for groups.
   Enter the following information:

   | Name | Name format | Filter | Value |
   | --- | --- | --- | --- |
   | groups | Unspecified | Matches regex | .+ |

   Tip noteThe filter and value suggested here retrieve all user groups. The filter can be adjusted to only return specific subsets of groups, based on your preferences.

   Group attribute statements.

   ![Group attribute statements pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-okta-attributes-groups.png "Click to view full size")
8. To finish the Okta setup, select I'm an Okta customer adding an internal app and This is an internal app that we have created, and then click Finish.

Once the application is created, there are two more things you need to do in Okta:

1. Download the IdP metadata: You should be presented with metadata URL. If not, you can find it on the Sign On tab of the application. Copy and open the URL in your browser, then save the page as a file to be used later. (If using Chrome, right-click on the page and select Save as.)
2. Add users and groups: On the Assignments tab, add the users and groups that are allowed to log in to your Qlik Cloud tenant.

## Create an IdP configuration in Qlik Cloud

Log in to Qlik Cloud as a tenant admin to create an IdP configuration.

Do the following:

1. IIn the Qlik Cloud Administration activity center, go to Identity provider and click Create new.
2. For Type, select SAML.
3. For Provider, select Okta.
4. Optionally, enter a description for the IdP configuration.
5. Select Use IdP metadata.
6. Under SAML IdP metadata, click Upload file and select the IdP metadata file you downloaded during the Okta setup.

   IdP configuration.

   ![IdP configuration pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-okta-qcs-setup.png "Click to view full size")
7. Click Create.
8. In the Create interactive identity provider dialog, clear the Validate IdP checkbox, and then click Create.
   This creates the IdP configuration without immediate validation. Validation will be performed at a later stage.

   Information noteIf preferred, you can validate now. However, we recommend that you complete the next section and upload the certificate file in Okta first.

## Configure SAML request signature validation

Download the Qlik Cloud SAML request signing certificate and upload it in Okta.

Do the following:

1. In the Qlik Cloud Administration activity center, go to Identity providers.
2. On your SAML IdP configuration, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select View provider configuration.
3. Select Download signing certificate and then click Done.

Return to your SAML application in Okta.

Do the following:

1. In Okta, go to the General tab of the application.
2. Under SAML Settings, click Edit.
3. Click Next to arrive at Configure SAML.
4. Under SAML Settings, click Show Advanced Settings.
5. Next to Signature Certificate, click Browse files and upload the signing certificate file.

   Upon successful upload, Okta shows details about the certificate.

   Certificate details.

   ![Certificate details shown in Okta.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-okta-certificate.png "Click to view full size")
6. Next to Signed Requests, select Validate SAML requests with signature certificates.
7. Click Next to continue through Okta's setup flow and save your changes.

Okta is now set up to validate SAML request signatures. Go back to Qlik Cloud to start the validation.

## Validate your identity provider in Qlik Cloud

After successfully setting up Okta, you can validate the IdP configuration in Qlik Cloud.

Do the following:

1. In the Qlik Cloud Administration [activity center](#glossary-0 "Glossary term"), go to Identity providers.
2. On your SAML IdP configuration, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Validate.
3. Follow the steps in the validation wizard to perform a login as the user added to the Okta application. Verify that the user profile data is correct.

   You will be presented with the options to promote the user to a Qlik Cloud tenant admin and to activate the IdP. Note that activating the IdP will deactivate any previously configured interactive identity provider in the tenant.
