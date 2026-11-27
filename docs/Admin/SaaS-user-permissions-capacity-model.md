---
title: "Permissions granted by security roles"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-user-permissions-capacity-model.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - Capacity-based subscriptions", "Roles and permissions for users and administrators"]
---

# Permissions granted by security roles

A security role grants a set of permissions to all users who have been assigned the role. When a user is assigned to more than one role, they are granted the permissions from each role. Permissions define what a user can see and do in Qlik Cloud.

Information note

This topic is applicable to the Standard, Premium, and Enterprise editions of Qlik Cloud Analytics and Qlik Talend Data Integration. If you have a Qlik Sense Enterprise SaaS, Qlik Sense Business, or Qlik Cloud Government subscription, see [*Managing users - User-based subscriptions*](SaaS-user-management.htm).

Security roles control actions and access rights for users and administrators in the tenant. In addition to the tenant-level security roles, there are also space roles that control user actions on content within spaces. For more information about the different types of roles, see [*Roles and permissions for users and administrators*](permissions-admins-users-capacity-model.htm).

You can assign the following security roles.

Security roles

| Role | Type | Permissions | Access granted with role |
| --- | --- | --- | --- |
| Tenant Admin | Administrator | An administrator with full permissions to manage and administer all aspects of the tenant. | Access to the Administration activity center from the navigation menu |
| Analytics Admin | Administrator | An administrator with limited permissions to manage only some areas of governance and content. | Access to the Administration activity center from the navigation menu |
| Audit Admin | Administrator | An administrator with limited permissions, including:   - Access to events and data from the Natural Language API (the Manage API keys permission is also needed). - Review user conversations with [Qlik Answers](#glossary-0 "Glossary term") [assistants](#glossary-1 "Glossary term"). | Access to the Administration activity center from the navigation menu |
| Data Admin | Administrator | Administrator with limited permissions to manage only data spaces. | Access to the Administration activity center from the navigation menu |
| Data Space Creator | User | A user who can create [data spaces](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataSpaces/working-spaces.htm). | Create data space option in the Home page in the Qlik Talend Data Integration activity center. |
| Managed Space Creator | User | A user who can create [managed spaces](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/working-in-managed-spaces.htm). | Space option in the Create page of the Analytics activity center |
| Shared Space Creator | User | A user who can create [shared spaces](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/working-in-shared-spaces.htm). | Space option in the Create page of the Analytics activity center |
| Data Services Contributor | User | A user who has access to Data Integration services | Access to the Qlik Talend Data Integration activity center from the navigation menu |
| Private Analytics Content Creator | User | A user who can create private analytics content. | Personal space option in the Space list when adding new content |
| Warning triangle Automation Creator (deprecated) | User | A user who can create private automations. | Automation option in the Create page of the Analytics activity center. |
| Collaboration Platform User | User | A user who can communicate with Qlik Cloud through external collaboration platforms. | Can add external environments and use these environments to communicate with their Qlik Cloud applications. |
| Steward | User | A user who can:  - In Analytics: create, update, and delete a glossary, and approve, edit, and delete terms. - Create, read, update, and delete validation rules. | Glossary option in the Create page of the Analytics activity center.  Validation rules tab in Data Quality. |
| Data Product Manager | User | A user who can create, read, update, delete and activate data products, and manage semantic types and validation rules. | Data products menu. |
| Embedded Analytics User | User | A user who can only access applications directly in embedded use cases. They are blocked from accessing activity centers and other interfaces, except if they also have an administrator role. | This role restricts access to all other parts of Qlik Cloud. |
| Automl Experiment Contributor | User | A user who can view, create, use, and manage ML experiments. They can also deploy models trained within an experiment into ML deployments. | Ability to view ML resources. Full access to using ML experiments. |
| Automl Deployment Contributor | User | A user who can view, create, use, and manage ML deployments. They can also view the ML experiments in a space, if they have the required permission in the space. | Ability to view ML resources. Full access to using ML deployments. |

Information noteDeprecated role: The Automation Creator role is deprecated and it will be removed in a future release. Avoid assigning it to users or groups. To replace it, use the Private automations permission in the default permissions or create a custom role. For more information, see [*Managing custom roles*](permissions-custom-roles-capacity-model.htm).

## Permissions for tenant administrators

Users who are assigned the Tenant Admin role have broad permissions to manage a tenant. This includes managing users, access control, and tenant configuration.

For certain actions, the tenant administrator needs additional permissions. For example:

- You need a custom role that includes the Manage API keys permission to create API keys, and you need to be a member of a space to access data and applications in that space.
- Data connections:

  - To move a data connection to your personal space, you need the built-in Private Analytics Content Creator role and the Data connections permission set to Allowed.
  - To move a data connection to a shared, managed, or data space, you and the data connection owner need the required space roles in the target space, as well as the Data connections permission set to Allowed.
  - For changing owner of a data connection, you and the new connection owner need the required space roles in the space.
  - To open data connections for application reload, you also need the Read value for the Data connections permission.

  See [*Managing data connections for administrators*](mc-administer-data-connections.htm).

Tenant administrators are the only administrators that can take ownership of and delete other users' personal content. Tenant admins cannot export applications from other users' personal spaces, but they can take ownership of these applications and then export them. See: [*Changing owner of applications*](mc-administer-apps.htm#Changing2) and [*Downloading applications*](../Apps/export-apps-cloud-hub.htm).

The table lists the permitted actions on content in other users' personal spaces.

Tenant Admin permissions on content in other users' personal spaces

| Resources | Permissions |
| --- | --- |
| Applications | List, Open, Delete, Change owner |
| Data connections | List, Move (change space), Change owner, Delete, Open (for application reload) |
| Data files | List, Open, Create, Change owner, Edit, Move (change space), Delete, Read |
| ML experiments | List, Open, Delete |
| ML deployments | List, Open, Delete, Move (change space), Approve deployed models |
| Knowledge bases | List, Open, Delete |
| Assistants | List, Open, Delete |

Information noteA tenant administrator cannot delete their own Tenant Admin role.

Warning note

Anyone assigned the Tenant Admin role may be granted access to content, including personal content, relating to all users within the tenant to which the Tenant Admin role is assigned.

## Permissions for analytics administrators

Users who are assigned the Analytics Admin role are administrators with limited permissions. They have access to parts of the Administration activity center, such as managing shared and managed spaces, extensions, and themes.

Analytics administrators cannot manage users in the Manage users section of the Administration activity center. They can manage space members in space types that they are allowed to manage.

Analytics administrators can manage user resources for analytics services within shared and managed spaces. They cannot access content in other users' personal spaces. This includes applications, data files, data assets, and data connections.

The tables list the permissions that are granted by this role.

Analytics Admin permissions

| Resources | Permissions |
| --- | --- |
| Shared spaces | Create, Read, Update, Delete |
| Managed spaces | Create, Read, Update, Delete |
| Automations | Enable, Disable, List, Delete, Change owner |
| Extensions | Create, Read, Update, Delete |
| Themes | Create, Read, Update, Delete |
| Sharing service task | Create, Read, Update, Delete |

Analytics Admin permissions on content in shared and managed spaces

| Resources | Permissions |
| --- | --- |
| Applications | List, Delete |
| Generic links | Create, Read, Update, Delete |
| Data sets | Read, Delete |
| Data assets | Read, Delete |
| REST data files | List, Delete |
| Data connections | List, Delete |
| Assistants | Read, List, Delete |
| Knowledge bases | Read, List, Delete |

## Permissions for data administrators

Users who are assigned the Data Admin role are administrators with limited permissions for [data spaces](#glossary-2 "Glossary term") and data resources within those spaces. In the Administration activity center, they can access only the areas for which they have permissions.

Data administrators cannot manage users in the Manage users section of the Administration activity center. They can manage space members in space types that they are allowed to manage.

Data administrators cannot access content in other users' personal spaces.

The tables list the permissions that are granted by this role.

Data Admin permissions

| Resources | Permissions |
| --- | --- |
| Data space | Create, Read, Update, Delete |

Data Admin permissions on content in data spaces

| Resources | Permissions |
| --- | --- |
| Data sets | List, Read, Delete |
| Data assets | List, Read, Delete |
| Resource connections | List, Create, Read, Update, Delete |
| Data stores | List, Read, Delete |

## Permissions for audit administrators

Users who are assigned the Audit Admin role can:

- Access application feedback and usage information captured as part of the Natural Language API (requires the Manage API keys permission).
- Access and view conversations in [Qlik Answers](#glossary-3 "Glossary term") [assistants](#glossary-4 "Glossary term") to review feedback.

### Application feedback and usage

With the addition of the Manage API keys permission, an audit administrator can view a variety of usage metrics for [Insight Advisor](#glossary-5 "Glossary term") and [Insight Advisor Chat](#glossary-6 "Glossary term") captured as a part of the Natural Language API.
This API enables evaluation of patterns in user interactions with applications, including feedback provided for analyses generated by Insight Advisor and Insight Advisor Chat. This information can be used to improve user experience through adjustments to the application, either within the data or in the business logic of the application.

This API only returns application information from shared and managed spaces. An audit administrator does not have access to usage metrics data for personal spaces.

To view the usage metrics of an application, an audit administrator must also be assigned one of the following space roles in the space where the application is located.

Roles in shared spaces:

- Owner
- Can manage
- Can edit
- Can view

Roles in managed spaces:

- Is owner
- Can manage
- Can contribute
- Can view
- Has restricted view

Information note

The Natural Language API does not check section access controls in the application's load script. If an audit administrator has the Manage API keys permission and can open applications (as provided through the space permissions), they can view the application usage metrics.

For more information about how Insight Advisor user interaction data can be used to improve application usability, see [*Using feedback and usage metrics to improve application usability*](../Insights/insight-advisor-usage-metrics.htm). For specifics about the Natural Language API, see [Natural language](https://qlik.dev/apis/rest/natural-language), and for a tutorial on using the Natural Language API, see [Collect and share Insight Advisor feedback](https://qlik.dev/tutorials/collect-and-share-insight-advisor-feedback).

The table lists the permissions that are granted by this role.

Audit Admin permissions

| Resources | Permissions |
| --- | --- |
| Audit | Read |
| Filter action of the Natural Language API | Read |

### Qlik Answers

With Qlik Answers, audit administrators can view and review conversations users have had with individual assistants. They can view the feedback left by users as well as the sources used by the assistants. For more information, see [*Reviewing assistant conversations*](../QlikAnswers/Assistants/reviewing-assistant-conversations.htm).

Information noteTo review conversations from Qlik Answers agentic experiences in Answers review portal, users need a custom role with the Agentic AI > Review agent and chat interactions permission set to Allowed. For more information, see [*Reviewing conversations from Qlik Answers agentic experiences*](../QlikAnswers/reviewing-with-answers-review-portal.htm).

To view Qlik Answers conversations, audit administrators require the View assistants permission. In addition, they must be also assigned one of the following space roles in space where the assistant is located:

Roles in shared spaces:

- Owner
- Can manage
- Can edit

Roles in managed spaces:

- Is owner
- Can manage
- Can contribute
- Can view

The table lists the permissions that are granted by this role.

Audit Admin permissions

| Resources | Permissions |
| --- | --- |
| Assistant-audit | Read, Audit |

## Permissions for space creators

Users with one of the space creator roles have the permission to create a space of that type from the Create page in the Analytics activity center.

The table lists the permissions that are granted by the roles.

Data Space Creator permissions

| Resources | Permissions |
| --- | --- |
| Data spaces | Create |

Managed Space Creator permissions

| Resources | Permissions |
| --- | --- |
| Managed spaces | Create |

Shared Space Creator permissions

| Resources | Permissions |
| --- | --- |
| Shared spaces | Create |

For new tenants, the Shared Space Creator role is automatically assigned to all users by default.

To turn off this automatic role assignment:

1. In the Administration activity center, go to Manage users > Permissions.
2. Toggle off Auto assign for the role.

For more information about the settings, see [*Assigning security roles and custom roles to everyone in the tenant*](SaaS-roles-capacity-model.htm#Assignin).

## Permissions for private analytics content creators

Users with the Private Analytics Content Creator role can create analytics content in [personal spaces](#glossary-7 "Glossary term"). Users without this role can still create monitored [charts](#glossary-8 "Glossary term"), alerts, subscriptions, and [notes](#glossary-9 "Glossary term") in their personal space.

The table lists the permissions that are granted by this role on resources in personal spaces.

Private Analytics Content Creator permissions

| Resources | Permissions |
| --- | --- |
| Qlik Sense applications | Create, Duplicate, Import, Source |
| QlikView applications | Duplicate, Import, Source |
| Data connections | Create, Update, Change space  You also need a value of Allowed for the Data connections tenant-wide role to perform these actions. |
| Data files | Create, Update |
| Data sets | Create, Update, Profile |

Note that tenant administrators must also have the Private Analytics Content Creator role to perform the actions in the table.

For new tenants, the Private Analytics Content Creator role is automatically assigned to all users by default.

To turn off this automatic role assignment:

1. In the Administration activity center, go to Manage users > Permissions.
2. Toggle off Auto assign for the role.

For more information about the settings, see [*Assigning security roles and custom roles to everyone in the tenant*](SaaS-roles-capacity-model.htm#Assignin).

As you can see in the table above, this role does not control all actions on the resources. If you remove the role from a user who has analytics content in their personal space, the user can still use that content. Any already existing [data connections](#glossary-10 "Glossary term") and data files can be selected and used, and scripts can be updated and reloaded.

If a scheduled reload task, that has a binary load or store in the script and is located in a personal space, stops working, the user of the personal space needs to log in. By logging in, the Private Analytics Content Creator role is automatically assigned to the user, which solves the reload issue.

## Permissions for automation creators

Information noteDeprecated role: The Automation Creator role is deprecated and it will be removed in a future release. Avoid assigning it to users or groups. To replace it, use the Private automations permission in the default permissions or create a custom role. For more information, see [*Managing custom roles*](permissions-custom-roles-capacity-model.htm).

Users with the Automation Creator role can create automations in personal spaces.

The table lists the permissions that are granted by this role.

Automation creator permissions

| Resources | Permissions |
| --- | --- |
| Qlik Automate | Create, Update, Run, Enable, Disable, Duplicate |

## Permissions for collaboration platform users

Users with the Collaboration Platform User role in the tenant can interact with the Insight Advisor Chat service in external collaboration platforms.

The Collaboration Platform User role is assigned on an opt-in basis, meaning that tenant administrators must assign the role to specific users who need it. The Auto assign option is off by default for this user role. Tenant administrators can turn on this automatic role assignment by toggling the option on under Manage users > Permissions in the Administration activity center. See:

- [*Assigning security roles and custom roles to everyone in the tenant*](SaaS-roles-capacity-model.htm#Assignin) (capacity-based subscriptions)
- [*Assigning security roles and custom roles to everyone in the tenant*](SaaS-roles.htm#Assignin) (user-based subscriptions)
- [*Assigning security roles and custom roles to everyone in the tenant*](SaaS-roles-anonymous.htm#Assignin) (Qlik Anonymous Access subscriptions)

## Permissions for data services contributors

You need the Data Services Contributor role to work with Qlik Cloud Data Integration. Users with this role can access the Qlik Cloud Data Integration home by selecting Data Integration from the navigation menu ![Navigation menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg).

The table lists the permissions that are granted by this role.

Data Services Contributor permissions

| Resources | Permissions |
| --- | --- |
| Data services | Read |

For new tenants, the Data Services Contributor role is automatically assigned to all users by default.

To turn off this automatic role assignment:

1. In the Administration activity center, go to Manage users > Permissions.
2. Toggle off Auto assign for the role.

For more information about the settings, see [*Assigning security roles and custom roles to everyone in the tenant*](SaaS-roles-capacity-model.htm#Assignin).

## Permissions for stewards

With the Steward role, you can:

- In Analytics: create, update, and delete a glossary as well as edit or delete a term in Verified state or change the term status to Verified. In addition to the Steward role, you must also be assigned the Can edit space role in the space where the glossary is located.
- In Analytics and Data Integration: create, read, update, and delete validation rules.

The table lists the permissions that are granted by this role.

Steward permissions

| Application | Resources | Permissions |
| --- | --- | --- |
| Analytics | Business glossaries | Create, Read, Update, Delete |
| Analytics | Glossary terms | Change status |
| Analytics, Data Integration | Validation rules | Create, Read, Update, Delete |

For new tenants, the Steward role is automatically assigned to all users by default. Tenant administrators can turn off this automatic role assignment by toggling off the Auto assign option under Manage users > Permissions in the Administration activity center. See [*Assigning security roles and custom roles to everyone in the tenant*](SaaS-roles-capacity-model.htm#Assignin).

## Permissions for data product managers

With the Data Product Manager role, you can work with data products and manage semantic types and validation rules.

The table lists the permissions that are granted by this role:

Data Product Manager permissions

| Resources | Permissions |
| --- | --- |
| Data products | Create, Read, Update, Delete, Activate |
| Semantic types | Create, Read, Update, Delete |
| Validation rules | Create, Read, Update, Delete |

For more information, see [*Working with data products*](../DataIntegration/DataProducts/Data-products.htm).

## Permissions for embedded analytics users

The Embedded Analytics User role is a limiting user role. This role provides access to applications and application content while blocking access to all other parts of Qlik Cloud, such as the Qlik Cloud Analytics activity centers, Automations, Data Integration, and personal settings. However, if a user has both an administrator role and the Embedded Analytics User role, these restrictions do not apply. The user will still have full access.

Users with the Embedded Analytics User role can access applications and sheets via direct links, for example, in embedded use cases. What the user is permitted to do with applications is based on the user's other security roles and space roles.

The Embedded Analytics User role is disabled for all users by default. Tenant administrators can turn on automatic assignment of the role to all users by toggling on the Auto assign option under Manage users > Permissions in the Administration activity center. See [*Assigning security roles and custom roles to everyone in the tenant*](SaaS-roles-capacity-model.htm#Assignin).

## Permissions for ML experiment contributors

The Automl Experiment Contributor role allows a user to work with ML experiments. With this role, you can create and manage ML experiments. You can also create ML deployments from models trained in an experiment, and view the ML deployments in a space where you have the required permissions.

Note that to work with ML experiments, you must meet all other user requirements as well. For a list of requirements for working with Qlik Predict, see [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

The table lists the permissions that are granted by this role.

Automl Experiment Contributor permissions

| Resources | Permissions |
| --- | --- |
| ML experiments | Read, Create, Update, Delete, Move |
| ML deployments | Read, Create |

This role is automatically assigned to all users by default. Tenant administrators can turn off this automatic role assignment by toggling off the Auto assign option under Manage users > Permissions in the Administration activity center. See [*Assigning security roles and custom roles to everyone in the tenant*](SaaS-roles-capacity-model.htm#Assignin).

## Permissions for ML deployment contributors

The Automl Experiment Contributor role allows a user to work with ML deployments. With this role, you can create and manage ML deployments. You can also view the ML experiments in a space where you have the required permissions.

Note that to work with ML experiments, you must meet all other user requirements as well. For a list of requirements for working with Qlik Predict, see [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

The table lists the permissions that are granted by this role.

Automl Deployment Contributor permissions

| Resources | Permissions |
| --- | --- |
| ML experiments | Read |
| ML deployments | Read, Create, Edit, Delete, Move, Run (use in predictions) |

This role is automatically assigned to all users by default. Tenant administrators can turn off this automatic role assignment by toggling off the Auto assign option under Manage users > Permissions in the Administration activity center. See [*Assigning security roles and custom roles to everyone in the tenant*](SaaS-roles-capacity-model.htm#Assignin).
