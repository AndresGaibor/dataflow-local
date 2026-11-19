---
source: https://qlik.dev/changelog/150-api-updates-reload-weight/
last_updated: 2025-07-08T13:03:54+01:00
---

# Updated API - The Reloads API supports prioritization of reload execution with new weight parameter

To support dynamic reload workloads, reload weight configuration has been added
for Analytics apps. This defines how quickly the task is picked up for execution
relative to other tasks already in the queue for your subscription.

### Reload weight

Using the new `weight` property on the [Reloads API](https://qlik.dev/apis/rest/reloads/#post-v1-reloads),
you can define a weight value between `1` and `10`.

A weight of `10` will begin execution faster than a weight of `1`. If not specified,
an app will be assigned a weight of `1`. Apps in personal
spaces will always be executed with a weight of `1`, irrespective of the provided
value. The weight affects how quickly a reload is started relative to other reloads
already queued for your subscription, and doesn't impact the task execution once
running, or the overall prioritization of that reload within a Qlik Cloud region.

For example, to set the reload weight to 5:

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/reloads" \
  -X POST \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-type: application/json" \
  -d '{
        "appId": "your-app-id",
        "weight": 5
      }'
```

For more information on reload weight, refer to the [Reloads API reference](https://qlik.dev/apis/rest/reloads/#post-v1-reloads).
