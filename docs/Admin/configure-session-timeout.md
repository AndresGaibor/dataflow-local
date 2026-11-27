---
title: "Configuring session timeouts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/configure-session-timeout.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Configuring session timeouts

Session timeout settings control when users are signed out of Qlik Cloud due to inactivity or when a session reaches the maximum allowed duration. Qlik Cloud provides default values, but you can change them if your organization requires different limits.

Configure these settings to balance security and user convenience. Shorter timeouts reduce security risks but may interrupt users. Longer timeouts improve usability but increase risk if devices are left unattended. Choose values based on your organization’s security requirements and user activity patterns.

Session timeouts do not control OAuth token durations. Configure those separately for each OAuth client. See [*Configuring OAuth token duration*](oauth-token-duration.htm).

## Changing session timeout values

You must have the Tenant Admin role to change these settings.

Information noteChanges apply only to new sessions. Existing sessions keep their current timeout values.

Do the following:

1. In the Administration activity center, go to Settings > Security > Session timeouts.
2. For Session inactivity timeout, enter a value in minutes, then click Save.
3. For Maximum session duration, enter a value in hours, then click Save.

## Session timeout settings

Session timeout settings control how long user sessions stay active.

- Session inactivity timeout: Requires users to sign in again after the set period of inactivity.
- Maximum session duration: Requires users to sign in again after the specified duration, regardless of activity.

Information noteThe session inactivity timeout applies only to user sessions. It does not affect application timeouts.

The following table shows default values and allowed ranges for each session timeout setting.

Session timeout values

| Setting | Default | Minimum | Maximum |
| --- | --- | --- | --- |
| Session inactivity timeout | 30 minutes | 15 minutes | 1,440 minutes (24 hours) |
| Maximum session duration | 24 hours | 1 hour | 168 hours (7 days) |

## How session timeouts interact with your identity provider

When session timeouts in Qlik Cloud are used together with an external identity provider (IdP), the user experience depends on which timeout expires first. In most cases, users remain on the current page. In some cases, the page may briefly reload due to silent reauthentication with the IdP.

### When the Qlik Cloud inactivity timeout expires first

- Users are not prompted to sign in again.
- A page reload icon may appear while the IdP silently reauthenticates the session.
- If both Qlik Cloud and IdP inactivity timeouts expire, users are prompted to sign in again.
- Users remain on the current page.

### When the IdP inactivity timeout expires first

- Users are not prompted to sign in again.
- No page reload icon appears, as silent reauthentication does not occur.
- Users remain on the current page.

### When the Qlik Cloud maximum session duration expires first

- Behavior depends on the IdP implementation:
  - The IdP may silently reauthenticate the user, briefly showing a page reload icon, or
  - The user may be prompted to sign in again (initiated by Qlik Cloud).
- In both cases, users remain on the current page.

### When the IdP maximum session duration expires first

- Users are not prompted to sign in again.
- No page reload icon appears, as silent reauthentication does not occur.
- Users remain on the current page.

### Aligning session timeout settings

If users experience unexpected sign-in prompts or sessions do not behave as expected, review both Qlik Cloud session timeout settings and IdP timeout settings. For a consistent user experience and predictable session behavior, align the values according to your organization's security requirements.
