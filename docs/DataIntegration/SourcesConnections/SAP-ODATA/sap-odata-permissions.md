---
title: "Required permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-ODATA/sap-odata-permissions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP OData"]
---

# Required permissions

To use SAP OData as a source, the following permissions are required:

## OData user authorizations

To use a single SAP Gateway framework or application services, the user role needs to have the corresponding authorizations. The proposals can be found in transaction SU22.

In the SAP Gateway hub system, the repository objects are R3TR IWSG and R3TR IWOM.

In the SAP Business Suite backend system, all authorizations are collected in the repository object R3TR IWSV.

In addition to the authorizations maintained in the SU22 proposal, the role needs to have the authorization object S\_SERVICE assigned with the following specifications. This is a service allowing exploration of the framework or application services exposed by the SAP Gateway framework.

| Type of Application: | TADIR Service |
| --- | --- |
| Program ID: | R3TR |
| Object Type: | IWSG or IWSV |
| Object Name: | /IWFND/SG\_MED\_CATALOG |

For more information, see [Roles in the SAP Gateway Landscape](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/4a/5d22518bc72214e10000000a44176d/frameset.htm).

To add OData services to the role:

1. Call transaction PFCG and create a single role.
2. Assign the authorization defaults of SAP Gateway Business Suite Enablement - Service: as follows:
   1. On the Menu tab, select Authorization Default from the Transaction menu.

      A new window opens.
   2. From the Authorization Default drop-down list, select SAP Gateway: Service Groups Metadata (R3TR IWSG).
   3. In TADIR Service, assign the following services required for catalog read:

      /IWFND/SG\_MED\_CATALOG\_0001

      /IWFND/SG\_MED\_CATALOG\_0002
   4. Add the required OData service(s) metadata.
      Specify the service name with ‘\*’ at the end to find the service with a version number. Click Copy.
   5. From the Authorization Default drop-down list, select SAP Gateway Business Suite Enablement – Service (R3TR IWSV).
   6. In TADIR Service, select and assign the required service(s). Specify the service name with ‘\*’ at the end to find the service with a version number. Click Copy.
   7. Verify the result.

      Each service should now have two entries:

      R3TR IWSG (for service metadata)

      R3TR IWSV (for the service itself)

      The catalog should include the following entries:

      /IWFND/SG\_MED\_CATALOG\_0001

      /IWFND/SG\_MED\_CATALOG\_0002
3. Save the settings and then generate an authorization profile.
4. Assign the role to the communication user for Qlik Talend Data Integration.

### Authorizations required by ODP

SAP regularly updates the required authorizations for ODP. To ensure you have the latest information, please refer to SAP Note 2855052 – "Authorizations required for ODP Data Replication API 2.0". This note provides the current list of roles and authorization objects necessary for ODP functionality.

### Other

| Authorization object | Field name | Value | Activity |
| --- | --- | --- | --- |
| S\_ADMI\_FCD | S\_ADMI\_FCD | PADM, ST22 |  |
| S\_ADT\_RES | URI | /sap/bc/adt/\* |  |
| S\_DEVELOP | OBJTYPE | DEBUG, ST22 | 03 |
| S\_TCODE | TCD | ST22 |  |
| S\_BTCH\_ADM | BTCADMIN | Y |  |
| S\_BTCH\_JOB | JOBACTION | RELE |  |
|  | JOBGROUP | \* |  |
| S\_BTCH\_NAM | BTCUNAME | BWREMOTE |  |
| S\_DMIS (Only required when moving from an SLT Replication Server) | MBT\_PR\_ARE | SLOP | 03 |
|  | MBT\_PR\_LEV | PACKAGE |  |
