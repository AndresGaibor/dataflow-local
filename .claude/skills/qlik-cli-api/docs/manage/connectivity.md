---
source: https://qlik.dev/manage/connectivity/
last_updated: 2026-09-22T18:29:29+02:00
---

# Overview

A [Direct Access gateway](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm)
lets Qlik Cloud reach data sources behind your organization's firewall over an
outbound-only, encrypted connection, without opening inbound firewall ports.
Once a gateway is registered and used for data connections, you can use the
[Direct Access Agents API](https://qlik.dev/apis/rest/direct-access-agents/) to measure and
monitor its performance programmatically.

This section covers two related, but distinct, performance workflows:

- **Gateway benchmarks**: a synthetic, controlled test that measures the raw
  data-transfer throughput and latency between a Direct Access gateway and
  Qlik Cloud, independent of any specific app or data source.
- **Reload performance metrics**: real measurements captured while an actual
  Qlik application reload is processed through the gateway, broken down by
  data source and load statement.

## Get started

- [Run and review Direct Access gateway benchmarks](https://qlik.dev/manage/connectivity/run-review-direct-access-gateway-benchmarks/) - Start a gateway benchmark, monitor progress, and interpret throughput and latency results
- [Analyze Direct Access gateway reload performance](https://qlik.dev/manage/connectivity/analyze-direct-access-gateway-reload-performance/) - Retrieve and interpret performance metrics for real application reloads processed through a gateway

## Related resources

- To create data connections that route through a Direct Access gateway, see
  [Connect via a direct access data gateway](https://qlik.dev/manage/data-connections/gateway-data-connections).
- For the complete set of gateway management endpoints, see the
  [Direct Access Agents API reference](https://qlik.dev/apis/rest/direct-access-agents/).
