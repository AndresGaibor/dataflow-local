---
title: "Creating and managing generic links"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-generic-links.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing resources"]
---

# Creating and managing generic links

Generic links make external resources available in the cloud. For example, in a multi-cloud deployment with QlikView or Qlik Sense Enterprise on Windows combined with Qlik Cloud, these links provide access to on-premises applications.

## Who can create links

- Tenant admins can add links to all spaces, including their personal space.
  They can create and manage links both from the Analytics and Administration [activity centers](#glossary-0 "Glossary term").
- Analytics admins can add links to all spaces except personal spaces. They can create and manage links both from the Analytics and Administration [activity centers](#glossary-1 "Glossary term") but cannot manage links in personal spaces.
- Users with the following permissions can add links to specific spaces:

  - The Owner or Can manage role in the space.
  - The Manage links permission set to Allowed. This is configured by a tenant administrator.

  These users cannot add links to personal spaces and can only manage links from the Analytics activity center.

### The Manage links permission

Tenant administrators configure the Manage links permission to control whether users can work with generic links.

For the Manage links permission, the following options are available:

- Allowed: Users can view, create, update, and use links in the Analytics activity center. They can delete links that they created.

  With Allowed, users cannot add links to personal spaces and can only manage links from the Analytics activity center. Users can also view and use links in the Insights activity center.
- Not allowed: Users cannot view or work with links in the Analytics activity center.

  With Not allowed, users also cannot view or use links in the Insights activity center.

The Manage links permission is configured in the Administration activity center through two processes:

- Creating custom roles. See:

  - [*Creating custom roles*](permissions-custom-roles-capacity-model.htm#Creating) (capacity-based subscriptions)
  - [*Creating custom roles*](permissions-custom-roles.htm#Creating) (user-based subscriptions)
  - [*Creating custom roles*](permissions-custom-roles-anonymous.htm#Creating) (Qlik Anonymous Access subscriptions)
- Configuring the default permissions. See:

  - [*Default permissions*](permissions-admins-users-capacity-model.htm#UserDefault) (capacity-based subscriptions)
  - [*Default permissions*](permissions-admins-users.htm#UserDefault) (user-based subscriptions)
  - [*Default permissions*](permissions-admins-users-anonymous.htm#UserDefault) (Qlik Anonymous Access subscriptions)

For information about the permissions available through default permissions and custom roles, see:

- [*Default permissions and custom roles*](permissions-scopes-capacity-model.htm) (Capacity-based subscriptions)
- [*Default permissions and custom roles*](permissions-scopes.htm) (User-based subscriptions)
- [*Default permissions and custom roles*](permissions-scopes-anonymous.htm) (Qlik Anonymous Access subscriptions)

## Access control for linked content

Access to linked content is controlled by the permissions at the destination of the link. If a member has access to the space where the link is added but lacks permission for the linked content, they cannot view it.

## Managing links from the Analytics activity center

Links can be created and managed individually from the Administration activity center.
For detailed instructions, see [*Adding links in the Analytics activity center*](../Hub/links.htm).

## Managing links from the Administration activity center

You can create, upload, edit, move, and delete links from the Generic links page.

### Creating a link

Do the following:

1. In the Administration activity center, go to Generic links.
2. Click Create new.
3. To add an image, drag and drop an image file or click Browse to select the file.
4. Enter the following link details:

   - Name: Enter a name for the link.
   - Link URL: Enter the URL in the format https://domain.com.

     - Only HTTPS URLs are allowed.
     - Domain names can contain letters (a-z), numbers (0-9), and hyphens (-), but not underscores (\_) or the '@' symbol. For example, https://my-domain.com/ is valid, while https://my\_domain.com/ is not.
   - Space: Select the space where the link will be added.
   - Description (optional): Enter a description for the link.
   - Tags (optional): Add tags to help categorize the link.
5. Click Create.

### Uploading a file with multiple links

Tenant administrators can upload a CSV file containing one or more links. The links are initially created in the administrators personal space, from where they can be moved to other spaces.

Important notes:

- The file must be saved in UTF-8 encoding to be correctly processed by Qlik Cloud.
- The CSV file should contain the fields Name and URL.
- Ensure that each row in the CSV file includes the same number of fields as the header row. If a field is optional and not used, leave it blank but include the comma to maintain the correct format.

Do the following:

1. In the Administration activity center, go to Generic links.
2. Click Upload CSV file.
3. Add your CSV file and click Upload.

#### Example: CSV file for uploading links

Here’s an example of what the CSV file could look like:

```
Name,URL,Description
Qlik Help Center,https://help.qlik.com,Access Qlik's official help documentation
Qlik Community,https://community.qlik.com,A forum for Qlik users to share and discuss ideas
Company Intranet,https://intranet.company.com,Internal company resources and tools
Sales Dashboard,https://qlikcloud.com/sales_dashboard,A link to the sales performance dashboard
Project Management Tool,https://project.company.com,Tool for managing company projects
```

### Moving generic links

You can move generic links to a different space.

Do the following:

1. In the Administration activity center, go to Generic links.
2. Select the generic links you want to move.
3. Click Move.
4. Select a new space and click Confirm.

### Editing links

Do the following:

1. In the Administration activity center, go to Generic links.
2. Find the link you want to edit.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Edit.
4. Modify the details as needed.
5. Click Save.

### Deleting generic links

Do the following:

1. In the Administration activity center, go to Generic links.
2. Select the links you want to delete.
3. Click Delete.
4. Confirm the deletion.
