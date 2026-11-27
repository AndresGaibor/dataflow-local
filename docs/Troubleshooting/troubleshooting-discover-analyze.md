---
title: "Troubleshooting - Using applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Troubleshooting/troubleshooting-discover-analyze.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data"]
---

# Troubleshooting - Using applications

This section describes problems that can occur when discovering and analyzing in Qlik Sense.

## My search does not produce any results

Possible cause

You have locked [selections](#glossary-0 "Glossary term").

Proposed action

Unlock the selections and then perform a new search.

Do the following:

1. Click on the selection with ![Locked](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_lock.svg).
2. Click ![Locked](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_lock.svg) to unlock.
3. Perform a new search.

## My search using Insight Advisor does not produce any results

Possible cause

You are searching for a field which is not a [master item](#glossary-1 "Glossary term").

Proposed action

Search for a master item instead. Additionally you can use smart search to find fields which are not master items.

## Incomplete visualization

A [visualization](#glossary-2 "Glossary term") is not displayed, instead an error message Incomplete visualization is displayed.

Possible cause

The visualization contains data fields that you do not have access to.

Proposed action

Contact your Qlik Sense administrator to see if you can get access to the omitted data fields, to be able to use the visualization.
