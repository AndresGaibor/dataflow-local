---
title: "Configuring Active Directory Federation Services as a SAML identity provider"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/configuring-idp-adfs.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud", "SAML for integration with identity providers"]
---

# Configuring Active Directory Federation Services as a SAML identity provider

This topic describes how to set up Active Directory Federation Services (AD FS) as an identity provider for Qlik Cloud.

## Prerequisites

Ensure that you have a fully functioning installation of Active Directory Federation Services (AD FS) and a set of users within your Active Directory (AD).

## Download the AD FS server metadata

Retrieve the metadata for your AD FS server, as it will be needed for later configuration in Qlik Cloud.

Download the metadata file by accessing the following URL:

https://<adfs-server.example.com>/FederationMetadata/2007-06/FederationMetadata.xml

## Create an IdP configuration in Qlik Cloud

Log in to Qlik Cloud as a tenant admin to create an IdP configuration.

Do the following:

1. In the Administration activity center, go to Identity provider and click Create new.
2. For Type, select SAML.
3. For Provider, select ADFS.
4. Optionally, provide a description for the IdP configuration.
5. Select Use IdP metadata.
6. Under SAML IdP metadata, click Upload file and select the metadata file downloaded from AD FS.

   IdP configuration.

   ![IdP configuration pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-adfs-qcs-setup.png "Click to view full size")
7. Click Create.
8. In the Create interactive identity provider dialog, clear the Validate IdP checkbox, and then click Create.
   This creates the IdP configuration without immediate validation. Validation will be performed at a later stage.
9. Locate the the IdP configuration you just created, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and select View provider configuration.

   The service provider metadata is displayed.
10. Click Download metadata to download the Qlik Cloud metadata file.
11. Click Download signing certificate to download the Qlik Cloud signing certificate.

## Configure a SAML application in AD FS

Set up a SAML application in AD FS to establish trust with your Qlik Cloud tenant as a service provider (SP).

Do the following:

1. Log in to your Windows server hosting AD FS using administrator credentials.
2. Open the AD FS Management application.
3. Right-click Relying Party Trusts and select Add Relying Party Trust.
4. In the Add Relying Party Trust Wizard, select Claims aware and click Start.
5. Select Import data about the relying party from a file. Browse to the Qlik Cloud metadata file saved earlier, and then click Next.

   Importing SP metadata.

   ![Select data source pane in ADFS.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-adfs-provide-metadata.png "Click to view full size")
6. Enter a Display name, such as Qlik Cloud, and click Next to proceed.
7. Choose the appropriate access control policy and click Next. Click Next once again to confirm the configuration.
8. Select Configure claims issuance policy for this application and click Close.
9. In the Edit Claim Rules dialog, click Add Rule.
10. Select Send LDAP Attributes as Claims and click Next.
11. Provide a Claim rule name and select your Attribute store from the list, for example, Active Directory.
12. Configure the following mappings (or customize them based on your organization's specific requirements):

    - SAM-Account-Name to Name ID
    - Display-Name to Name
    - E-Mail-Addresses to E-Mail Address
    - Token-Groups - Unqualified Names to groups

    Claim rule mappings.

    ![Claim rule pane in ADFS.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-adfs-claims-mapping.png "Click to view full size")
13. Save the changes.
14. Go to the Properties for the Qlik Cloud relying party and select the Signature tab.
15. Click Add, and then locate the Qlik Cloud signing certificate that you downloaded earlier.

    Specifying the signature certificate.

    ![Signature tab in Properties dialog in ADFS.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-adfs-signature-tab.png "Click to view full size")
16. Save the changes.

AD FS is now set up to validate SAML request signatures. Return to Qlik Cloud to initiate the validation process.

## Validate your identity provider in Qlik Cloud

After successfully setting up AD FS, you can validate the IdP configuration in Qlik Cloud.

Do the following:

1. In the Administration activity center, go to Identity providers.
2. On your AD FS IdP configuration, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Validate.
3. Follow the steps in the validation wizard to perform a login as the user added to the AD FS application. Verify that the user profile data is correct.

   You will be presented with the options to promote the user to a Qlik Cloud tenant admin and to activate the IdP. Note that activating the IdP will deactivate any previously configured interactive identity provider in the tenant.
