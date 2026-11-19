---
source: https://qlik.dev/changelog/250-direct-access-agents-api-connectivity-benchmark-updates/
last_updated: 2026-11-12T18:51:23+01:00
---

# Direct Access Agents benchmarking endpoints added to the Connectivity namespace

> **Note:** Updated on November 12, 2026: The `/api/v1/direct-access-agents` API has since been deprecated. See
> [Direct Access Agents API deprecation](https://qlik.dev/changelog/268-direct-access-agents-api-deprecation/) for details.

Direct Access Agents benchmarking endpoints are now available in the `connectivity` namespace at
`/api/connectivity/direct-access-agents`.

The namespaced API includes:

- `POST /api/connectivity/direct-access-agents/{agentId}/benchmarks` - Start a benchmark.
- `GET /api/connectivity/direct-access-agents/{agentId}/benchmarks` - Retrieve a paginated list of benchmark statuses.
- `GET /api/connectivity/direct-access-agents/{agentId}/load-performance-metrics` - Retrieve reload performance metrics.
  Recording is off by default. Turn it on by setting the
  `BENCHMARK_LOAD_PERFORMANCE_METRICS_RECORDING_ENABLED` configuration property to `true`.

The benchmark start endpoint supports `name` and `description` query parameters for labeling a benchmark run.

The existing [Direct Access Agents API](https://qlik.dev/apis/rest/direct-access-agents/) at `/api/v1/direct-access-agents` is not
deprecated and continues to work as documented.

These endpoints require the `TenantAdmin` (Tenant Admin) role. The requester must also be either the gateway's space
owner or a member of the gateway's space with the `dataconsumer` (Can consume data) role.

The new `GET` endpoints are supported from Direct Access gateway 1.7.17 onward. The benchmark start endpoint is
supported from Direct Access gateway 1.7.8 onward.

For step-by-step guidance, see
[Run and review Direct Access gateway benchmarks](https://qlik.dev/manage/connectivity/run-review-direct-access-gateway-benchmarks/)
and [Analyze Direct Access gateway reload
performance](https://qlik.dev/manage/connectivity/analyze-direct-access-gateway-reload-performance/).

> **Tip:** For details about API namespaces, timing, and the complete list of available namespaced APIs, see the
> [API namespaces overview](https://qlik.dev/apis/namespaces/).
