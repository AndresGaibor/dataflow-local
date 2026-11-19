---
title: "CreateSearchIndexOnReload"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/CreateSearchIndexOnReload.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "System variables"]
---
# CreateSearchIndexOnReload

This variable defines if search index files are created when an application's data is reloaded.

Syntax:

CreateSearchIndexOnReload

You can define if search index files are created during data reload, or if they are created with the first user search request.

Creating search index files during data reload avoids the waiting time experienced by the first user search. This must be weighed against the longer data reload time required by search index creation.

Omitting this variable (or setting to 0) results in the search index files not being created during data reload.

If this variable is set to 1, search index files are created upon data reload, with the following condition:

- The first time a reload is performed on the application.
- The application has been searched recently (determined by the number of days that have passed since the last search was performed on the application).
- The application's data is relatively large (determined by the duration of the most recent index creation).

> **Note:** For session applications, search index files will not be created during data reload, regardless of the setting of this variable.

> **Note:** New applications include `set
> CreateSearchIndexOnReload=1` in the default `SET` statements. When creating scripts in the Analytics activity center, the SET expressions does not include `CreateSearchIndexOnReload` as script assets do not persist data, making an index value unnecessary.

Example 1: Create search index fields during data reload

set
CreateSearchIndexOnReload=1;

Example 2: Create search index fields after first search request

set
CreateSearchIndexOnReload=0;
