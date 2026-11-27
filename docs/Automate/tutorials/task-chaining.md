---
title: "Task chaining"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/tutorials/task-chaining.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Tutorials"]
---

# Task chaining

Automations make it easy to use events and actions to trigger other events and actions. This is called task chaining. A task chain is a set of tasks that are executed in an automation, either in parallel or one after the other. This tutorial walks you through an end-to-end example in steps of increasing complexity that shows you how to build a task chain. The goal of this automation is to trigger app reloads for multiple apps in your tenant by chaining multiple reloads together.

## Create a simple reload automation

Start by creating an automation that triggers an app reload.

1. From the Block library on the left side of the automation canvas, select the Qlik Cloud Services connector.
2. Drag the Do reload block onto the canvas and attach it to the start block.

   ![A simple reload automation](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/ui_QAA_reload-automation.png)
3. In the App ID input field for the Do reload block, enter the App ID for the app you want to reload.

   Information note

   You can use the lookup function in the App ID field to find the App ID.
4. Click Run.
5. Verify in the block output that you see `status: SUCCEEDED`. This indicates that the reload was successful.

   ![Output of reload block showing succeeded](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/status-succeeded.png)

### Reload run modes

In the steps above, you did not specify the run mode for the Do reload block. However, when creating task chains, this input is important. You have two options: Wait for reload to complete and Start reload and continue. That is, run the reloads one after the other or run them in parallel.

The default setting is Wait for reload to complete, which is a run mode where the automation waits for the current reload to return the status before proceeding to the next block.

When using this run mode with the Do reload block, you can set the block to throw an error when the reload fails. To do this, select Yes in the Throw Error On Failed Reload input field. The default setting is No.

The alternative setting is Start reload and continue, which is a run mode where the reload is triggered, a reload ID is returned, and the automation moves to the next block. If there are multiple Do reload blocks, they are triggered before waiting for the preceding reload to return a status.

Tip note

Use the reload ID in the block Get reload record block to get the reload status.

## Create a reload task chain

Continuing with the same reload automation from above, add another Do reload block to create a task chain to reload two apps.

1. Set the run mode for the first Do reload block to Wait for reload to complete. This way, the second Do reload block will only execute once the first Do reload block is finished.
2. Drag a second Do reload block onto the canvas and attach it to the existing Do reload block.

   ![Task chain with two reloads](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/ui_QAA_task-chain.png)
3. Click Run.
4. Verify in the block output that you see `status: SUCCEEDED` for both reload blocks. This indicates that the reloads were successful.

## Add a condition to the task chain

In the task chain above, both reloads are triggered regardless of the reload status. Add a condition to trigger the second reload only if the first reload is successful.

1. Remove the second Do reload block from the automation by dragging to another place on the canvas.

   ![Taks chain reload block removed](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/ui_QAA_task-chain-removed.png)
2. From the block selector pane, drag a basic condition block onto the canvas and attach it below the first Do reload block.
3. In the Inputs field for the condition block, field map the status of the app reload from the Do reload block and set the condition statement to `equals` and type SUCCEEDED in the Value field.

   ![Task chain condition settings](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/ui_QAA_task-chain-condition.png)
4. Re-add the second Do reload block to the YES branch of the condition. This means that if the condition is `true`, the second Do reload block is executed.

   Tip note

   Add block comments so you can see what each block does without opening it.

   ![task chain with two reload blocks and condition](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/ui_QAA_task-chain-condition-full.png)
5. Click Run to see the output.

## Run reloads in parallel

Next, add multiple Do reload blocks to your automation. For each Do reload block, set the run mode to Start reload and continue.

1. Move the condition block to the side so you are left with the start block and a single Do reload block.
2. Take the second Do reload block from inside the condition and reattach it below the first Do reload block.
3. Set the run mode for each Do reload block to Start reload and continue.

   The automation looks like this, with both reloads running in parallel:

   ![Task chain with two reloads](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/ui_QAA_task-chain.png)
4. Below the second Do reload block, add a Wait for reloads to complete block.
5. In the Reload IDs field, add the reload ID from the first two Do reload blocks, separated by a comma.

   The raw input looks like this: `{$.DoReload.id},{$.DoReload2.id}`.

   Tip note

   Make sure to use the reload ID and not the app ID.
6. Add another Do reload block and configure it to reload another app.

   ![An automation with 3 reload blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/ui_QAA_task-chain-reloads.png)

## Add a loop to the task chain

In this example, use a loop block to loop over all the apps in your tenant and to trigger a reload for each one.

1. Move all of the blocks below the start block to the side.
2. Add a List apps block to the start block. This block is a loop block.
3. Click Test run on the block to get the IDs you need for the next block.
4. Inside the loop, add a Do reload block.
5. In the App ID field of the Do reload block, map the App ID obtained from the from the List apps block. Set the Run Mode to Start reload and continue.
   The raw format looks like this: `{$.listApps.item.id}`. The input to the Do reload block will loop through the app IDs in the list until it reaches the end of the list.

Information note

If you don't have reload permission for all apps on the tenant, specify a space ID to which you have reload permission in the List Apps block. Alternatively, you can set the On error field to Ignore or Warning.

## Add a loop and condition to the task chain

Finally, add a condition inside the loop from the previous example.

1. Add a basic Condition block inside the loop, above the Do reload block.
2. Set the condition to reload apps only if the app name contains the word production.

   ![Full task chain automation with loop and condition](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/ui_QAA_task-chain-final.png)
3. Add the Do reload block to the YES branch of the condition.
4. In the App ID field for the Do reload block, map the App ID obtained from the List Apps block. Set the Run Mode to Start reload and continue.

   ![Full task chain automation with loop and condition](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/ui_QAA_task-chain-final2.png)

The final result is an automation that loops through all of the apps on your tenant, and if the app name contains the word *production*, the app reload is triggered. Modify this automation to build your own custom task chain.

## Learn more

- [How to use task chaining with Qlik Automate](https://community.qlik.com/t5/Official-Support-Articles/How-to-use-task-chaining-with-Qlik-Application-Automation/ta-p/1834006 "Qlik Community article")
