---
title: "Installing and upgrading the R4Z product in z/OS"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/R4Z_Install_Config/installing-the-r4z-product.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for z/OS", "Installing and configuring R4Z"]
---

# Installing and upgrading the R4Z product in z/OS

This section explains how to install and upgrade the R4Z product in z/OS.

Warning noteThe Data Movement gateway and R4Z versions you install must be part of the same release, which can either be an initial release or a patch/service release. This means that if you upgrade Data Movement gateway, you must also upgrade your R4Z installation (to the version that correlates with the Data Movement gateway release you are installing), unless it has the same build number as your currently installed R4Z. Note that despite being part of the same release, the Data Movement gateway and R4Z build numbers (reflected in their file names) might not be the same.

## Installing the R4Z product in z/OS

The configuration steps below include submitting jobs found in the INSTALL library (referred to as `<r4z-vnd-hlq>.INSTALL` in [*R4Z product libraries*](r4z-product-libraries-standard.htm)). Each job requires the INSTALL library (or its copy) as its JCLLIB, and must have both a job card and JES control statements that comply with the site’s regulations.

### Applying the installation in the processing environment

During the installation process you are required to submit most of the members with the prefixed “DO\*” in the library. Before you submit these members you have to edit them as follows:

1. Set the job name, the job card parameters, and JES control statements to comply with your system requirements.
2. Set the library specified in the `JCLLIB ORDER` parameter as the INSTALL library.

Therefore, before submitting any job, you should create a JCL library that contains all updated “DO” jobs. If you want to create a single set of jobs per all CDC services, it is advisable to assign the JCL library the name `<r4z-hlq>.COMMON.CNTL`; otherwise use the CDC service qualifier as a DSNAME node; for example `<r4z-bsc-hlq>.<CDC-qual>.CNTL`.

Information note

The installation kit also includes members with the prefix “UN\*”; each job starting with “UN” performs the UNDO action of the job by the same name that starts with “DO”. If need to use one of these jobs, make the same changes that you applied to the “DO” jobs.

#### Step 1: Setting the INSTALL library INCLUDE members

You need to set the JCL symbols below before running any job, as the “DO” jobs use these JCL symbols to configure the R4Z processing. To change their values, you will need to first run the “UNDO” job with the old value, and then the “DO” job with the new value.

Variables common to the entire R4Z installation

|  |  |  |
| --- | --- | --- |
| **DFSYMLST** | **INCMEM: define general system resources** | **Once per installation** |
| Sets: &SSID, &PROCLIB, &DB2HLVL, &CEERUNL, &DB2LOADL, &DB2EXITL, &DB2RUNL, &DB2VER, &R4ZHLVL, &R4ZLOADL, &R4ZINSTL, &R4ZCNFGL, &R4ZUSER, &DEFWLMAE, &ALCSMS, &ALCSMSPM, &ALCVLSER |

