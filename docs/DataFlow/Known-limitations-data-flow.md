---
title: "Known limitations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/Known-limitations-data-flow.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow"]
---
# Known limitations

This release of the data flow capability includes several limitations and known issues that will be fixed over time.

## General

- On Android devices, dragging and dropping nodes in the data flow canvas may cause nodes to fade or disappear. To restore the view, navigate to the **Overview** tab and then return to the editor.
- A minimum supported size for the browser window exists, but is not enforced. Reducing the window size too much will cause a poor experience with the interface.
- If the source or target of a data flow refers to a space that has been renamed since the creation of the flow, it will appear valid but will fail to run. Configure your sources and targets again to fix the data flow.
- The **Modified date** available in the **Overview** tab will only be updated after a run or when any of the name, description or tags of the data flow are edited, and not when the design of the data flow itself is changed.
- To make sure latest developments and fixes from the development team are properly applied to your data flow, we recommend making an edit to the name or description of the data flow. This will trigger a recomputation of the script and related applications.
- When editing a node (source, processor, target) in the properties panel, name or description edits in the upper panel, and node configuration in the lower panel must be saved separately or information can be lost. In the example of a processor, if you edit the name without clicking **Save changes**, change the processor parameters and click **Apply**, the name change will not be saved.
- Data flows are subject to the same data and field limits that apply when loading data in Qlik Cloud Analytics. For example, a field cannot have more than 2,147,483,648 distinct values, and the total number of fields and rows that can be loaded is limited by available memory. For details, see [*Guidelines for data and fields*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/guidelines-data-fields.htm).

## Data preview

- If you change the type or name of a data flow target, the underlying script will be updated, invalidating the current data preview. You need to manually refresh the data preview panel if you want to use it again.
- The row limit of the data preview can cause some inconsistencies between rows displayed in two processors that seemingly have the same configuration. For example, two **Aggregate** processors can return different results if one uses a load statement referring directly to the source data file, and the other uses a resident load statement referring to the same table but placed after a processor like **Fork** This is due to slight differences in the script generation. However, when running the data flow on the full data, the values will be correctly calculated.

## Sources and targets

- Data flows targets can only be stored as files.

## Processors

- **Dates**:

  - The **Convert to date** and **Convert to timestamp** can fail when applied to a field that is read from a source format with a native date support such as Excel.
  - When adding years, months, weeks or days to a timestamp with the **Add duration** function, it will be formatted as a date. However, the underlying value contains the correct timestamp.
  - When formatting dates using a **Date** processor located after a **Filter**, **Fork**, or **Unpivot** processor (where the script uses a resident load statement), you will get a validation error and the function may not work. Try moving the **Date** processor upstream of the other ones.
- **Window**:

  - Relies on the [window script function](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/WindowFunctions/Window.htm), with the same limitations.
  - When using the **Concatenate** operation, a delimiter is required. You cannot leave the **Delimiter** field empty.
- **Filter**: The processors show "Undefined" as description when no field has been selected.
- **Pivot**:

  - The field to pivot and the value field cannot have duplicated content.
  - Null and empty values are not allowed in the field to pivot because the Qlik engine does not support blank field names.
  - If a **Sort** processor is placed before a **Pivot** processor, the pivot operation will work but the sorting will be lost. You need to place the **Sort** processor downstream of the **Pivot** processor.
  - There is an upper limit of 500 on the number of distinct values that can be contained in the field to pivot. Use the cog icon in the Preview panel to set the load limit.
  - It is not possible to use a field that is the output of a **Hash** processor as field to pivot.

## Collaborative work

- Although collaboration from two users or more on a single data flow is limited at this time, it is possible for multiple users to edit a data flow in a shared space. If you open a data flow, and someone makes a concurrent change, a prompt will open to notify that you need to reload the data flow. After you get the latest version, you can make your change.
- Data flows do not currently support the versioning feature found in Scripts and Applications.
