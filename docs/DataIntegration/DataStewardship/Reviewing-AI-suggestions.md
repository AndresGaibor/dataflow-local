---
title: "Reviewing AI fixes in a resolution sprint"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataStewardship/Reviewing-AI-suggestions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Validating and correcting your data with data stewardship"]
---

# Reviewing AI fixes in a resolution sprint

When Data remediation is enabled on a resolution sprint, an AI agent analyzes records and fixes invalid cell values. The fixed records are then reassigned to data stewards for review.

Data remediation uses generative AI to analyze records in the sprint and correct cells that contain invalid data. The AI agent edits cell values. The records are then reassigned to a data steward for review. Cells that were edited by the AI are marked with an AI indicator badge so you can distinguish them from original values.

Information noteData remediation fixes invalid cell values only. Empty cells are not corrected unless a validation rule marks empty values as invalid.

Record data is sent to a third party generative AI (GenAI) model. The information is treated as customer data and will not be used to train Qlik Cloud or the GenAI model. For more information, see [Information that is shared](#shared-information).

Warning noteThis feature uses generative artificial intelligence ("GenAI"). It is the user's responsibility to review and verify any GenAI output before using or sharing it, and to evaluate whether the use of it is appropriate for any particular use case and whether it complies with applicable laws.

Qlik Cloud Government note

Data remediation is not available in Qlik Cloud Government.

## Prerequisites

Before you can use Data remediation in a resolution sprint:

- A Tenant Admin must enable cross-region inference. For more information, see [*Enabling cross-region inference*](../../Admin/cross-region-data-processing.htm).
- Data remediation must be enabled in the sprint settings when creating or editing the sprint. For more information, see [*Creating a resolution sprint with a Talend Studio job*](Creating-sprint-job.htm) or [*Creating a resolution sprint from a CSV file*](Creating-sprint-file.htm).

## How AI fixes are displayed

When Data remediation is enabled, the AI agent processes records when the sprint is populated. Cells that were edited by the AI are marked with an AI indicator badge. The badge uses a distinctive color to help you identify which values were corrected by the AI agent.

## Reviewing AI fixes

After the AI agent has corrected invalid values and marked the records as ready, the records are reassigned to a data steward for review. As a data steward, you review the AI-edited records in Assigned to me.

For each record with AI fixes, you can:

- **Keep the AI fix** — If the corrected value is accurate, no further action is needed on that cell.
- **Edit the value** — If the corrected value is not accurate, edit the cell to enter the correct value.

When you have reviewed all cells in a record, click Mark as ready to confirm the record.

## Viewing cell history and AI reasoning

You can view the full history of changes for a cell, including AI edits and the reasoning behind each AI fix.

- Click on a cell and open the cell history to see all changes, including the original value, the AI-corrected value, the reasoning for the fix, and any manual edits.

## AI processing

When the sprint is populated with records, the AI agent processes the records to identify and fix invalid values. A progress indicator shows the processing status. You can continue working on records that have already been processed while the remaining records are being analyzed.

## Information that is shared

The following information is shared with the generative AI model to generate remediation suggestions:

- The column names and data types defined in the sprint schema
- The validation rules applied to columns
- The cell values in the records being processed
