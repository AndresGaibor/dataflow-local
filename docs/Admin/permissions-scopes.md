---
title: "Default permissions and custom roles"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-scopes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - User-based subscriptions", "Roles and permissions for users and administrators"]
---

# Default permissions and custom roles

Expand/Collapse all

# Default permissions and custom roles

Default permissions and custom roles control permissions for users and administrators. Default permissions define a baseline for all users, while custom roles allow more specific permissions for selected users or groups. The table below lists all available settings, with additional details in the sections that follow.

Information note

This topic is applicable to Qlik Sense Enterprise SaaS, Qlik Sense Business, and Qlik Cloud Government. If you have a subscription for the Standard, Premium, or Enterprise edition of Qlik Cloud Analytics or Qlik Talend Data Integration, see [*Managing users - Capacity-based subscriptions*](SaaS-user-management-capacity-model.htm).

## Understanding default permissions

Default permissions provide a tenant-wide baseline of permissions for all users. Administrators can change these permissions by clicking Manage default permissions to remove certain permissions for everyone and restrict broad access.

## Understanding custom roles

Custom roles grant additional permissions to selected users or groups. To grant a permission only to specific users, first grant the permission through a custom role and assign the role to those users. Then, set the permission to Not allowed in Manage default permissions.

## Permission hierarchy

Default permissions and custom roles, along with built-in security roles, control user and administrator access at the tenant level. Additionally, space roles control user actions on content within specific spaces. For more information about the different types of roles, see [*Roles and permissions for users and administrators*](permissions-admins-users.htm).

## Permission settings

The following sections list the permissions available in the default permissions and custom roles.

For each permission in a custom role, the default setting is shown, for example, (Default) Not allowed. This indicates the permission level that applies when the custom role does not override the default setting.

When a permission is Allowed by default, the Not allowed option is not available for that permission in a custom role. Custom roles can only grant additional permissions. They cannot remove permissions that are allowed by default.

### Permission settings — Content types

The Content types section contains permissions to take action on different content types. These are user permissions.

Permission settings — Content types

Permission settings — Content types section

