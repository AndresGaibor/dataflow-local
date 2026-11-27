---
title: "Managed space permissions for users with Analyzer entitlement"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/permissions-managed-space-analyzer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces", "Working in managed spaces", "Managing permissions in managed spaces"]
---

# Managed space permissions for users with Analyzer entitlement

This help topic contains tables outlining what members with Analyzer entitlement can do in a [managed space](#glossary-0 "Glossary term").

For more information about managing permissions in managed spaces, including special considerations, see [*Managing permissions in managed spaces*](managing-managed-spaces.htm).

When assigning space roles to a user with Analyzer entitlement, consider that this entitlement is intended only for consumption of content. Users with Analyzer entitlement should not be assigned roles for space management. For more information, see [*Space permissions and user entitlement*](managing-managed-spaces.htm#Space).

## Space actions

Space actions by space role in a managed space – Analyzer entitlement

| Action | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| See the space exists | Yes | Yes | Yes | Yes | Yes | No |

## Application actions

### Application actions – General

General application actions by space role in a managed space – Analyzer entitlement

| Action | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Publish or republish applications to this space  If the application being published is in a shared space, you also need the Can edit space role or higher in that shared space in order to publish the application. | No | No | No | No | No | No |
| See applications they published to this space | Yes | No | Yes | Yes | Yes | No |
| See all applications in the space | Yes | No | Yes | Yes | Yes | No |
| Download applications in the space (Download without data option only) | Yes | No | No | No | No | No |
| Remove application-only access to applications from non-space members | Yes | No | No | No | No | No |
| Open an application | Yes | No | Yes | Yes | Yes | No |
| Delete an application | Yes | No | No | No | No | No |
| Approve application access requests | Yes | Yes | No | No | No | No |

### Application actions – Sheets, storytelling, and visualizations

Sheets, storytelling, and visualizations actions by space role in a managed space – Analyzer entitlement

| Action | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Add private sheets to the application | Yes | No | Yes | No | No | No |
| View, create, edit, and delete media library content | No | No | No | No | No | No |
| Paste copied visualizations onto private sheets | No | No | No | No | No | No |
| Paste copied sheets in the application | No | No | No | No | No | No |
| Add private bookmarks to the application | Yes | No | Yes | Yes | Yes | Yes |
| Add private stories to the application | Yes | No | Yes | Yes | No | No |
| Publish and unpublish your own private bookmarks and stories to and from Community | Yes | No | Yes | No | No | No |
| Make all Community bookmarks and stories private in the application (unpublish them) | No | No | No | No | No | No |
| Update and delete your own private sheets, bookmarks, and stories | Yes | No | Yes | Yes | Yes | No |
| Take snapshots in the application | Yes | No | Yes | Yes | No | No |
| Monitor a [visualization](#glossary-1 "Glossary term") in your personal space | Yes | No | Yes | Yes | No | No |
| Share a visualization to monitor in the managed space | Yes | No | No | No | No | No |
| Create links to sheets | Yes | No | No | No | No | No |
| View write tables and make changes to their editable columns | Yes | No | Yes | Yes | No | No |

### Application actions – Augmented analytics

#### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator to perform Insight Advisor and Insight Advisor Chat actions. If you cannot perform these actions and you have the needed space roles, contact your administrator.

Augmented analytics actions by space role in a managed space – Analyzer entitlement

| Action | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Search for application fields in Insight Advisor Chat | Yes | Yes | No | No | No | No |
| Search for application master items in Insight Advisor Chat | Yes | Yes | No | Yes | Yes | Yes |
| Toggle Insight Advisor Chat and key driver analysis on and off | Yes | No | No | No | No | No |
| Create, edit, rerun, view, and delete key driver analyses | Yes | No | Yes | Yes | No | No |

### Application actions – Subscriptions and alerts

Subscriptions and alerts actions by space role in a managed space – Analyzer entitlement

| Action | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Subscribe to a chart or sheet in the application | Yes | No | Yes | Yes | No | No | No |
| Create an alert for the application | Yes | No | Yes | Yes | No | No | No |
| Manage a subscription or alert you have created  Managing these items includes actions such as deleting, sending, evaluating, editing, disabling, and re-enabling. | Yes | No | Yes | Yes | No | No | No |
| Unsubscribe from a subscription or alert for which you are a recipient | Yes | No | Yes | Yes | Yes | No | No |

### Application actions – Notes

Application notes actions by space role in a managed space – Analyzer entitlement

| Action | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Add notes | Yes | No | Yes | Yes | Yes | No |
| List all notes in the space  To view the contents of a note, the note must be shared with the user at the note level. Space members can access a note if the note has been shared with them individually. | Yes | No | No | No | No | No |
| Delete notes in the space  The note owner can also delete the note. | Yes | No | No | No | No | No |

### Application actions – Reporting

For permissions related to Qlik Reporting Service automations, see [*Space permissions for reporting with Qlik Automate*](../Reporting/reporting-permissions.htm#Space2).

#### Prerequisites

In addition to required space roles, you may also need to be assigned or more permissions by a tenant administrator before being able to perform Qlik Reporting Service actions. In particular, you might need Generate all reports permissions.

If you cannot perform Qlik Reporting Service actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for the Qlik Reporting Service, administrators can refer to [*Administering reporting and subscriptions*](../Admin/mc-administer-subscriptions.htm).

Reporting actions by space role in a managed space – Analyzer entitlement

| Action | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Connect to the application in Qlik add-ins for Microsoft Office | Yes | No | Yes | No | No | No |
| View and use the Reporting section in the application | Yes | No | No | No | No | No |
| Work with PixelPerfect and HTML report templates  Working with these templates involves viewing, creating, editing, deleting, uploading, downloading, and configuring on-demand reporting for the templates. | Yes | No | No | No | No | No |
| Generate an on-demand report from the application | Yes | No | Yes | Yes | Yes | No |

## Script actions

Script actions by space role in a managed space – Analyzer entitlement

| Action | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Publish or republish scripts to this space  If the script being published is in a shared space, you also need the Can edit space role or higher in that shared space in order to publish the script. | No | No | No | No | No | No |
| See scripts they published to this space | Yes | No | Yes | Yes | Yes | No |
| See all scripts in the space | Yes | No | Yes | Yes | Yes | No |
| Open a script | Yes | No | Yes | Yes | Yes | No |
| Delete a script | Yes | No | No | No | No | No |

## Data sources actions

Data sources actions by space role in a managed space – Analyzer entitlement

| Action | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| List data file in the space | Yes | No | No | No | No | Yes |
| List data connection in the space  You also need a value of Allowed or Read for the Data connections permission. | Yes | No | No | No | No | Yes |
| Duplicate data files in the space | No | No | No | No | No | No |
| Move data files | No | No | No | No | No | No |
| Delete data file from the space | Yes | No | No | No | No | No |
| Delete data connection from the space  You also need a value of Allowed for the Data connections permission. | Yes | No | No | No | No | No |
| Profile data source | Yes | No | No | No | No | No |
| Edit and apply properties to data source in the space | Yes | No | No | No | No | No |
| Create application from data source | No | No | No | No | No | No |
| Open data connection or file for application reload  You also need a value of Allowed or Read for the Data connections permission. | Yes | No | No | No | No | Yes |
| Binary load from applications inside space | No | No | No | No | No | Yes |

## Data flow actions

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Publish or republish a data flow to this space | Yes | No | Yes | No | No | No | No | No |
| See all data flows in the space | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Open a data flow | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Delete a data flow | Yes | Yes | No | No | No | No | No | No |
| View | Yes | Yes | No | Yes | Yes | No | No | Yes |
| View run history | Yes | Yes | No | No | No | No | No | Yes |
| View lineage and impact analysis  You also need View lineage set to Allowed in the default permissions or a custom security role | Yes | Yes | No | Yes | Yes | No | No | Yes |
| Edit a data flow attributes | Yes | Yes | No | No | No | No | No | Yes |
| Reload a data flow and schedule reloads | Yes | Yes | No | No | No | No | No | Yes |

## Table recipe actions

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

## Qlik Predict — ML deployment actions

Information notePermissions related to using [prediction](#glossary-2 "Glossary term") data (for example, opening or profiling the dataset, or using it in an application) are generally the same as [*Data sources actions*](#DataSrcActions).

### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator before being able to perform these actions. These permissions are:

- Automl Deployment Contributor built-in security role
- Manage ML deployments permission (user)

If you cannot perform these actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for Qlik Predict, administrators can refer to [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

ML deployment prediction actions by space role in a managed space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Run [batch prediction](#glossary-3 "Glossary term") | Yes | No | No | No | No | No | No |
| Run prediction with real-time API endpoint | Yes | No | No | No | No | No | Yes |
| Run prediction with Qlik Predict analytics connector  You also need sufficient access to the space of the data connection:   - Shared space: Owner, Can manage, Can edit, or Can consume data - Managed space: Owner, Can manage, or Can consume data | Yes | No | No | No | No | No | Yes |

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

Business glossary actions by space role and user role in a managed space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- | --- |
| List glossaries in the space | Yes | Yes | No | Yes | Yes | Yes | No |
| Open a glossary (details page only) | Yes | Yes | No | Yes | Yes | Yes | No |
| View glossary and terms | Yes | Yes | No | Yes | Yes | Yes | No |
| Move glossary from this space | Yes | Yes | No | Yes | No | No | No |
| Move glossary to this space | Yes | Yes | No | Yes | No | No | No |
| Create a glossary | Yes | Yes | No | Yes | No | No | No |
| Edit glossary settings and page | Yes | Yes | No | Yes | No | No | No |
| Delete a glossary | Yes | Yes | No | Yes | No | No | No |
| Add a term in glossary | Yes | Yes | No | Yes | No | No | No |
| Edit term not in Verified state | Yes | Yes | No | Yes | No | No | No |
| Edit term in Verified state | Yes | Yes | No | Yes | No | No | No |
| Delete term not in Verified state | Yes | Yes | No | Yes | No | No | No |
| Delete term in Verified state | Yes | Yes | No | Yes | No | No | No |
| Change state of a term to/from Verified | Yes | Yes | No | Yes | No | No | No |
| Change state of a term between states other than Verified | Yes | Yes | No | Yes | No | No | No |
| Create, edit, delete categories | Yes | Yes | No | Yes | No | No | No |
| Can export glossaries and terms | Yes | Yes | No | Yes | Yes | Yes | No |

## Qlik Answers actions

Qlik Answers assistant actions by space role in a managed space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restrictive view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chat with an assistant | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Create new assistants | Yes | Yes | No | Yes | No | No | No | No |
| Move assistants to the space | Yes | Yes | No | Yes | No | No | No | No |
| Move assistants to another space | Yes | Yes | No | Yes | No | No | No | No |
| Open an assistant | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| Delete an assistant | Yes | Yes | No | Yes | No | No | No | No |
| Edit an assistant | Yes | Yes | No | Yes | No | No | No | No |
| Add and remove knowledge bases | Yes | Yes | No | Yes | No | No | No | No |
| Review answers and feedback  Information noteThis also requires the Audit Admin user role. | Yes | Yes | No | Yes | Yes | No | No | No |

Qlik Answers knowledge base actions by space role in a managed space – Analyzer entitlement

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

Qlik Answers skill actions by space role in a managed space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restrictive view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Upload skill | Yes | Yes | No | Yes | No | No | No | No |
| Move skills to the space | Yes | Yes | No | Yes | No | No | No | No |
| Move skills to other spaces | Yes | No | No | Yes | No | No | No | No |
| Open skills | Yes | Yes | No | Yes | Yes | No | No | No |
| Delete skills | Yes | Yes | No | Yes | No | No | No | No |
| Edit skill details | Yes | Yes | No | Yes | No | No | No | No |

## Notes actions

Notes actions by space role in a managed space – Analyzer entitlement

| Action | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Add notes | Yes | No | Yes | Yes | Yes | No |
| List all notes in the space  To view the contents of a note, the note must be shared with the user at the note level. Space members can access a note if the note has been shared with them individually. | Yes | No | No | No | No | No |
| Delete notes in the space  The note owner can also delete the note. | Yes | No | No | No | No | No |

## Discovery Agent actions

### Prerequisites

In addition to required space roles, you may also need to be assigned or more permissions by a tenant administrator before being able to perform Discovery Agent actions. In particular, you might need one or more of the following:

- Insight triggers
- Insights feed

For a list of all permission requirements for the Discovery Agent, administrators can refer to [*Administering Discovery Agent*](../DiscoveryAgent/discovery-agent-admin.htm).

Discovery Agent actions by role in managed spaces – Analyzer users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Create and manage [insight triggers](#glossary-4 "Glossary term") in the application | No | No | No | No | No | No | No | No |
| View [insight triggers](#glossary-5 "Glossary term") in the application | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| View insights from the application in your feed | Yes | Yes | No | Yes | Yes | Yes | No | Yes |

## Other content actions

Other content actions by space role in a managed space – Analyzer entitlement

| Action | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create, edit, and delete generic links | Yes | No | No | No | No | No |
