---
source: https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-offline-snapshots-m2m-tutorial/
last_updated: 2026-06-17T14:20:40Z
---

# Offline analytics snapshot embedding with qlik-embed and OAuth M2M

## Overview

This tutorial shows how to configure and run a web app that fetches and displays analytics snapshots using qlik-embed,
the `analytics/snapshot` UI, and OAuth machine-to-machine (M2M) authentication.

> **Notes:**
>
> - This tutorial is based on version [v1.0.0](https://github.com/qlik-oss/qlik-cloud-embed-snapshot/tree/v1.0.0) of the project repository.
> - **This project is not production-ready**. It is intended for learning and evaluating Qlik Cloud API access and artifact handling with a simple Node.js backend.
> - For a production app:
>   - Review the [Machine-to-Machine OAuth2 client applications documentation](https://qlik.dev/authenticate/oauth/#machine-to-machine-oauth2-client-applications).
>   - Never expose client secrets in frontend code.
>   - Use HTTPS rather than HTTP.

This project leverages the [Sharing tasks API](https://qlik.dev/apis/rest/sharing-tasks/) and OAuth M2M to securely list
chart-monitoring tasks and download their snapshot artifacts.
It demonstrates:

- Listing Qlik Sense chart-monitoring tasks, using the Sharing tasks API.
- Downloading and saving snapshot artifacts (images, JSON) to the backend.
- Serving minimal snapshot metadata to the frontend for display.
- Keeping monitoring charts active to prevent expiration by accessing them
  before they reach 90 days of inactivity.

> **Important: Monitoring charts are disabled after 90 days of inactivity:** Monitoring charts are automatically disabled and no longer updated if they are not viewed or accessed for 90
> consecutive days. To keep your monitoring charts active and continuously refreshed, the project regularly fetches
> snapshots from the Sharing tasks API. This automated refresh prevents deactivation and ensures your charts remain
> available.

## How the web app works

The web app operates in two modes:

- Fresh snapshot retrieval:
  When you click **Refresh snapshots from Qlik Cloud**, the backend authenticates using OAuth M2M, retrieves
  chart-monitoring tasks, downloads the latest snapshot artifacts, and saves them in `public/snapshots/`.
  These are then served to users without requiring authentication.

- Local snapshot serving:
  Previously downloaded snapshots are served from local storage, enabling fast loading, offline access, and reduced API
  calls to Qlik Cloud.

Snapshots can be displayed in two modes:

- Image mode: Static PNG images for fast loading.
- Interactive mode: Full qlik-embed snapshots with limited interactivity.

## What you'll learn

By the end of this step-by-step tutorial, you'll have:

- Fetched and displayed analytics snapshots in your web app.
- Configured OAuth M2M authentication for secure backend API access.
- Deployed a working example of a Node.js backend serving analytics snapshots.

## Prerequisites

- [Node.js](https://nodejs.org) version 22 or higher.
- A Qlik Cloud tenant with chart-monitoring tasks and available analytics snapshots.
- An [OAuth M2M client](https://qlik.dev/authenticate/oauth/create/create-oauth-client/) with scope `user_default` and allowed origins
  set to `http://localhost:3000`.

## Step 1: Set up your local project

In this step, you'll set up a local development environment by cloning the GitHub repository or downloading the project
files.

### Method 1: Create a repository from the template

1. Go to [GitHub repository](https://github.com/qlik-oss/qlik-cloud-embed-snapshot/tree/v1.0.0) for this template.
2. Click **Use this template**.
3. Follow the instructions to create a new repository from this template.
4. Clone your newly created repository:
   ```shell
   git clone <your-repo-url>
   ```

### Method 2: Download and extract the project files

Alternatively, you can download and extract the project files.

1. On the project's [GitHub page](https://github.com/qlik-oss/qlik-cloud-embed-snapshot), click **Code**.
2. Select **Download ZIP**.
3. Extract the content of the ZIP file in the folder of your choice.

## Step 2: Configure environment variables

In this step, you'll configure environment variables to securely store sensitive information and connect to the right
resources.

1. Rename the `template.env` file to `.env`.
2. Edit the `.env` file with values that match your Qlik Cloud deployment:

- `QLIK_M2M_CLIENT_ID` and `QLIK_M2M_CLIENT_SECRET`: Specify the credentials obtained when you created the OAuth M2M
  client in the Administration activity center.
- `QLIK_TENANT_URL`: Specify the hostname of your Qlik Cloud tenant, such as `z29kgagw312sl0g.eu.qlikcloud.com`.

> **Note:** Keep these secrets safe as they provide wide access to your tenant.

## Step 3: Install dependencies and run the app

Now that the project is configured, you can install the required dependencies and run the app locally to view the
embedded analytics snapshots.

1. Open a terminal window and navigate to the folder containing the project files you cloned or extracted.

   ```shell
   cd <project-folder>
   ```

2. Install the project dependencies.

   ```shell
   npm install
   ```

3. Start the server.

   ```shell
   npm start
   ```

4. Open `http://localhost:3000` in your browser.

You should see your web app running locally, displaying available analytics snapshots from your Qlik Cloud tenant.
Selecting a snapshot will display its images and metadata.

![Screenshot of a web app displaying embedded analytics snapshots](https://qlik.dev/_astro/qlik-embed-snapshot-tutorial.DfghQAZ7.png)

## Troubleshooting

- If the app does not load, verify the environment variable values configured in [step 2](#step-2-configure-environment-variables)
  and review any error messages in the terminal.
- If you get authorization errors, verify the scopes and credentials for your OAuth M2M client.
- Ensure your Qlik Cloud tenant has chart-monitoring tasks with available analytics snapshots.

## Next steps

You now have a working web application that lets you retrieve, store, and display analytics snapshots offline in your
browser using qlik-embed and the `analytics/snapshot` UI.

To enhance and extend your solution, consider the following next steps:

- Add more analytics snapshot details or visualizations to the frontend.
- Deploy your backend and frontend behind HTTPS and test end-to-end.
