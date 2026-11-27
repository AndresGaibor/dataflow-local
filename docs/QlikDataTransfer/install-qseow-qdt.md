---
title: "Installing Qlik Sense Enterprise on Windows on a server with Qlik DataTransfer installed"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikDataTransfer/install-qseow-qdt.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing data governance and transfers", "Installing Qlik DataTransfer"]
---

# Installing Qlik Sense Enterprise on Windows on a server with Qlik DataTransfer installed

You can install Qlik Sense Enterprise on Windows on a server that already has Qlik DataTransfer installed.

Do the following:

1. In Windows Services, stop the Qlik DataTransfer service.
2. Navigate to C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate and delete the certificates in the folder.
3. Navigate to C:\Program Files\Qlik\DataTransfer\DataUploadService\install-utils.
4. Run Remove-Certificate.ps1 in PowerShell as administrator
5. In the Windows Certificate Store, please verify that the following certificates are removed:

   - Local Computer > Personal > QdtClient
   - Local Computer > Trusted Root Certification Authority > <hostname.domain> or <hostname>
   - Current user > Personal > QdtClient
6. Install Qlik Sense Enterprise on Windows.

   [Installing Qlik Sense Enterprise on Windows](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Deploy_QSEoW/installing-qlik-sense-enterprise-on-windows.htm)
7. Navigate to C:\Program Files\Qlik\DataTransfer\DataUploadService\install-utils.
8. Run Configure-Service.ps1 in PowerShell as the Qlik Sense services user.

   1. For the first input dataTransferCertificatePath, enter C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate.
   2. For the second input qsefwPresent, enter Yes.
9. Navigate to C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate and confirm the following files are present:

   - root.pfx
   - client.pfx
   - server.pfx
10. Start the Qlik DataTransfer service
