---
title: "Customizing the Insights activity center Home"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-customized-home.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Customizing your system"]
---

# Customizing the Insights activity center Home

Enhance the user experience by customizing the Insights Home page for all users within your tenant. By adding custom home pages, you can highlight the most relevant content directly upon login, helping users quickly access the information they need.

## Who can create customized home pages?

To create a customized home page for all users, you must have one of the following roles:

- Tenant Admin
- Analytics Admins
- A custom role with Custom home permission set to Allowed

For more information, see [*Default permissions and custom roles*](permissions-scopes.htm).

Information note

Each user can personalize their individual home pages on the Personal tab.

## How it works

- When you add a custom home page, it will appear as a tab next to the Personal tab in Home.
- The custom page will be the default home page for all users. This page can include applications, collections, and other resources.
- Users will only see content they have permission to access.

The Insights activity center Home with a custom page named “Tenant Home".

![Custom home page for admin showing two collections](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_custom_home_admin-rev.png "Click to view full size")

## Creating a new custom home page

Do the following:

1. Navigate to the Qlik Cloud Insights activity center.
2. From there, select Home.
3. Click Create page.
4. In the Create page dialog, enter a name for the page, and then click Create.
5. In the Add widgets dialog, search for widgets and click to add them to the page.

   Adding widgets.

   ![The Add widgets dialog](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_add_widgets.png "Click to view full size")
6. Click Done.

   The custom home page is created and added to Home for all users in the tenant.
7. To rearrange the widgets on the page, click and hold ![drag handle](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_draggable.svg) next to a widget and move it into place.

## Editing a custom home page

Do the following:

1. In the Insights Home, select the custom home page.
2. To change the name:

   1. Click Page settings.
   2. In the Page settings dialog, enter a new name and click Done.
3. To add or remove widgets:

   1. Click Add widgets.
   2. In the Add widgets dialog, click a widget to add or remove it.
   3. Click Done.

   You can also remove widgets directly from the page:

   1. Hover to the right of a widget and click the More actions menu (![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg)) that appears.

      More actions menu on widget.

      ![The Add widgets dialog](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_remove_widgets.png "Click to view full size")
   2. Select Remove.
4. To rearrange widgets on the page:

   - Click and hold ![drag handle](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_draggable.svg) next to a widget and move it into place.

## Deleting a custom home page

Do the following:

1. In the Insights Home, select the custom home page.
2. Click Page settings.
3. In the Page settings dialog, click Delete page.
4. Select Delete to confirm the deletion.
