---
source: https://qlik.dev/manage/connectivity/run-review-direct-access-gateway-benchmarks/
last_updated: 2026-09-22T18:29:29+02:00
---

# Run and review Direct Access gateway benchmarks

## Overview

A [Direct Access gateway](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm)
benchmark measures gateway performance under a controlled workload. Use it to establish a repeatable performance
baseline and compare results under similar conditions, without needing a real application reload.

The workflow is asynchronous: start a benchmark, poll it until it completes, then inspect the results.

```text
Start benchmark → get benchmark ID → monitor status → inspect completed metrics → review history
```

## What you'll learn

At the end of this guide, you'll have a benchmark result that you can retain as a baseline and
compare with later runs performed under similar conditions, using the
[Direct Access Agents API](https://qlik.dev/apis/rest/connectivity/direct-access-agents/).

If you want performance data for a real application reload instead of a synthetic test, see
[Analyze Direct Access gateway reload performance](https://qlik.dev/manage/connectivity/analyze-direct-access-gateway-reload-performance).

## Prerequisites

- A Direct Access gateway registered on your tenant, running version **1.7.17** or later.
- The requester must have the `TenantAdmin` role and be either the gateway's space owner or a
  member of the gateway's space with the `Can Consume Data` role.
- A bearer access token for authenticating requests. For setup, see [Authentication](https://qlik.dev/authenticate).
- The Direct Access agent's identifier. To find the agent ID:
  1. In Qlik Cloud go to **Administration** > **Data gateways**.
  2. Locate the Direct Access gateway, select **...** > **Gateway settings**, and copy
     the Agent ID under General settings.

## Step 1: Start a benchmark

Give the benchmark a meaningful `name` and `description`, since you'll use them to find this run
later in the benchmark history.

```bash
curl -X POST -G \
  "https://<TENANT>/api/connectivity/direct-access-agents/<AGENT_ID>/benchmarks" \
  --data-urlencode "name=connectivity-baseline" \
  --data-urlencode "description=Morning gateway baseline" \
  --data-urlencode "gigaBytesToTransfer=1" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

A successful response includes the `benchmarkId`:

```json
{
  "benchmarkId": "<BENCHMARK_ID>"
}
```

Save the `<BENCHMARK_ID>` for the next steps.

> **Note:** Starting a benchmark only queues the task. The benchmark runs in the background, so you need to
> poll its status to know when it completes.

This example requests a 1 GB benchmark and uses `connectivity-baseline` as the name.
`name` and `description` are limited to 50 and 200 characters respectively.
For supported values and the full parameter list, including the `force` parameter,
see [Start an agent benchmark](https://qlik.dev/apis/rest/direct-access-agents/) in the API reference.

## Step 2: Monitor the benchmark

Retrieve the benchmark status by ID:

```bash
curl \
  "https://<TENANT>/api/connectivity/direct-access-agents/<AGENT_ID>/benchmarks/<BENCHMARK_ID>" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

While the benchmark is running, `results` is `null` and `benchmarkEndTime` is unset:

```json
{
  "benchmarkId": "<BENCHMARK_ID>",
  "status": "ReloadInProgress",
  "statusMessage": null,
  "benchmarkEndTime": null,
  "results": null
}
```

Poll this resource periodically while the benchmark remains in progress. Choose an interval
appropriate to your environment.

Treat the run as successful only when `status` is `Completed` and `results` is populated. If the
benchmark finishes without a populated result, inspect `status` and `statusMessage` before deciding
how to handle the run.

## Step 3: Review the completed results

Once the benchmark finishes, the same request returns the performance results:

```json
{
  "benchmarkId": "<BENCHMARK_ID>",
  "name": "connectivity-baseline",
  "status": "Completed",
  "statusMessage": null,
  "concurrentReloads": 0,
  "benchmarkStartTime": "2026-01-15T09:12:04.201Z",
  "benchmarkEndTime": "2026-01-15T09:14:47.588Z",
  "results": {
    "throughput": 15420,
    "latency": 385,
    "connectorLatency": 6,
    "totalBytesTransferred": 1073741824,
    "dataTransmissionStartTime": "2026-01-15T09:12:41.055Z",
    "dataTransmissionEndTime": "2026-01-15T09:14:47.402Z"
  }
}
```

> **Note:** `results.connectorLatency` can be `null` on this endpoint.

## Step 4: Understand the benchmark metrics

Use benchmark results primarily as a baseline for comparison.
Compare runs from the same gateway under similar workload and environmental
conditions rather than treating an individual throughput or latency value as a
universal performance threshold.

### Throughput

`results.throughput` is the measured data-transfer throughput in KB/s. Use it to compare
benchmark runs performed under similar conditions.

### Latency

Two fields describe latency:

- `results.latency`: the latency measured during data transmission.
- `results.connectorLatency`: the average latency measured on the connector side during data
  transmission.

The Direct Access gateway benchmark UI displays a single **Latency** value that combines both:

```text
UI Latency = results.latency + results.connectorLatency
```

For example, `385 ms + 6 ms = 391 ms`.

### Concurrent reloads

`concurrentReloads` reports the number of concurrent benchmarks and reloads observed when this
benchmark started. Use it as context when comparing runs performed under different levels of
gateway activity.

### Data transferred

`results.totalBytesTransferred` is the total number of bytes successfully transferred during the
benchmark.

### Duration

The API exposes two different durations:

- **Data transmission duration**: `results.dataTransmissionEndTime` minus
  `results.dataTransmissionStartTime`. This corresponds to the UI **Duration** value.
- **Overall benchmark time**: `benchmarkEndTime` minus `benchmarkStartTime`. This corresponds to
  the UI **Time taken** value and includes setup work that happens before data transmission
  starts.

## Step 5: Review previous benchmarks

List the benchmark history for the gateway when you need to compare the current result with earlier
runs:

```bash
curl \
  "https://<TENANT>/api/connectivity/direct-access-agents/<AGENT_ID>/benchmarks" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

The response is a paginated collection. The following example shows one entry from `data` for
readability:

```json
{
  "page": 1,
  "limit": 20,
  "totalCount": 3,
  "totalPages": 1,
  "data": [
    {
      "benchmarkId": "<BENCHMARK_ID>",
      "name": "connectivity-baseline",
      "status": "Completed"
    }
  ]
}
```

By default, the newest benchmark is returned first. For example, filter by `name` to retrieve runs
created for the same baseline:

```bash
curl -G \
  "https://<TENANT>/api/connectivity/direct-access-agents/<AGENT_ID>/benchmarks" \
  --data-urlencode 'filter=name eq "connectivity-baseline"' \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

Compare runs performed under similar conditions, including gateway activity such as
`concurrentReloads`. For the complete filtering, sorting, and pagination options, see the
[Direct Access Agents API reference](https://qlik.dev/apis/rest/direct-access-agents/).

## Verification

A benchmark run is complete when `GET /benchmarks/{benchmarkId}` returns `status: "Completed"`
with a populated `results` object. You can then retrieve the run from the benchmark history in
[Step 5](#step-5-review-previous-benchmarks).

## Troubleshooting

### Issue: `name` or `description` rejected with a validation error

**Solution:** Keep `name` to 50 characters or fewer and `description` to 200 characters or fewer.

### Issue: Filter request rejected with HTTP 400

The filter request returns HTTP 400 with an unsupported attribute error.

**Solution:** Only filter on properties documented for this endpoint, such as `name` and
`benchmarkStartTime`.
