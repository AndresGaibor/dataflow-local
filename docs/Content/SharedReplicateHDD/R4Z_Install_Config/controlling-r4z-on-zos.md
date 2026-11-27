---
title: "Controlling the CDC process"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/R4Z_Install_Config/controlling-r4z-on-zos.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for z/OS", "Installing and configuring R4Z"]
---

# Controlling the CDC process

Data Movement gateway uses ECSA memory structures - called R4Z CDC services - which are formed during CDC processing. Each z/OS LPAR may contain several such R4Z CDC services. To form the R4Z CDC services, a special utility program, R4ZCTL, is provided.

This program can also be used for managing the state of CDC processing, as well as the level of traffic on the z/OS side.

The R4Z control program (R4ZCTL ) is required for the following purposes: checking CDC and reporting the CDC service’s status, pausing CDC processing, resuming a paused CDC, and terminating the CDC process, either normally or forcefully.

The command parameters available when running the R4ZCTL program are:

Information note

If you run the command without any parameters, it will return the current status of the CDC service.

- CHECKCONFIG - Verifies that configuration parameters are valid.
- PAUSE\_TASK - Stops the service of a specific CDC task.
- PAUSE\_CDC - Stops the entire activity of a CDC service.
- RESUME\_TASK - Enables a paused task to continue.
- RESUME\_CDC - Enables a paused CDC service to continue.
- TERMINATE - Stops the CDC service, and, once stopped – releases its resources.
- FORCE - Same as TERMINATE, when task holding resources “hangs”.
- RECLAIM\_HOURS – Reclaims orphaned ECSA slots for reuse.

As the R4ZCTL programs requires APF-authorization, all libraries in the STEPLIB must be APF- authorized.

When running R4ZCTL with no parameter, its completion-code is set based on whether the environment was initialized (CC=0) or not initialized (CC=1).

## Control program invocation syntax

The R4ZCTL program is invoked as a job step, i.e. EXEC PGM=R4ZCTL, and accepts instructions via the invocation parameter of the job step.

The R4ZCTL invocation parameter is a string that can contain optional sub-parameters, separated by a comma as follows:

[SERVICE=CDC-service-qualifier,][MSGLVL={0 | 1},][action]

Information note

The order of the sub-parameters in the string is not important.

Where:

SERVICE=CDC-service-qualifier designates the logical scope of Qlik Talend Data Integration activity, upon which the control program is to act.

MSGLVL={0 | 1 | 2} designates the level of notifications to be displayed in the message file during the operation of the control program.

- 0 = No notifications
- 1 = Moderate
- 2 = Maximum

action-verb can be one of the following:

- PAUSE\_TASK(\*|ALL|task-qualifier)

  Suspends CDC retrieval for the task(s) designated in parentheses.
- PAUSE\_CDC

  Suspends CDC retrieval for entire CDC service. Replication tasks suspended for more than a certain time are stopped will attempt recovery multiple times. No new tasks will be served.
- RESUME\_TASK(\*|ALL|task-qualifier)

  Resumes CDC retrieval for the task designated by task-qualifier.
- RESUME\_CDC

  Resumes CDC retrieval for all instances matching the session-limits qualifier.
- DUMP\_TASK(\*|ALL|task-qualifier)

  Requests formatted dumping of the control information in the resident memory structures. ALL designates all sessions; SUMMARYONLY designates only the anchor.
- TERMINATE

  Frees all the R4Z resident memory structures, terminates all active instances and deletes associated resources. From this point on, all CDC requests will return the inactive status until CDC service is auto-activated by an incoming call to the CDC reader UDF.
- RECLAIM\_HOURS=(1 to 72)

  Examines ECSA slots and frees any that have not been used in the specified number of hours. This replaces the previous mechanisms used within the R4Z UDTF to free ECSA slots.

### Syntax elements reference

The elements used in the syntax descriptions above are as follows:

- CDC-service-qualifier

  A 4-character name (first character alphabetic, rest alphanumeric), which designates a CDC service.

  “CDC service” refers to a group of resources – memory structures, a user-defined table-function (UDTF) defined in DB2 and an application environment (APPLENV) defined in the WLM policy. R4Z lets you specify properties – memory limits and processing thresholds – per each CDC service. It may be necessary to manage several CDC services for another reason as well; namely, to allow for more than one Data Movement gateway release being used in a single LPAR, with each release maintaining its memory structures independently of others.
- task-qualifier

  A 4-digit identifier being assigned upon initiation of the task. This identifier is aimed mainly for controlling and tracking CDC traffic of a specific task. It forms the CORRID (Correlation-ID) of the DB2 thread serving CDC – it occupies bytes 9-12 there.

## Control program completion codes

- 0 – Normal completion
- 1 – Environment does not exit the session-limits qualifier (when no action is specified)
- 4 – Warning
- 8 – Error

## Sample jobs (in the INSTALL library)

IV1CHECK – Checks the configuration of all CDC services

XMDUMP – Dumps all sessions

XMPAUSE – Pauses a session

XMRESUME – Resumes a session

