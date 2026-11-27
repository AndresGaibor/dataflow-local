---
title: "Managing automation connections"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-managing-automation-connections.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing automations"]
---

# Managing automation connections

Use the Administration activity center to manage automation connections by changing their owners, moving them to another space, or deleting them.

## Changing the owner of a connection

The tenant admin or Analytics admin can change the connection owners from the Administration activity center. To change the owner, click ![Three dots to show more options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), then select Change owner. When the tenant admin changes the owner, all configured details related to the connection are removed and must be reconfigured. All automations using the connection will fail at the next run. Any webhooks configured to the connection will be removed.

## Moving a connection

The tenant admin or analytics admin can move a connection to a new space. To move it, click ![Three dots to show more options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), then select Move. The connection is no longer available in its original space. Members of the new space can access it.

Warning noteMoving a connection to a new space could break existing automations. Prior to moving a connection, ensure that the owners of any automations using the connection have access to the new space with sufficient permissions to use the connection, otherwise, the automations will fail.

## Deleting a connection

The tenant admin or analytics admin can delete an Automations connection from the Administration activity center. To delete a connection, click ![Three dots to show more options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), then select Delete. Deleting a connection cannot be undone.
