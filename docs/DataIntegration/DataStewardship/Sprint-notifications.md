---
title: "Sprint notifications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataStewardship/Sprint-notifications.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Validating and correcting your data with data stewardship"]
---

# Sprint notifications

Sprint notifications keep you informed about changes to your sprint roles and record assignments. They are configured in your tenant-level notification preferences and are delivered through the channels that you enable.

## Notification types

All sprint notification types are enabled by default. You can receive notifications through the ![Web notification](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bell_outline.svg) Web and ![Email notification](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_mail_2.svg) Email channels for these events:

- You are assigned as the sprint owner for a sprint.
- You are removed as the sprint owner from a sprint.
- You are added as a data steward for a sprint.
- You are removed as a data steward from a sprint.
- Records are assigned to you in a sprint.

Each notification includes an Open sprint action. The action opens the related sprint so that you can review its current state.

Email notifications use the subject pattern `<sprint name> - Sprint assignments updated`.

## How assignment notifications work

Record assignment notifications depend on the sprint role and workflow. For example, a record assigned for correction can notify the assigned data steward or sprint owner, as applicable. A record submitted for a second validation step can notify the assigned sprint owner. For more information about the validation workflow, see [*Managing your sprints*](Managing-sprints.htm).

Assignment notifications prompt you to check the sprint. They are not a per-record audit trail. The sprint view is the source of truth for the current assignment state, especially after assigning multiple records or reassigning records.

Information note

A notification can become stale if the assignment changes after the notification is sent. Record unassignment does not send a correction notification.

## What does not trigger a notification

- Your own action does not send a role-change notification to you. Use an action performed by another user to test role-change notifications.
- Adding records to a sprint does not, by itself, send a sprint notification.
- Record comments do not send sprint notifications.
- Record unassignment does not send a correction notification.

This list is not exhaustive. It covers common scenarios that do not trigger notifications but can cause confusion.

A deduplication process helps prevent users from receiving multiple notifications for the same event.

## What to expect from automatic assignments

When a user validates or assigns records to another data steward, notifications are sent immediately after the user clicks Apply changes.

However, when records are added through a file import or a Talend Studio job, assignments can happen over time. If AI processing assigns records progressively, you may receive notifications as those assignments happen.

You will not receive a separate notification for every assignment. To reduce repeated messages, the system does not send the same type of notification to the same user again for approximately 10 minutes.

This applies when assignments happen automatically after:

- Records are delivered following AI changes.
- Records are added to a sprint through a Talend Studio job or another connected system.
- AI processing is canceled.

## Notification settings and access

Sprint notifications are configured in your tenant-level notification preferences. They are not configured at the space, sprint, or record level.

Notifications are not sent for eligible events that occur while notifications are paused, even after notifications resume.

A notification does not grant access to a sprint. You must have access to the space that contains the sprint.

## Troubleshooting missing notifications

If you do not receive a sprint notification, check the following:

- The delivery channel that you need, ![Web notification](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bell_outline.svg) Web or ![Email notification](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_mail_2.svg) Email, is enabled.
- Notifications are not paused.
- The notification is addressed to the email account that you are checking.
- You currently have the relevant sprint role or record assignment.
- You have access to the space that contains the sprint.
