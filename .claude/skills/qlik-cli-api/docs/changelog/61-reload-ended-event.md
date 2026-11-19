---
source: https://qlik.dev/changelog/61-reload-ended-event/
last_updated: 2025-07-08T16:09:30Z
---

# The Audits API is changing the event for app reload ended

> **Update:** This changelog was updated to add information on the other services
> impacted by this change, and how to move to the new event on 2023-11-23. The event change
> was deployed on 2023-11-14.

Qlik Cloud leverages an event driven architecture to communicate between the
services in the platform. To support customer use cases, Qlik surfaces some of these
events. These events may be made accessible in several ways, via:

- The [audits](https://qlik.dev/apis/rest/audits) API, which provides
  visibility of events in your Qlik Cloud tenant. This data is also accessible in
  the [Events page in the management console](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-events.htm).
- As an event you can subscribe to from a third party application via
  the [Webhook service](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-webhooks.htm).
- As an event you can subscribe to from Qlik Automate via
  the [Qlik Cloud Services connector start block](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-webhooks.htm).

The event emitted when an analytics reload completes, `com.qlik.app.reload.ended`,
will be replaced by `com.qlik.v1.app.reload.finished` no sooner than 30 days from
this notice. The events presented in the webhooks service, and on the Qlik Cloud
Services connector will also be updated to reflect the new format.

> **Note:** The `com.qlik.app.reload.ended` event is experimental and unpublished.
> In general, Qlik does not post deprecation notices for experimental and/or unpublished
> events. An exception has been made in this circumstance because of the external
> usage of this event. Qlik reserves the right to deprecate without notice experimental
> and/or unpublished events.

The key differences for `com.qlik.v1.app.reload.finished` are:

- Layout and field name changes, such as:
  - The location of the app ID has changed from `data>id` to `extensions>topLevelResourceId`.
  - The location of the space ID has changed from `data>spaceId` to `extensions>spaceId`.
- The `statements` section will not return data, since more complex reloads can make
  the payload of the event too large. You can still access this information using
  the app
  reload metadata API endpoint, if required.
- The event is published, and stable

Review the Audits API specification, and
the app reload finished
event specification for further information.
