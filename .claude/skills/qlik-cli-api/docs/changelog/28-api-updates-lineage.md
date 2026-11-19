---
source: https://qlik.dev/changelog/28-api-updates-lineage/
last_updated: 2025-07-08T16:09:30Z
---

# New API - Lineage

### Lineage

The Lineage API enables users to keep track of the origins
and impacted content of the base objects on resource, table,
and field levels.

Additionally, the Lineage API supports search, expansion,
and overview on the nodes within input and output graphs.

With this API you can:

- `GET/v1/lineage-graphs/nodes/{id}`: Returns a lineage graph of a source node.

`{id}`is the QRI of the base node

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/lineage-graphs/nodes/{id}" \
 -H "Authorization: Bearer <API-key>"
```

- `GET/v1/lineage-graphs/impact/{id}/source` : Returns all levels of the requested root node.
  `{id}`is the QRI of the base node

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/lineage-graphs/impact/{id}/source" \
 -H "Authorization: Bearer <API-key>"
```

- `POST/v1/lineage-graphs/nodes/{id}/overview`: Update lineage flag for this request.
  `{id}`is the QRI of the base node

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/lineage-graphs/nodes/{id}/overview" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{
        "":[]
    }'
```

- `GET/v1/lineage-graphs/impact/{id}/overview`: Returns all resource level nodes
  that are impacted by a change in the source node.
  `{id}`is the QRI of the base node

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/lineage-graphs/impact/{id}/overview" \
 -H "Authorization: Bearer <API-key>"
```

See full API reference [here](https://qlik.dev/apis/rest/lineage-graphs).

You can also read more in [this tutorial](https://qlik.dev/manage/get-started-lineage).
