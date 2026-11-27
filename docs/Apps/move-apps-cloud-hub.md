---
title: "Moving applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/move-apps-cloud-hub.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Managing applications"]
---

# Moving applications

You can move applications between shared spaces as well as between a shared space and a personal space.

If you create an application in a shared space, the data connections related to it will stay in that space, even if the application moves. For example, you create an application called QuarterlyAnalysis in the Data Team shared space. If you move QuarterlyAnalysis to a different shared space, the data connections will remain in the Data Team shared space. If the data needs to be edited or reloaded, it must be done by a user with Can edit or Can edit data in applications roles in the Data Team shared space. The same would apply if you created an application in a personal space and moved it to a shared space.

If you move an application with a reload schedule between spaces, the reload schedule is deleted. Recreate the schedule in the new space if required.

## Moving applications from an activity center

Do the following:

1. In your activity center, click ![Move](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select Manage > Move to space.
2. Select the new space from Space.
3. To open the new space, select Navigate to space.
4. Click Move.

## Moving applications from the application details area

Do the following:

1. In your application, click the application name to open the application details area.
2. In the application details area, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Move.
3. Select the new space from Space.
4. To open the new space, select Navigate to space.
5. Click Move.

If you are a tenant admin or analytics admin, you can move applications between spaces in the Administration activity center.
Applications can be moved between shared spaces, between a shared space and a personal space, or between managed spaces. For information about these administrator privileges, see [*Managing applications for tenant and analytics administrators*](../Admin/mc-administer-apps.htm#Changing).

## Movement of data connections

Once a data connection has been created in a space, it is not possible to move the connection to another space unless you have access to the Administration activity center as a tenant admin, analytics admin, or data admin.
To move an existing data connection to another space, contact an administrator or create a new connection in the desired space with the same settings as the existing connection.

For documentation about how an administrator can move a connection, see [*Moving data connections*](../Admin/mc-administer-data-connections.htm#Moving).
