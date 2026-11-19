---
source: https://qlik.dev/changelog/80-api-data-connections-dcaas/
last_updated: 2026-01-19T14:21:00Z
---

# Updates to the data-connections API, and new data-sources API

Qlik Sense applications running in Qlik Cloud rely on Analytics Data Connections
to load data from external sources. The first API to support the creation of these
connections was the Data Connectivity as a Service (DCaaS) API released in September
2023 (see the [DCaaS changelog](https://qlik.dev/changelog/60-api-data-connections-dcaas/)),
and this and additional capabilities have now been merged into
the [data-connections](https://qlik.dev/apis/rest/data-connections/) API.

This release of the data-connections API supports creation of standard analytics
connections, as well as connections via the direct access gateway, to all analytics
data sources.

An example creation request for a MySQL connection via a direct access Data Gateway:

```bash
curl --location "https://<TENANT>/api/v1/data-connections" ^
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

If you are currently using the `/api/v1/dcaas` paths, you should transition to using
the updated `/api/v1/data-connections` endpoints.

There are some differences between the parameters the two APIs accept, with `data-connections`
maintaining legacy naming to remove the need for breaking changes in the API:

- The parameter for passing the name of the connection is `qName` rather
  than `connectionName`.
- The parameter for passing the ID of the space to create the connection in is
  `space` rather than `spaceId`.

## Learn more about Analytics Data Connection APIs

To discover more about how to create Analytics Data Connections:

- Review the [data connections](https://qlik.dev/manage/data-connections/) topic
  to learn about the overall capability.
- Visit the [create a connection](https://qlik.dev/manage/data-connections/create-data-connections/)
  tutorial to begin creating new connections.
- Understand how to create connections via
  the [direct access data gateway](https://qlik.dev/manage/data-connections/gateway-data-connections).
- Review [example connection creation requests](https://qlik.dev/manage/data-connections/examples/data-connection-create-examples/).
