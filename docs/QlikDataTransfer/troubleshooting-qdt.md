---
title: "Troubleshooting Qlik DataTransfer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikDataTransfer/troubleshooting-qdt.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics", "Uploading on-premises data with Qlik DataTransfer"]
---

# Troubleshooting Qlik DataTransfer

This section describes problems that can occur when using Qlik DataTransfer.

## Qlik DataTransfer opens to a white screen

I open Qlik DataTransfer, but it only displays a white screen. If I check Services in Windows, Qlik DataTransfer is shown as running.

Possible cause

There may be one or more of the following issues.

- The client certificate is not available from C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate
- The server certificate is not available from C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate
- Certificates are invalid.
- Certificate chain is invalid.
- Certificates are not present in the Windows Certificate Store.

Proposed action

If only Qlik DataTransfer is installed on the machine, do the following:

1. In Windows Services, stop the Qlik DataTransfer service.
2. Navigate to C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate and delete the certificates there.
3. Navigate to C:\Program Files\Qlik\DataTransfer\DataUploadService\install-utils.
4. Run Remove-Certificate.ps1 in PowerShell.
5. Start the Qlik DataTransfer service.
6. Navigate to C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate and confirm the following files are present:

   - client.pfx
   - server.pfx

If Qlik DataTransfer and Qlik Sense Enterprise on Windows are installed on the machine, do the following:

1. In Windows, Services, stop the Qlik DataTransfer service.
2. Navigate to C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate and delete the certificates in the folder.
3. In the Windows Certificate Store, delete the following certificates:

   - Local Computer > Personal > QdtClient
   - Local Computer > Trusted Root Certification Authority > <hostname.domain> or <hostname>
   - Current user > Personal > QdtClient

   Alternatively, you can run Remove-Certificate.ps1 in PowerShell as the administrator.
4. Run Configure-Service.ps1 in PowerShell as the Qlik Sense services user.

   1. For the first input dataTransferCertificatePath, enter C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate.
   2. For the second input qsefwPresent, enter Yes.
5. Navigate to C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate and confirm the following files are present:

   - root.pfx
   - client.pfx
   - server.pfx
6. Restart the Qlik DataTransfer service.

## Qlik DataTransfer opens to a white screen and https://localhost:5505/ shows the error err\_ssl\_version\_or\_cipher\_mismatch

I open Qlik DataTransfer, but it only displays a white screen. If I check Services in Windows, Qlik DataTransfer is shown as running. If I go to https://localhost:5505/ in a browser, I get the error err\_ssl\_version\_or\_cipher\_mismatch.

Possible cause

The TLS cipher suite on your server is not supported by Qlik DataTransfer.

Proposed action

Add the TLS cipher suite in the server group policy by following the steps in the following support article: [Disabling Weak Cipher suites for TLS 1.2 in Qlik Sense Application](https://community.qlik.com/t5/Knowledge/Disabling-Weak-Cipher-suites-for-TLS-1-2-in-QlikSense/ta-p/1716891).

## Qlik DataTransfer is not running and the log shows there was an error executing a PowerShell script command

Qlik DataTransfer is not running. The log shows the following error message:

Error while executing powershell script command,Command failed: & "C:\Program
 Files\Qlik\DataTransfer\DataUploadService\install-utils\Remove-Certificate.ps1"
& : File C:\Program Files\Qlik\DataTransfer\DataUploadService\install-utils\Remove-Certificate.ps1 cannot be loaded
because running scripts is disabled on this system. For more information, see about\_Execution\_Policies at
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:3
+ & "C:\Program Files\Qlik\DataTransfer\DataUploadService\install-utils ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+ CategoryInfo : SecurityError: (:) [], PSSecurityException
+ FullyQualifiedErrorId : UnauthorizedAccess"

Possible cause

ExecutionPolicy is disabled or restricted for that user.

Proposed action

Enable or give permissions to execute PowerShell script by giving the user the RemoteSigned execution policy. You can do this from PowerShell in administrator mode by running PS C:\> Set-ExecutionPolicy RemoteSigned in PowerShell and selecting Y. You can contact your system administrator to do the same.

## I am experiencing high CPU usage from Qlik DataTransfer

Qlik DataTransfer is using a high amount of CPU.

Possible cause

There may be a shared folder configured as a data folder, Qlik DataTransfer may be polling on the folder, which uses more CPU.

Proposed action

Do one of the following:

- To stop polling, navigate to the services.conf file, located in %Program Files%\Qlik\DataTransfer. Open the file and remove --usePolling. This will discontinue watching a shared folder after the service is restarted.
- To poll at a greater interval, you can change the default polling interval from 100 milliseconds to a greater value, such as 3000 milliseconds. Navigate to the services.conf file, located in %Program Files%\Qlik\DataTransfer. Open the file and add --pollingInterval after --usePolling. Set the polling interval in milliseconds, for example --pollingInterval 3000.

## Qlik DataTransfer shows a blank page when installed on secondary nodes of Qlik Sense Enterprise on Windows cluster

Qlik DataTransfer has a blank page. Qlik Sense certificates are not exportable in a developer node.

Possible cause

Qlik DataTransfer was not installed on the central node.

Proposed action

Follow these step:

1. Perform the regular [installation](install-Qlik-DataTransfer.htm) steps.
2. In Windows Services, stop the Qlik DataTransfer service.
3. Navigate to C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate and delete the certificates in the folder.
4. In the Windows Certificate Store, delete the following certificates, if available:

   - Local Computer > Personal > QdtClient
   - Local Computer > Trusted Root Certification Authority > <hostname.domain> or <hostname>
   - Current User > Personal > QdtClient

Alternatively, you can run Remove-Certificate.ps1 (C:\Program Files\Qlik\DataTransfer\DataUploadService\install-utils) in PowerShell as the administrator.

5. Navigate to C:\Program Files\Qlik\DataTransfer\DataUploadService\install-utils.
6. Copy Configure-Service.ps1.
7. Log in to central node using Qlik Sense Enterprise on Windows service user account.
8. Paste this file to central node at any location.
9. Run Configure-Service.ps1 in PowerShell as the Qlik Sense services user.

1. For the first input dataTransferCertificatePath, enter any folder location on the machine. This will export certificates to this location.
2. For the second input qsefwPresent, enter Yes.

10. Navigate to location where certificates are exported and confirm the following files are present:

    1. root.pfx
    2. client.pfx
    3. server.pfx
11. Copy all three certificates.
12. Go to the Qlik DataTransfer installed machine.
13. Navigate to C:\ProgramData\Qlik\DataTransfer\DataUpload\certificate and paste all certificates.
14. Restart the Qlik DataTransfer service.
