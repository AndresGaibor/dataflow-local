---
title: "Working with errors"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-errors.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations"]
---

# Working with errors

Errors are thrown when the automation fails. This section shows you how to configure error handling and how to catch errors in the automation.

## Error setting for each block

The Settings tab on each block lets you choose how the block behaves on error.

Error settings options

![The error options on the settings section of block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/on-error.png)

- Ignore - Continue automation and ignore errors

  The automation continues to run, and the error is ignored and not logged. The status is set to Finished.
- Warning - Warning - Continue automation and report errors

  The automation continues to run and the error is logged. The status is set to Finished with warnings.
- Stop - Stop automation and set status to `failed`

  The automation stops execution when the first error occurs. The status is set to Failed.

## Execution history

The automation history shows the status of each execution. The History tab is available in the Overview section of the automation.

View of automation history

![The history section of the automation](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/automation-history.png)

An automation can have one of the following statuses:

- Not started
- Starting
- Running
- Paused
- Finished
- Stopped
- Failed
- Must stop
- Finished with warnings

The execution logs contain the input and output for each block. This lets you search automation executions based on data that was processed during that execution. The execution logs can help you find errors in your automation.

Information note

The history is limited to 5000 automation executions and a total of 500 MB per automation. If these limits are exceeded, older executions are deleted.

## Catching errors

Execution details identify a renamed block by its custom display name. To catch its error with a formula, use the block's original internal name, not its custom display name. The basic formula looks like this:

`{ $.state.blockName.error }`

To return specific error status, use `{ $.state.blockName.error.response.status }`.

To return the error body, use `{ $.state.blockName.error.response.body }`.
