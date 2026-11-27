---
title: "Comment threads and permissions in a sprint"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataStewardship/Comment-threads-and-permissions-in-a-sprint.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Validating and correcting your data with data stewardship"]
---

# Comment threads and permissions in a sprint

Cell comments in a sprint are tied to the record and field context. They provide a lightweight collaboration channel for data stewards and sprint owners while validation work is in progress.

Comment threads are scoped to the relevant cell value. A thread is a flat chronological list of comments. It does not support replies to a specific comment.

## Key behaviors to expect when using in-cell comments

- Comments and edited comments can contain up to 200 characters.
- Comments are not included when you export sprint data.
- Adding a comment does not send a sprint notification.

## Who can comment

Any user with read access to a record can view all comments for that record. Only the sprint owner and the steward can author comments, and only the author of a comment can edit or delete it. A comment's author can edit it at any time, but can delete it only before the comment change is applied.

Comment capabilities do not change the record status or approval workflow. The sprint view remains the source of truth for the current validation state, while the comment thread provides supporting collaboration context.

## How comment threads work

- Each cell can have one discussion thread.
- Comments appear in a flat chronological list. To add another comment, reopen the cell's Comment menu.
- Adding, editing, and deleting comments are not saved until you click Apply changes.
- Comments remain actionable for records shown in the Pending changes panel.
- Comments remain connected to the record and field value. Changing a cell value does not remove its comments.
- Comments remain when their author is deleted. Deleting a record also deletes all comments associated with that record.
- The time and date of a comment uses the timezone configured in your user settings.

Information note

Comment threads are designed to support operational collaboration. They do not replace the sprint assignment, owner validation, or export workflow.

Comments are not currently tied to sprint notifications. Use comments to ask clarifying questions, capture rationale, or record decisions that help other users understand the validation result. For more detail on adding, editing, and viewing comments, see [*Working with cell comments in a resolution sprint*](Working-with-cell-comments-in-a-resolution-sprint.htm).
