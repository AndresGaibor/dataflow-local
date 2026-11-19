---
source: https://qlik.dev/changelog/94-deprecate-impersonation-audit/
last_updated: 2024-05-14T15:20:10-04:00
---

# Removing com.qlik.user-identity.impersonation from audits service

Qlik is removing the `com.qlik.user-identity.impersonation` event from the audits service
in Qlik Cloud. Events of this type will no longer appear in the Events panel in your
tenant's management console and responses from the audits API will no longer include
this event.

This change is a result of analysis which found the event added little customer
value, with a better solution being to add the actor attribute to service events to
indicate when a user was impersonated. This reduces audit complexity for customers,
as well as the volume of events a customer needs to process to determine the actions
their users are generating in the platform.

> Note: The `com.qlik.user-identity.impersonation` is not deprecated, it is simply
> being removed from a service that aggregates and surfaces events for external
> consumption.

This change will take effect no sooner than sixty days from the date on this changelog entry.