XMTERMIN – Terminates all sessions

XMRCLAIM – Runs ECSA slot reclamation

Information note

If R4Z ECSA slots are completely used by running tasks or slots waiting to be freed by XMRCLAIM, and ALLOWWTO is set to 1, the following warning is written to the operator console: R4Z0003W ALL CB ENTRIES ARE IN USE.

Information note

Customers using R4Z in a DB2 Data Sharing environment should schedule XMRCLAIM as a nightly batch job to free eligible ECSA slots for reuse.

Information note

Non-Data Sharing DB2 customers who have had UDTF user abends 3306 or SIGABRTs should also consider scheduling XMRCLAIM as a nightly batch job.

Warning note

Scheduling XMRCLAIM with RECLAIM\_HOURS set lower than the longest valid IFI wait time can lead to data loss.

## Enabling the CDC process (auto-activation)

To enable the CDC reader UDTF function to work, this function needs to be able to allocate and pre-format memory structures in ECSA when the UDTF is called and the first time after the z/OS system was started; it also needs to access the configurations set for the CDC service the UDTF is serving (or the “default” configurations, for values not specified at the CDC service level).

To account for this, the installation process ensures that:

1. A special UDTF is created to serve the CDC service. The created UDTF has its name suffixed with a double-underscore (“\_\_”) followed by the CDC-service-qualifier, forming a name as such: <*schema*>.R4Z\_UDTF\_\_<*CDC-service-qualifier*>.
2. A WLM APPLENV is created to execute invocations of the above UDTF. The created APPLENV may also have its name suffixed with the CDC service qualifier, to ensure uniqueness of the APPLENV name – which is recommended; however, multiple UDTFs may use a single APPLENV.
3. A JCL procedure is created to “host” the WLM APPLENV executions. This JCL procedure differs from a usual WLM STC procedures in that a special DDNAME, R4ZCNFG, must be specified, its DSN referring to the CONFIG library of the R4Z product. In this library, there MUST be an existing member named “CDCS”, specifying the default CDC service configurations. There MAY also exist a member named “CDCS<CDC-service-qualifier>” with the configuration values you want to apply for this CDC service.
4. The content of each of the CDCS\* members in the CONFIG library is a list of assignment statements, one per card, in the format “keyword=value”. The statement may follow spaces, and are space-terminated; no spaces are allowed with the statement. Cards beginning with a hyphen (‘-‘) are treated as comment cards; and the content following the terminating space is also treated as comment.

   Keywords, max values, min values, and default values

   | Keyword | Description | Minimum | Maximum | Default |
   | --- | --- | --- | --- | --- |
   | MAXSESSIONS | The maximum number of CDC sessions. | 1 | 128 | 32 |
   | SESSIONTIMEOUTSECS | The number of seconds after which session is timed out. | 300 | 7200 | 900 |
   | MAXIFIBUFKBYTES | The maximum buffer size allowed for IFI reads, in Kbytes. | 64 | 1024 | 256 |
   | MAXRESULTSETMBYTES | The maximum size in Mbytes for the accumulated result set to reach; when reached, the result set is returned. | 1 | 2048 | 4 |
   | MAXRESULTSETSECS | The maximum time interval, in seconds, for accumulating the result set; when reached, the result set is returned. | 1 | 120 | 30 |
   | ALLOWSTMON2 | Allow START TRACE MON(2).  Allow: This is the default. Any special character is allowed and is used as the command prefix.  Deny: 0  Enable without a prefix: 1  Set to a special prefix character. | N/A | N/A | - (Dash symbol is the default) |
   | ALLOWWTO | Allow WTO to JESLOG.  Allow: 1  Deny: 0 | N/A | N/A | 1 |
   | USECDDS | Use the Compression Dictionary Data Set (CDDS):  1=Use  0=Do not use | N/A | N/A | 0 |

   ## Establishing R4Z CDC services

   **Deciding on the CDC services:** Based on predicting the need for independent replication processes (to allow different versions, to ensure sufficient ECSA memory, to account for different latencies allowed, etc.), determine which R4Z CDC services are to exist in each LPAR. For each service, choose the CDC service qualifiers (4 characters).
   You also need to decide whether each CDC service is to have its own WLM APPLENV (application environment), or a single APPLENV to serve all CDC services.

   You need to set variable DEFWLMAE (DEFine WLM Applic. Env.) in DFSYMLST member to either PER (first option) or ONE (second option). Once set, you can proceed with the installation:

   Information note
   - If you select ONE for DEFWLMAE, jobs DO2\* and DO3SRVTF should be run one time ; if you select PER , these jobs should be run for each CDC service, after the JCL SET variable CDCSRV is set to the CDC service’s qualifier.
   - Job DO3SRVDF creates a CONFIG library, and places a member named “CDCS”, which serves as the default configuration file. After running job DO3SRVTF the library will contain the configuration of all CDC services, making it possible to edit them and change the configurations of a specific CDC service.
   - If ONE is used for DEFWLMAE, then the product defaults are used instead of the CONFIG library members.
