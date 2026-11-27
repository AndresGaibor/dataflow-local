---
title: "Manage your pipeline projects with version control"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/VersionControl/Project-version-control.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project"]
---

# Manage your pipeline projects with version control

You can use version control to manage development of a pipeline project, and to keep track of changes.

Information noteVersion control is not available with a Qlik Talend Cloud Starter subscription.

When working with version control, you can commit versions of the projects during design. This allows you to see changes between two versions of the project. You can also develop your data projects using a branching strategy. This lets you work on an isolated version of the project in each work area, or branch. The work area can be shared by several users. You can then merge your changes from the work area to a main branch for deployment to production.

GitHub is used as provider for version control. The implementation follows the shared repository model.

- GitHub Enterprise Cloud and GitHub Enterprise Server are not supported.
- For more information about the shared repository model, see [About collaborative development models](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models).
- For more information about Git and GitHub, see [About GitHub and Git](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git).
- GitHub security considerations

  Qlik Talend Cloud supports the HTTPS security protocol and Personal Access Tokens (PAT), which is the default authentication mode for GitHub. For more information, see [About authentication to GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github).

## Getting started

- Create a user in GitHub that the tenant can use to access GitHub. This may already be created for you by an admin.

  The user must have the following scopes:

  - repo
  - read:org
  - read:user
  - read:project
