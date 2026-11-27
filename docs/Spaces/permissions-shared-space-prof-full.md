---
title: "Shared space permissions for Professional and capacity-based subscription users"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/permissions-shared-space-prof-full.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces", "Working in shared spaces", "Managing permissions in shared spaces"]
---

# Shared space permissions for Professional and capacity-based subscription users

This topic shows what members can do in a shared space. It applies to all users in capacity-based subscriptions and to user with Professional entitlement in user-based subscriptions.

For more information about managing permissions in shared spaces, including special considerations, see [*Managing permissions in shared spaces*](managing-shared-spaces.htm).

## Space actions

You need the Shared Space Creator user role in the [tenant](#glossary-0 "Glossary term") to create new shared spaces.

Space actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Rename the space | Yes | Yes | No | No | No | No |
| Add members to the space | Yes | Yes | No | No | No | No |
| Change member permissions for the space  Space owners can be changed by tenant and analytics administrators in the Administration activity center. | Yes | Yes | No | No | No | No |
| Remove members from the space | Yes | Yes | No | No | No | No |
| Delete the space | Yes | Yes | No | No | No | No |
| Add, delete, rename, duplicate, and move folders in the space | Yes | Yes | Yes | Yes | No | No |

## Application actions

### Application actions – General

General application actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create new applications in the space | Yes | Yes | Yes | Yes | No | No |
| Move applications to the space | Yes | Yes | Yes | Yes | No | No |
| Move applications to another space | Yes | Yes | Yes | Yes | No | No |
| Duplicate applications in the space | Yes | Yes | Yes | Yes | No | No |
| Export applications in the space | Yes | Yes | Yes | Yes | No | No |
| Publish or republish applications from this space  When publishing or republishing an application to a managed space, you also need the Owner or Can publish space role in the managed space to which the application is being published. | Yes | Yes | Yes | Yes | No | No |
| Share applications in the space with non-space members | Yes | Yes | No | No | No | No |
| Remove application-only access to applications from non-space members | Yes | Yes | No | No | No | No |
| Open an application | Yes | Yes | Yes | Yes | Yes | No |
| Delete an application | Yes | Yes | Yes | Yes | No | No |
| Edit application attributes (change name, description, and tags) | Yes | Yes | Yes | Yes | No | No |
| Edit application properties (select theme, enable right-to-left reading order, set a bookmark as application default, and sheet title styling) | Yes | Yes | Yes | Yes | No | No |
| Approve application access requests | Yes | Yes | No | No | No | No |

### Application actions – Data modeling and reload

Data management actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Open Data model viewer | Yes | Yes | Yes | Yes | No | No |
| Open and edit the data model in Data load editor or Data manager (in an application you own) | Yes | Yes | Yes | Yes | No | No |
| Open and edit the data model in Data load editor or Data manager (in another user's application) | No | No | Yes | No | No | No |
| Add data files to a space in Data load editor and Data manager (in an application you own) | Yes | No | Yes | Yes | No | No |
| Add data files to a space in Data load editor and Data manager (in another user's application) | No | No | Yes | No | No | No |
| Reload the application | Yes | Yes | Yes | Yes | No | No |
| Create and manage tasks for scheduled reloads  Managing these tasks includes the following actions:   - Viewing all tasks - Running - Editing - Activating and deactivating - Viewing run history, including logs - Deleting | Yes | Yes | Yes | Yes | No | No |

### Application actions – Sheets, storytelling, and visualizations

Sheets, storytelling, and visualizations actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create, edit, and delete master items and variables | Yes | Yes | Yes | Yes | No | No |
| View media library content | Yes | Yes | Yes | Yes | Yes | No |
| Create and manage media library content | Yes | Yes | Yes | Yes | No | No |
| Add private sheets to the application | Yes | Yes | Yes | Yes | No | No |
| Paste copied visualizations onto private sheets | Yes | Yes | Yes | Yes | No | No |
| Paste copied sheets in the application | Yes | Yes | Yes | Yes | No | No |
| Add private bookmarks and stories to the application | Yes | Yes | Yes | Yes | Yes | No |
| Make private sheets, bookmarks, and stories public in the application | Yes | Yes | Yes | Yes | No | No |
| Update and delete your own private sheets, bookmarks, and stories | Yes | Yes | Yes | Yes | Yes | No | No |
| Make public sheets, bookmarks, and stories private in the application | Yes | Yes | Yes | Yes | No | No |
| Take snapshots in the application | Yes | Yes | Yes | Yes | Yes | No |
| Make snapshots public | Yes | Yes | Yes | Yes | No | No |
| View on-demand application navigation links | Yes | Yes | Yes | Yes | Yes | No |
| Create or update application navigation on-demand links | Yes | Yes | Yes | Yes | No | No |
| Open on-demand selection applications | Yes | Yes | Yes | Yes | Yes | No |
| Generate on-demand applications | Yes | Yes | Yes | Yes | Yes | No |
| Create dynamic views | Yes | Yes | Yes | Yes | No | No |
| Add dynamic charts to sheets | Yes | Yes | Yes | Yes | No | No |
| Monitor a visualization in your personal space | Yes | Yes | Yes | Yes | Yes | No |
| Share a visualization to monitor in the shared space | Yes | Yes | Yes | Yes | No | No |
| Create links to sheets | Yes | Yes | No | No | No | No |
| Create, edit, and delete [write table](#glossary-1 "Glossary term") chart configurations | Yes | Yes | Yes | Yes | No | No |
| View write tables and make changes to their editable columns | Yes | Yes | Yes | Yes | Yes | No |

### Application actions – Augmented analytics

#### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator to perform Insight Advisor and Insight Advisor Chat actions. If you cannot perform these actions and you have the needed space roles, contact your administrator.

Augmented analytics actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Customize your own application's business logic and vocabulary | Yes | Yes | Yes | Yes | No | No |
| Customize another user's application's business logic and vocabulary (see also: [*Considerations for business logic and vocabulary*](#Considerations)) | Yes | Yes | Yes | Yes | No | No |
| Use Insight Advisor in an application | Yes | Yes | Yes | Yes | Yes | No |
| Access an application via Insight Advisor Chat | Yes | Yes | Yes | Yes | Yes | No |
| Search for application fields in Insight Advisor Chat | Yes | Yes | Yes | Yes | No | No |
| Search for application master items in Insight Advisor Chat | Yes | Yes | Yes | Yes | Yes | No |
| Toggle Insight Advisor Chat and key driver analysis on and off | Yes | Yes | Yes | Yes | No | No |
| Create, edit, rerun, view, and delete key driver analyses | Yes | Yes | Yes | Yes | Yes | No |

#### Considerations for business logic and vocabulary

Information noteThe presence of a logical model associated with an application can result in outcomes which differ from those shown above for Insight Advisor and Insight Advisor Chat. Logical model documentation should be referenced in these scenarios.

Warning note

Business logic and vocabulary assets are stored in Qlik Sense applications via generic objects (see [Generic object](https://qlik.dev/embed/foundational-knowledge/app-anatomy/generic-object-model/)). Updating a generic object requires a user has Can edit permissions on a space, meaning a user with Can edit has API permission to update both business logic and vocabulary, as noted in the table above. However, the UIs for business logic and vocabulary are disabled if an end user does not own the application or have Can edit data in applications in the space of the application.

### Application actions – Notes

Application notes actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Add notes | Yes | Yes | Yes | Yes | Yes | No |
| List all notes in the space  To view the contents of a note, the note must be shared with the user at the note level. Space members can access a note if the note has been shared with them. | Yes | Yes | No | No | No | No |
| Delete notes in the space  The note owner can also delete the note. | Yes | Yes | No | No | No | No |

### Application actions – Subscriptions and alerts

Subscriptions and alerts actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Subscribe to a chart or sheet in the application | Yes | Yes | Yes | Yes | Yes | No |
| Create an alert for the application | Yes | Yes | Yes | Yes | Yes | No |
| Manage a subscription or alert you have created  Managing these items includes actions such as deleting, sending, evaluating, editing, disabling, and re-enabling. | Yes | Yes | Yes | Yes | Yes | No |
| Unsubscribe from a subscription or alert for which you are a recipient | Yes | Yes | Yes | Yes | Yes | No |

### Application actions – Reporting

For permissions related to Qlik Reporting Service automations, see [*Space permissions for reporting with Qlik Automate*](../Reporting/reporting-permissions.htm#Space2).

#### Prerequisites

In addition to required space roles, you may also need to be assigned or more permissions by a tenant administrator before being able to perform Qlik Reporting Service actions. In particular, you might need Generate all reports permissions.

If you cannot perform Qlik Reporting Service actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for the Qlik Reporting Service, administrators can refer to [*Administering reporting and subscriptions*](../Admin/mc-administer-subscriptions.htm).

Reporting actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Connect to the application in Qlik add-ins for Microsoft Office | Yes | Yes | Yes | Yes | No | No |
| View the Reporting section in the application | Yes | Yes | Yes | Yes | No | No |
| Work with PixelPerfect and HTML report templates  Working with these templates involves viewing, creating, editing, deleting, uploading, downloading, and configuring on-demand reporting for the templates. | Yes | Yes | Yes | Yes | No | No |
| View, create, edit, enable, disable, run, and delete report tasks | Yes | Yes | Yes | Yes | No | No |
| View, create, edit, and delete report filters | Yes | Yes | Yes | Yes | No | No |
| Create, upload, and delete report distribution lists in your own application | Yes | Yes | Yes | Yes | No | No |
| Create, upload, and delete report distribution lists in another user's application | No | No | Yes | No | No | No |
| View the recipients and groups from a report distribution list | Yes | Yes | Yes | Yes | No | No |
| View, upload, re-upload, download, and delete report templates | Yes | Yes | Yes | Yes | No | No |
| Enable, disable, or re-configure on-demand reporting from the application | Yes | Yes | Yes | Yes | No | No |
| Generate an on-demand report from the application | Yes | Yes | Yes | Yes | Yes | No |

## Script actions

Script actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create a script | Yes | Yes | Yes | Yes | No | No |
| Open a script | Yes | Yes | Yes | Yes | Yes | No |
| Delete a script | Yes | Yes | Yes | Yes | No | No |
| View the load script in Editor | Yes | Yes | Yes | Yes | No | No |
| Edit the load script in Editor (in your own script) | Yes | Yes | Yes | No | No | No |
| Edit the load script in Editor (in another user's script) | No | No | Yes | No | No | No |
| View script history in Editor | Yes | Yes | Yes | Yes | No | No |
| Preview and download earlier versions in History | Yes | Yes | Yes | Yes | No | No |
| Restore earlier versions in History (in your own script) | Yes | No | Yes | No | No | No |
| Restore earlier versions in History (in another user's script) | No | No | Yes | No | No | No |
| Add data files to a space in Editor (in a script you own) | Yes | No | Yes | No | No | No |
| Add data files to a space in Editor (in another user's script) | No | No | Yes | No | No | No |
| Edit script attributes (change name, description, and tags) | Yes | Yes | Yes | Yes | No | No |
| Reload the script | Yes | Yes | Yes | Yes | No | No |
| Create and manage tasks for scheduled reloads  Managing these tasks includes the following actions:   - Viewing all tasks - Running - Editing - Activating and deactivating - Viewing run history, including logs - Deleting | Yes | Yes | Yes | Yes | No | No |

## Data flow actions

Data flow actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create a data flow | Yes | Yes | Yes | Yes | No | No |
| Open a data flow | Yes | Yes | Yes | Yes | Yes | No |
| Delete a data flow | Yes | Yes | Yes | Yes | No | No |
| View | Yes | Yes | Yes | Yes | Yes | No |
| Edit a data flow in the editor | Yes (if it's your own data flow) | Yes (if it's your own data flow) | Yes | Yes (if it's your own data flow) | No | No |
| Edit a data flow attributes | Yes | Yes | Yes | Yes | No | No |
| Run and schedule a data flow | Yes | Yes | Yes | Yes | No | No |

## Table recipe actions

Table recipe actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create a table recipe | Yes | Yes | Yes | Yes | No | No |
| Open a table recipe | Yes | Yes | Yes | Yes | Yes | No |
| Delete a table recipe | Yes | Yes | Yes | Yes | No | No |
| View | Yes | Yes | Yes | Yes | Yes | No |
| Edit a table recipe in the editor | Yes (if it's your own table recipe) | Yes (if it's your own table recipe) | Yes | Yes (if it's your own table recipe) | No | No |
| Assess data quality in the editor  You also need the Data quality permission set to Allowed by a tenant administrator. | Yes (if it's your own table recipe) | Yes (if it's your own table recipe) | Yes | Yes (if it's your own table recipe) | No | No |
| Edit a table recipe attributes | Yes | Yes | Yes | Yes | No | No |
| Run and schedule a table recipe | Yes | Yes | Yes | Yes | No | No |

## Dataset actions

A dataset represents structured metadata describing an addressable data object. It can reference a file stored in Qlik Cloud or objects behind data connections, such as relational database tables and files in cloud storage. To learn about the differences between datasets and data files, see [*Distinctions between data files and datasets*](../Catalog/data-files-and-datasets.htm).

Dataset actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| View a dataset and its metadata  Dataset metadata refers to information derived from the source data connection or data file, such as the schema, operational information (for example, size and number of rows), and other related properties. | Yes | Yes | Yes | Yes | No | Yes |
| Profile or sample a dataset | Yes | Yes | Yes | Yes | No | No |
| Update a dataset and its metadata  Dataset metadata refers to information derived from the source data connection or data file, such as the schema, operational information (for example, size and number of rows), and other related properties. | Yes | Yes | Yes | Yes | No | No |

## Data sources actions

Data sources actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| List and use data connections in the space  You also need a value of Allowed or Read for the Data connections permission. | Yes | Yes | Yes | Yes | No | Yes |
| List and use data files in the space | Yes | Yes | Yes | Yes | No | Yes |
| Create data connections in the space  You also need a value of Allowed for the Data connections permission. | Yes | Yes | Yes | Yes | No | No |
| Create data files in the space | Yes | Yes | Yes | Yes | No | No |
| Edit data connections in the space  To edit a data connection, the user must be the connection owner.  User credentials are cleared each time a connection is edited.  You also need a value of Allowed for the Data connections permission. | Yes | Yes | Yes | Yes | No | No |
| Edit your own credentials for connections with User defined credentials  You also need a value of Read or Allowed for the Data connections permission. | Yes | Yes | Yes | Yes | No | Yes |
| Edit data files in the space | Yes | Yes | Yes | Yes | No | No |
| Duplicate data files in the space | Yes | Yes | Yes | Yes | No | No |
| Move data files | Yes | Yes | Yes | Yes | No | No |
| Delete data connections from the space  You also need a value of Allowed for the Data connections permission. | Yes | Yes | Yes | Yes | No | No |
| Delete data files from the space | Yes | Yes | Yes | Yes | No | No |
| Edit and apply properties to data connections in the space  You also need a value of Allowed for the Data connections permission. | Yes | Yes | Yes | Yes | No | No |
| Edit and apply properties to data files in the space | Yes | Yes | Yes | Yes | No | No |
| Create application from data source | Yes | Yes | Yes | Yes | No | No |
| Open data connection for application reload  You also need a value of Allowed or Read for the Data connections permission. | Yes | Yes | Yes | Yes | No | Yes |
| Open data file for application reload | Yes | Yes | Yes | Yes | No | Yes |
| Binary load from applications inside space | Yes | Yes | Yes | Yes | No | Yes |

## Automation actions

Automation actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| List and use automations in the space | Yes | Yes | Yes | Yes | No | No |
| Create automations in the space | Yes | Yes | Yes | Yes | No | No |
| Delete automations from the space | Yes | Yes | Yes | Yes | No | No |
| Edit automations in the space | Yes - If user owns the automation | Yes - If user owns the automation | Yes - If user owns the automation | Yes - If user owns the automation | No | No |
| Enable or disable automations in the space | Yes | Yes | Yes | Yes | No | No |
| Duplicate automations in the space | Yes | Yes | Yes | Yes | No | No |
| Create automation using automation connection | Yes | Yes | Yes | Yes | No | No |

### Automation connections actions

Automation connections actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| List and use automation connections in the space | Yes | Yes | Yes | Yes | No | Yes |
| Create automation connection in the space | Yes | Yes | Yes | Yes | No | No |
| Delete automation connection from the space | Yes | Yes | Yes | Yes | No | No |
| Edit automation connection in the space | Yes - If user owns the connection | Yes - If user owns the connection | Yes - If user owns the connection | Yes - If user owns the connection | No | No |
| Create automation using automation connection | Yes | Yes | Yes | Yes | No | Yes |

## Qlik Predict — ML experiment actions

### ML experiment actions - View access

#### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator before being able to perform these actions. These permissions are:

- Automl Experiment Contributor built-in security role
- Automl Deployment Contributor built-in security role
- Manage ML experiments permission (user)
- Manage ML deployments permission (user)
- Manage ML experiments and deployments admin permission

If you cannot perform these actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for Qlik Predict, administrators can refer to [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

ML experiment view actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| List ML experiments in the space | Yes | Yes | No | Yes | Yes | No |
| Open ML experiment | Yes | Yes | No | Yes | Yes | No |
| Download training reports for models in the experiment | Yes | Yes | No | Yes | Yes | No |
| Open Lineage directly from the experiment  You also need View lineage set to Allowed in the default permissions or a custom security role | Yes | Yes | No | Yes | Yes | No |
| Open and view the experiment in Impact analysis | Yes | Yes | No | Yes | Yes | No |

### ML experiment actions - Creation, use, and management

#### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator before being able to perform these actions. These permissions are:

- Automl Experiment Contributor built-in security role
- Manage ML experiments permission (user)

If you cannot perform these actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for Qlik Predict, administrators can refer to [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

ML experiment use actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create ML experiment | Yes | Yes | No | Yes | No | No |
| Delete ML experiment | Yes | Yes | No | Yes | No | No |
| Edit ML experiment | Yes | Yes | No | Yes | No | No |
| Move ML experiment to the space | Yes | Yes | No | Yes | No | No |
| Move ML experiment to another space | Yes | Yes | No | Yes | No | No |

## Qlik Predict — ML deployment actions

### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator before being able to perform these actions. These permissions are:

### ML deployment actions – View access

#### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator before being able to perform these actions. These permissions are:

- Automl Experiment Contributor built-in security role
- Automl Deployment Contributor built-in security role
- Manage ML experiments permission (user)
- Manage ML deployments permission (user)
- Manage ML experiments and deployments admin permission

If you cannot perform these actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for Qlik Predict, administrators can refer to [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

ML deployment view actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| List ML deployments in the space | Yes | Yes | No | Yes | Yes | No |
| Open ML deployment | Yes | Yes | No | Yes | Yes | No |
| Download training reports for models in an ML deployment  You also need view access for the experiment in which the model was trained. | Yes | Yes | No | Yes | Yes | No |
| Open Lineage directly from the deployment  You also need View lineage set to Allowed in the default permissions or a custom security role | Yes | Yes | No | Yes | Yes | No |
| Open and view the deployment in Impact analysis | Yes | Yes | No | Yes | Yes | No |

### ML deployment actions – Model deployment and approval

#### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator before being able to perform these actions. These permissions are:

- Automl Deployment Contributor built-in security role
- Manage ML deployments permission (user)
- Manage ML experiments and deployments admin permission
- Approve or reject your ML models permission (user)
- Approve or reject ML models admin permission

If you cannot perform these actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for Qlik Predict, administrators can refer to [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

ML deployment model actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Deploy model to an ML deployment (new or existing)  If the source experiment is in shared space, you also need one of the following roles in its space:   - Owner (of the space) - Can manage - Can edit | Yes | Yes | No | Yes | No | No |
| Remove a model from an ML deployment | Yes | Yes | No | Yes | No | No |
| Activate and deactivate a model in an ML deployment | Yes | Yes | No | Yes | No | No |

### ML deployment actions – Management

#### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator before being able to perform these actions. These permissions are:

- Automl Deployment Contributor built-in security role
- Manage ML deployments permission (user)

If you cannot perform these actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for Qlik Predict, administrators can refer to [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

ML deployment management actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Delete ML deployment | Yes | Yes | No | Yes | No | No |
| Edit ML deployment | Yes | Yes | No | Yes | No | No |
| Create, rename, and delete [model aliases](#glossary-2 "Glossary term") in an ML deployment | Yes | Yes | No | Yes | No | No |
| Move ML deployment to the space | Yes | Yes | No | Yes | No | No |
| Move ML deployment to another space | Yes | Yes | No | Yes | No | No |
| Download training reports for models in an ML deployment  You also need view access for the experiment in which the model was trained. | Yes | Yes | No | Yes | Yes | No |

### ML deployment actions – Predictions

Information notePermissions related to using [prediction](#glossary-3 "Glossary term") data (for example, opening or profiling the dataset, or using it in an application) are generally the same as [*Data sources actions*](#DataSrcActions).

#### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator before being able to perform these actions. These permissions are:

- Automl Deployment Contributor built-in security role
- Manage ML deployments permission (user)

If you cannot perform these actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for Qlik Predict, administrators can refer to [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

ML deployment prediction actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create, edit, and delete prediction configurations | Yes | Yes | No | Yes | No | No |
| Create, edit, and delete prediction schedules | Yes | Yes | No | Yes | No | No |
| Change the owner of a prediction configuration | Yes | Yes | No | Yes | No | No |
| Create, rename, and delete [model aliases](#glossary-4 "Glossary term") in an ML deployment | Yes | Yes | No | Yes | No | No |
| Run [batch prediction](#glossary-5 "Glossary term") | Yes | Yes | No | Yes | No | No |
| Run prediction with real-time API endpoint | Yes | Yes | No | Yes | No | Yes |
| Run prediction with Qlik Predict analytics connector  You also need sufficient access to the space of the data connection:   - Shared space: Owner, Can manage, Can edit, or Can consume data - Managed space: Owner, Can manage, or Can consume data | Yes | Yes | No | Yes | No | Yes |

## Business glossary actions for all user entitlements

In user-based subscriptions, both users with Professional and Analyzer entitlement can work with business glossaries.

Access to business glossaries are controlled by your user role's permissions. In addition to your space permissions, you need to be assigned one of the following permissions to your user role by an administrator to use business glossaries:

- Manage glossaries and approve terms:

  - Allowed
  - Read and collaborate on terms only
  - Manage only

For a list of what actions each permission supports, see [*Glossary actions by user role permission*](../Catalog/BusinessGlossary/Working-business-glossaries.htm#Glossary).

Information note

The Allowed setting for Manage glossaries and approve terms is the equivalent of the Steward global role that previously was used to administer business glossaries. The Steward role is still supported, but will eventually be replaced by the user role permissions.

If you cannot perform these actions and you have the needed space roles, contact your administrator.

Business glossary actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| List glossaries in the space | Yes | Yes | Yes | Yes | Yes | No |
| Open a glossary (details page only) | Yes | Yes | Yes | Yes | Yes | No |
| View glossary and terms | Yes | Yes | Yes | Yes | Yes | No |
| Move glossary from this space | Yes | Yes | Yes | Yes | No | No |
| Move glossary to this space | Yes | Yes | Yes | Yes | No | No |
| Create a glossary | Yes | Yes | Yes | Yes | No | No |
| Edit glossary settings and page | Yes | Yes | Yes | Yes | No | No |
| Delete a glossary | Yes | Yes | Yes | Yes | No | No |
| Add a term in glossary | Yes | Yes | Yes | Yes | No | No |
| Edit term not in Verified state | Yes | Yes | Yes | Yes | No | No |
| Edit term in Verified state | Yes | Yes | Yes | Yes | No | No |
| Delete term not in Verified state | Yes | Yes | Yes | Yes | No | No |
| Delete term in Verified state | Yes | Yes | Yes | Yes | No | No |
| Change state of a term to/from Verified | Yes | Yes | Yes | Yes | No | No |
| Change state of a term between states other than Verified | Yes | Yes | Yes | Yes | No | No |
| Create, edit, delete categories | Yes | Yes | Yes | Yes | No | No |
| Link glossary terms to master items in applications | Yes | Yes | Yes | Yes | Yes | No |
| Can export glossaries and terms | Yes | Yes | Yes | Yes | Yes | No |

## Notes actions

Notes actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Add notes to the space | Yes | Yes | Yes | Yes | Yes | No |
| List all notes in the space  To view the contents of a note, the note must be shared with the user at the note level. Space members can access a note if the note has been shared with them. | Yes | Yes | No | No | No | No |
| Delete notes in the space  The note owner can also delete the note. | Yes | Yes | No | No | No | No |

## Qlik Answers actions

Qlik Answers assistant actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data | Can view and Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| View assistants in Answers assistants | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Chat with an assistant | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Create new assistants | Yes | Yes | Yes | Yes | No | No | No |
| Move assistants to the space | Yes | Yes | Yes | Yes | No | No | No |
| Move assistants to another space | Yes | Yes | Yes | Yes | No | No | No |
| Open an assistant | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Delete an assistant | Yes | Yes | Yes | Yes | No | No | No |
| Edit an assistant | Yes | Yes | Yes | Yes | No | No | No |
| View assistant applications and knowledge bases | Yes | Yes | Yes | Yes | No | No | Yes |
| Add and remove applications and knowledge bases | Yes | Yes | Yes | Yes | No | No | No |
| Review answers and feedback  Information noteThis also requires the Audit Admin user role. | Yes | Yes | Yes | Yes | Yes | No | Yes |

Qlik Answers knowledge base actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data | Can view and Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Create knowledge bases | Yes | Yes | Yes | Yes | No | No | No |
| Move knowledge bases to the space | Yes | Yes | Yes | Yes | No | No | No |
| Move knowledge bases to another space | Yes | Yes | Yes | Yes | No | No | No |
| Open a knowledge base | Yes | Yes | Yes | Yes | No | No | Yes |
| Delete a knowledge base | Yes | Yes | Yes | Yes | No | No | No |
| Edit a knowledge base | Yes | Yes | Yes | Yes | No | No | No |
| Index sources | Yes | Yes | Yes | Yes | No | No | No |
| Set up an index schedule | Yes | Yes | Yes | Yes | No | No | No |
| Get answers from knowledge bases using an assistant | Yes | Yes | Yes | Yes | No | No | Yes |
| View sources from knowledge base | Yes | Yes | Yes | Yes | No | No | Yes |

Qlik Answers skill actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data | Can view and Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Upload skill | Yes | Yes | Yes | Yes | No | No | No |
| Move skills to the space | Yes | Yes | Yes | Yes | No | No | No |
| Move skills to other spaces | Yes | Yes | Yes | Yes | No | No | No |
| Open skills | Yes | Yes | Yes | Yes | No | No | Yes |
| Delete skills | Yes | Yes | Yes | Yes | No | No | No |
| Edit skill details | Yes | Yes | Yes | Yes | No | No | No |

Qlik Answers application actions – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data | Can view and Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| View applications in Application analysis | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Open Answers in an open application | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Ask question about the application in Qlik Answers | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Make application available to Qlik Answers | Yes | Yes | Yes | Yes | No | No | No |

## Discovery Agent actions

### Prerequisites

In addition to required space roles, you may also need to be assigned or more permissions by a tenant administrator before being able to perform Discovery Agent actions. In particular, you might need one or more of the following:

- Insight triggers
- Insights feed

For a list of all permission requirements for the Discovery Agent, administrators can refer to [*Administering Discovery Agent*](../DiscoveryAgent/discovery-agent-admin.htm).

Discovery Agent actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create and manage [insight triggers](#glossary-6 "Glossary term") in the application | Yes | Yes | Yes | Yes | No | No |
| View [insight triggers](#glossary-7 "Glossary term") in the application | Yes | Yes | Yes | Yes | Yes | No |
| View insights from the application in your feed | Yes | Yes | Yes | Yes | Yes | No |

## Other content actions

Other content actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create, edit, and delete generic links | Yes | Yes | No | No | No | No |
