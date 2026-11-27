---
title: "Managing API keys"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-generate-api-keys.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Securing the system"]
---

# Managing API keys

API keys are unique identifiers used for authentication, allowing users, developers, or programs to access APIs securely. They are essential for tracking and controlling API usage, helping to prevent abuse and ensure secure communication.

## Using API keys to connect to Qlik Cloud APIs

You can use API keys to interact with the Qlik REST API reference. Tools such as Postman or qlik-cli can be used for API access. For more information, see [Overview of Qlik APIs](https://qlik.dev/apis) and [qlik-cli](https://qlik.dev/toolkits/qlik-cli).

Information note

API credentials provide direct programmatic access to Qlik Cloud and are not limited to workflows available in the user interface. Assign roles and OAuth scopes using the principle of least privilege. Treat service accounts and API credentials with the same level of care as administrator credentials. For more information, see [API access control and trust boundaries](https://qlik.dev/manage/access-control/api-trust-boundaries/).

Example: Using Postman to connect to Qlik APIs

Do the following:

1. Start Postman.
2. Set the HTTP method to GET.
3. Enter the URL for the Qlik Cloud API endpoint.

   For example, to list all spaces in the tenant:

   https://your-tenant.eu.qlikcloud.com/api/v1/spaces
4. On the Auth tab, choose Bearer Token as the Auth Type.
5. Enter your API key in the Token [field](#glossary-0 "Glossary term").
6. Click Send.

If the request is successful, the API will return a JSON response. In this example, the response would include a list of spaces.

## Configuring API key settings

Do the following:

1. In the Administration activity center, go to the Settings page.
2. Select the Security tab.
3. In the API keys section, adjust the following settings as needed:

   - Change maximum token expiration: Set the expiration period for newly generated API tokens. Existing API keys will retain their original expiration value. There is no upper limit for this value.
   - Change maximum of active API keys per user: Set the limit for how many API keys a user can have. This limit applies only to new keys. If the limit is reached, users won't be able to create additional keys. The maximum value is 1000.

You may need to refresh your browser to see the changes reflected in the API keys section of your personal settings page.

## Generating and managing API keys

### Generating API keys

To generate new API keys, you must have a custom role with the Manage API keys permission, or the permission must be allowed in the default permissions.

Do the following:

1. Click your user profile icon and select Settings.
2. Go to the API keys section and click Generate new key.
3. Provide a description and set an expiration time for the API key.
4. Click Generate to create the key.
5. Copy the generated API key and store it securely. Note that the key cannot be retrieved later.

### Editing API keys

You can change the name of an API key after creation.

### Deleting API keys

Information noteDeleting API keys is permanent and cannot be undone. Ensure that this action won't disrupt any ongoing processes or integrations relying on the key.

Do the following:

1. Click your user profile icon and select Settings.
2. Go to the API keys section.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the API key you want to delete and select Delete.
4. To remove all keys, click Delete all above the list of keys.

## Monitoring and revoking API keys

You can view all API keys associated with your tenant in the API keys section of the Administration activity center. You can search for keys by name, ID, or owner.

### API key statuses

API keys can have the following statuses:

- Active: The API key is currently in use.
- Expired: The expiry date has been reached.
- Revoked: The API key has been revoked and can no longer be used.

### Revoking API keys

As a tenant administrator, actively monitoring API key activities is essential for maintaining security. If suspicious activities are detected, you can revoke the API key.

Information noteRevoking an API key immediately deactivates it, affecting any ongoing processes or integrations relying on it. Revocation is irreversible; a revoked API key cannot be re-activated.

Do the following:

1. In the Administration activity center, go to Events.
2. Look for any suspicious activities, such as excessive usage of a particular API key.
3. Click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) next to the event to expand its details and copy the API key ID.
4. Go to the API keys section and search for the API key using its ID.
5. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the key and select Revoke. You can only revoke keys with status Active.
6. To revoke multiple API keys, select them in the table and click Revoke in the upper-right corner.

### Best practices for API key management

- Keep keys confidential: Store API keys securely and avoid exposing them in public code repositories.
- Regenerate regularly: Periodically regenerate your API keys to enhance security.
- Monitor usage: Regularly check API key activities to identify any suspicious behavior.
