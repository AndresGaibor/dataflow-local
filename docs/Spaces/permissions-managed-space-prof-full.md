---
title: "Managed space permissions for Professional and capacity-based subscription users"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/permissions-managed-space-prof-full.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces", "Working in managed spaces", "Managing permissions in managed spaces"]
---

# Managed space permissions for Professional and capacity-based subscription users

This topic shows what members can do in a managed space. It applies to all users in capacity-based subscriptions and to user with Professional entitlement in user-based subscriptions.

## Space actions

You need the Managed Space Creator user role in the [tenant](#glossary-0 "Glossary term") to create new managed spaces.

Space actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| See the space exists | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Delete the space | Yes | Yes | No | No | No | No | No | No |
| Add members to the space | Yes | Yes | No | No | No | No | No | No |
| Change member permissions for the space  Space owners can be changed by tenant and analytics administrators in the Administration activity center. | Yes | Yes | No | No | No | No | No | No |
| Remove members from the space | Yes | Yes | No | No | No | No | No | No |
| Add, delete, rename, duplicate, and move folders in the space | Yes | Yes | No | No | No | No | No | Yes |

## Application actions

### Application actions – General

General application actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Open an application | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Publish or republish applications to this space  If the application being published is in a shared space, you also need the Can edit space role or higher in that shared space in order to publish the application. | Yes | No | Yes | No | No | No | No | No |
| See applications they published to this space | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| See all applications in the space | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Download applications in the space (Download without data option only) | Yes | Yes | No | No | No | No | No | No |
| Share applications in the space with non-space members | Yes | Yes | No | No | No | No | No | No |
| Remove application-only access to applications from non-space members | Yes | Yes | No | No | No | No | No | No |
| Delete an application | Yes | Yes | No | No | No | No | No | No |
| Edit application attributes (change name, description, and tags) | Yes | Yes | No | No | No | No | No | Yes |
| Edit application properties (select theme, enable right-to-left reading order, set a bookmark as application default, and [sheet](#glossary-1 "Glossary term") title styling) | Yes | Yes | No | No | No | No | No | Yes |
| Approve application access requests | Yes | Yes | No | No | No | No | No | No |

### Application actions – Data modeling and reload

Data management actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Open [Data model viewer](#glossary-2 "Glossary term") | Yes | Yes | No | No | No | No | No | Yes |
| Reload the application | Yes | Yes | No | No | No | No | No | Yes |
| Create and manage tasks for scheduled reloads  Managing these tasks includes the following actions:   - Viewing all tasks - Running - Editing - Activating and deactivating - Viewing run history, including logs - Deleting | Yes | Yes | No | No | No | No | No | Yes |

### Application actions – Sheets, storytelling, and visualizations

Sheets, storytelling, and visualization actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| View master items | Yes | Yes | No | Yes | No | No | No | No |
| View [variables](#glossary-3 "Glossary term") | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| View media library content | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Create and manage media library content | Yes | Yes | No | No | No | No | No | Yes |
| Add private sheets to the application | Yes | Yes | No | Yes | No | No | No | No |
| Paste copied visualizations onto private sheets | Yes | Yes | No | Yes | No | No | No | No |
| Paste copied sheets in the application | Yes | Yes | No | Yes | No | No | No | No |
| Add private bookmarks to the application | Yes | Yes | No | Yes | Yes | Yes | No | No |
| Add private stories to the application | Yes | Yes | No | Yes | Yes | No | No | No |
| Publish and unpublish your own private sheets, bookmarks, and stories to and from Community | Yes | Yes | No | Yes | No | No | No | No |
| Make all Community sheets, bookmarks, and stories private in the application (unpublish them) | Yes | Yes | No | No | No | No | No | No |
| Update and delete your own private sheets, bookmarks, and stories | Yes | Yes | No | Yes | Yes | Yes | No | No |
| Copy a link to a Public or Community bookmark | Yes | Yes | No | Yes | No | No | No | No |
| Take [snapshots](#glossary-4 "Glossary term") in the application | Yes | Yes | No | Yes | Yes | No | No | No |
| Monitor a [visualization](#glossary-5 "Glossary term") in your personal space | Yes | Yes | No | Yes | Yes | No | No | No |
| Share a visualization to monitor in the managed space | Yes | Yes | No | No | No | No | No | No |
| Create links to sheets | Yes | Yes | No | No | No | No | No | No |
| Create, edit, and delete [write table](#glossary-6 "Glossary term") chart configurations | Yes | Yes | No | Yes | No | No | No | No |
| View write tables and make changes to their editable columns | Yes | Yes | No | Yes | Yes | No | No | Yes |

### Application actions – Augmented analytics

#### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator to perform Insight Advisor and Insight Advisor Chat actions. If you cannot perform these actions and you have the needed space roles, contact your administrator.

Augmented analytics actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Search for application fields in Insight Advisor Chat | Yes | Yes | No | No | No | No | No | No |
| Search for application master items in Insight Advisor Chat | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Toggle Insight Advisor Chat and key driver analysis on and off | Yes | Yes | No | No | No | No | No | Yes |
| Create, edit, rerun, view, and delete key driver analyses | Yes | Yes | No | Yes | Yes | No | No | No |

### Application actions – Subscriptions and alerts

Subscription and alerts actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Subscribe to a chart or sheet in the application | Yes | Yes | No | Yes | Yes | No | No | No |
| Create an alert for the application | Yes | Yes | No | Yes | Yes | No | No | No |
| Manage a subscription or alert you have created  Managing these items includes actions such as deleting, sending, evaluating, editing, disabling, and re-enabling. | Yes | Yes | Yes | No | Yes | No | No | No |
| Unsubscribe from a subscription or alert for which you are a recipient | Yes | Yes | No | Yes | Yes | Yes | No | Yes |

### Application actions – Notes

You can add notes to the space when you are viewing an application.

Application notes actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add notes | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| List all notes in the space  To view the contents of a note, the note must be shared with the user at the note level. Space members can access a note if the note has been shared with them individually. | Yes | Yes | No | No | No | No | No | No |
| Delete notes in the space  The note owner can also delete the note. | Yes | Yes | No | No | No | No | No | No |

### Application actions – Reporting

For permissions related to Qlik Reporting Service automations, see [*Space permissions for reporting with Qlik Automate*](../Reporting/reporting-permissions.htm#Space2).

#### Prerequisites

In addition to required space roles, you may also need to be assigned or more permissions by a tenant administrator before being able to perform Qlik Reporting Service actions. In particular, you might need Generate all reports permissions.

If you cannot perform Qlik Reporting Service actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for the Qlik Reporting Service, administrators can refer to [*Administering reporting and subscriptions*](../Admin/mc-administer-subscriptions.htm).

Reporting actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connect to the application in Qlik add-ins for Microsoft Office | Yes | Yes | No | Yes | No | No | No | Yes |
| View and use the Reporting section in the application | Yes | Yes | No | No | No | No | No | Yes |
| Work with PixelPerfect and HTML report templates  Working with these templates involves viewing, creating, editing, deleting, uploading, downloading, and configuring on-demand reporting for the templates. | Yes | Yes | No | No | No | No | No | Yes |
| Generate an on-demand report from the application | Yes | Yes | Yes | Yes | Yes | Yes | No | Yes |

## Script actions

Script actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Publish or republish scripts to this space  If the script being published is in a shared space, you also need the Can edit space role or higher in that shared space in order to publish the script. | Yes | No | Yes | No | No | No | No | No |
| See scripts they published to this space | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| See all scripts in the space | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Open a script | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Delete a script | Yes | Yes | No | No | No | No | No | No |
| View load script in Editor | Yes | Yes | No | No | No | No | No | Yes |
| View script history in Editor | Yes | Yes | No | No | No | No | No | Yes |
| Preview and download earlier versions in History | Yes | Yes | No | No | No | No | No | Yes |
| Edit script attributes (change name, description, and tags) | Yes | Yes | No | No | No | No | No | Yes |
| Reload the script | Yes | Yes | No | No | No | No | No | Yes |
| Create and manage tasks for scheduled reloads  Managing reload tasks includes the following actions:   - Viewing all reload tasks - Running - Editing - Activating and deactivating - Viewing history - Deleting | Yes | Yes | No | No | No | No | No | Yes |

## Data flow actions

Data flow actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Publish or republish a data flow to this space | Yes | No | Yes | No | No | No | No | No |
| See all data flows in the space | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Open a data flow | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Delete a data flow | Yes | Yes | No | No | No | No | No | No |
| View | Yes | Yes | No | Yes | Yes | No | No | Yes |
| View run history | Yes | Yes | No | No | No | No | No | Yes |
| View lineage and impact analysis  You also need View lineage set to Allowed in the default permissions or a custom security role | Yes | Yes | Yes | Yes | Yes | No | No | Yes |
| Edit a data flow attributes | Yes | Yes | No | No | No | No | No | Yes |
| Reload a data flow and schedule reloads | Yes | Yes | No | No | No | No | No | Yes |

## Table recipe actions

Table recipe actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Publish or republish a table recipe to this space | Yes | No | Yes | No | No | No | No | No |
| See all table recipes in the space | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Open a table recipe | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Delete a table recipe | Yes | Yes | No | No | No | No | No | No |
| View run history | Yes | Yes | No | No | No | No | No | Yes |
| View lineage and impact analysis  You also need View lineage set to Allowed in the default permissions or a custom security role | Yes | Yes | No | Yes | Yes | No | No | Yes |
| Edit a table recipe attributes | Yes | Yes | No | No | No | No | No | Yes |
| Reload a table recipe and schedule reloads | Yes | Yes | No | No | No | No | No | Yes |

## Dataset actions

A dataset represents structured metadata describing an addressable data object. It can reference a file stored in Qlik Cloud or objects behind data connections, such as relational database tables and files in cloud storage. To learn about the differences between datasets and data files, see [*Distinctions between data files and datasets*](../Catalog/data-files-and-datasets.htm).

Dataset actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| View a dataset and its metadata  Dataset metadata refers to information derived from the source data connection or data file, such as the schema, operational information (for example, size and number of rows), and other related properties. | Yes | Yes | No | No | No | No | Yes | Yes |
| Profile or sample a dataset | Yes | Yes | No | No | No | No | Yes | Yes |
| Update a dataset and its metadata  Dataset metadata refers to information derived from the source data connection or data file, such as the schema, operational information (for example, size and number of rows), and other related properties. | Yes | Yes | No | No | No | No | No | Yes |

## Data sources actions

Data source actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| List and use data connections in the space  You also need a value of Allowed or Read for the Data connections permission. | Yes | Yes | No | No | No | No | Yes | Yes |
| List and use data files in the space | Yes | Yes | No | No | No | No | Yes | Yes |
| Create data connections in the space  You also need a value of Allowed for the Data connections permission. | Yes | Yes | No | No | No | No | No | Yes |
| Create data files in the space | Yes | Yes | No | No | No | No | No | Yes |
| Edit data connections in the space  To edit a data connection, the user must be the connection owner.  User credentials are cleared each time a connection is edited.  You also need a value of Allowed for the Data connections permission. | Yes | Yes | No | No | No | No | No | Yes |
| Edit your own credentials for connections with User defined credentials  You also need a value of Read or Allowed for the Data connections permission. | Yes | Yes | No | No | No | No | Yes | Yes |
| Duplicate data files in the space | Yes | Yes | No | No | No | No | No | Yes |
| Move data files | Yes | Yes | No | No | No | No | No | Yes |
| Delete data connections from the space  You also need a value of Allowed for the Data connections permission. | Yes | Yes | No | No | No | No | No | Yes |
| Delete data files from the space | Yes | Yes | No | No | No | No | No | Yes |
| Profile data source | Yes | Yes | No | No | No | No | No | Yes |
| Edit and apply properties to data files in the space | Yes | Yes | No | No | No | No | No | Yes |
| Edit and apply properties to data connections in the space  You also need a value of Allowed for the Data connections permission. | Yes | Yes | No | No | No | No | No | Yes |
| Create application from data source | No | No | No | No | No | No | No | No |
| Open data connection for application reload  You also need a value of Allowed or Read for the Data connections permission. | Yes | Yes | No | No | No | No | Yes | Yes |
| Open data file for application reload | Yes | Yes | No | No | No | No | Yes | Yes |
| Binary load from applications inside space | Yes | No | No | No | No | No | Yes | No |

## Qlik Predict — ML deployment actions

Information notePermissions related to using [prediction](#glossary-7 "Glossary term") data (for example, opening or profiling the dataset, or using it in an application) are generally the same as [*Data sources actions*](#DataSrcActions).

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

ML deployment view actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| List ML deployments in the space | Yes | Yes | No | Yes | Yes | No | No | Yes |
| Open ML deployment | Yes | Yes | No | Yes | Yes | No | No | Yes |
| Download training reports for models in an ML deployment  You also need view access for the experiment in which the model was trained. | Yes | Yes | No | Yes | Yes | No | No | No |
| Open Lineage directly from the deployment  You also need View lineage set to Allowed in the default permissions or a custom security role | Yes | Yes | No | Yes | Yes | No | No | Yes |
| Open and view the deployment in Impact analysis | Yes | Yes | No | Yes | Yes | No | No | Yes |

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

ML deployment model actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Deploy model to an ML deployment (new or existing)  If the source experiment is in shared space, you also need one of the following roles in its space:   - Owner (of the space) - Can manage - Can edit | Yes | No | Yes | No | No | No | No | No |
| Remove a model from an ML deployment | Yes | No | Yes | No | No | No | No | No |
| Activate and deactivate a model in an ML deployment | Yes | Yes | No | No | No | No | No | No |

### ML deployment actions – Management

#### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator before being able to perform these actions. These permissions are:

- Automl Deployment Contributor built-in security role
- Manage ML deployments permission (user)

If you cannot perform these actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for Qlik Predict, administrators can refer to [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

ML deployment management actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Delete ML deployment | Yes | Yes | No | No | No | No | No | No |
| Edit ML deployment | Yes | Yes | No | No | No | No | No | No |
| Create, rename, and delete [model aliases](#glossary-8 "Glossary term") in an ML deployment | Yes | Yes | No | No | No | No | No | No |
| Move ML deployment to the space | Yes | Yes | No | No | No | No | No | No |
| Move ML deployment to another space | Yes | Yes | No | No | No | No | No | No |

### ML deployment actions – Predictions

#### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator before being able to perform these actions. These permissions are:

- Automl Deployment Contributor built-in security role
- Manage ML deployments permission (user)

If you cannot perform these actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for Qlik Predict, administrators can refer to [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

ML deployment prediction actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Create, edit, and delete prediction configurations | Yes | Yes | No | No | No | No | No | No |
| Create, edit, and delete prediction schedules | Yes | Yes | No | No | No | No | No | No |
| Change the owner of a prediction configuration | Yes | Yes | No | No | No | No | No | No |
| Run [batch prediction](#glossary-9 "Glossary term") | Yes | Yes | No | No | No | No | No | No |
| Run prediction with real-time API endpoint | Yes | Yes | No | No | No | No | Yes | No |
| Run prediction with Qlik Predict analytics connector  You also need sufficient access to the space of the data connection:   - Shared space: Owner, Can manage, Can edit, or Can consume data - Managed space: Owner, Can manage, or Can consume data | Yes | Yes | No | No | No | No | Yes | No |

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

Business glossary actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| List glossaries in the space | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Open a glossary (details page only) | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| View glossary and terms | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Move glossary from this space | Yes | Yes | No | Yes | No | No | No | No |
| Move glossary to this space | Yes | Yes | No | Yes | No | No | No | No |
| Create a glossary | Yes | Yes | No | Yes | No | No | No | No |
| Edit glossary settings and page | Yes | Yes | No | Yes | No | No | No | No |
| Delete a glossary | Yes | Yes | No | Yes | No | No | No | No |
| Add a term in glossary | Yes | Yes | No | Yes | No | No | No | No |
| Edit term not in Verified state | Yes | Yes | No | Yes | No | No | No | No |
| Edit term in Verified state | Yes | Yes | No | Yes | No | No | No | No |
| Delete term not in Verified state | Yes | Yes | No | Yes | No | No | No | No |
| Delete term in Verified state | Yes | Yes | No | Yes | No | No | No | No |
| Change state of a term to/from Verified | Yes | Yes | No | Yes | No | No | No | No |
| Change state of a term between states other than Verified | Yes | Yes | No | Yes | No | No | No | No |
| Create, edit, delete categories | Yes | Yes | No | Yes | No | No | No | No |
| Can export glossaries and terms | Yes | Yes | No | Yes | Yes | Yes | No | Yes |

## Notes actions

Notes actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add [notes](#glossary-10 "Glossary term") | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| List all notes in the space  To view the contents of a note, the note must be shared with the user at the note level. Space members can access a note if the note has been shared with them individually. | Yes | Yes | No | No | No | No | No | No |
| Delete notes in the space  The note owner can also delete the note. | Yes | Yes | No | No | No | No | No | No |

## Qlik Answers actions

Qlik Answers assistant actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restrictive view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chat with an assistant  Can contribute, Can view, and Has restrictive view also require Can consume data to chat with assistants. | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Create new assistants | Yes | Yes | No | Yes | No | No | No | No |
| Move assistants to the space | Yes | Yes | No | Yes | No | No | No | No |
| Move assistants to another space | Yes | Yes | No | Yes | No | No | No | No |
| Open an assistant | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Delete an assistant | Yes | Yes | No | Yes | No | No | No | No |
| Edit an assistant | Yes | Yes | No | Yes | No | No | No | No |
| View assistant knowledge bases | Yes | Yes | No | Yes | Yes | No | No | No |
| Add and remove knowledge bases | Yes | Yes | No | Yes | No | No | No | No |
| Review answers and feedback  Information noteThis also requires the Audit Admin user role. | Yes | Yes | No | Yes | Yes | No | No | No |

Qlik Answers knowledge base actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restrictive view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Create knowledge bases | Yes | Yes | No | Yes | No | No | No | No |
| Move knowledge bases to the space | Yes | Yes | No | Yes | No | No | No | No |
| Move knowledge bases to another space | Yes | No | No | Yes | No | No | No | No |
| Open a knowledge base | Yes | Yes | No | Yes | Yes | No | No | No |
| Delete a knowledge base | Yes | Yes | No | Yes | No | No | No | No |
| Edit a knowledge base | Yes | Yes | No | Yes | No | No | No | No |
| Index sources  Can contribute requires Can consume data in the space with the data. | Yes | Yes | No | Yes | No | No | No | Yes |
| Set up an index schedule | Yes | Yes | No | Yes | No | No | No | Yes |
| Get answers from knowledge bases using an assistant | Yes | Yes | No | Yes | Yes | Yes | Yes | No |
| View sources from knowledge base | Yes | Yes | No | Yes | Yes | Yes | Yes | No |

Qlik Answers skill actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restrictive view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Upload skill | Yes | Yes | No | Yes | No | No | No | No |
| Move skills to the space | Yes | Yes | No | Yes | No | No | No | No |
| Move skills to other spaces | Yes | No | No | Yes | No | No | No | No |
| Open skills | Yes | Yes | No | Yes | Yes | No | No | No |
| Delete skills | Yes | Yes | No | Yes | No | No | No | No |
| Edit skill details | Yes | Yes | No | Yes | No | No | No | No |

## Discovery Agent actions

### Prerequisites

In addition to required space roles, you may also need to be assigned or more permissions by a tenant administrator before being able to perform Discovery Agent actions. In particular, you might need one or more of the following:

- Insight triggers
- Insights feed

For a list of all permission requirements for the Discovery Agent, administrators can refer to [*Administering Discovery Agent*](../DiscoveryAgent/discovery-agent-admin.htm).

Discovery Agent actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Create and manage [insight triggers](#glossary-11 "Glossary term") in the application | Yes | Yes | No | No | No | No | No | No |
| View [insight triggers](#glossary-12 "Glossary term") in the application | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| View insights from the application in your feed | Yes | Yes | No | Yes | Yes | Yes | No | Yes |

## Other content actions

Other content actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Create, edit, and delete generic links | Yes | Yes | No | No | No | No | No | No |
