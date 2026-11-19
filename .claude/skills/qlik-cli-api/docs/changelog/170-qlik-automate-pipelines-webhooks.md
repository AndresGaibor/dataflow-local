---
source: https://qlik.dev/changelog/170-qlik-automate-pipelines-webhooks/
last_updated: 2026-04-20T13:34:03+01:00
---

# Webhooks for Qlik Talend Cloud Pipelines now available in Qlik Automate

New pipeline events were recently published in Qlik Cloud and are available to subscribe to:

- Pipeline project task is Started
- Pipeline project task is Stopped
- Pipeline project task is Completed
- Pipeline project task Failed

For more information, see the [reference documentation](https://qlik.dev/apis/event/di-projects/).

With the latest Qlik Automate connector release, you can now use webhooks to trigger an automation
on any of these four events.

![Qlik Automate - webhook configuration screenshot](https://qlik.dev/_astro/qlik-automate-pipelines-webhook-screenshot.DJUFMbrv.png)

Using the built-in filters, you can listen to any webhook occurring in the data space, data projects,
data tasks of your choice, and more.

You can, for instance, open a ServiceNow ticket whenever a pipeline task fails or is stopped, and even
trigger corrective measures to solve the issue.

Using the Completed webhook, you are able to automatically start downstream processes, or inform users
about the availability of new datasets in the data products catalog.

For more information on how to get started with webhook automations, see the
[documentation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-webhooks.htm#native-webhooks)
on Qlik Help.

You can also create and manage webhooks from your Qlik Cloud Administration activity center in the Webhooks section,
and leverage them using a third-party monitoring tool of your choice.

These new webhook events enable new use cases for your organization such as automating monitoring, triggering
dependencies, handling incidents, or keeping business processes running.
