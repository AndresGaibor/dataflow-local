---
source: https://qlik.dev/changelog/50-platform-ops-connector-handle-ratelimiting/
last_updated: 2025-07-08T16:09:30Z
---

# Ratelimit handling - Qlik Platform Operations connector

The [Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview)
is a connector
for [Qlik Automate](https://qlik.dev/toolkits/no-code/) that
makes deploying and managing tenants in Qlik Cloud possible without code.

## Change to ratelimit handling

When making API calls against Qlik's APIs, you are subject to ratelimits as
described on the [REST ratelimits](https://qlik.dev/apis/rest/rate-limiting/) page.

Previously, hitting a ratelimit during an automation would cause a failure of
the automation, but new handling has been added that has changed the behavior
to respect the `retry-after` header returned when the ratelimit is hit.

This addition means you can remove any custom ratelimit handling implemented within
your automations. It should now result in automations, which were failing previously,
running until completion.

This change applies to all blocks on the Platform Operations connector.

## Block updates

The following blocks have been updated in the connector:

- Update auto create group settings - this has been updated to ensure that the
  value of both `autoCreateGroups` and `syncIdpGroups` are toggled on each call.
  This is to ensure parity with the behavior in the management console. If you
  wish to change these independently in future, use the Raw API call block.

Review how to [get started with the Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview)
