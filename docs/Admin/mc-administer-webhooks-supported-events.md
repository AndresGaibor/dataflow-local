---
title: "Supported event types for webhooks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-webhooks-supported-events.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Extending Qlik Cloud", "Creating and managing webhooks for workflows"]
---

# Supported event types for webhooks

Webhooks are a simple way to automate communication between applications by sending event data automatically when certain actions occur. In Qlik Cloud, webhooks can trigger actions in other applications without manual intervention, making it easier to integrate Qlik Cloud into your workflows and automate tasks based on system events. To learn more about webhooks in Qlik Cloud, see [*Creating and managing webhooks for workflows*](mc-administer-webhooks.htm).

### Available event types for webhooks

The table lists available event types for webhooks in Qlik Cloud:

| Webhook category | Webhook name | Webhook description | Event name | Event type | User level | Tenant level |
| --- | --- | --- | --- | --- | --- | --- |
| Analytics applications | Application created | This event is sent when an analytics application (for example, a Qlik Sense application) is created. | com.qlik.v1.app.created  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/apps/#com-qlik-v1-app-created). | Legacy | Yes | Yes |
| Analytics applications | Application exported | This event is sent when an application (for example, a Qlik Sense application) is exported. | com.qlik.v1.app.exported  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/apps/#com-qlik-v1-app-exported). | Legacy | Yes | Yes |
| Analytics applications | Application published | This event is sent when an analytics application (for example, a Qlik Sense application) is published to a managed space. | com.qlik.v1.app.published  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/apps/#com-qlik-v1-app-published). | Legacy | Yes | Yes |
| Analytics applications | Application deleted | This event is sent when an analytics application (for example, a Qlik Sense application) is deleted. | com.qlik.v1.app.deleted  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/apps/#com-qlik-v1-app-deleted). | Legacy | No | Yes |
| Analytics applications | Application reload finished | This event is sent when an analytics application (for example, a Qlik Sense application) is reloaded and the reload has finished on the engine. It does not indicate the application has been saved. Consider using the Reload finished event if you wish to know when a reloaded application is ready for use. | com.qlik.v1.app.reload.finished  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/apps/#com-qlik-v1-app-reload-finished). | Legacy | Yes | Yes |
| Analytics applications | Application data updated | This event is sent when an analytics application (for example, a Qlik Sense application) data has been updated and the application is saved. | com.qlik.v1.app.data.updated  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/apps/#com-qlik-v1-app-data-updated). | Legacy | Yes | Yes |
| Analytics applications | Reload finished | This event is sent when an analytics application (for example, a Qlik Sense application) reload has been completed and the resource has been saved. | com.qlik.v1.reload.finished | Legacy | Yes | Yes |
| API keys | API key validation failed | This event is sent when an API key validation has failed, indicating an API key is expired or revoked. | com.qlik.v1.api-key.validation.failed | Legacy | No | Yes |
| Users | User created | This event is sent when a user is created. | com.qlik.v1.user.created.  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/users/#com-qlik-v1-user-created) | Legacy | No | Yes |
| Users | User deleted | This event is sent when a user is deleted. | com.qlik.v1.user.deleted.  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/users/#com-qlik-v1-user-deleted) | Legacy | No | Yes |
| Automations | Automation created | This event is sent when an automation is created. | com.qlik.v1.automation.created | Legacy | Yes | Yes |
| Automations | Automation updated | This event is sent when an automation is updated and has been saved. | com.qlik.v1.automation.updated | Legacy | Yes | Yes |
| Automations | Automation deleted | This event is sent when an automation is deleted. | com.qlik.v1.automation.deleted | Legacy | Yes | Yes |
| Automations | Automation run started | This event is sent when an automation run has been started. | com.qlik.v1.automation.run.started | Legacy | Yes | Yes |
| Automations | Automation run ended | This event is sent when an automation run has ended successfully. | com.qlik.v1.automation.run.ended | Legacy | Yes | Yes |
| Automations | Automation run failed | This event is sent when an automation run has ended with failure. | com.qlik.v1.automation.run.failed | Legacy | Yes | Yes |
| Data integration projects | Data integration task started | This event is sent when a Data-Integration task starts. | com.qlik.v1.di-projects.di-tasks.started  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/di-projects/#com-qlik-v1-di-projects-di-tasks-started) | Cloud | Yes | Yes |
| Data integration projects | Data integration task stopped | This event is sent when a Data-Integration task has been stopped. | com.qlik.v1.di-projects.di-tasks.stopped  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/di-projects/#com-qlik-v1-di-projects-di-tasks-stopped) | Cloud | Yes | Yes |
| Data integration projects | Data integration task completed | This event is sent when a Data-Integration task has ended successfully. | com.qlik.v1.di-projects.di-tasks.completed  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/di-projects/#com-qlik-v1-di-projects-di-tasks-completed) | Cloud | Yes | Yes |
| Data integration projects | Data integration task failed | This event is sent when a Data-Integration task has ended with failure. | com.qlik.v1.di-projects.di-tasks.failed  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/di-projects/#com-qlik-v1-di-projects-di-tasks-failed) | Cloud | Yes | Yes |
| Write Table | Changes Saved | Triggered when one or more changes made through a Write Table visualization are saved. | com.qlik.analytics.change-store.changes.saved  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/analytics/change-stores/#com-qlik-analytics-change-store-changes-saved) | Cloud | Yes | Yes |
| Scheduling | Scheduling task updated | This event is sent when a scheduling task (for example, a task to reload an app or run a script) is updated and the change has been saved. | com.qlik.scheduling.task.updated  See: Qlik Developer portal for [API reference](https://qlik.dev/apis/event/scheduling/tasks/#com-qlik-scheduling-task-updated) | Cloud | Yes | Yes |

Information noteThis list reflects the currently supported events in webhooks. You can find a complete list of events on the Qlik Developer Portal  [Cloud events](https://qlik.dev/apis/event/).
