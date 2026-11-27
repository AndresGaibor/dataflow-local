---
title: "Importing the transports via TMS"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Shared/Import_Transports_via_TMS.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP (Application)", "Prerequisites", "Install the Replicate for SAP Client on the SAP machine", "Importing the Replicate transports into the SAP system"]
---

# Importing the transports via TMS

Starting from R/3 version 4.0, SAP allows importing transports through the SAP system via transaction code STMS.

Information note

Security authorization in the SAP system must include proper access to import the transport request.

1. Sign-on to SAP system with a User ID that contains proper authority.
2. Execute transaction STMS.
3. Select the Transport (Truck) icon from the toolbar.
4. Select the desired system for import.
5. Add the Transport to the import queue by selecting the following path from the menu list:

   Extras > Other Requests > Add

   Add the transport request number to the proper import queue and execute. Re-authentication of the user.s SAP User ID is likely in order to complete the step.

   If an Information message is received that the "Transport request is invalid" check that the transport number was typed correctly. Otherwise, it may indicate a problem with the files. Verification of existence, location, permissions, or ownership may be needed.
6. Import the Transport request by selecting the transport number from the queue, and clicking the Import (Truck) icon from the toolbar. Set the target client to either `000’ or any other valid client within the system and execute with the truck icon. Once again, re-authentication of the SAP User ID may be necessary. The transport will execute in asynchronous mode; a record of success or failure can be found in the transport logs.
7. The system will return to the import queue screen, where the Transport results can be checked. Select the Logs icon from the toolbar, or follow the menu path:

   Request > Display > Logs

   Locate the source system and verify all relevant logs. For this transport there should be 5 logs:

   - DD Import
   - DD Activation
   - Import
   - Check Versions
   - ABAP/scrn. Generation

   All logs should display Ended OK (return code 0) or Ended with warning (return code 4). If any logs are missing, or display a return code of 8 or higher, follow the instructions in step 6 to re-import the transport.
