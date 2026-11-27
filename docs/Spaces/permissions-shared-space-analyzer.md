---
title: "Shared space permissions for users with Analyzer entitlement"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/permissions-shared-space-analyzer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces", "Working in shared spaces", "Managing permissions in shared spaces"]
---

# Shared space permissions for users with Analyzer entitlement

This help topic contains tables outlining what members with Analyzer entitlement can do in a [shared space](#glossary-0 "Glossary term").

For more information about managing permissions in shared spaces, including special considerations, see [*Managing permissions in shared spaces*](managing-shared-spaces.htm).

## Application actions

### Application actions – General

General application actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Export applications in the space | Yes | Yes | Yes | Yes | No | No |
| Publish or republish applications from this space  If the application being published is in a shared space, you also need the Can edit space role or higher in that shared space in order to publish the application. | Yes | Yes | Yes | Yes | No | No |
| Share applications in the space with non-space members | Yes | Yes | No | No | No | No |
| Remove application-only access to applications from non-space members | Yes | Yes | No | No | No | No |
| Move applications to the space | Yes | Yes | Yes | Yes | No | No |
| Move applications to another space | Yes | Yes | Yes | Yes | No | No |
| Open an application | Yes | Yes | Yes | Yes | Yes | No |
| Delete an application | Yes | Yes | Yes | Yes | No | No |
| Edit application attributes (change name, description, and tags) | No | No | No | No | No | No |
| Edit application properties (select theme, enable right-to-left reading order, set a bookmark as application default, and sheet title styling) | No | No | No | No | No | No |
| Approve application access requests | Yes | Yes | No | No | No | No |

### Application actions – Sheets, storytelling, and visualizations

Sheets, storytelling, and visualizations actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| View, create, edit, and delete media library content | No | No | No | No | No | No |
| Paste copied visualizations onto private sheets | No | No | No | No | No | No |
| Paste copied sheets in the application | No | No | No | No | No | No |
| Add private sheets to the application | Yes | Yes | Yes | Yes | No | No |
| Add private bookmarks and stories to the application | Yes | Yes | Yes | Yes | Yes | No |
| Update and delete your own private sheets, bookmarks, and stories | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Take snapshots in the application | Yes | Yes | Yes | Yes | Yes | No |
| View on-demand application navigation links | Yes | Yes | Yes | Yes | Yes | No |
| Open on-demand selection applications | Yes | Yes | Yes | Yes | Yes | No |
| Generate on-demand applications | Yes | Yes | Yes | Yes | Yes | No |
| Create dynamic views | Yes | Yes | Yes | Yes | No | No |
| Add dynamic charts to sheets | Yes | Yes | Yes | Yes | No | No |
| Monitor a visualization in your personal space | Yes | Yes | Yes | Yes | Yes | No |
| Share a visualization to monitor in the shared space | Yes | Yes | Yes | Yes | No | No |
| Create links to sheets | Yes | Yes | No | No | No | No |
| View write tables and make changes to their editable columns | Yes | Yes | Yes | Yes | No | No |

### Application actions – Augmented analytics

#### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator to perform Insight Advisor and Insight Advisor Chat actions. If you cannot perform these actions and you have the needed space roles, contact your administrator.

Augmented analytics actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Use Insight Advisor in an application | Yes | Yes | Yes | Yes | Yes | No |
| Access an application via Insight Advisor Chat | Yes | Yes | Yes | Yes | Yes | No |
| Search for application fields in Insight Advisor Chat | Yes | Yes | Yes | Yes | No | No |
| Search for application master items in Insight Advisor Chat | Yes | Yes | Yes | Yes | Yes | No |
| Toggle Insight Advisor Chat and key driver analysis on and off | Yes | Yes | Yes | Yes | No | No |
| Create, edit, rerun, view, and delete key driver analyses | Yes | Yes | Yes | Yes | Yes | No |

Information noteThe presence of a logical model associated with an application can result in outcomes which differ from those shown above for Insight Advisor and Insight Advisor Chat. Logical model documentation should be referenced in these scenarios.

### Application actions – Notes

You can add notes to the space when you are viewing an application.

Application notes actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Add notes | Yes | Yes | Yes | Yes | Yes | No |
| List all notes in the space  To view the contents of a note, the note must be shared with the user at the note level. Space members can access a note if the note has been shared with them. | Yes | Yes | No | No | No | No |
| Delete notes in the space  The note owner can also delete the note. | Yes | Yes | No | No | No | No |

### Application actions – Subscriptions and alerts

Subscriptions and alerts actions by space role in a shared space – Analyzer entitlement

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

Reporting actions by space role in a shared space – Analyzer entitlement

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

## Data sources actions

Data sources actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| List and use data connection in the space | Yes | Yes | Yes | Yes | No | Yes |
| List and use data file in the space | Yes | Yes | Yes | Yes | No | Yes |
| Delete data connection from the space  You also need a value of Allowed for the Data connections permission. | Yes | Yes | Yes | Yes | No | No |
| Delete data file from the space | Yes | Yes | Yes | Yes | No | No |
| Edit your own credentials for connections with User defined credentials  You also need a value of Read or Allowed for the Data connections permission. | Yes | Yes | Yes | Yes | No | No |
| Profile data source | Yes | Yes | Yes | Yes | No | No |
| Edit and apply properties to data source in the space | Yes | Yes | Yes | Yes | No | No |
| Create application from data source | Yes | Yes | Yes | Yes | No | No |
| Open data connection for application reload  You also need a value of Allowed or Read for the Data connections permission. | Yes | Yes | Yes | Yes | No | Yes |
| Open data file for application reload | Yes | Yes | Yes | Yes | No | Yes |
| Binary load from applications inside space | Yes | Yes | Yes | Yes | No | Yes |

## Automation actions

Automation actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| List and use automations in the space | Yes | Yes | Yes | Yes | No | No |
| Create automations in the space | Yes | Yes | Yes | Yes | No | No |
| Delete automations from the space | Yes | Yes | Yes | Yes | No | No |
| Edit automations in the space | Yes - If user owns the automation | Yes - If user owns the automation | Yes - If user owns the automation | Yes - If user owns the automation | No | No |
| Enable or disable automations in the space | Yes | Yes | Yes | Yes | No | No |
| Duplicate automations in the space | Yes | Yes | Yes | Yes | No | No |
| Create automation using automation connection | Yes | Yes | Yes | Yes | No | No |

## Automation connections actions

Automation connections actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| List and use automation connections in the space | Yes | Yes | Yes | Yes | No | Yes |
| Create automation connection in the space | Yes | Yes | Yes | Yes | No | No |
| Delete automation connection from the space | Yes | Yes | Yes | Yes | No | No |
| Edit automation connection in the space | Yes - If user owns the connection | Yes - If user owns the connection | Yes - If user owns the connection | Yes - If user owns the connection | No | No |
| Create automation using automation connection | Yes | Yes | Yes | Yes | No | Yes |

## Data flow actions

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

## Qlik Predict — ML deployment actions

Users with Analyzer entitlement cannot view or work with ML experiments. They have a limited set of permissions for ML deployments.

Information notePermissions related to using [prediction](#glossary-1 "Glossary term") data (for example, opening or profiling the dataset, or using it in an application) are generally the same as [*Data sources actions*](#DataSrcActions).

### Prerequisites

In addition to required space roles, you may need to be assigned one or more permissions by a tenant administrator before being able to perform these actions. These permissions are:

- Automl Deployment Contributor built-in security role
- Manage ML deployments permission (user)

If you cannot perform these actions and you have the needed space roles, contact your administrator.

For a list of all permission requirements for Qlik Predict, administrators can refer to [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

ML deployment prediction actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Run [batch prediction](#glossary-2 "Glossary term") | Yes | No | No | No | No | Yes |
| Run prediction with real-time API endpoint | Yes | No | No | No | No | Yes |
| Run prediction with Qlik Predict analytics connector  You also need sufficient access to the space of the data connection:   - Shared space: Owner, Can manage, Can edit, or Can consume data - Managed space: Owner, Can manage, or Can consume data | Yes | No | No | No | No | Yes |

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

Business glossary actions by space role and user role in a shared space – Analyzer entitlement

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

Notes actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Add notes to the space | Yes | Yes | Yes | Yes | Yes | No |
| List all notes in the space  To view the contents of a note, the note must be shared with the user at the note level. Space members can access a note if the note has been shared with them. | Yes | Yes | No | No | No | No |
| Delete notes in the space  The note owner can also delete the note. | Yes | Yes | No | No | No | No |

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

### Prerequisites

In addition to required space roles, you may also need to be assigned or more permissions by a tenant administrator before being able to perform Discovery Agent actions. In particular, you might need one or more of the following:

- Insight triggers
- Insights feed

For a list of all permission requirements for the Discovery Agent, administrators can refer to [*Administering Discovery Agent*](../DiscoveryAgent/discovery-agent-admin.htm).

Discovery Agent actions by role in shared spaces – Analyzer users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create and manage [insight triggers](#glossary-3 "Glossary term") in the application | Yes | Yes | Yes | Yes | No | No |
| View [insight triggers](#glossary-4 "Glossary term") in the application | Yes | Yes | Yes | Yes | No | No |
| View insights from the application in your feed | Yes | Yes | Yes | Yes | Yes | No |

## Other content actions

Other content actions by space role in a shared space – Analyzer entitlement

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create, edit, and delete generic links | Yes | Yes | No | No | No | No |