- You need write access on the repositories you plan to change.
- You must create a GitHub personal access token (classic). Fine-grained personal access tokens are not supported.

  For more information, see GitHub documentation: [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
- Organization is mandatory in GitHub configuration.
- You need Can edit role in the space where the project resides to perform version control actions.
- Before you can start using version control, you must set up a configuration to connect to GitHub with the GitHub user that you created.

  [*Setting up configuration to GitHub*](#Set)
- When you have set up a connection to GitHub, you can connect a project to a repository.

  [*Connecting a project to a repository*](#Connecti)

## Setting up configuration to GitHub

All users that want to work with version control must set up a configuration to connect to GitHub using a GitHub user account.

GitHub connection

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qdi_version_github.png "Click to view full size")

You can configure GitHub in Pipeline projects, or in your user profile settings. Make sure that you have prepared according to [*Getting started*](#Getting).

To configure GitHub in Pipeline projects:

1. Click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GitHubConnector-square_26x26.png) and then GitHub configuration.
2. Set up authentication using your organization and the GitHub personal access token described in [*Getting started*](#Getting).
3. Click OK.

Information noteA connection of the type GitHub - Version Control will be created in your personal space. All users will have a personal version control connection, so it does not need to be managed.

You can now connect your projects to a repository.

## Connecting a project to a repository

You must connect a project with a repository before you can start using version control. Make sure that you have set up a connection to GitHub.

Connect a project to version control.

![Dropdown list with regions during tenant setup.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GitHub3-pointer.png "Click to view full size")

1. In Pipeline projects, click ... on a project and select Connect to version control.
2. Select which repository to associate the project with.
3. Add a base directory path.

   If you want to connect to an existing project in GitHub, you must use the same path.
4. You can select to commit the project and push the project to the remote repository after connection. Enter a commit message.

   If you do not commit and push, a main branch will be created in the work area, but not in the remote repository.
5. Click Connect.

The project is now connected to the selected repository. This is indicated at the bottom of the project card with ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GitHubConnector-square_26x26.png), the name of the repository, and the current branch.

When you open the project, the title row will now contain a GitHub menu with version control options. The project name will also be appended with the name of the current branch.

## Developing a project with version control

You can use version control with different approaches:

- Working directly on the main branch. This is mainly suitable for a single developer on a project who wants to keep track of changes, but can also be used by a group of developers that work in sync.
- Working with a branching strategy, where multiple developers can contribute. You can also create branches to isolate new features or changes from each other.

### Simplified workflow for a single-developer project

You can work directly on the main branch of a project. This approach is simpler and contains fewer operations, but still lets you keep track of changes. If there are more than one developer, they need to be careful to be in sync.

When you have made changes to the project that you want to apply, just make a Commit and Push.

### Workflow for a multi-developer project

This workflow can be used if there are more than one developer working on a project, or if you want to isolate changes. This involves creating a development branch that you can share with other users. With this workflow, the developers can keep track of each others changes, and decide when to merge the changes to the main branch.

Workflow for a multi-developer project with version control

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qdi_version_flow_multi.png "Click to view full size")

1. Create a new branch

   Create a new development branch from main branch. You can share the branch with more users.
2. Develop

   Make all required changes in the project.

   Information noteDatabase schemas and connections are not maintained in version control.
3. Apply remote changes

   Apply remote changes from another branch to your work area to make sure that you are up to date with changes from the other branch. This is helpful to avoid or mitigate conflicting changes.

   If you have two branches containing changes that may conflict, a workaround is to:

   1. Commit changes to both work areas.
   2. Merge both branches to main.
   3. Apply remote changes again.
4. Commit and push

   Commit and push your changes to the development branch. All objects will be pushed, so it is a good idea to validate your project before committing it.
5. Create a pull request and merge

   When you are ready with development, it is time to merge the changes from the work area to the main branch.

   You can create the pull request in the project version control, but the merge must be performed in GitHub where you can also set up approvals. For more information, see [GitHub Pull requests documentation](https://docs.github.com/en/pull-requests)

### Creating a new branch

1. In the project, click GitHub and select Create new branch.

   The project must be connected to version control. You must also have permission to the space where the target connection of the project resides.
2. Select to create a branch from the main branch.
3. Enter a name for the branch.
4. Set a prefix to be added to all schemas in the project in Branch prefix for all schemas. This allows all schemas to be uniquely named to avoid naming conflicts.
5. Click Create

A new branch is created from main, and checked out from the repository. The branch contains a new version of the project, with all tasks in status New. That is, they are not prepared and do not contain any data.

### Applying remote changes

You can apply changes from the remote repository to your work area. This could be changes created outside Qlik Cloud integrated version control, for example in GitHub or by other tools. This helps you to avoid conflicts when you want to commit and push your changes to the branch.

1. In the project, click GitHub and select Apply remote changes.

   The Apply remote changes to work area dialog is displayed if there are changes found.
2. You can now select which tasks to apply changes for and inspect the changes. For each change, you can select which version to use, the remote version or the version in your work area.

   Make any required changes for mapping connections that are different between the project and the imported project.

   For example, the imported project could be using a source connection named SQL1, while this project uses a similar connection named SQL2. In this case, map the imported connection to SQL2 in Set connections for the tasks added in the original version.

   If the changes include cross-project sources and the referenced project is under version control, a Branch selector is available for each cross-project source. Select the branch to consume. If the referenced project is not under version control, the branch selector is not shown.

   Information noteWhen selecting a connection to map, you can create a new database connection, but not a SaaS application connection.
3. Click Apply remote changes

You must add source connections and target connections if the changes include new data tasks.

Information noteIf you apply only selected tasks, you must take care to maintain the structural validity of the project. For example, if you apply a new Storage task, you must also apply the source Landing task. Adding the Landing dataset manually does not work.

### Committing and pushing

You can commit and push your changes to the branch. As remote changes that are not applied to your work area can be overwritten, you should perform Apply remote changes before committing and pushing.

1. In the project, click GitHub and select Commit and push.

   The Commit and push dialog is displayed if there are changes found.
2. Add a commit message that can help you keep track of what has changed.
3. Click Commit and push

### Creating a pull request

Create a pull request (PR) to merge to the changes from the work area to the main branch.

1. In the project, click GitHub on a project and select Create pull request.

   The Create pull request dialog is displayed.
2. Add a title and a description of the pull request.

   You can also select to open the pull request in GitHub after creation.
3. Click Create pull request.

You can now set up approvals for the pull request and perform the merge in GitHub.

Information noteYou can also select to create the pull request in GitHub if you need to use more advanced options.

### Deleting a branch

You can delete a branch when you have merged your changes to the main branch.

1. In the project, click on the branch to delete and select Delete branch.

   You can select to delete the remote branch in version control as well.

   If there are uncommitted changes you will need to confirm that these changes will be lost when deleting the branch.

## Removing version control for a project

You can disconnect your project from version control. If there are existing branches they must be deleted before you can disconnect the project.

1. In Pipeline projects, click ... on the project to disconnect and select Disconnect from GitHub.

## Importing a project from version control

You can import a project from version control, for example if you want to review another developer's project or collaborate on a project. Importing a project from version control also enables sharing a project with other spaces or tenants. You can share a version of a project with a different space on the same tenant, or on another tenant. This is useful when you want to create two environments, for example one for development, and one for production."

### Before importing a project

Before you start importing a project:

- Create all new connections that you will need if you are importing to a new tenant or space.
- If the project uses SaaS application connections that do not exist yet on the tenant or space, you must create the connections and generate metadata before you start importing.
- If you are importing a cross-project pipeline, you must import the upstream projects first.

### Importing a project

If the project consumes tasks from other projects, you must map projects and tasks unless names for spaces and projects are identical.

1. In Data Integration > Projects, click Create new and select Import project from version control.
2. Select the repository, and then select the branch.

   Select the base directory path if needed, and click Show projects.

   Select the project to import from the list.

   Click Next.
3. Set Project properties for the new project.

   You must select which space to add the project to in Space.

   In Data platform you can change the data platform of the project, and the connection to the data platform.

   Changing Connection is required if you imported a project from another tenant, or if you changed the data platform in the previous step.

   You can change the connection to the staging area. This is required if you imported a project from another tenant, or in some cases if you changed the data platform in the previous step.

   Click Next.
4. Set Default project settings for the new project.

   You can add a prefix to the data schemas that are created in the project in Prefix for all schemas. This is useful when the imported project is in the same cloud data warehouse as the exported project.

   You can also set a default name in Database name. For Snowflake projects you can set a default Data warehouse name, and for Databricks projects you can set a default Catalog name. You can use the project default name for all task types, or set the name to default or a custom name for each task type.

   Click Next.
5. Set Connections and task settings.

   You can replace the imported source connections or cross-project sources. This is required if you imported a project from another tenant.

   When mapping a cross-project source to a project that is under version control, a Branch selector is available. Select the branch of the referenced project to consume. If the referenced project is not under version control, the branch selector is not shown. If a cross-project source is mapped to a non-main branch, the branch name is shown in parentheses next to the project name.

   In Optional task settings you can also change task settings that were overridden in the original project.
6. When you are ready, click Import.

The project is added to Data Integration home.

### Working on a project imported from version control

You work the same way as with regular version-controlled projects, with a few differences:

- You can only switch to the main branch, or to another branch that was imported from version control.
- If you imported from a branch, the main branch will be empty.
- Deleting a project will not delete the remote version.

## Security considerations

Make sure that you maintain synchronized security configurations between Qlik Talend Data Integration and GitHub.

- In Qlik Talend Data Integration permissions are based on spaces that may contain several projects. In GitHub, permissions are based on repositories that may also contain several projects. Best practice is to align them and connect all projects in one space to the same repository.
- Keep in mind that Qlik Talend Data Integration and GitHub use different permissions and roles for users.

## Best practices

Here are some general best practices when working with projects using version control.

- Add a README file that describes the repository in GitHub. For more information, see [About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes).

  If you start with an empty repository, Qlik Talend Cloud version control will add an empty README.md file automatically.
- In general you should let Qlik Talend Cloud version control manage the GitHub repository.
- Commit only projects that are valid and tested to run.

  If you add projects with Landing or Registered data tasks that have not been prepared or transformed, the source columns are not yet included. Source columns are added when the task is prepared and transformed.
- When you create a branch for replication projects, you should be aware that the branches use the same target by default. This means that running tasks in the branch can override data of the main version. To avoid data loss, change the target settings in the branch not to conflict with the main version.
- When you create a branch, there may be remote changes that are not applied yet to the work area. Apply remote changes either before or after creating the branch, unless you want to discard the remote changes.
- Making changes to the same dataset in two different branches can result in merge conflicts that are hard to resolve and in recreation of the dataset.

  Information noteWhen a dataset is added to a task, it gets an internal identifier. Internal identifiers are used to allow for seamless renaming and other metadata operations in a pipeline. When creating the same dataset in a separate project or branch, the internal identifier will be different which may cause a conflict when merging the two branches. This may cause the prepare process to drop and recreate a dataset even if it has the same name.

### Working in branches

You can create a project, design it and when ready, deploy it to production using the MAIN branch. The version on MAIN corresponds to your production pipeline. You should never edit the MAIN branch directly beyond the first deployment.

Anytime a developer wants to make a new change in a project, such as adding a feature or correcting a bug, a new branch needs to be created.

Developers can create any number of branches for their development needs

- Use schema prefixes for branches to avoid database conflicts while making the changes.
- In a branch, developers can make any number of changes, and commit & push as many times as required. It is recommended to isolate each change in a self-contained, separate commit. For example, if you make a change to a transform task which also impacts the data mart, make sure to include both changes within a single commit
- All team members should use Apply remote changes at any time to make sure that their MAIN is up to date, especially before committing their changes.

When developers are done working in their branch, they can create a pull request for peer review.

Information noteCreating a pull request is required before you can use Apply remote changes and merge branch changes back to main.

After review and approval from other team members, you can merge the pull request with the MAIN version in GitHub .

Finally, use Apply remote changes in the project to pull the approved branch changes back to the MAIN branch (production).

Information noteAll team members should use Apply remote changes at any time to make sure that their MAIN is up to date.

### Working in spaces

For larger and critical deployments it is recommended to use dedicated spaces for development and production to isolate changes and ensure pipeline integrity. Use dedicated data connections for sources and target in each space.

- Production

  The MAIN branch reflects what is in production. This means that there is only one MAIN version of a project.

  The production is isolated in a dedicated data space, for example, PROD. Dedicated connections are assigned to the production space.

  No changes are made directly in the production space/MAIN branch. All changes are made in other spaces with dedicated connections, using branches.

  You can reuse the MAIN version of an existing project in GitHub. Create an empty project with the same name as the existing project in GitHub. This retrieves the latest available version on the MAIN branch to start editing.

  Users create a new branch, make their changes, create pull requests, merge, and pull back to MAIN/Production.
- Development

  Developers can isolate their changes in a dedicated data space, for example, DEV. Dedicated connections are assigned to the DEV space.

  Changes are isolated using branches, usually one branch per developer. Use schema prefixes when a branch is created to avoid database conflicts while making the changes.
- Review / quality acceptance

  Reviewers are granted access to development spaces and connections to:.

  - Open and test project branches in Qlik Talend Cloud.
  - Approve pull requests to proceed with merging in GitHub.
  - Inform team members when approved changes can be pulled back to MAIN/Production.

When deploying the approved changes back to the MAIN/Production space, you must re-assign connections to the production space connections.

## Declarative pipeline management

When version control is enabled, projects are stored in GitHub as YAML configuration files. You can export these files, edit them in an IDE, and re-import them to update the project. This declarative workflow supports code review, automated validation in CI/CD pipelines, and environment promotion using Git branching.

For more information, see [*Declarative pipelines*](../DeclarativePipelines/Declarative-pipelines-overview.htm).

## Limitations

- Version control is not supported for projects with Qlik Cloud (QVD) as target.
- It is not possible to disconnect or delete a project using version control if there are branches. The branches must be deleted before you can disconnect or delete the project.
- It is not possible to rename a project using version control.
- When you delete a tenant, objects stored with version control in GitHub will not be deleted. You need to delete these objects manually.
- if a repository is used by many projects, or contains many files that are not stored in Qlik Talend Data Integration, performance may degrade.
- Database schemas and connections are not maintained in version control.
- GitHub fine-grained personal access tokens are not supported.
- A branch (except the main branch) can be used by only one project per repository, even if two projects are in the same repository.
- It is not possible to apply remote changes from a project that uses a different target platform. For example, if you commit changes to a project on Snowflake, you cannot apply the changes to a Databricks project.