| Subsection | Permission | Options |
| --- | --- | --- |
| Applications | Activate Qlik Answers for applications | Allowed: Users can activate Qlik Answers for applications and view AI readiness details and scores.  Not allowed: Users cannot activate Qlik Answers for applications or view AI readiness details and scores.  Information noteAlthough this permission is allowed by default, we recommend that you set it to Not allowed in the default permissions and create a custom role with it set to Allowed. Assign the custom role to the specific users who should be able to activate Qlik Answers for applications and optimize applications for AI. |
| Applications | Share applications via fine-grained access control | Allowed: Space owners and users with the Can manage role can share individual applications with users or groups without adding them to the space.  Not allowed: Users can only share the entire space, not individual applications. |
| Applications | Manage engine assignments for applications | Allowed: Users can assign an engine size to applications, overriding the default automatic engine selection.  Not allowed: Users cannot override the automatic engine selection.  For more information, see [*Assigning engines to improve application performance*](../Apps/app-performance-select-engine.htm). |
| Applications | In-app content download | No data: Users can only download images and PDFs. Data downloads are not permitted.  Allowed: Users can download all types of application content.  Not allowed: Application content downloads are not permitted. |
| Applications | Use GeoOperations | Allowed: Users can use all GeoOperations functions.  No geocoding: Users can use all GeoOperations functions, except for Address to point lookup and Point to address lookup.  Not allowed: Users cannot use GeoOperations. |
| Applications | Manage write table charts | Allowed: Users have full access to write table functionality, including chart configuration, making changes in editable columns, and access to the change-stores API.  Read and write access only: Users can view and interact with write tables in applications. They can make changes in editable columns added to the write table. Users cannot create write table charts or edit existing write table chart configurations, and cannot use API keys to extract changes from the change-stores API.  Not allowed: Users cannot view or make changes in editable columns within write tables. They also cannot create write tables or edit existing write table configurations, and they are not granted access to the change-stores API.  For more information, see [*Setting permissions for write tables*](write-table-permissions-capacity.htm). |
| Applications | Generate all reports | Allowed: Users can configure and generate all types of reports available with value-add capabilities of the Qlik Reporting Service.  On-demand reports: Users can only configure and generate reports using on-demand reporting and the Qlik Reporting Service API.  Not allowed: Users cannot work with any value-add capabilities of the Qlik Reporting Service.  For more information, see [*Setting permissions for metered reporting features*](mc-permissions-reporting.htm). |
| Applications | Insight triggers | Allowed: Users can create, manage, and view [insight triggers](#glossary-0 "Glossary term").  Not allowed: Users cannot create or manage insight triggers. They can view insight triggers. |
| Assistants | Manage assistants | Allowed: Users can create and manage assistants.  Not allowed: Users cannot access assistants. |
| Automations | Private Automations | Allowed: Users have access to private automations.  Not allowed: Users do not have access to private automations. Admins can set the permission to Not allowed in the default permissions, and create custom roles to provide access to specific users or groups. |
| Automations | Shared Automations | Allowed: Users have access to shared automations.  Not allowed: Users do not have access to shared automations. Admins can set the permission to Not allowed in the default permissions, and create custom roles to provide access to specific users or groups. |
| Data content | Data connections | Allowed: Users can list, create, view, update, and delete data connections. Users can also read data from, and store data to, these connections.  Read: Users can view data connections, select and load data from connections, and store data to data connections.  Not allowed: Users cannot create, view, update, or delete data connections. Users also cannot read data from, or store data to, these connections.  For more information, see [*Assigning permissions for users to work with data connections*](mc-administer-data-connections.htm#Permissions). |
| Data products | Manage data products | Consume only: Users have access to the Data marketplace.  Allowed: Users can view, create, update, activate, and delete data products on the Data marketplace.  Not allowed: Users cannot access data products on the Data marketplace. |
| Glossaries | Manage glossaries and approve terms | Allowed: Users can list, create, view, and delete glossaries. In glossaries, Users can read, create, edit, and remove terms. Users can verify terms.  Read and collaborate on terms only: Users can read, create, edit, and remove glossary terms.  Manage only: Users can list, create, view, and delete glossaries, but cannot change terms. In glossaries, Users can read, create, edit, and remove terms.  Not allowed: Users have no access to glossaries and their terms. |
| Knowledge bases | Manage knowledge bases | Allowed: Users can create, manage, index, and search knowledge bases.  Not allowed: Users cannot access knowledge bases in Qlik Cloud. |
| Knowledge bases | Index knowledge bases | Allowed: Users can index knowledge bases and create a reindexing schedule.  Not allowed: Users cannot index knowledge bases. |
| Knowledge bases | Search knowledge bases | Allowed: Users can search knowledge bases when asking questions of Qlik Answers assistants.  Not allowed: Users cannot search knowledge bases. |
| Lineage | View lineage | Allowed: Users can view lineage and impact analysis between assets.  Not allowed: Users cannot view lineage and impact analysis between assets. |
| Links | Manage links | Allowed: Users can view, create, update, and use links in the Analytics activity center. They can delete links that they created.  Not allowed: Users cannot view or work with links in the Analytics activity center.  For more information, see [*Who can create links*](mc-administer-generic-links.htm#Permissions). |
| ML experiments and deployments | Manage ML deployments | Allowed: Users can view, manage, and delete, and run predictions with ML deployments. With sufficient permissions for the ML experiment, they can also deploy models to ML deployments. Additionally, users can view ML experiments.  Run predictions only: Users can run predictions from ML deployments using the real-time predictions endpoint in the Machine Learning API or the Qlik Predict analytics connector. Other access to ML deployments, such as [batch predictions](#glossary-1 "Glossary term") and ML model management, is blocked.  Not allowed: Users cannot view, manage, delete, or run predictions with ML deployments. They also cannot deploy models to ML deployments.  [*Manage ML deployments*](../AutoML/who-can-work-with-automl.htm#ManageDeployments) |
| ML experiments and deployments | Manage ML experiments | Allowed: Users can view, create, manage, and delete ML experiments, including in-product access to GenAI for bias detection feature recommendations. They can also deploy models from experiments into ML deployments.  Manage ML experiments without GenAI: Users can view, create, manage, and delete ML experiments. They can also deploy models from experiments into ML deployments. They are blocked from using GenAI functionality in experiments—that is, using GenAI to recommend features for bias detection.  Not allowed: Users cannot view, create, manage, or delete ML experiments.  [*Manage ML experiments*](../AutoML/who-can-work-with-automl.htm#ManageExperiments) |
| ML experiments and deployments | Approve or reject your ML models | Allowed: From any ML deployment they can access, users can activate and deactivate predictions for the source model.  Not allowed: From any ML deployment they can access, users cannot activate or deactivate predictions for the source model.  For more information about model approval by non-administrators, see [*Approving deployed models*](../AutoML/approve-models.htm). |
| Notes | Manage notes | Allowed: Users can create, view, update, delete, and share [notes](#glossary-2 "Glossary term") in activity centers and applications.  Not allowed: Users cannot create, view, update, delete, or share notes in activity centers and applications.  For more information, see [*Enabling note creation*](mc-managing-notes.htm). |
| Pipeline projects | Create, update, or view pipeline projects based on space access | Read only: Users can view and list pipeline projects based on space access.  Allowed: Users can create, update, or view pipeline projects based on space access.  Not allowed: Users cannot create, update, or view pipeline projects. |
| Reporting | Generate all reports | Allowed: Users can configure and generate all types of reports available with value-add capabilities of the Qlik Reporting Service.  On-demand reports: Users can only configure and generate reports using on-demand reporting and the Qlik Reporting Service API.  Not allowed: Users cannot work with any value-add capabilities of the Qlik Reporting Service.  For more information, see [*Setting permissions for metered reporting features*](mc-permissions-reporting.htm). |
| Skills | Manage skills | Allowed: Users can upload and manage skills.  Not allowed: Users cannot upload or manage skills. |

### Permission settings — Features and actions

The Features and actions section contains permissions for tenant-wide access to special features and actions. These are user permissions.

Permission settings — Features and actions

Permission settings — Features and actions section

| Subsection | Permission | Options |
| --- | --- | --- |
| Agentic AI | Data analysis | Allowed: Users can use application analysis and Answers assistants within the Qlik Answers agentic chat from Answers.  Not allowed: Users cannot access application analysis or Answers assistants from the Qlik Answers agentic chat. If they have the permissions, they can use the experience with legacy assistants. |
| Agentic AI | Data governance | Allowed: Users can interact with data governance in the Qlik Answers agentic chat.  Not allowed: Users cannot interact with data governance in the Qlik Answers agentic chat. |
| Agentic AI | Insights feed | Allowed: Users can view insights in feeds.  Not allowed: Users cannot view insights in feeds. |
| Agentic AI | Qlik product help | Allowed: Users can access the Help agent.  Not allowed: Users cannot access the Help agent. |
| Agentic AI | Review agent and chat interactions | Allowed: Users can access the review portal and Feedback in agentic assistants to view conversations from Qlik Answers agentic experiences.  Not allowed: Users cannot access the review portal or view Feedback in agentic assistants. |
| Data quality | AI-based descriptions and suggestions | Allowed: Users can generate AI-based validation rules for datasets, and descriptions for any resources.  Not allowed: Users cannot generate AI-based validation rules, descriptions or suggestions. |
| Data quality | Compute data quality | Read: Users can view the results of the data quality computation.  Allowed: Users can compute data quality and view the results.  Not allowed: Users cannot compute data quality. |
| Data quality | Manage validation rules | Apply only: Users can list and view validation rules (depending on their license), and apply rules on datasets.  Allowed: Users can view, create, update, and delete validation rules on a space.  Not allowed: Users cannot view validation rules. |
| Data quality | Assign classifications and regulations | Allowed: Users can assign classifications and regulations on datasets, and view assigned classifications and regulations.  Not allowed: Users cannot assign classifications and regulations, and cannot view assigned classifications and regulations. |
| Data quality | Manage semantic types | Assign only: Users can list and view semantic types (depending on their license), and apply semantic types on datasets.  Allowed: Users can view, create, update, and delete semantic types. No space role is needed.  Not allowed: Users cannot view semantic types. |
| Data quality | Configure Qlik Trust Score™ | Allowed: Users can configure the Qlik Trust Score™ dimensions at the tenant level, view the score and its history.  Not allowed: Users cannot configure, or view the Qlik Trust Score™. |
| Developer | Manage API keys | Allowed: Users can create, view, update, and delete their own API keys in their personal settings.  Not allowed: Users cannot create or manage API keys. |
| Model Context Protocol (MCP) | MCP | Allowed: Users can use Qlik MCP server.  Not allowed: Users cannot use Qlik MCP server. |
| Insight Advisor | Data analysis | Allowed: Users can access Insight Advisor in all forms within Qlik Cloud. In other words, users can access Insight Advisor and Insight Advisor Chat from activity centers and applications.  Not allowed: Users cannot access Insight Advisor with in Qlik Cloud. In other words, users cannot access Insight Advisor or Insight Advisor Chat from activity centers or applications. |
| Insight Advisor | Insight Advisor in Microsoft Teams | Allowed: Users can access Insight Advisor Chat from Microsoft Teams.  Not allowed: Users cannot access Insight Advisor Chat from Microsoft Teams. |
| Mobile | Native mobile app | Allowed: Users can access the Qlik Analytics app.  Allowed with Intune: Users can access the Qlik Analytics mobile app with enforced MSAL authentication. MSAL cannot be disabled by users. Enables Intune MAM data protection policies.  Not allowed: Users cannot access the Qlik Analytics app.  For more information, see [*Setting access to the Qlik Analytics mobile app*](mobile-set-access.htm) and [*Securing and configuring the Qlik Analytics mobile app with Microsoft Intune*](configure-mobile-app.htm). |
| Feature preview | Activate feature preview | Allowed: Users can activate and deactivate preview features.  Not allowed: Users can view available preview features but cannot activate or deactivate them.  For more information, see [*Managing feature preview for your tenant*](mc-manage-preview-features.htm). |
| Space management | Request access to content | Allowed: Users can request access to content through the standard Qlik process.  Not allowed: Users cannot request access. You can customize the message shown when they try to access content to guide them to your organization's process.  For more information, see [*Customizing the access request process*](configure-access-request-message.htm) and [*Approving access requests*](../Share/approving-access-requests.htm). |
| Webhooks | Use webhooks | Allowed: Users can create, update, delete, and list their own webhooks using the webhooks API and automations UI.  Not allowed: Users cannot manage webhooks.  For more information, see [*Working with webhooks*](../../Sense_QlikAutomation/working-with-automations/working-with-webhooks.htm). |
| Learn | Access learning | Allowed: Can access the learning center.  Not allowed: Cannot access the learning center.  For more information, see [*Getting started and learning options*](../../Global_Common/HelpSites/get-started-qlik-cloud.htm). |

### Permission settings — Admin permissions

The Admin permissions section contains permissions for administrators of the Qlik Cloud tenant.

Permission settings — Admin permissions

Permission settings — Admin permissions section

| Subsection | Permission | Options |
| --- | --- | --- |
| Automations | Tenant Admin Automations | Allowed: Users can list, enable, disable, change the space, change the owner, manage automation settings, list and delete connections, list users, and delete automations.  Not allowed: Users can only manage their own automations. |
| Add-ons | Manage extensions | Allowed: Users can upload and manage extensions.  Not allowed: Users cannot upload or manage extensions. |
| Add-ons | Manage themes | Allowed: Users can upload and manage themes.  Not allowed: Users cannot upload or manage themes. |
| ML experiments and deployments | Approve or reject ML models | Allowed: In the Administration activity center, users can activate and deactivate predictions for any deployed model in the tenant. From any ML deployment they can access, users can also activate and deactivate predictions for the source model.  Not allowed: In the Administration activity center, users cannot activate or deactivate predictions for any deployed model in the tenant. However, users can activate and deactivate predictions for the source model from any ML deployment they have access to.  For more information about model approval by administrators, see [*Working with model approval as an administrator*](mc-approve-models-admin.htm). |
| ML experiments and deployments | Manage ML experiments and deployments | Allowed: Users can list, open, and delete any experiment or deployment. Users can also activate and deactivate predictions for any deployed model via the Administration activity center.  Not allowed: Users cannot list or delete experiments or deployments, or activate and deactivate deployed models. They cannot access the Qlik Predict section of the Administration activity center.  [*Manage ML experiments and deployments*](../AutoML/who-can-work-with-automl.htm#ManageExpDepl) |
| Content Security Policy (CSP) | Admin CSP | Allowed: Users can create, update, read, list, and delete content security policies.  Not allowed: Users cannot manage content security policies.  [*Managing Content Security Policy (CSP)*](mc-administer-content-security-policy.htm) |
| Curate content | Custom home | Allowed: Can customize the Insights Home page for all users.  Not allowed: Can only customize their own home pages.  For more information, see [*Customizing the Insights activity center Home*](mc-administer-customized-home.htm). |
| Curate content | Public collections | Allowed: Can set any collection in the tenant to public or private.  Not allowed: Cannot set any collection in the tenant to public or private.  For more information, see [*Managing public collections*](public-collections.htm). |
| Data products | Administer data products | Allowed: Users can access and manage all data products without space restrictions.  Not allowed: Users cannot manage data products. |
| Data quality | Administer AI-based descriptions and suggestions | Allowed: Users can manage tenant settings for generating AI-based descriptions for any resources and any validation rule suggestions for datasets. They can access and manage AI generations without space restrictions.  Not allowed: Users cannot manage AI generation settings. |
| Data quality | Administer semantic types | Allowed: Users can access and manage all semantic types.  Not allowed: Users cannot manage semantic types. |
| Data quality | Administer validation rules | Allowed: Users can access and manage all validation rules without space restrictions.  Not allowed: Users cannot manage validation rules. |
| Direct Access Gateway | Delete Direct Access gateway | Allowed: Users can clean up gateways registered through the automatic registration process. This action is for cleaning up gateways on the gateway machine rather than in Qlik Cloud.  Not allowed: Users cannot clean up gateways registered through the automatic registration process. This action is for cleaning up gateways on the gateway machine rather than in Qlik Cloud.  For more information about automatic gateway registration, see [*Option 2: Automatic registration using the command line*](../Gateways/direct-access-gateway-setting-up.htm#StageAuto). |
| Direct Access Gateway | Register Direct Access gateway | Allowed: Users can register Direct Access gateways.  Not allowed: Users cannot register Direct Access gateways.  For more information about automatic gateway registration, see [*Option 2: Automatic registration using the command line*](../Gateways/direct-access-gateway-setting-up.htm#StageAuto). |
| Pipeline projects | Read, delete, list, or change owner of all pipeline projects in the tenant for admin. | Allowed: Users can read, delete, list, or change owner of all pipeline projects in the tenant. Not allowed: Users cannot manage pipeline projects. |

## 'In-application content download' permission: Additional details

The value assigned to a user for the In-app content download permission can impact their access to other Qlik Cloud features. The following sections breaks down the difference between each of the available options.

### No data

The following apply for the No data option:

- Allows the user to add static charts to a [report template](#glossary-3 "Glossary term") using Qlik add-ins for Microsoft Office.
- Provides full access to Insight Advisor Chat when it is accessed through Qlik Cloud or an external collaboration platform (for example, Microsoft Teams).

### Allowed

The following apply for the Allowed option:

- Allows the user to add static charts to a report template using Qlik add-ins for Microsoft Office.
- Provides full access to Insight Advisor Chat when it is accessed through Qlik Cloud or an external collaboration platform (for example, Microsoft Teams).

### Not allowed

The following apply for the Not allowed option:

- The user cannot add static charts to a report template using Qlik add-ins for Microsoft Office.
- The user will not see static charts in Insight Advisor Chat. The user will also not be able to see any visualizations when using Insight Advisor Chat through a collaboration platform (for example, Microsoft Teams). All other Insight Advisor Chat capabilities, such as natural language insights, will be available.
