---
title: "Creating and saving automations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/creating-automation.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Getting started"]
---

# Creating and saving automations

Users with the Automation Creator role can create automations in the Analytics or Qlik Talend Data Integration [activity center](#glossary-0 "Glossary term") by clicking Automation.
This opens the automation template window. From the template window, either start from a blank canvas or start configuring a pre-built template.

## Creating automations from templates

Automation [templates](templates.htm) are pre-built automations that you can use out-of-the-box with minimal configuration. Templates also help you see the logic of a certain workflow. You can customize a template by swapping out automation and connector blocks while keeping the same design of the template.

When you click Create new automation, the template window opens. The template window displays the available templates, including a blank automation if you want to start building an automation from scratch. You can search templates by keyword, or by using the Categories or Connectors filters. Templates are also organized by Recently used and Favorites.

Automations template window

![Template window main page showing all templates](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/template-window.png)

Hover over a template tile and click the ![star icon on the template tile card to add as favorite](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/Icons/ic_star.svg) icon to add it to your favorites; you can have up to 12 favorites.

Click on Use template to save the template to a Space and start working with it in the [automation editor](navigating-UI.htm#anchor-2).

### Template details

Hover over a template tile and select Details. Here, you can see what the template looks like, find useful information about the automation, which connectors are used in the selected template, and specific configuration information. To start your automation with the selected template, click Use template.

Details page for an automation template

![The details window for the parallel reload template](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/template-details.png)

## Saved automations

Automations can be saved to your personal space or to a shared space in which you have the CanEdit permission. See [working in spaces](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/Spaces.htm) for details about the different types of spaces.

You can find your saved automations by selecting Automations from the Analytics or Qlik Talend Data Integration activity centers.

Do the following:

1. From the cloud hub, click the Catalog tab.
2. From the Types list, click Automations.
3. From the Owner list, click You.

Catalog view of your automations

![The catalog view from the cloud hub filtering for your automations](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/automation-catalog-rev.png)

Opening a saved automation takes you to the automation overview page. If an automation was closed with unsaved work, you can restore it the next time you open the editor. Unsaved changes are kept for two weeks.

### Sharing automations

You can share an automation by inviting a user, group, or everyone in your tenant to the space where it is stored.

Do the following:

1. In the catalog, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the item to be shared and select Share > Invite.
2. Search for users or groups by name or email address.
3. Select space permissions for the users or groups.
4. Or, select permissions for Anyone at <your tenant name> from the dropdown list.
5. Click Done.

The users receive access to the shared item and all other content in the space.

For more information about shared automations, see [Introducing Automation Sharing and Collaboration](https://community.qlik.com/t5/Official-Support-Articles/Introducing-Automation-Sharing-and-Collaboration/ta-p/2516095) on Qlik Community.

## Save automations as templates

To save time creating new complex automations, you can save an automation as a template for later use. Further, you can create a template for your personal use only, or you can choose to share it with other users.

Warning noteSharing a template shares all data included in the template. Users should remove any confidential, personally identifiable or other sensitive data from any template inputs, variables, and/or blocks before sharing. Qlik is not responsible for the user’s failure to remove any such content prior to sharing the template.

Information note

Tenant admins can view templates across the tenant, change their owners, and delete them in the Administration activity center. For details, see [*Managing automation templates*](../../Sense_Hub/Admin/mc-managing-automation-templates.htm).

Do the following:

1. Open the automation in the editor.
2. Right-click an empty area on the automation canvas, and then click Save as template.
3. Enter a name for the template.
4. Optionally, do any of the following:

- If you want to add a thumbnail to your template, drag it to the box.
- Enter a description for the template.
- If you want to share your template with other users on your tenant, from the Visibility list, click Shared.

5. Click Save.

### Edit a saved template's properties

After you have saved an automation as a template, you can edit it to change the name, description, thumbnail, or the visibility of it. For example, you can edit your template to change it from personal to shared rather than creating a new template and sharing it.

Information note

Only the template owner can edit a saved template.

Do the following:

1. In the Analytics or Qlik Talend Data Integration activity center, click Automation.
2. Click New automation.
3. Click either Shared or Personal, depending on whether you have shared the template.
4. Click See other actions![See other actions menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/see-other-actions.PNG) , and then click Edit template.
5. Edit the template as required, and then click Save.

### Make a shared template private

If you don't want others to use a template that you have shared, you can make it private rather than deleting it.

Do the following:

1. In the Analytics or Qlik Talend Data Integration activity center, select Automation.
2. Click New automation.
3. Click Shared.
4. Click See other actions![See other actions menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/see-other-actions.PNG) , and then click Make personal.

### Delete a saved template

You can only delete templates you have created. You cannot delete templates created by other users.

Do the following:

1. In the Analytics or Qlik Talend Data Integration activity center, select Automation.
2. Click New automation.
3. Click either Shared or Personal.
4. Click See other actions![See other actions menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/see-other-actions.PNG) , then click Delete template, and then click Delete to confirm.

## Enabling and disabling automations

An automation is set to enabled when it is created and will run based on its settings. You can choose to disable an automation to prevent it from running or being triggered. Automations can be enabled or disabled in one of the following ways:

- In the Automation overview list, click on the More menu ![More menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Enable or Disable.
- When editing an automation, click on the Settings menu ![settings menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/Icons/ic_settings_cloud.svg) on the upper-right corner of the navigation bar and select Enable or Disable.

To enable or disable multiple automations, open the Automations overview list and select the automations you want to modify. Then, click on the Actions drop-down menu, and select Enable or Disable.

Tip note The Qlik Cloud connector has specific blocks to enable or disable an automation.

Information note Tenant admins can enable or disable automations under Automations in the Administration activity center.
For more information, see [Managing automations - Enabling individual automations](../../Sense_Hub/Admin/mc-managing-automations.htm#Enabling).

### Renewing the execution token

When an automation is re-enabled, you have the option of renewing the execution token. Renewing the execution token will break references to the automation that use a trigger URL or a Qlik Sense button object. Token renewal cannot be undone.

Automations that have the Run mode set to Triggered in the Start block, have a button in the block settings pane that allows for manual token renewal. Manually renewing the token does not require the automation to be re-enabled.

For more information about triggered automations, see [Triggered webhooks](../working-with-automations/working-with-webhooks.htm#triggered-webhooks).
