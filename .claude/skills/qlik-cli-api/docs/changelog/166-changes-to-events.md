---
source: https://qlik.dev/changelog/166-changes-to-events/
last_updated: 2025-09-02T16:29:48+01:00
---

# The payload structure of events emitted via Webhook is changing

Qlik Cloud is beginning a phased migration to a modernized event structure, which
will initially be introduced via the [Webhooks service](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-webhooks.htm).

This update introduces a standardized event format to improve consistency, extensibility,
and interoperability across Qlik Cloud services.

> **Note:** The Webhooks service is leveraged by Qlik Automate for&#x20;
> [webhook automations](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-webhooks.htm).
> &#x20;The migration plan for Qlik Automate will be provided at a later date.

**On or after November 3rd, 2025**, the format for most existing webhooks will change to
a temporary event structure which includes both legacy and future event formats.
This dual-format payload applies to any legacy events, and will allow you to begin adapting
to the new schema without any immediate breaking changes. You should ensure your
downstream apps will not be affected by additional fields being sent in the payload
prior to this date.

Each event payload will contain:

- The existing legacy event structure (unchanged)
- Additional items within the event object that reflect the future format

This approach ensures backward compatibility while enabling early adoption of the
future structure. You should migrate your downstream applications to use the future event
attributes. Qlik will announce a formal 6-month deprecation of the current attributes at a
future date.

The [Data integration project events](https://qlik.dev/apis/event/di-projects/) will
remain unchanged as they already return the future event format.

To learn more about the planned changes please review [the migration guide on Qlik Community](https://community.qlik.com/t5/Official-Support-Articles/Qlik-Cloud-Webhooks-Migration-to-new-event-formats-is-coming/ta-p/2528660).
