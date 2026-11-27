---
title: "Publishing scripts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ScriptEditor/publishing-scripts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Working with scripts in the catalog", "Managing scripts"]
---

# Publishing scripts

You can publish scripts from a [personal space](#glossary-0 "Glossary term") to a [managed space](#glossary-1 "Glossary term") , or [shared space](#glossary-2 "Glossary term") to a managed space. Publishing creates a copy of the script in the managed space.

You must have the Owner or Can publish permission in the managed spaces to which you are publishing the script. If the script being published is in a shared space, you also need the Can edit space role or higher in that shared space to publish the script.

You can view the spaces that a script has been published to in Details.

Scripts indicate when they were last published to a managed space in the publish dialog.

Information noteScheduled runs are not included for the published copy of an script. Published scripts must have scheduled tasks reconfigured on the script in the managed space.

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the script and select Publish.
2. Select a managed space.
3. Optionally, change the Published script name, Description, and Tags of the script.
4. Click Publish.

## Republishing scripts

Scripts in managed spaces are updated by republishing the source script. When you republish a script, you can either publish a new version of the script or replace existing copies of the script in managed spaces.

Publishing a script to a managed space that shares a name with a script in a managed space is treated as replacing the script.

For example, you may upload a script that is an older version of a script in a shared space that has previously been published and has the same script name. If you published that script to the same managed space, you would be presented with replacing options rather than publishing options.

Republishing dialog

![Republishing dialog for the script Sample script. There is an option to publish a new copy of the script as well as an option to republish the published copies of the script.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_republish-script.png "Click to view full size")

If you do not want to replace the script in this way, click Publish new, change the name of the script, and publish again.

A script does not have to be in the same space to republish. For example, you may develop scripts with separate developing and verification spaces, each with copies of the original script. Either space can republish their copy of the script to the managed space.

If another copy of the script has republished and replaced the script in the managed space, you will see the publishing dialog. If you change the name when publishing to match the name of the script in the managed space, you will republish that script.

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the script and then select Publish.
2. If you want to publish a new version of the script, click Publish new.
3. If you want to replace existing published copies of the script, select the copies to replace.
4. To include data with the script, select Include data.
5. Click Republish.
