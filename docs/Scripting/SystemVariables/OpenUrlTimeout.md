---
title: "OpenUrlTimeout"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/OpenUrlTimeout.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "System variables"]
---

# OpenUrlTimeout

This
variable defines the timeout in seconds that Qlik Sense should respect when
getting data from URL sources (e.g. HTML pages). If omitted, the timeout
is about 20 minutes.

Syntax:

OpenUrlTimeout

Example:

set
OpenUrlTimeout=10;

## Learn more

- [*System variables*](system-variables.htm)
