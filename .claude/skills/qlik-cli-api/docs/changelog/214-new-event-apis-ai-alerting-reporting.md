---
source: https://qlik.dev/changelog/214-new-event-apis-ai-alerting-reporting/
last_updated: 2026-04-23T18:37:33+01:00
---

# New system events for AI MCPs, alerting tasks, and reporting tasks

Qlik Cloud system events now include three new event APIs, enabling you to build
reactive integrations that respond to AI agent activities, alert management operations,
and reporting task completions.

### AI MCPs \{#213-ai-mcps}

The [AI MCPs event API](https://qlik.dev/apis/event/ai/mcps/) publishes events related to AI Model Context Protocol
Server (MCP) tool executions:

- `com.qlik.ai.mcp.tool.calls.aggregated`: Aggregated summary of tool calls published when a configured threshold or
  timeout is reached
- `com.qlik.ai.mcp.tool.executed`: Individual tool execution events

Use these events to analyze tool usage patterns, detect performance trends, and monitor tool performance.

### Alerting tasks \{#213-alerting-tasks}

The [Alerting Tasks event API](https://qlik.dev/apis/event/alerting-tasks/) covers the complete lifecycle of alerting
task management:

- `com.qlik.v1.alerting-task.created`: New alerting task created
- `com.qlik.v1.alerting-task.deleted`: Alerting task deleted
- `com.qlik.v1.alerting-task.execution-summary.created`: Execution summary generated after an alert runs
- `com.qlik.v1.alerting-task.recipient.removed`: Recipient removed from an alerting task
- `com.qlik.v1.alerting-task.task-status.changed`: Task status changed

Use these events to track alert creation, clean up alert subscriptions, monitor alert execution health, revoke alert
access, and implement status-driven workflows.

### Reporting tasks \{#213-reporting-tasks}

The [Reporting Tasks event API](https://qlik.dev/apis/event/reporting-tasks/) provides events for reporting
task execution:

- `com.qlik.reporting-task.summary.created`: Summary generated when a reporting task completes

Use these events to track reporting outcomes and execution statistics.
