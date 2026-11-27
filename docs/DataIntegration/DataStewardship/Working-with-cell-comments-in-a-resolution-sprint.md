---
title: "Working with cell comments in a resolution sprint"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataStewardship/Working-with-cell-comments-in-a-resolution-sprint.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Validating and correcting your data with data stewardship"]
---

# Working with cell comments in a resolution sprint

Use cell comments to capture context about a value, explain a correction, or ask a follow-up question while you work in a resolution sprint.

Cell comments are attached to a specific record and field value. They help data stewards and sprint owners collaborate without leaving the sprint workflow. Comments remain associated with the relevant record so that the context is easy to review later.

## Adding a comment to a cell

1. Open the record that you want to review in the sprint.
2. Click or hover your mouse over the cell that needs context or a note.
3. Click the cell's three-dot menu and then click Comment.
4. Enter your comment and click Comment.

   The comment is not immediately saved until you click Apply changes. Before that, if you switch tabs or navigate away, the comment is discarded.

   Adding a comment alone does not activate the Apply
   changes button. You must mark the record as ready or assign the
   record to another steward.

A comment can contain up to 200 characters. If your comment exceeds the limit, an inline error appears and you cannot submit it until you shorten the text.

Click Cancel to discard your changes.

After applying changes, your comment is associated with the selected cell and is available to other users who can view the record.

## Replying to a thread

1. Click the small triangle to open the cell menu for the comment you want to reply to.

   This opens the comment thread for the selected cell.
2. Click Comment.
3. Enter your comment and click Comment.

The new comment is appended to the chronological list. Cell comments do not support replies to a specific comment.

## Saving your comments

Comments also appear in Pending changes. You can add, edit, or delete comments for records shown in that panel.

As explained earlier, you must click Apply changes to save the comment change. If you switch tabs before applying the change, the change is discarded.

## Editing or deleting a comment

You can edit your own comment at any time. You can delete your own comment only before you click Apply changes. After you apply the change, you can edit the comment but you cannot delete it. Deleting a comment requires confirmation and cannot be undone.

1. Open the cell comment.
2. Click the ellipsis menu next to your comment.
3. Click Edit or Delete.

When editing a comment, the 200-character limit also applies.

## Viewing all comments in a sprint

Click Comments in the sprint toolbar to open the comments drawer. The drawer lists comment threads for records currently loaded in the grid. It shows a preview with the author, date, first comment, and number of additional comments. You can sort the list by date.

Click a comment entry to scroll to its record and open the cell comment. To find comments on other records, load those records in the grid by clicking Fetch more.

## Viewing comments on a cell

Open the cell menu and click Comment to view the chronological list for that cell. The same menu includes History, which shows the cell's value-change history. For more information, see [*Reviewing AI fixes in a resolution sprint*](Reviewing-AI-suggestions.htm).

Comments can still be added to resolved records after the sprint is closed.

## Troubleshooting cell comments

- **Your comment disappeared after you changed tabs:** Click Apply changes before changing tabs. Unapplied comment changes are discarded.
- **You cannot find a Reply button:** Cell comments use a flat chronological list. Add another comment from the cell's Comment menu instead.
- **You cannot delete a comment:** Only the comment's author can delete it, and deletion is available only before the comment change is applied.
- **A comment does not appear in the comments drawer:** The drawer lists comments only for records currently loaded in the grid. Click Fetch more and check again.
- **You can add a comment to a record in a closed sprint:** This is expected for resolved records. Closed sprints are read-only for record data, but comments can still be added.

For permissions, persistence, and export details, see [*Comment threads and permissions in a sprint*](Comment-threads-and-permissions-in-a-sprint.htm).

Information note

Comments are intended to support collaboration during the sprint. They are not a replacement for the formal record validation status or the sprint assignment workflow.
