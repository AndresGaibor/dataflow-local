---
title: "Unlinking your GitHub account"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/UnlinkingGithubAccount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "Pushing an API version to GitHub"]
---

# Unlinking your GitHub account

To disable the link to your GitHub account, you need to unlink your account from API Contracts and revoke the access token from GitHub.

1. Click Open API settings next to the repository.
2. Click Unlink your GitHub account.

   ![Screenshot of the GitHub account section in the API Contracts settings.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/unlink_github_01_designer_unlink.png)

Your account is now unlinked. The token
used to access your repositories is removed from the Talend database and from GitHub. If needed, you can link a different
account.
