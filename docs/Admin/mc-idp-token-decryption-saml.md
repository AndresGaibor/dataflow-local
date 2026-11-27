---
title: "Managing key pairs for signed and encrypted ID assertion (SAML)"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-idp-token-decryption-saml.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud", "Configuring an identity provider (IdP)"]
---

# Managing key pairs for signed and encrypted ID assertion (SAML)

With SAML identity providers, JSON Web Tokens (JWT) are used to authenticate and authorize users. These assertions can be signed to verify their authenticity and encrypted to protect their contents.

Qlik Cloud supports token signature verification and decryption for all SAML identity providers compatible with the platform.

## Understanding key pairs

A key pair, consisting of a public key and a private key, is central to this process:

- Public key: Used by the identity provider to encrypt tokens.
- Private key: Used by Qlik Cloud to decrypt tokens and access the information they contain.

How it works:

1. When a user logs in to Qlik Cloud, the external identity provider initiates the SAML authentication flow with Qlik Cloud.
2. The identity provider sends back the user's ID assertion, which includes user-specific information such as their identity:

   - The assertion is signed with the identity provider’s private key to confirm their authenticity and integrity.
   - The assertion is encrypted using the Qlik Cloud public key to ensure that only Qlik Cloud can decrypt and access the contained information.
3. Qlik Cloud verifies the signature of the ID assertion using the identity provider's public key. It then decrypts the token using its own private key to retrieve the user's details.

This process ensures only authorized parties can access and use the assertions information.

## Generating key pairs

You can generate key pairs for assertion signature verification and decryption for SAML IdP configurations.

Do the following:

1. In the Administration activity center, go to Identity provider.
2. Create a new IdP configuration.

   For detailed steps on configuring IdPs, see [*Configuring an identity provider (IdP)*](mc-creating-idp.htm).
3. Expand the Advanced options section.
4. Under Assertion signature verification and decryption, choose the key type: RSA 2048 or RSA 4096.
5. Click Create.
6. In the confirmation dialog:

   - Click ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) to copy the public key.
   - Click ![Download](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) to download the key as a certificate.

   Confirmation dialog.

   ![Confirmation dialog with copy option and the two action buttons Later and Validate.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_generate_success.png "Click to view full size")

   Information noteWhether you need the public key or the certificate depends on your identity provider's requirements. Both are downloaded in PEM format. If your identity provider requires a different format, use a tool like OpenSSL to convert the PEM file.
7. Before you can validate, you need to provide the public key to your identity provider. Click Later to temporarily exit the configuration process.
8. Share the public key or certificate with your identity provider:

   - Go to your identity provider’s setup interface and follow their instructions to upload or enter the public key. Refer to their documentation for detailed steps.
9. After completing the setup in your identity provider, return to the Administration activity center to finish the validation:

   1. On your IdP configuration, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Validate.
   2. Click Validate to start the validation process.
   3. Follow the instructions on screen to log in and confirm that the key pair is correctly set up and recognized.

Once the key pair is successfully validated, the identity provider can be used for secure assertion signature verification and decryption.

## Rotating key pairs

Key rotation involves periodically replacing cryptographic keys to minimize security risks. In Qlik Cloud, you can regenerate key pairs with the same or different strength. The new key pair will replace the old one after successful validation.

Information noteRegenerating the key pair doesn’t replace the old one immediately. The old key pair remains active until the new IdP configuration is validated. You need to upload the new public key or certificate to your identity provider and complete the validation process to activate the new key.

### Regenerating key pairs

Do the following:

1. In the Administration activity center, go to Identity provider.
2. Find your IdP configuration, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Edit.
3. Expand the Advanced options section.
4. Under Assertion signature verification and decryption, choose the desired key strength under Regenerate key.

   You can select the same or a different strength from the previous key.

   Settings for regenerating keys.

   ![The configuration settings showing the generated key and option to regenerate.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_regenerate_keypair.png "Click to view full size")
5. Click Regenerate key ![Regenerate](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg).
6. In the confirmation dialog:

   - Click ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) to copy the public key.
   - Click ![Download](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) to download the key as a certificate.

   Information noteWhether you need the public key or the certificate depends on your identity provider's requirements. Both are downloaded in PEM format. If your identity provider requires a different format, use a tool like OpenSSL to convert the PEM file.
7. Before you can validate, you need to update the setup in your identity provider. Click Later to temporarily exit the configuration process.
8. Share the new public key or certificate with the identity provider:

   - Go to your identity provider’s setup interface and follow their instructions to upload or enter the public key. Refer to their documentation for detailed steps.
9. After completing the setup in your identity provider, return to the Administration activity center to finish the validation:

   1. On your IdP configuration, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Validate.
   2. Click Validate to start the validation process.
   3. Follow the instructions on screen to log in and confirm that the key pair is correctly set up and recognized.

Upon successful validation, the new key pair will replace the previous one for all future logins. If the validation fails, the newly generated key pair will be ignored, and the previous key pair will remain in use.

## Deleting key pairs

Do the following:

1. In the Administration activity center, go to Identity provider.
2. On your IdP configuration, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Edit.
3. Expand the Advanced options section.
4. Under Assertion signature verification and decryption, click ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg) next to the generated key.
5. Confirm the deletion.

Ensure that the public key is also removed from your identity provider to avoid login issues.