Edit this member to set the JCL symbols to be used by jobs in this library and then save (override) the member. These symbols are listed in the [*Installation symbols*](#Installa) table below.

Here is a more detailed explanation of several of the parameters:

- Parameters that specify the R4Z product library names:
  `&R4ZHLVL` - Set to the high-level-qualifier which is common to the R4Z INSTALL, LOAD and CONFIG libraries, i.e. the longest common part of these libraries names:
  - `&R4ZVNDH` - Set to the value you used as the “versioned” high-level qualifier (`<r4z_vnd_HLQ>`) when receiving the INSTALL and LOAD libraries.
  - `&R4ZBSCH` - Set to the value you chose for the “basic” high-level qualifier (`<r4z_bsc_HLQ>`), which will be used when creating the CONFIG library.
  - `&R4ZINSTL, &R4ZLOADL, &R4ZCNFGL`  - Specify these only if their value is different than that set within DFSYMLST member, based on the symbols described above.
- Parameters that control DASD allocation:
  - `ALCSMSPM, &ALCVLSER`  - Use these parameters to designate the volume(s) on which the CONFIG library, and some intermediate datasets will be allocated.

    Use `&ALCSMSPM` to specify SMS allocation attributes in a comma-delimited, space-terminated string, in the following format:

    `'[STORCLAS=…][,MGMTCLAS=…][,DATACLAS=…] '`

    Use `&ALCVLSER` to specify the volume serial.

    If SMS-managed allocation is driven by ACS routines, you can omit all attributes and specify `&ALCSMSPM`=' '(a single space) instead.

    If you specify `&ALCSMSPM`=' '(a single space), you must specify a value for the `&ALCVLSER` parameter.

    For non SMS-managed allocations, use `&ALCVLSER` to specify the volume serial.

- CDC service and UDF- related variables:

  |  |  |  |
  | --- | --- | --- |
  | **DFSYMPER** | **Define names for the UDF, the WLM application env and STC procedure, based on the CDC service qualifier** | **Per R4Z installation** |
  | Uses: `&CDCSRV`  Sets: `&R4ZWLMPR, &R4ZAPPNV, &R4ZIFITF, &R4ZSCNM, &STCUSER, &UDFUSER` |
  | **DFSYMONE** | **Define names for the UDF, the WLM application env and STC procedure, assuming a single CDC service is used** | **Per DB2 subsystem** |
  | Sets: `&R4ZWLMPR, &R4ZAPPNV, &R4ZIFITF, &R4ZSCNM, &STCUSER, &UDFUSER` |

Depending on the value selected for DEFWLMAE, ONE or PER, edit member DFSYMONE or DFSYMPER respectively, and select values for the WLM APPLENV, the WLM JCL procedure for the CDC reader UDTF.

Information note

In DFSYMPER member, these names are formed by a symbol designating the name prefix, followed by a 4-character qualifier specifying the CDC service. Do not remove the double-underscore at the end of the APPLENV name or UDTF name – these are used as delimiters, denoting the CDC service to be associated with the named resource.

#### Step 2: Performing configuration actions

1. Set the R4Z LOAD library as APF-authorized.

   To set a library as APF-authorized temporarily (until the next IPL or APF update), you can run one of the following system commands:

   - For non SMS-managed data sets:

     setprog apf,add,dsn=<xmit-HLQ>.LOAD,volume=<volser>
   - For SMS-managed data sets:

     setprog apf,add,dsn=(<xmit-HLQ>.LOAD,sms

     To make the setting permanent, add the library to your PROGxx member in PARMLIB.
2. Set up a WLM application environment to execute the CDC process.|

   |  |  |  |
   | --- | --- | --- |
   | DO2WLMAE | Define WLM Application environment | Per CDC service |
   | Accepts: &CDCSRV  Uses: **&R4ZAPPNV, &R4ZWLMPR, &CEERUNL, &DB2EXITL, &DB2LOADL, &DB2RUNL** | | |
   | DO2WLMPR | Create JCL procedure for WLM STC | per WLM procedure |
   | Accepts: &CDCSRV  Uses: &PROCLIB, &R4ZWLMPR, &SSID | | |
   | DO2WLMPV | Job: In define WLM server as a resource in RACF, and authorize APPLENV and DB2 subsystem to use it | per CDC service and WLM procedure |
   | Accepts: &CDCSRV  Uses: &R4ZAPPNV, &R4ZWLMPR, &STCUSER | | |

   Depending on the value set for DEFALMAE, run the following jobs, once (if ONE is selected) or PER each CDC service to be defined (if PER is selected), after setting JCL symbol CDCSRV with the relevant CDC service qualifier.
   1. Edit job DO2WLMAE; set symbol &CDCSRV to the relevant CDC service qualifier and submit. The job will define the WLM APPLENV in the WLM policy dataset and activate it.

      - **Prerequisites:**

        - &R4ZWLMPR is the name of the started task that WLM will use. You need to associate a valid user to the started task and set &STCUSER to that user.

          - The submitter needs UPDATE access to MVSADMIN.WLM.POLICY, to query and update the WLM policy.

          - UPDATE on the procedure library specified in DSSYMLST in the &PROCLIB symbol.
   2. Edit job DO2WLMPR; set the symbol &CDCSRV to the relevant CDC service qualifier and submit. The job will create a JCL procedure for the APPLENV, and should terminate with RC 0.

      - **Authorizations:**

        UPDATE on the PROCLIB library.
   3. Edit job DO2WLMPV; set the symbol &CDCSRV to the relevant CDC service qualifier and submit.
      The job will set RACF privileges for the APPLENV to use the WLM server, and for the DB2 subsystem to call it. The job should terminate with RC 0.

      - **Authorizations:**

        ALTER on class SERVER

        If you are using a security package other than RACF (for example, as CA-TSS or CA-ACF2) , you will need to run the commands relevant to your security package.
3. Create the CDC reader UDTF(s).

   |  |  |  |
   | --- | --- | --- |
   | **DO3SRVDF** | **Create the default CDC service UDTF** | **Per DB2 subsystem** |
   | Uses: &R4ZSCNM, &R4ZIFITF, &R4ZCNFGL, &ALCSMS, &ALCSMSPM, &ALCVLSER, &SSID, &DB2EXITL, &DB2LOADL, &DB2RUNL, &UDFUSER |
   | **DO3SRVTF** | **Create a UDTF to be used by a specific CDC service** | **Per CDC service and DB2 subsystem** |
   | Accepts: &CDCSRV  Uses: &R4ZSCNM, &R4ZIFITF, &R4ZCNFGL, &ALCSMS, &ALCSMSPM, &ALCVLSER, &SSID, &DB2EXITL, &DB2LOADL, &DB2RUNL, &UDFUSER |

   The first job creates the default-service UDTF with specific name &R4ZIFITF (under schema name &R4ZSCNM) and grants execution on it to &UDFUSER. It also instantiates a “supplied” CDC service, CDC1 (by creating such a member CONFIG library), setting it with default configurations. This job must be run first.

   The second job, which is ran per each CDC service defined explicitly, performs exactly as the first job, except each UDF is associated with a specific CDC service, which is instantiated from the CDC1 service.

   1. Run job DO3SRVDF. It will:

      - Create a UDTF with an un-suffixed name, which will be associated with the default CDC service (CDC1).
      - Create the CONFIG library and place a member named CDCS, to be used when no CDC service-related member exists.

      Jobs should terminate with `RC``4`.
   2. Per each CDC service you want to define, edit job DO3SRVTF; set symbol &CDCSRV to the relevant CDC Service qualifier and submit. It will:

      - Create a UDTF with its name suffixed "\_\_&CDCSRV", which will be associated with the default CDC service ""&CDCSRV".
      - Create a member named "&CDCSRV" in the CONFIG library.
      - Set JCL symbol CDCSRV with the relevant CDC service qualifier (xxxx), and submit the job.

      Jobs should terminate with `RC``4`.

      - **Authorizations:**

        The submitting user must have one of the following authorizations:

        - SYSADM or SYSCTRL authority.
        - CREATEIN authorization in the schema designated by `&R4ZSCNM.`
4. Enable specified user-ID to run CDC tasks.

   |  |  |  |
   | --- | --- | --- |
   | **DO4GRANT** | **Grant ODBC user access to catalog tables, and permission to read CDC** | **Per DB2 subsystem** |
   | Uses: &R4ZUSER, &SSID, &DB2EXITL, &DB2LOADL, &DB2RUNLR |

   This job enables the user-ID selected for ODBC interaction. This is the “ODBC user”, that is authorized (DB2-wise) to read CDC data and some of the DB2 catalog tables.

   Information note

   There is no point submitting the job from the ODBC user itself, (as a user cannot grant itself privileges), or from a user that does not own the privileges it attempts to grant.

   Run job DO4GRANT. It will:

   - GRANT SELECT to the ODBC user on the following tables:

     - SYSIBM.SYSTABLES
     - SYSIBM.SYSTABLESPACE
     - SYSIBM.SYSCOLUMNS
     - SYSIBM.SYSROUTINES
     - SYSIBM.SYSDUMMY1
     - ALTER SYSIBM.SYSTABLES enabling DATA CAPTURE.

   Jobs should terminate with `RC 0` or `RC 4`.

   **Authorizations:**

   The submitting user must have either of the following authorizations:

   - SYSADM or SYSCTRL authority.
   - TRACE/ MONITOR2 with grant option.
5. Provide security permissions for the WLM started task to cancel itself.
   In RACF this is done as follows:

1. Define a PROFILE for the OPERCMDS class called PERMIT MVS.CANCEL.STC.mbrname.\*:

   `RDEFINE OPERCMDS MVS.CANCEL.STC.mbrname.* UACC(NONE)
   SETROPTS REFRESH RACLIST(OPERCMDS)`

   Where `mbrname` is the name of the started task.
2. Grant the USERID assigned to the WLM started TASK the authority to cancel the started task:

   `PERMIT MVS.CANCEL.STC.mbrname.* CL(OPERCMDS) ACCESS(UPDATE) ID(stcuser)`

   Where `stcuser` is the USERID associated with the WLM started task.

6. Performance considerations:
   1. **Full Load** – The Full Load processes will utilize any available ZIIP processors. Best practice is to set the performance goal that the processes get classified to lower than online workloads. In a very busy system, you might want to consider setting **Honor Priority** to **NO** for the service class assigned to the Full Load. This requires z/OS 2.1 + OA50845 or z/OS 2.2 and above.
   2. **CDC** – Best practice is to set the performance goal for the CDC processes equal to any online workloads and higher than the Full Load goal. These processes can either be classified using any of the following:

      - The name of the WLM application environment started task

      - The DDF classification with 'Procedure Name'

Installation symbols

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Symbol Name | **Description** | | Attribute | | --- | | Default Value | |
| &SSID | The subsystem-ID of the source DB2. | 4-character name. |
| `DSN1` |
| &DB2HLVL | High-level qualifier of DB2 installation libraries, not including SSID qualifier. | <qualifier>.<qualifier>… |
| `DSNB10` |
| &DB2LOADL | High-level qualifier of DB2 SDSNLOAD library. | Library name. |
| `&DB2HLVL..&SSID..SDSNLOAD` |
| &DB2EXITL | High-level qualifier of DB2 SDSNEXIT library. | Library name. |
| `&DB2HLVL..&SSID..SDSNEXIT` |
| &DB2RUNL | High-level qualifier of DB2 RUNLIB.LOAD library. | Library name. |
| `&DB2HLVL..&SSID..RUNLIB.LOAD` |
| &DB2VER | The z/OS DB2 version. | Number (10..12) |
| `11` |
| &CDCSRV | **CDC service:** A set of resources - ECSA structures, a table function and possibly a WLM application environment - used for reading CDC data by all tasks designating this service. | Qualifier of up to four characters, forming a valid name. |
| `CDC1` |
| &CEERUNL | z/OS LE (language environment) and C++ runtime library. | Library name. |
| `CEE.SCEERUN` |
| &PROCLIB | JCL procedure library where third-party JCL procedures are located. You can choose a PROCLIB used by third-party products. | Library name. |
| N/A |
| &R4ZHLVL | R4Z high-level qualifier. | <qualifier>.<qualifier>… |
| `R4Z` |
| &DEFWLMAE | Determine whether a separate WLM APPLENV is to be created PER CDC service, or all services are to use ONE WLM APPLENV | ‘PER’ or ‘ONE’ |
| N/A |
| &R4ZLOADL | R4Z load library. | Number (09..12). |
| `&R4ZHLVL..LOAD` |
| &R4ZWLMPR | WLM STC for the Data Movement gateway application environment. | Member name (JCL procedure). |
| `&SSID.WR4Z` |
| &R4ZAPPNV | The WLM application environment serving the Data Movement gateway UDTF. | Upper case name, up to 32 characters (underscores allowed). |
| `R4ZWLM` |
| &STCUSER | The user ID assigned to regions started by WLM application-environment | User ID (up to 7 characters). |
| `(none)` |
| &R4ZUSER | User ID used for issuing SQL select statements IFI306 READS; may be overridden by &UDFUSER. | User ID (up to 7 characters). |
| `ATTUSER` |
| &R4ZSCNM | Schema name qualifying the UDTF routine (to be specified in the IBM DB2 for z/OS connector settings) | Schema name. |
| `&R4ZUSER` |
| &R4ZIFITF | User-defined function name (to be specified in the IBM DB2 for z/OS connector settings). | Function name (not including the schema name). |
| `R4ZUDF` |

## Migrating the R4Z product in z/OS

Information note

If an older version of the product is already installed and operating in the environment, it is mandatory to complete these instructions before starting the installation of the new version.

If you want to upgrade your R4Z installation and override the current installation, or if you want to upgrade your R4Z installation without overriding the currently installed version, you need to perform the relevant steps outlined below.

To upgrade your R4Z installation and override the currently installed version, suspend all CDC services using R4Z as follows:

1. Use the following operator command to quiesce the WLM application environment and prevent clients from auto-activating the CDC service before it is ready:

   `VARY WLM,APPLENV=<applic.env-name>,Q`

   Repeat this for all application environments using the JCL procedure(s) which specify the LOAD library of the version being replaced. If the host is a Parallel Sysplex, precede the command with `ROUT *ALL`, routing it to all systems in plex.
2. Use the `R4ZUTIL TERMINATE` verb to free all system resources currently used by the CDC service.

   Repeat this in all LPARs where it may be executing (if the source DB2 has data sharing members in those systems).
