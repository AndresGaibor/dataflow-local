---
title: "Uninstalling Qlik Sense Enterprise on Windows from a server with Qlik DataTransfer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikDataTransfer/uninstall-qseow-qdt.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing data governance and transfers", "Installing Qlik DataTransfer"]
---

# Uninstalling Qlik Sense Enterprise on Windows from a server with Qlik DataTransfer

You can uninstall Qlik Sense Enterprise on Windows from a server that also has Qlik DataTransfer while keeping Qlik DataTransfer.

Do the following:

1. In Windows Services, stop the Qlik DataTransfer service.
2. Navigate to C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate and delete any certificates in the folder.
3. Uninstall Qlik Sense Enterprise on Windows.

   [Uninstalling Qlik Sense](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Deploy_QSEoW/Uninstalling.htm)
4. Start the Qlik DataTransfer service.
5. Navigate to C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate and confirm the following files are present:

   - client.pfx
   - server.pfx
