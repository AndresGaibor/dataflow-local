---
source: https://qlik.dev/changelog/180-api-updates-direct-access-agents-benchmarking/
last_updated: 2025-11-20T16:51:56+01:00
---

# Updated API - Direct Access Agents API now includes benchmarking endpoints

The [Direct Access Agents API](https://qlik.dev/apis/rest/direct-access-agents/) has been updated with new endpoints that allow you to
benchmark the performance of Direct Access agents. These endpoints enable you to measure agent throughput and latency
for capacity planning and performance optimization.

The following new endpoints give you control over agent benchmarking:

- `POST /api/v1/direct-access-agents/{agentId}/benchmarks` - Start a background benchmark task to measure the
  performance of a Direct Access agent.
- `GET /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}` - Retrieve the current status and progress of a
  running or completed benchmark task, including performance metrics.
- `POST /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel` - Request cancellation of a running
  benchmark task.

These new endpoints are supported from Direct Access Gateway 1.7.8 onward and are available only to users with the
`TenantAdmin` (Tenant Admin) role. Users must also be either a Gateway's space owner or a member in the Gateway's space
with `dataconsumer` (Can consume data) role.

For more information, refer to the [API reference documentation](https://qlik.dev/apis/rest/direct-access-agents/).
