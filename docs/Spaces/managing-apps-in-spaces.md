---
title: "Using applications in shared spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-apps-in-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces", "Working in shared spaces"]
---

# Using applications in shared spaces

Applications can be created, developed, and shared with other members of Qlik Cloud Analytics in a [shared space](#glossary-0 "Glossary term").

Applications can be created and developed in a similar way to how applications are created and shared in a [personal space](#glossary-1 "Glossary term"). Depending on your space [permissions](#glossary-2 "Glossary term") and your user entitlement, you can create and develop applications in the space. If you have Can view permission, you can only view the applications in the space.

For a detailed view of what you can do with applications based on your permission and user entitlement, see [*Managing permissions in shared spaces*](managing-shared-spaces.htm).

## Creating applications in a shared space

Users can create or upload applications in a shared space by going to the Create page of the Analytics [activity center](#glossary-3 "Glossary term") and clicking Analytics app or Upload. You can also create analytic applications from Analyze in Analytics or by clicking Create new in Catalog.
You cannot duplicate applications to a space, but you can move applications to a space.

Tags you add to an application are shared with other members of Qlik Cloud, but only if they have access to your application.

[Data connections](#glossary-4 "Glossary term") and data files can be created, modified, and deleted by users with Can edit and Can edit data in applications permissions in a shared space.

Application owners with Can edit and Can edit data in applications permission can read, write, and load data connections and load scripts in [Data manager](#glossary-5 "Glossary term") or [Data load editor](#glossary-6 "Glossary term") in their own applications. They can also create data connections to external sources and load data from those connections. Users with Can edit data in applications permissions can also edit load scripts in so in other users' applications.

The DataFiles [connection](#glossary-7 "Glossary term") for a shared space is created automatically and cannot be removed while the space is still available to a user.

You can create on-demand selection applications in a shared space. Selection applications and template applications must be in the same space. For more information, see [Creating an on-demand selection application](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/creating-OnDemand-selection-app.htm).

For more information about creating applications, see [*Creating applications and adding data*](../Apps/create-app-cloud-hub.htm).

## Adding data sources in shared spaces

Users with Can edit, Can edit data in applications, or Can manage permissions can add data sources to shared spaces. Data sources can be used by other members of the space.

For information, see [*Adding and managing your analytics data*](managing-data-resources-spaces.htm).

## Adding content to applications in shared spaces

Users with Can edit, Can edit data in applications, or Can manage permissions can add [sheets](#glossary-8 "Glossary term"), [stories](#glossary-9 "Glossary term"), and [bookmarks](#glossary-10 "Glossary term") to applications in the shared space.
Sheets, stories, and bookmarks added to the application are private. Only the creator of the private content can see it in the application. When they are ready to be shared, the creator makes them public.

For information, see [*Granting access to sheets, sheet groups, bookmarks, and stories*](../Share/make-public-or-private.htm).

Only the space owner can edit data in the application, but other shared space members can create, edit, and delete:

- Master items
- Variables
- Media library content

Information note

Snapshots taken for stories are not shared with other users.

Shared space members with Owner, Can edit, Can edit data in applications, or Can manage permissions can modify the following application properties:

- Selected theme
- Enable right-to-left reading order
- Setting a bookmark as application default
- Sheet title styling

## Reloading applications in a shared space

Users with Owner, Can manage, Can edit, or Can edit data in applications permissions can manually reload applications and create scheduled reloads for applications in the space.

## Moving applications between spaces

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

### Movement of data connections

Once a data connection has been created in a space, it is not possible to move the connection to another space unless you have access to the Administration activity center as a tenant admin, analytics admin, or data admin.
To move an existing data connection to another space, contact an administrator or create a new connection in the desired space with the same settings as the existing connection.

For documentation about how an administrator can move a connection, see [*Moving data connections*](../Admin/mc-administer-data-connections.htm#Moving).

## Duplicating applications in a shared space

You can duplicate applications in a shared space.

Information note

If an application uses [section access](#glossary-11 "Glossary term") for data, you cannot duplicate the application.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select Manage > Duplicate.

## Downloading applications from shared spaces

You can download an application from a shared space as a .qvf file. Downloaded applications do not include any private sheets in the application.

Information note

If an application uses section access for data, you cannot export the application.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select Download > Download or Download without data.

## Sharing applications from shared spaces

You can add members to a space and give them Can view permission so they can view the applications. For information about sharing individual applications, see [*Sharing applications with users who are not space members*](sharing-content-with-non-space-members.htm). If your subscription doesn’t include this feature, you can move the application to a space you create for application viewers.

For more information on adding members to shared spaces, see [*Managing permissions in shared spaces*](managing-shared-spaces.htm).

Related learning:

- [How do I upload an application with a drag and drop?](/lnk/How_upload_app_drag_and_drop)
