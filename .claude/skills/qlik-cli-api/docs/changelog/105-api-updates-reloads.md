---
source: https://qlik.dev/changelog/105-api-updates-reloads/
last_updated: 2024-08-20T09:02:50-04:00
---

# Updated API - Reloads API breaking change

The [reloads API](https://qlik.dev/apis/rest/reloads/) allows for triggering data refreshes in Qlik
Sense applications in Qlik Cloud.

The query `log` default value is being changed from `true` to `false`.  This
will reduce response size for the majority of queries where the `log` attribute
in the response is not required.

The query parameter `log` can have a `true` or `false` value that controls
whether the `log` attribute is sent in the response. Today, the default value of
this `log` parameter is `true`, when not specified - hence the `log` is returned
by default.

To continue receiving this attribute after the notice period, you should
specify `log=true` in your request.

This change will take effect no sooner than 30 days from the date on this changelog, on,
or after September 19, 2024.

Endpoints affected:

- GET `/v1/reloads`

The current response, when no `log` query parameter is included in the request, returns the `log` field.

```json
{
    "data": [
            {
                "id": "65ad4a0df4bd1ffb55555a51",
                "appId": "349216c2-5555-5555-5555-5555379f68bb",
                "tenantId": "xqFQ0k66vSR555555-55555QkiYrCpct",
                "userId": "nEgFMHPnm6ye55555555PSKuCUDzEtFO",
                "type": "chronos",
                "status": "SUCCEEDED",
                "log": "ReloadID: 65ad4a0df4bd1ffb55555a51\nStarted loading data\n(A detailed script progress log can be downloaded when the reload is finished)\nreload-result-join-22-23 \u003c\u003c reload-result-join-22-23 446,756 Lines fetched\n\nApp saved\nFinished successfully\n",
                "partial": false,
                "creationTime": "2024-01-21T16:45:01Z",
                "startTime": "2024-01-21T16:45:02.766Z",
                "endTime": "2024-01-21T16:45:10.125Z",
                "engineTime": "2024-01-21T16:45:07.915Z",
                "links": {
                    "self": {
                        "href": "https://tenant.region.qlikcloud.com/api/v1/reloads/65ad4a0df4bd1ffb55555a51"
                    }
                }
            },
        ]
}
```

In future, if the query param `log=true` is not specified, or is `false`, the
`log` attribute will be omitted from the response:

```json
{
    "data": [
            {
                "id": "65ad4a0df4bd1ffb55555a51",
                "appId": "349216c2-5555-5555-5555-5555379f68bb",
                "tenantId": "xqFQ0k66vSR555555-55555QkiYrCpct",
                "userId": "nEgFMHPnm6ye55555555PSKuCUDzEtFO",
                "type": "chronos",
                "status": "SUCCEEDED",
                "partial": false,
                "creationTime": "2024-01-21T16:45:01Z",
                "startTime": "2024-01-21T16:45:02.766Z",
                "endTime": "2024-01-21T16:45:10.125Z",
                "engineTime": "2024-01-21T16:45:07.915Z",
                "links": {
                    "self": {
                        "href": "https://tenant.region.qlikcloud.com/api/v1/reloads/65ad4a0df4bd1ffb55555a51"
                    }
                }
            },
        ]
}
```

Add query parameter `log=true` to return the log attribute in the response,
such as in `/reloads?appId=349216c2-5555-5555-5555-5555379f68bb&log=true`:

```json
{
    "data": [
            {
                "id": "65ad4a0df4bd1ffb55555a51",
                "appId": "349216c2-5555-5555-5555-5555379f68bb",
                "tenantId": "xqFQ0k66vSR555555-55555QkiYrCpct",
                "userId": "nEgFMHPnm6ye55555555PSKuCUDzEtFO",
                "type": "chronos",
                "status": "SUCCEEDED",
                "log": "ReloadID: 65ad4a0df4bd1ffb55555a51\nStarted loading data\n(A detailed script progress log can be downloaded when the reload is finished)\nreload-result-join-22-23 \u003c\u003c reload-result-join-22-23 446,756 Lines fetched\n\nApp saved\nFinished successfully\n",
                "partial": false,
                "creationTime": "2024-01-21T16:45:01Z",
                "startTime": "2024-01-21T16:45:02.766Z",
                "endTime": "2024-01-21T16:45:10.125Z",
                "engineTime": "2024-01-21T16:45:07.915Z",
                "links": {
                    "self": {
                        "href": "https://tenant.region.qlikcloud.com/api/v1/reloads/65ad4a0df4bd1ffb55555a51"
                    }
                }
            },
        ]
}
```

For more information on this API, review the [Reloads API specification](https://qlik.dev/apis/rest/reloads/).
