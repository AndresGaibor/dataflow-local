---
source: https://qlik.dev/embed/foundational-knowledge/visualizations/write-table/
last_updated: 2026-03-24T09:51:59+01:00
---

# Write table

The write table allows users to make changes in editable columns during data analysis.
Saved changes are stored in a change store, which analytics developers
can use to implement automated, real-time processes and ensure data quality.

> **Limitations:** The write table cannot be embedded using qlik-embed.
>
> The write table supports custom themes, but you cannot use custom themes to
> change colors that define cell statuses (orange, green, and blue).

> **Security considerations:** A malicious user with access to an application and write table permissions could
> emulate a client session on an application containing a write table.
> By guessing primary key values, they can gain access to changes that were made
> on records they cannot access according to the application's section access rules.
> Consider these risks when adding the write table to applications that use section access,
> and when granting users view and edit access to applications containing the write table.

## Additional references

For more information about the write table, see
[Write table](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Analyze/write-table.htm)
on the Qlik help site.
