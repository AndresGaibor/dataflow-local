---
title: "Managed space permissions for administrators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/permissions-managed-space-admin.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces", "Working in managed spaces", "Managing permissions in managed spaces"]
---

# Managed space permissions for administrators

This help topic contains tables outlining what tenant and analytics administrators can and cannot do without [managed space](#glossary-0 "Glossary term") permissions.

Tenant and analytics administrators, without specific permissions, have limitations to what they can and cannot do in a managed space. These administrators, unlike general users, also have permissions to perform certain actions without needing space roles and security roles. For more information, see [*Administrator roles*](managing-managed-spaces.htm#AdministratorRoles).

For more information about managing permissions in managed spaces, including special considerations, see [*Managing permissions in managed spaces*](managing-managed-spaces.htm).

## Space actions

Tenant and analytics administrator space actions in a managed space

| Action | Tenant and analytics admin supported |
| --- | --- |
| See the space exists in the Administration activity center | Yes |
| See the space exists in Qlik Cloud Analytics [activity centers](#glossary-1 "Glossary term") | Yes |
| Delete the space | Yes |
| Add members to the space | Yes |
| Change member permissions for the space (Can manage, Can publish, Can contribute, Can view, Has restricted view) | Yes |
| Remove members from the space | Yes |
| Change space owner in the Administration activity center | Yes |
| Delete and change the owner of folders in the space | Yes |
| Add, rename, duplicate, and move folders in the space | No |

## Application actions

### Application actions – General

Tenant and analytics administrator permissions in a managed space – General application actions

| Action | Tenant and analytics admin supported |
| --- | --- |
| Open an application | Yes |
| Delete an application | Yes |
| Change application owner in Administration | Yes |
| Share applications in the space with non-space members | No |
| Publish/republish applications to this space | No |
| See all applications in the space | Yes |
| Export an application | No |
| Export an application from the Administration activity center | No |
| Edit application attributes (change name, description, and tags) | No |
| Edit application properties (select theme, enable right-to-left reading order, set a bookmark as application default, and sheet title styling) | No |
| Approve application access requests | No |

### Application actions – Data modeling and reload

Tenant and analytics administrator permissions in a managed space – Data management actions

| Action | Tenant and analytics admin supported |
| --- | --- |
| Open Data model viewer | No |

### Application actions – Sheets, storytelling, and visualizations

Tenant and analytics administrator permissions in a managed space – Sheets, storytelling, and visualizations
actions

| Action | Tenant and analytics admin supported |
| --- | --- |
| View master items and variables | No |
| View, create, edit, and delete media library content | No |
| Add private sheets to the application | No |
| Add private bookmarks and stories to the application | No |
| Make private sheets, bookmarks, and stories public in the application | No |
| Make public sheets, bookmarks, and stories private in the application | No |
| Take snapshots in the application | No |
| Monitor a visualization in your activity centers | No |
| Create, edit, and delete [write table](#glossary-2 "Glossary term") chart configurations | No |
| View write tables and make changes to their editable columns | No |

### Application actions – Augmented analytics

Tenant and analytics administrator permissions in a managed space – Augmented analytics
actions

| Action | Tenant and analytics admin supported |
| --- | --- |
| Create, edit, rerun, view, and delete key driver analyses | No |

### Application actions – Subscriptions and alerts

Tenant and analytics administrator permissions in a managed space – Subscriptions and alerts actions

| Action | Tenant and analytics admin supported |
| --- | --- |
| Subscribe to a chart or sheet in the application | No |
| Create an alert for the application | No |
| Manage a subscription or alert you have created  Managing these items includes actions such as deleting, sending, evaluating, editing, disabling, and re-enabling. | No |
| Unsubscribe from a subscription or alert for which you are a recipient | Yes |

### Application actions – Reporting

Tenant and analytics administrator permissions in a managed space – Reporting
actions

| Action | Tenant and analytics admin supported |
| --- | --- |
| Connect to the application in Qlik add-ins for Microsoft Office | No |
| View and use the Reporting section in the application | No |
| Work with PixelPerfect and HTML report templates  Working with these templates involves viewing, creating, editing, deleting, uploading, downloading, and configuring on-demand reporting for the templates. | No |
| Enable, disable, or re-configure on-demand reporting from the application | No |

## Script actions

Tenant and analytics administrator script actions in a managed space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Open a script | No |
| Delete a script | Yes |
| Change script owner in the Administration activity center | Yes |
| Export a script from the Administration activity center | No |
| Publish/republish scripts to this space | No |
| See all scripts in the space | Yes |
| Edit script attributes (change name, description, and tags) | No |

## Data sources actions

Tenant and analytics administrator permissions in a managed space – Data sources actions

| Action | Tenant and analytics admin supported |
| --- | --- |
| See data files | Yes |
| Delete data files | Yes |
| Update data file (overwrite with same name) | No |
| Move data files | No |
| See data connections | Yes |

## Qlik Predict — ML deployment actions

Tenant and analytics administrator permissions in a managed space – ML deployment actions

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
| Run prediction (from configuration, real-time API, or Qlik Predict connector) | No |
| Move ML deployment to the space | No |
| Move ML deployment to another space | No |
| Activate and deactivate a model in an ML deployment | No |
| Activate and deactivate a model in an ML deployment from the Administration activity center | Yes |
| Download training reports for models in an ML deployment | Yes |

## Business glossary actions

Tenant and analytics administrator permissions in a managed space – Business glossary actions

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

## Qlik Answers actions

Tenant and analytics administrator Qlik Answers assistant actions in a shared space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Chat with an assistant | Yes |
| Create new assistants | No |
| Move assistants to the space | No |
| Move assistants to another space | No |
| Open an assistant | Yes |
| Delete an assistant | Yes |
| Edit an assistant | No |
| Add and remove applications and knowledge bases | No |
| Review answers and feedback  Information noteThis also requires the Audit Admin user role. | Yes |

Tenant and analytics administrator Qlik Answers knowledge base actions in a shared space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Create knowledge bases | No |
| Move knowledge bases to the space | No |
| Move knowledge bases to another space | No |
| Open a knowledge base | Yes |
| Delete a knowledge base | Yes |
| Edit a knowledge base | No |
| Index sources | No |
| Set up an index schedule | No |
| Get answers from knowledge bases using an assistant | Yes |

Tenant and analytics administrator Qlik Answers skill actions in a shared space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Upload skill | No |
| Move skills to the space | No |
| Move skills to other spaces | No |
| Open skills | Yes |
| Delete skills | Yes |
| Edit skill details | No |

## Discovery Agent actions

Tenant and analytics administrator Discovery Agent actions in a managed space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Create and manage [insight triggers](#glossary-5 "Glossary term") in the application | No |
| View [insight triggers](#glossary-6 "Glossary term") in the application | Yes |
| View insights from the application in your feed | Yes |

## Other content actions

Tenant and analytics administrator space actions in a managed space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Create, edit, and delete generic links | Yes |
| Add and manage applications and other content from this space in public collections | Yes |
