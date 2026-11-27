---
title: "Shared space permissions for administrators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/permissions-shared-space-admin.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces", "Working in shared spaces", "Managing permissions in shared spaces"]
---

# Shared space permissions for administrators

This help topic contains tables outlining what tenant and analytics administrators can and cannot do without [shared space](#glossary-0 "Glossary term") permissions.

Tenant and analytics administrators, without specific permissions, have limitations to what they can and cannot do in a shared space. These administrators, unlike general users, also have permissions to perform certain actions without needing space roles and security roles. For more information, see [*Administrator roles*](managing-shared-spaces.htm#AdministratorRoles).

For more information about managing permissions in shared spaces, including special considerations, see [*Managing permissions in shared spaces*](managing-shared-spaces.htm).

## Space actions

Tenant and analytics administrator space actions in a shared space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Create the space | Yes |
| See the space exists in the Administration activity center | Yes |
| See the space exists in Qlik Cloud Analytics [activity centers](#glossary-1 "Glossary term") | Yes |
| Delete the space | Yes |
| Add members to the space | Yes |
| Change name and roles for the space | Yes |
| Change member permissions for the space | Yes |
| Remove members from the space | Yes |
| Delete and change the owner of folders in the space | Yes |
| Add, rename, duplicate, and move folders in the space | No |
| Change space owner in the Administration activity center | Yes |

## Application actions

### Application actions – General

Tenant and analytics administrator permissions in a shared space – General application actions

| Action | Tenant admin supported | Analytics admin supported |
| --- | --- | --- |
| Open an application | Yes | Yes |
| Delete an application | Yes | Yes |
| Change application owner in the Administration activity center | Yes | Yes |
| Publish or republish applications from this space | No | No |
| See all applications in the space | Yes | Yes |
| Share applications in the space with non-space members | No | No |
| Export an application | No | No |
| Export an application from the Administration activity center | No | No |
| Edit application attributes (change name, description, and tags) | No | No |
| Edit application properties (select theme, enable right-to-left reading order, set a bookmark as application default, and sheet title styling) | No | No |
| Approve application access requests | No | No |

### Application actions – Data modeling and reload

Tenant and analytics administrator permissions in a shared space – Data management actions

| Action | Tenant admin supported | Analytics admin supported |
| --- | --- | --- |
| Open Data model viewer | No | No |

### Application actions – Sheets, storytelling, and visualizations

Tenant and analytics administrator permissions in a shared space – Sheets, storytelling, and visualizations
actions

| Action | Tenant admin supported | Analytics admin supported |
| --- | --- | --- |
| View master items and variables | No | No |
| View, create, edit, and delete media library content | No | No |
| Add private sheets to the application | No | No |
| Add private bookmarks and stories to the application | No | No |
| Make private sheets, bookmarks, and stories public in the application | No | No |
| Make public sheets, bookmarks, and stories private in the application | No | No |
| Take snapshots in the application | No | No |
| Monitor a visualization in your activity centers | No | No |
| Create, edit, and delete [write table](#glossary-2 "Glossary term") chart configurations | No | No |
| View write tables and make changes to their editable columns | No | No |

### Application actions – Augmented analytics

Tenant and analytics administrator permissions in a shared space – Augmented analytics
actions

| Action | Tenant admin supported | Analytics admin supported |
| --- | --- | --- |
| Create, edit, rerun, view, and delete key driver analyses | No | No |

### Application actions – Subscriptions and alerts

Tenant and analytics administrator permissions in a shared space – Subscriptions and alerts actions

| Action | Tenant and analytics admin supported |
| --- | --- |
| Subscribe to a chart or sheet in the application | No |
| Create an alert for the application | No |
| Manage a subscription or alert you have created  Managing these items includes actions such as deleting, sending, evaluating, editing, disabling, and re-enabling. | No |
| Unsubscribe from a subscription or alert for which you are a recipient | Yes |

### Application actions – Reporting

Tenant and analytics administrator permissions in a shared space – Reporting
actions

| Action | Tenant admin supported | Analytics admin supported |
| --- | --- | --- |
| Connect to the application in Qlik add-ins for Microsoft Office | No | No |
| View the Reporting section in the application | No | No |
| Work with PixelPerfect and HTML report templates  Working with these templates involves viewing, creating, editing, deleting, uploading, downloading, and configuring on-demand reporting for the templates. | No | No |
| View, create, edit, and run report tasks | No | No |
| Delete report tasks | No | No |
| View, create, edit, and delete report filters | No | No |
| Create, upload, and delete report distribution lists | No | No |
| View the recipients and groups from a report distribution list | No | No |
| View, upload, re-upload, download, and delete report templates | No | No |
| Enable, disable, delete, and change the owner of report tasks in the Administration activity center | Yes | No |
| Enable, disable, or re-configure on-demand reporting from the application | No | No |
| Generate an on-demand report from the application | No | No |

## Script actions

Tenant and analytics administrator script actions in a shared space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Open a script | Yes |
| Delete a script | Yes |
| Change script owner in the Administration activity center | Yes |
| Export a script from the Administration activity center | No |
| Publish or republish scripts from this space | No |
| Open and edit the load script in Editor | No |
| Edit script attributes (change name, description, and tags) | No |

## Data sources actions

Tenant and analytics administrator permissions in a shared space – Data sources actions

| Action | Tenant admin supported | Analytics admin supported |
| --- | --- | --- |
| See data files | Yes | Yes |
| Delete data files | Yes | Yes |
| Update data file (overwrite with same name) | No | No |
| Move data files | No | No |
| Use data file in application | Yes | Yes |
| See data connections | Yes | Yes |

## Automation actions

Tenant and analytics administrator permissions in a shared space – Automation actions

| Action | Tenant admin supported | Analytics admin supported |
| --- | --- | --- |
| See automation | Yes | Yes |
| Delete automation | Yes | Yes |
| Move automation | Yes | Yes |
| Use automation | Yes | Yes |
| Enable automation | Yes | Yes |

Information noteA tenant admin can move an automation from a shared space to another space and delete an automation from a shared space. Only a tenant admin or an OAuth bot user with the admin.automations scope can change the owner of an automation.

### Automation connections actions

Tenant and analytics administrator permissions in a shared space – Automation connections actions

| Action | Tenant admin supported | Analytics admin supported |
| --- | --- | --- |
| See automation connections | Yes | Yes |
| Delete automation connections | Yes | Yes |
| Move automation connections | No | No |
| Use automation connections in automations | Yes | Yes |

## Qlik Predict — ML experiment actions

Tenant and analytics administrator permissions in a shared space – ML experiments
actions

| Action | Tenant and analytics admin supported |
| --- | --- |
| List ML experiments in the space | Yes |
| Open ML experiment | Yes |
| Create ML experiment | No |
| Delete ML experiment | Yes |
| Edit ML experiment | No |
| Move ML experiment to the space | No |
| Move ML experiment to another space | No |
| Download training reports for models in the experiment | Yes |

## Qlik Predict — ML deployment actions

Tenant and analytics administrator permissions in a shared space – ML deployments actions

| Action | Tenant and analytics admin supported |
| --- | --- |
| List ML deployments in the space | Yes |
| Open ML deployment | Yes |
| Deploy model to an ML deployment (new or existing) | No |
| Remove a model from an ML deployment | No |
| Delete ML deployment | Yes |
| Edit ML deployment | No |
| Create, edit, and delete prediction configurations | No |
| Create, edit, and delete prediction schedules | No |
| Change the owner of a prediction configuration | No |
| Create, rename, and delete [model aliases](#glossary-3 "Glossary term") in an ML deployment | No |
| Run prediction (from configuration, real-time API endpoint, or Qlik Predict connector) | No |
| Move ML deployment to the space | No |
| Move ML deployment to another space | No |
| Activate and deactivate a model in an ML deployment | No |
| Activate and deactivate a model in an ML deployment from the Administration activity center | Yes |
| Download training reports for models in an ML deployment | Yes |

## Business glossary actions

Tenant and analytics administrator permissions in a shared space – Business glossary actions

| Action | Tenant admin supported | Analytics admin supported |
| --- | --- | --- |
| List glossaries in the space | Yes | Yes |
| Open a glossary (details page only) | Yes | Yes |
| View glossary and terms | Yes | Yes |
| Move glossary from this space | No | No |
| Move glossary to this space | No | No |
| Create a glossary | No | No |
| Edit glossary settings and page | No | No |
| Delete a glossary | Yes | Yes |
| Add a term in glossary | No | No |
| Edit term not in Verified state | No | No |
| Edit term in Verified state | No | No |
| Delete term not in Verified state | No | No |
| Delete term in Verified state | No | No |
| Change state of a term to/from Verified | No | No |
| Change state of a term between states other than Verified | No | No |
| Create, edit, delete categories | No | No |
| Link glossary terms to master items in applications | Yes | Yes |
| Can export glossaries and terms | Yes | Yes |

## Qlik Answers

Qlik Answers assistant actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| View assistants in Answers assistants | Yes | Yes | Yes | Yes | Yes | No |
| Chat with an assistant  Can view also requires Can consume data to chat | Yes | Yes | Yes | Yes | Yes | No |
| Create new assistants | Yes | Yes | Yes | Yes | No | No |
| Move assistants to the space | Yes | Yes | Yes | Yes | No | No |
| Move assistants to another space | Yes | Yes | Yes | Yes | No | No |
| Open an assistant | Yes | Yes | Yes | Yes | Yes | No |
| Delete an assistant | Yes | Yes | Yes | Yes | No | No |
| Edit an assistant | Yes | Yes | Yes | Yes | No | No |
| View assistant applications and knowledge bases | Yes | Yes | Yes | Yes | No | No |
| Add and remove applications and knowledge bases | Yes | Yes | Yes | Yes | No | No |
| Review answers and feedback  Information noteThis also requires the Audit Admin user role. | Yes | Yes | Yes | Yes | Yes | No |

Qlik Answers knowledge base actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create knowledge bases | Yes | Yes | Yes | Yes | No | No |
| Move knowledge bases to the space | Yes | Yes | Yes | Yes | No | No |
| Move knowledge bases to another space | Yes | Yes | Yes | Yes | No | No |
| Open a knowledge base | Yes | Yes | Yes | Yes | Yes | No |
| Delete a knowledge base | Yes | Yes | Yes | Yes | No | No |
| Edit a knowledge base | Yes | Yes | Yes | Yes | No | No |
| Index sources | Yes | Yes | Yes | Yes | No | No |
| Set up an index schedule | Yes | Yes | Yes | Yes | No | No |
| Get answers from knowledge bases using an assistant | Yes | Yes | Yes | Yes | Yes | No |
| View sources from knowledge base | Yes | Yes | Yes | Yes | Yes | No |

Qlik Answers skill actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Upload skill | Yes | Yes | Yes | Yes | No | No |
| Move skills to the space | Yes | Yes | Yes | Yes | No | No |
| Move skills to other spaces | Yes | Yes | Yes | Yes | No | No |
| Open skills | Yes | Yes | Yes | Yes | Yes | No |
| Delete skills | Yes | Yes | Yes | Yes | No | No |
| Edit skill details | Yes | Yes | Yes | Yes | No | No |

Qlik Answers application actions – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data | Can view and Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| View applications in Application analysis | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Open Answers in an open application | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Ask question about the application in Qlik Answers | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Make application available to Qlik Answers | Yes | Yes | Yes | Yes | No | No | No |

## Discovery Agent actions

Tenant and analytics administrator Discovery Agent actions in a shared space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Create and manage [insight triggers](#glossary-4 "Glossary term") in the application | No |
| View [insight triggers](#glossary-5 "Glossary term") in the application | Yes |
| View insights from the application in your feed | Yes |

## Other content actions

Tenant and analytics administrator permissions in a shared space – Other content actions

| Action | Tenant and analytics admin supported |
| --- | --- |
| Create, edit, and delete generic links | Yes |
| Add and manage applications and other content from this space in public collections | Yes |
