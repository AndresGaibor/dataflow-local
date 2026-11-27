---
title: "Configuring OAuth token duration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/oauth-token-duration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Securing the system", "Creating and managing OAuth clients"]
---

# Configuring OAuth token duration

You can set how long access tokens and refresh tokens stay valid for each OAuth client. Token durations are set per client and are not tenant-wide settings. For a published OAuth client, the durations apply to all tenants in the region that use that client.

Shorter durations limit how long a compromised token can be used. Longer durations reduce sign-in prompts for applications that do not receive refresh tokens.

When you choose a duration, consider the number of permissions (scopes) the client has. A client with many permissions, or with access to sensitive resources, should use shorter durations.

You must be a tenant administrator to configure token durations. The Access token setting is available for Web, Single-page app, and Native clients. The Refresh token setting depends on the client type and other settings. For details, see [*Refresh token configuration*](#RefreshToken).

## Token duration values

The following table shows the ranges and default values for each setting.

OAuth token duration values

| Setting | Range | Default |
| --- | --- | --- |
| Access token | 15 to 1,440 minutes (24 hours) | 360 minutes (6 hours) |
| Refresh token | 1 to 720 hours (30 days) | 720 hours (30 days) |

Enter whole numbers within the allowed ranges. The access token duration must be shorter than the refresh token duration. For example, an access token duration of 60 minutes requires a refresh token duration of more than 1 hour.

OAuth token durations are independent of user session timeouts and do not extend sessions. For session settings, see [*Configuring session timeouts*](configure-session-timeout.htm).

## Refresh token configuration

Whether you can set a refresh token duration, and whether refresh tokens are issued, depends on the client type and other settings.

### When you can set a refresh token duration

The Refresh token setting is available only when both of the following are true:

- The client type is Web or Native. Single-page app clients can't use the offline\_access permission, so they can't be issued refresh tokens.
- The client has at least one redirect URL (Allowlist step) and the offline\_access permission (Permissions step).

  - Refresh tokens are issued when a user signs in through a browser, which requires a redirect URL.
  - The offline\_access permission lets the application access resources while the user is offline.

If the client has no redirect URL or is missing the offline\_access permission, the Refresh token setting is unavailable. Add the missing item in the Allowlist or Permissions step, then return to configure the refresh token duration.

### When a refresh token is issued

Even when you can set a refresh token duration, a refresh token is issued only when all of the following are true:

- Your identity provider supports refresh tokens. The OAuth client settings can't override an identity provider that is configured not to issue them.
- Block offline\_access is turned off in your identity provider configuration. When it is turned on, Qlik Cloud doesn't pass the offline\_access scope to your identity provider. See [*Advanced options*](mc-creating-oidc-idp.htm#Advanced).
- The application signs in users through a browser (authorization code flow). Machine-to-Machine (M2M) flows never issue refresh tokens, even when Allow Machine-to-Machine (M2M) is turned on. A Web client can use both: M2M for system-to-system access, and browser sign-in, where refresh tokens are issued, if it has a redirect URL.

Your identity provider can't change the refresh token duration. It can only prevent a refresh token from being issued.

## Changing token durations

You can change token durations for any OAuth client after it is created, including clients created through DCR or CIMD.

Information noteIf the OAuth client is published, changing the token duration applies to all applications that use the client across all tenants in the region. For more information, see [*Publishing OAuth clients and consent methods*](oauth-publishing-and-consent.htm).

Do the following:

1. In the Administration activity center, go to OAuth.
2. Locate the client, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and select Edit.
3. Open the token duration settings:

   - Web clients: Open Authentication method and token duration.
   - Single-page or Native clients: Open Token duration.
4. Enter the Access token duration in minutes and, if available, the Refresh token duration in hours.
5. Click Save.

Changes apply only to tokens issued after you save. Existing tokens keep their original expiration time. Shortening a duration does not revoke existing tokens.

### Changing token durations through the API

You can also configure token durations through the [OAuth clients API](https://qlik.dev/apis/rest/oauth-clients/). The API uses integer seconds, not the minutes and hours used in the UI.

## Troubleshooting missing refresh tokens

If an application does not receive a refresh token, check the following in order:

1. The client type is Web or Native.
2. The client has at least one redirect URL.
3. The client includes the offline\_access permission.
4. Your identity provider is configured to issue refresh tokens.
5. The application uses the browser sign-in flow, not an M2M flow.
