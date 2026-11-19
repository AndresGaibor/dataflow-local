---
source: https://qlik.dev/changelog/144-qlik-cli-update/
last_updated: 2025-09-05T15:00:18+02:00
---

# qlik-cli 2.27.0 - June 2025

A new release of [qlik-cli](https://qlik.dev/toolkits/qlik-cli/) has been published, which expands the set of covered APIs
to include most published [REST APIs](https://qlik.dev/apis/rest/), removes some unused endpoints, and simplifies payload
property configuration.

## New commands \{#new-commands-2025-06}

qlik-cli now supports the following commands:

- `qlik assistant` - Assistants provide a chat interface for asking questions and getting personalized,
  relevant answers for Qlik Answers.
- `qlik condition` - Conditions are used by features such as data alerting and subscriptions to determine
  when action should be taken, based on data in a Qlik app.
- `qlik data-alert` - Supports chart sharing, chart monitoring and alerting features. The legacy sharing APIs refer to
  chart sharing and chart monitoring, which is a feature that allows the user to send an email with an embedded chart
  either manually (chart sharing) or in a recurring manner (chart monitoring). It also stores the history related to
  these actions. The alerting/data-alerts APIs support the alerting feature, where a user is able to create alerts that
  trigger notifications in case a condition in the dataset of an app is fulfilled.
- `qlik data-asset` - Data assets are part of the catalog in Qlik Cloud. A data asset is a member of a data store,
  and may contain multiple data sets.
- `qlik data-connection` - Data connections are used by analytics apps and gateways to connect to external data
  sources. Credentials are stored in data-credentials.
- `qlik data-credential` - Data credentials are the stored credentials leveraged by the data-connections service
  to connect to external data sources.
- `qlik data-quality` - API for triggering data quality computations and retrieving global results to assess the
  quality of your datasets.
- `qlik data-set` - Data sets are part of the catalog in Qlik Cloud. A data set is a member of a data asset.
- `qlik data-source` - Lists data sources available on the tenant for the creation of analytics data connections.
- `qlik data-store` - Data stores are part of the catalog in Qlik Cloud. A data store may contain one or more data
  stores, which in turn may contain multiple data sets.
- `qlik di-project` - Data integration projects are containers for data tasks and provide the context for building,
  monitoring, and controlling data integration pipelines.
- `qlik encryption` - Tenants in Qlik Cloud can be encrypted with a key you provide via a supported KMS. This API
  allows you to configure and manage encryption keys.
- `qlik knowledgebase` - Knowledgebases are collections of individual data sources, that are indexed for use in
  generating responses to user questions via Assistants for Qlik Answers.
- `qlik ml` - The Machine Learning API allows you to generate profile insights to analyze datasets, create and
  manage machine learning experiments, deploy models, and run predictions.
- `qlik notification` - Notifications are resources representing the various notifications that notification-prep can
  render.
- `qlik report` - Reports are downloadable assets generated from data in analytics applications.
- `qlik report-template` - Create and manage report templates.
- `qlik sharing-task` - For scheduled capabilities such as reports, data alerts, subscriptions, and more, sharing tasks
  define when these tasks execute, and tie together the resource definition with any conditions on execution.
- `qlik task` - API for managing tasks and task chains in Qlik Cloud. The requesting user needs the "reload" permission
  on the target resource to use this set of endpoints. A tenant administrator can use `GET /v1/tasks` and
  `DELETE /v1/tasks/{id}` to perform administrative actions, even without the "reload" permission.
- `qlik ui-config` - Pinned links are administrator-defined URLs which appear for all users under the More button in the
  global navigation menu.
- `qlik web-notification` - Web notifications are resource representing a user's notifications.

## Commands removed

The following unused commands have been removed and are no longer supported:

- `qlik data-file space-stats`
- `qlik identity-provider auth-secrets`
- `qlik note settings create` - Use `qlik note settings update` or `qlik note settings edit` instead.
- `qlik user metadata` - The underlying endpoint has been removed. Use `qlik role ls` instead.

## Extended flag support for payload properties

qlik-cli now fully supports the use of flags for all properties of a payload, instead of plain JSON.
A common pain point this addresses is `patch` operations, which usually take an array of JSON-objects.

For example, you can now do:

```shell
qlik space patch SPACE_ID --op replace --path /description --value "New and improved!"
```

In this example, the `--op`, `--path`, and `--value` flags can be used repeatedly and will
then correspond with that property of the nth object. For example, a second `--op` flag would
set the `op` property of the second object.

> **Note:** The previous syntax using the `--body` flag is still supported.
