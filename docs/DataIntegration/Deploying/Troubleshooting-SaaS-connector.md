---
title: "Troubleshooting SaaS application connector issues"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Deploying/Troubleshooting-SaaS-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Monitoring and operating your data tasks"]
---

# Troubleshooting SaaS application connector issues

In rare and complex cases when troubleshooting SaaS application connector issues, Qlik may need access to detailed debugging information to properly analyze the issue you are experiencing. Do not attempt to run Debug source connection unless you have been explicitly instructed to do so by a Qlik representative. This process will generate a password-protected file containing logs and data that we will ask you to share with Qlik to help with troubleshooting. Please follow the instructions in [*Collecting debug information*](#Collecti).

### Requirements

- You need View data permission in the space where the connection is located.
- You need to get a filter string from a Qlik representative. This filter string is required during the troubleshooting process.
- The task must be in Stopped status with scheduling turned off.

### Collecting debug information

Warning noteThis procedure can take a very long time to complete. During this time you cannot run or prepare the task.

1. In the task, click ... and then Debug source connection.
2. Enter the filter string that you have received from your Qlik representative and click Run.

   The debug operation will start running. The task will now be in debug mode with status In progress. You cannot run, prepare, or schedule the task in debug mode..

   When it is finished, the status of the task is Completed.

   You can abort the debug operation by clicking Abort. This will exit debug mode.
3. You can now download the logs by clicking Download logs.

   Make sure that you record the password that is displayed. This password is required to open the log file.

   Warning noteConsider how you are handling the downloaded log file, as well as the password, as the file may contain sensitive data.

   When the file is downloaded, the task exits debug mode.
4. Share the log file and the password with your Qlik representative.

You can exit debug mode by clicking Exit debug mode.

### Downloading the connection debug log file later

You can download the log file up to three days after it was created. The log file can only be downloaded by the user that initiated the debug operation.

1. Click View task logs in the task menu.
2. Click Download.
3. Select Connection debug log.
4. Click Download.

Make sure that you record the password that is displayed. This password is required to open the log file.

Warning noteConsider how you are handling the downloaded log file, as well as the password, as the file may contain sensitive data.
