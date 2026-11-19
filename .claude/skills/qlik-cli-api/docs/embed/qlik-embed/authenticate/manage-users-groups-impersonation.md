---
source: https://qlik.dev/embed/qlik-embed/authenticate/manage-users-groups-impersonation/
last_updated: 2026-10-20T17:44:28+02:00
---

# Manage users & groups with OAuth impersonation

## Introduction

When embedding Qlik Cloud into your own application, controlling user identity
and access from your portal is key. OAuth2 impersonation offers a modern,
cookie-less alternative to JWT for scenarios where your portal acts as the identity
provider (IDP) and wants to control user access at the moment of embedding - without
requiring authentication directly through a Qlik Cloud-configured identity provider.

Access control in Qlik Cloud is based on multiple factors, and it's your choice how to
configure this for your tenant. At minimum, you can expect to [manage roles](https://qlik.dev/manage/roles/)
on your users and/or groups to control access to content and features.

This guide demonstrates how to manage these on-the-fly in an embedded scenario.

If you're just starting your embedding journey with qlik-embed, review the
[authentication overview](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/) to
understand the available authentication options.

## Why use OAuth2 impersonation?

OAuth2 impersonation, uses Qlik's OAuth2 flow to establish the user context. It allows
your portal to:

- Provide user attributes dynamically at request time.
- Avoid cookies or interactive login flows.
- Support auditing and event tracking, since actions are performed by real users
  (via impersonation).

If you want to take a look at a working implementation, review the [OAuth impersonation
embedded example tutorial](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-impersonation-tutorial/).

## Migrating from JWT authorization

If you currently use [JWT authorization](https://qlik.dev/authenticate/jwt/create-signed-tokens-for-jwt-authorization/)
with qlik-embed, you pass the user's groups in the `groups` claim of the signed
token. When the user logs in, Qlik Cloud associates them with those groups. If
auto group creation is enabled on the tenant, groups that don't exist yet are
created for you.

With OAuth impersonation, you don't provide group memberships when requesting the
impersonation token. Instead, your backend manages users and custom group memberships
through the APIs before requesting the token:

1. Check whether the user exists in the tenant, and create the user if they don't.
2. Check whether the user belongs to the required custom groups.
3. Create any missing custom groups, then add the user to the groups they are missing.
4. Request the impersonated access token for the user.

The example code in this guide implements these steps. Because the groups are associated
with the user before the token is requested, they're already in place when the
user opens the embedded content.

> **Note:** This guide uses [custom groups](https://qlik.dev/manage/access-control/groups/#custom-groups),
> which you create and manage in Qlik Cloud using the Groups API. JWT auto-create
> groups are IdP-managed groups, not custom groups. When migrating, review the roles
> and space permissions configured for those groups. You can't change a user's membership
> of IdP-managed groups using the API.

## Group-based access control is essential

When using impersonation, you typically do not want to assign content access or
roles on a per-user basis. Instead, you should rely on groups, which your portal
can configure during the token request process.

This ensures your embedded experience:

- Scales with your user base.
- Is easier to audit and trace user access in the tenant.
- Keeps tenant configuration maintainable.

## Example scenario

For example, you run a customer portal that embeds analytics for your users. Your
requirements during the user login flow are:

- Must return an impersonated token which the signed in user can use to access the
  embedded analytics.
- If the user is new, create the user in the Qlik Cloud tenant, so that any content they
  create will persist to their next session (for example, data alerts, subscriptions,
  bookmarks, self service content).
- If the user exists, re-use the existing account so they keep their personal data.
- The user's identifier is their email address. This is what is used by the portal
  to uniquely identify them.
- If the user isn't assigned to the `Consumer` custom group, add this assignment.

The tenant's access configuration must also include:

- A managed space with the `Consumer` group added with `Can view` permissions. This
  makes content such as Qlik Sense apps in the space available to members of the
  group.
- Assigned tenant roles for the `Consumer` group that allow members to use the
  intended features.

If the group is created by the code example, you must also configure its roles and
space permissions before members can access the embedded content.

Your web app:

- Has a login form and flow.
- Is running a service such as node.js, which allows you to run server-side code.
- Your implementation is compatible with the [good practices for OAuth2 impersonation](https://qlik.dev/authenticate/oauth/guiding-principles-oauth-impersonation/).

## Example code

### What this example does

The following code demonstrates a complete OAuth2 impersonation flow that:

- **User Discovery**: Searches for existing users in the Qlik Cloud tenant using
  their email address.
- **User Creation**: Automatically creates new users if they don't exist in the tenant.
- **Group Creation**: When a user needs the specified custom group (for example, `Consumer`), checks whether
  the group exists and creates it if it's missing.
- **Group Management**: Ensures users are assigned to the specified custom group
  (for example, `Consumer`).
- **Token Generation**: Returns an impersonated access token that can be used for embedding.
- **Error Handling**: Reports errors if the provisioning or token request fails.
- **Input Validation**: Validates required parameters and email format.

### Integration with your web application

In a typical embedded scenario:

- **Backend Integration**: The `getImpersonatedUserToken()` function runs on your
  web application's backend (for example, Node.js server).
- **User Session**: Your web app provides the user information (email, name, subject)
  from the logged-in user's session.
- **Frontend Usage**: The output from the `exampleUsage()` function would be used
  in the qlik-embed tags in the frontend.

### Code

```javascript
// Import necessary modules from @qlik/api
import {
auth,
groups,
users,
} from "@qlik/api";

// Regular M2M client for provisioning users and custom groups.
// admin_classic is required for custom group creation with the current OAuth scopes.
// This scope grants broad administrative permissions; keep this client server-side.
const authAdmin = {
    authType: "oauth2",
    host: "https://mytenant.us.qlikcloud.com",
    clientId: process.env.QLIK_ADMIN_CLIENT_ID,
    clientSecret: process.env.QLIK_ADMIN_CLIENT_SECRET,
    scope: "admin_classic",
};

// Separate M2M impersonation client for obtaining the embedded user's token.
// Configure this OAuth client with Trusted consent and M2M user impersonation enabled.
const authUser = {
    authType: "oauth2",
    host: "https://mytenant.us.qlikcloud.com",
    clientId: process.env.QLIK_USER_CLIENT_ID,
    clientSecret: process.env.QLIK_USER_CLIENT_SECRET,
    scope: "user_default",
};

/**
 * Makes sure a custom group exists in the tenant, and returns its ID
 * @param {string} groupName - The name of the custom group
 * @returns {Promise<string>} - The group ID
 */
async function ensureGroupExists(groupName) {
    const options = { hostConfig: { ...authAdmin } };
    // JSON.stringify escapes quotation marks and backslashes in the filter value.
    const filter = `name eq ${JSON.stringify(groupName)}`;
    let response = await groups.getGroups({ filter }, options);

    // The list endpoint is paginated. Check all matching results before creating a group.
    while (response) {
        const match = (response.data.data || []).find(
            group => group.name === groupName && group.providerType === "custom"
        );
        if (match) {
            return match.id;
        }
        response = response.next ? await response.next(options) : null;
    }

    const { data: createdGroup } = await groups.createGroup(
        {
            name: groupName,
            status: "active",
            providerType: "custom",
        },
        options
    );
    return createdGroup.id;
}

/**
 * Adds a custom group to a user's assigned groups if they don't already have it
 * @param {string} userId - The ID of the user
 * @param {string} groupName - The name of the group to add
 * @param {Array} currentGroups - The user's current assigned groups
 * @returns {Promise<void>}
 */
async function ensureUserHasGroup(userId, groupName, currentGroups = []) {
    const hasRequiredGroup = currentGroups.some(
        group => group.name === groupName && group.providerType === "custom"
    );

    if (hasRequiredGroup) {
        console.log(`User ${userId} already has ${groupName} group`);
        return;
    }

    // Create the group only when the user needs to be assigned to it.
    const groupId = await ensureGroupExists(groupName);
    await users.patchUser(
        userId,
        [{
            op: "add",
            path: "/assignedGroups/-",
            value: groupId,
        }],
        { hostConfig: { ...authAdmin } }
    );

    console.log(`Added ${groupName} group to user ${userId}`);
}

/**
 * Gets an impersonated access token for a user based on their email and group name
 * @param {string} userEmail - The email address of the user
 * @param {string} userName - The name of the user (used when creating new users)
 * @param {string} userSubject - The subject of the user (used when creating new users, must be unique)
 * @param {string} groupName - The name of the group to assign to the user
 * @returns {Promise<string>} - The impersonated access token
 */
async function getImpersonatedUserToken(userEmail, userName, userSubject, groupName) {
// Input validation
if (!userEmail || !userName || !userSubject || !groupName) {
    throw new Error("All parameters are required: userEmail, userName, userSubject, groupName");
}

if (!userEmail.includes("@")) {
    throw new Error("Invalid email format provided");
}

try {
    // Step 1: Get user ID using their email
    const { data: usersResponse } = await users.getUsers(
    {
        filter: `email eq ${JSON.stringify(userEmail)} and status eq "active"`,
    },
    {
        hostConfig: {
        ...authAdmin,
        },
    }
    );

    const foundUsers = usersResponse.data || [];

    let userId;

    if (foundUsers.length === 0) {
        // User doesn't exist, create them
        console.log(`User with email ${userEmail} not found, creating new user`);
    
    const userPayload = {
        name: userName,
        email: userEmail,
        subject: userSubject,
    };

    const newUser = await users.createUser(userPayload, {
        hostConfig: {
        ...authAdmin,
        },
    });

        userId = newUser.data.id;
        console.log(`Created new user with ID: ${userId} for email: ${userEmail}`);
        
        // Add the required group to the new user
        await ensureUserHasGroup(userId, groupName, []);
    } else if (foundUsers.length === 1) {
        userId = foundUsers[0].id;
        const existingUser = foundUsers[0];
        console.log(`Found existing user ID: ${userId} for email: ${userEmail}`);
        
        // Ensure the existing user has the required group
        await ensureUserHasGroup(userId, groupName, existingUser.assignedGroups || []);
    } else {
        // Multiple users found - this should never happen and is an error
        throw new Error(`Multiple users found with email ${userEmail}. This is not possible in Qlik Cloud since user emails must be unique.`);
    }

    // Step 2: Generate impersonated access token for the user
    const accessToken = await auth.getAccessToken({
        hostConfig: {
            ...authUser,
            userId: userId,
            scope: "user_default",
        },
    });

    console.log(`Generated impersonated token for user: ${userId}`);
    return accessToken;

} catch (error) {
    console.error("Error generating impersonated user token:", error);
    throw new Error(`Failed to get impersonated token for user ${userEmail}: ${error.message}`);
}
}

// Example usage:
// This function demonstrates how to get an impersonated access token for a user
async function exampleUsage() {
    try {
        const accessToken = await getImpersonatedUserToken(
            "john.doe@qlik.com",        // userEmail - the email of the user to impersonate
            "John Doe",                 // userName - display name for the user
            "6893db654802ab50d228526e", // userSubject - subject identifier (avoid using personal identifiers such as email)
            "Consumer"                  // groupName - the custom group to assign
        );
        
        // Do not log access tokens.
        return accessToken;
    } catch (error) {
        console.error("Failed to get impersonated token:", error.message);
        throw error;
    }
}

// Uncomment the line below to run the example
// exampleUsage();
```

## Considerations

- `ensureGroupExists()` creates groups without roles or space permissions. Creating
  a group and assigning a user to it doesn't grant access to embedded content.
  Configure roles and space permissions for new groups before relying on them
  for access control. For more information, see [Manage users with groups](https://qlik.dev/manage/access-control/groups/).
- Use two separate OAuth clients. `authAdmin` is a regular machine-to-machine
  (M2M) client with `admin_classic` for user and custom group provisioning. This
  scope grants broad administrative access. The narrower `admin.groups` scope is
  not currently available to OAuth clients, and `admin.users` alone does not
  authorize the Groups API. Keep its client secret on the backend and grant access
  to the provisioning endpoint only to trusted callers.
- `authUser` is a separate M2M user-impersonation client with `user_default`. Enable
  M2M user impersonation and set its consent method to **Trusted**. The resulting
  token represents the end user and uses that user's permissions. The embedded user
  doesn't need to be a tenant administrator.

## Next steps

- Learn how to [create, list, and manage custom groups](https://qlik.dev/manage/access-control/groups/)
  using the Groups API.
- Review the [custom groups changelog entry](https://qlik.dev/changelog/120-custom-groups/) for
  the introduction of `providerType: "custom"`.
- Follow the
  [OAuth impersonation embedded example tutorial](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-impersonation-tutorial/)
  to see how impersonated tokens are used with qlik-embed.
