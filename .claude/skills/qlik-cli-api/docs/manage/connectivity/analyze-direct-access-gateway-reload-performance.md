---
source: https://qlik.dev/manage/connectivity/analyze-direct-access-gateway-reload-performance/
last_updated: 2026-09-22T18:29:29+02:00
---

# Analyze Direct Access gateway reload performance

## Overview

When a Qlik application reload runs through a [Direct Access gateway](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm),
the gateway can record performance metrics for each load operation it processes. Use these metrics to review reload
throughput, connector latency, and gateway activity for a real workload, rather than a synthetic benchmark.

```text
Turn on recording → run/identify a reload → find its metrics → interpret records → compare with a benchmark baseline
```

## What you'll learn

At the end of this guide, you'll have performance records correlated to a
[Direct Access Agents API](https://qlik.dev/apis/rest/connectivity/direct-access-agents/)
specific reload and can identify which operations warrant further investigation.

If you want a controlled baseline instead of real reload data, see
[Run and review Direct Access Gateway benchmarks](https://qlik.dev/manage/connectivity/run-review-direct-access-gateway-benchmarks/).

## Prerequisites

- A Direct Access gateway registered on your tenant, running version **1.7.17** or later.
- The requester must have the `TenantAdmin` role and be either the gateway's space owner or a
  member of the gateway's space with the `Can Consume Data` role.
- A bearer access token for authenticating requests. For setup, see [Authentication](https://qlik.dev/authenticate).
- An application reload that uses a data connection routed through the target gateway.
- The Direct Access agent's identifier. To find the agent ID:
  1. In Qlik Cloud go to **Administration** > **Data gateways**.
  2. Locate the Direct Access gateway, select **…** > **Gateway settings**, and copy
     the Agent ID under General settings.

## Step 1: Turn on load-performance recording

Load-performance metric recording is off by default. Check the current setting for the
`BENCHMARK_LOAD_PERFORMANCE_METRICS_RECORDING_ENABLED` configuration property:

```bash
curl -G \
  "https://<TENANT>/api/connectivity/direct-access-agents/<AGENT_ID>/configurations" \
  --data-urlencode "queryProperties=BENCHMARK_LOAD_PERFORMANCE_METRICS_RECORDING_ENABLED" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

The matching configuration entry includes the current `value` and whether the change can be
applied without restarting the gateway:

```json
{
  "name": "BENCHMARK_LOAD_PERFORMANCE_METRICS_RECORDING_ENABLED",
  "displayName": "Load Performance Metrics Recording Enabled",
  "value": "false",
  "defaultValue": "false",
  "apiActions": ["Read", "Write"],
  "applyWithoutRestart": true,
  "pendingApplication": false
}
```

If `value` is `false`, enable recording with a JSON Patch request:

```bash
curl -X PATCH \
  "https://<TENANT>/api/connectivity/direct-access-agents/<AGENT_ID>/configurations" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json-patch+json" \
  -d '[
    {
      "op": "replace",
      "path": "BENCHMARK_LOAD_PERFORMANCE_METRICS_RECORDING_ENABLED",
      "value": "true"
    }
  ]'
```

A successful request returns `204 No Content`. Because this configuration property has
`applyWithoutRestart: true`, the change takes effect without restarting the gateway.
Repeat the preceding `GET` request and confirm that `value` is `true` before continuing.

> **Note:** If a reload doesn't return metrics, confirm that load-performance recording is turned on before
> investigating the reload or filter values.

## Step 2: Run or identify a reload

Reload an application that uses a data connection routed through this gateway. For help building
or reloading a Qlik app, see the
[Qlik Cloud reload documentation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/Workflow/workflow.htm)
on Qlik Help.

Note the `appId` and approximate reload time so you can find the resulting metrics in the next
step.

## Step 3: Find the metrics for the reload

If you know the reload ID, retrieve all metric records associated with that reload:

```bash
curl -G \
  "https://<TENANT>/api/connectivity/direct-access-agents/<AGENT_ID>/load-performance-metrics" \
  --data-urlencode 'filter=reloadId eq "<RELOAD_ID>"' \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

If you don't know the reload ID, filter by `appId` first and use the reload time to identify the
records you need:

```bash
curl -G \
  "https://<TENANT>/api/connectivity/direct-access-agents/<AGENT_ID>/load-performance-metrics" \
  --data-urlencode 'filter=appId eq "<APP_ID>"' \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

Once you identify the `reloadId`, use the first request to retrieve all records for that reload.
Use `limit` and `page` when you need to paginate through a larger result set.

A matching metric record can look like the following. This example shows the fields most relevant
to this guide. The API returns additional fields such as `name`, `connectorUrl`, and
`sessionAppLoad`:

```json
{
  "metricId": "<METRIC_ID>",
  "status": "Completed",
  "dataSourceName": "PostgreSQL (via Direct Access gateway)",
  "reloadId": "<RELOAD_ID>",
  "appId": "<APP_ID>",
  "statement": "SELECT \"id\", \"customer_id\", \"product_id\", \"quantity\", \"order_date\" FROM \"public\".\"orders\"",
  "benchmarkingReload": false,
  "concurrentReloads": 1,
  "throughput": 8600,
  "approximateMaxConnectorThroughput": 9200,
  "connectorLatency": 42,
  "totalBytesTransferred": 15728640,
  "dataTransmissionStartTime": "2026-02-03T14:05:11.200Z",
  "dataTransmissionEndTime": "2026-02-03T14:05:12.980Z"
}
```

The endpoint also returns metrics generated by gateway benchmarks.
Use `benchmarkingReload` to distinguish the two:

- `benchmarkingReload: false`: application reload record.
- `benchmarkingReload: true`: benchmark-generated record.

Use `benchmarkingReload` as the discriminator rather than `appId`. The API contract doesn't
guarantee a specific `appId` value for benchmark-generated records.

A filter with no matches returns a successful, empty collection rather than an error:

```json
{
  "totalCount": 0,
  "totalPages": 0,
  "data": []
}
```

## Step 4: Analyze the reload

A single application reload can be associated with multiple metric records. Use `reloadId` to
group records from the same reload, and use fields such as `statement` and `dataSourceName` to
understand what each record represents.

The main correlation fields are:

- `metricId`: uniquely identifies one performance metric record.
- `reloadId`: the correlation key for all metric records associated with the same reload.
- `appId`: the Qlik application associated with the reload.
- `statement`: the load-script statement associated with the recorded operation.

### Interpret reload-performance metrics

The following fields are most relevant for analyzing reload performance.

- `throughput`: the measured data-transfer throughput in KB/s for this record. A record
  represents one load statement or transfer, not necessarily the whole reload.
- `approximateMaxConnectorThroughput`: an approximation of the maximum throughput the
  connector could deliver, excluding downstream write time.
- `connectorLatency`: the connector-side latency measured during data transmission.
- `concurrentReloads`: the number of concurrent benchmarks and reloads observed when this
  record's load started. Treat this as context, not a definitive overload indicator.
- `totalBytesTransferred`: the total bytes transferred for this record. Useful for comparing
  small operations against substantial ones.
- `statement`: the load-script statement for this record. Comparing records that share a
  `reloadId` can reveal which statement performed differently, without indicating a root cause.
- `dataSourceName` / `dataSourceId`: identify which data source was used; prefer
  `dataSourceName` in reports and `dataSourceId` for programmatic correlation.

### Compare records within the reload

Start by comparing records that share the same `reloadId` before comparing the reload with an
external baseline. For example:

```text
Reload <RELOAD_ID>

Statement A: throughput 8600 KB/s, connector latency 42 ms, 15 MB transferred
Statement B: throughput 1450 KB/s, connector latency 310 ms, 2 MB transferred
```

Use differences as investigation signals, not as proof of a root cause. For example:

| Observation                                        | Context to examine                                                               |
| -------------------------------------------------- | -------------------------------------------------------------------------------- |
| One statement has lower throughput than the others | Compare its statement, data source, transferred bytes, and connector latency.    |
| One statement has higher connector latency         | Check whether the difference is isolated to that data source or operation.       |
| Several records degrade together                   | Compare `concurrentReloads` and, if available, a recent gateway benchmark.       |
| A low-throughput record transferred little data    | Consider the transferred volume before treating throughput alone as significant. |

These comparisons narrow the investigation but don't establish whether the data source,
connector, gateway, application script, or workload factor caused the difference.

## Step 5: Compare with a benchmark baseline

Compare the reload metrics with a recent gateway benchmark from the same gateway under
comparable conditions. Use the benchmark as a baseline for comparison, not as an expected result for an
application reload.

Compare the baseline together with the reload's throughput, connector latency, transferred bytes,
and concurrent activity. Differences can show where further investigation may be useful, but they
don't establish a root cause because application reloads include data-source, load-statement,
data-volume, and workload factors that the benchmark doesn't represent in the same way.

For how to run and interpret a benchmark, see
[Run and review Direct Access Gateway benchmarks](https://qlik.dev/manage/connectivity/run-review-direct-access-gateway-benchmarks/).

## Verification

Confirm the workflow succeeded when a `GET` request filtered by `reloadId` or `appId` returns at
least one metric record with `status: "Completed"` for the reload you ran.

## Troubleshooting

### Issue: No metrics are returned for a reload

**Solution:** Confirm that load-performance recording is turned on (see
[Step 1](#step-1-turn-on-load-performance-recording)), that the reload used a data connection
routed through this gateway, and that your `reloadId` or `appId` filter value is correct.

### Issue: Filter request rejected with HTTP 400

**Solution:** Only filter on properties documented for this endpoint, such as `reloadId` and
`appId`. Unsupported filter attributes return a validation error.
