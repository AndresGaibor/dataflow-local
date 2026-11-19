---
source: https://qlik.dev/changelog/102-api-deprecation-dcaas/
last_updated: 2024-12-06T12:07:40Z
---

# The DCaaS API is being deprecated

> **Updated on December 6, 2024**: The DCaaS API has now been unpublished from qlik.dev.

The `DCaaS` API provides
the ability to create analytics data connections in your Qlik Cloud tenant.

In response to customer feedback, the functionalities of `DCaaS` were merged into
the [`data-connections`](https://qlik.dev/apis/rest/data-connections) and [`data-sources`](https://qlik.dev/apis/rest/data-sources) APIs
in March 2024, as [announced in this changelog](https://qlik.dev/changelog/80-api-data-connections-dcaas/).

This post serves as notice that `DCaaS` will be deprecated no sooner than 120 days
from the date of this changelog, **on or after November 23, 2024**.

## Migrating from `POST /v1/dcaas/actions/data-connections`

You must move from `POST /v1/dcaas/actions/data-connections`
to [`POST /v1/data-connections`](https://qlik.dev/apis/rest/data-connections/#post-v1-data-connections).

To prevent breaking changes for current users of [`POST /v1/data-connections`](https://qlik.dev/apis/rest/data-connections/#post-v1-data-connections),
some parameter names have changed to incorporate the capabilities from
`POST /v1/dcaas/actions/data-connections`.
Namely:

- The parameter for passing the name of the connection is `qName` rather than `connectionName`.
- The parameter for passing the ID of the space to create the connection in is `space` rather than `spaceId`.

With `POST /v1/dcaas/actions/data-connections`,
you sent:

```bash
curl --location "https://your-tenant.us.qlikcloud.com/api/v1/dcaas/actions/data-connections" ^
--header "Content-Type: application/json" ^
--header "Authorization: <ACCESS_TOKEN>" ^
--data "{
    \"dataSourceId\": \"DG_mysql\",
    \"connectionName\": \"<CONNECTION_NAME>\",
    \"spaceId\": \"<SPACE_ID>\",
    \"connectionProperties\": {
        \"gatewayInstance\": \"<GATEWAY_ID>\",
        \"host\": \"<HOST>\",
        \"port\": \"3306\",
        \"database\": \"<DATABASE_NAME>\",
        \"username\": \"<USERNAME>\",
        \"password\": \"<PASSWORD>\"
    }
}"
```

With [`POST /v1/data-connections`](https://qlik.dev/apis/rest/data-connections/#post-v1-data-connections),
you should send:

```bash
curl --location "https://your-tenant.us.qlikcloud.com/api/v1/data-connections" ^
--header "Content-Type: application/json" ^
--header "Authorization: <ACCESS_TOKEN>" ^
--data "{
    \"dataSourceId\": \"DG_mysql\",
    \"qName\": \"<CONNECTION_NAME>\",
    \"space\": \"<SPACE_ID>\",
    \"connectionProperties\": {
        \"gatewayInstance\": \"<GATEWAY_ID>\",
        \"host\": \"<HOST>\",
        \"port\": \"3306\",
        \"database\": \"<DATABASE_NAME>\",
        \"username\": \"<USERNAME>\",
        \"password\": \"<PASSWORD>\"
    }
}"
```

## Migrating from `GET /v1/dcaas/actions/data-connections/{connectionId}`

You must move from `GET /v1/dcaas/actions/data-connections/{connectionId}`
to [`GET /v1/data-connections/{qID}`](https://qlik.dev/apis/rest/data-connections/#get-v1-data-connections-qID).

Changes:

- The `qName` property is used instead of `connectionName`.
- The `space` property is used instead of `spaceId`.
- The `qID` property is used instead of `connectionId`.
- The legacy response of the data-connections API will be returned along with the
  DCaaS style response.

You must pass the parameter `parseConnection=true` to return
the DCaaS style response.

With `GET /v1/dcaas/actions/data-connections/{connectionId}`,
you sent:

```bash
curl --location "https://your-tenant.us.qlikcloud.com/api/v1/dcaas/actions/data-connections/{connectionId}" ^
--header "Authorization: <ACCESS_TOKEN>" 
```

With [`GET /v1/data-connections/{qID}`](https://qlik.dev/apis/rest/data-connections/#get-v1-data-connections-qID),
you should send:

```bash
curl --location "https://your-tenant.us.qlikcloud.com/api/v1/data-connections/{qID}?parseConnection=true" ^
--header "Authorization: <ACCESS_TOKEN>" 
```

## Migrating from `GET /v1/dcaas/actions/data-connections/api-specs`

You must move from `GET /v1/dcaas/actions/data-connections/api-specs`
to [`GET /v1/data-sources/{dataSourceId}/api-specs`](https://qlik.dev/apis/rest/data-sources/#get-v1-data-sources-dataSourceId-api-specs).

With `GET /v1/dcaas/actions/data-connections/api-specs`,
the `dataSourceId` was a query parameter, and you sent:

```bash
curl --location "https://your-tenant.us.qlikcloud.com/api/v1/dcaas/actions/data-connections/api-specs?dataSourceId={dataSourceId}" ^
--header "Authorization: Bearer <API-key>"
```

With [`GET /v1/data-sources/{dataSourceId}/api-specs`](https://qlik.dev/apis/rest/data-sources/#get-v1-data-sources-dataSourceId-api-specs),
you pass the `dataSourceId` in the path, so you should send:

```bash
curl --location "https://your-tenant.us.qlikcloud.com/api/v1/data-sources/{dataSourceId}/api-specs" ^
--header "Authorization: Bearer <API-key>"
```

Consider reviewing the guides on how to [create data connections](https://qlik.dev/manage/data-connections/create-data-connections/).
