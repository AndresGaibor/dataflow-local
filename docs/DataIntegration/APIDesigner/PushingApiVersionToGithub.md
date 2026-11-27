---
title: "Pushing an API version to GitHub"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/PushingApiVersionToGithub.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts"]
---

# Pushing an API version to GitHub

Link your API to a GitHub repository and push your API definition in OAS/Swagger or RAML.

- You have a GitHub account and a repository.
- Your browser is supported by GitHub (since Internet Explorer 11
  is no longer supported by GitHub, this feature is not supported by API Contracts for IE11).

1. If your GitHub account is not linked to your API Contracts
   account yet, go to the API Contracts settings.
2. Click Link your GitHub account.

   ![GitHub account section in API Contracts settings.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/link-your-github-account.png)
3. In the window that opens, sign in to GitHub and click Authorize Talend to allow API Contracts to
   access your GitHub account.

   Information noteWarning: If you are using Internet Explorer 11, you will be prompted to
   upgrade to the latest version of Microsoft Edge, Google Chrome or Firefox.

   Your GitHub account is now linked to your API Contracts
   account and you can start pushing your API definitions to GitHub.
4. Open the API version that you want to push to GitHub.
5. Click Link at the top-right corner.
6. In the Edit GitHub settings section, enable the option and
   edit the following fields:

   - Owner
   - Repository
   - Branch
   - Path
   - Format

   Information noteNote: If your API has
   several versions, each version can have different GitHub settings.

   ![Edit GitHub settings section of the API Settings view.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/push_to_github_01_link.png)
7. Once your settings are saved, click Push.

   A green dot appears to the right of Push when your project
   contains changes that have not been pushed to GitHub.![Screenshot of the project when it contains changes that have not been pushed to GitHub.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/push_to_github_03_push.png)
8. Enter a commit message and a tag if needed, then click
   Push.

   A tag should be unique and should follow these rules:
   - It can contain only alphanumeric characters and the
     following special characters: \_,
     -, . and /.
   - It cannot start or end with a special character.
   - It cannot contain the following character patterns:
     .., // and /..

The selected version of your API
definition is pushed to your repository. The name of the file generated contains the
name of the API and the version.

You can click View on GitHub to open the selected
repository.
