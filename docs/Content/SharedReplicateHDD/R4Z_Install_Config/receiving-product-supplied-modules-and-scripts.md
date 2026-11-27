---
title: "Receiving product-supplied modules and scripts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/R4Z_Install_Config/receiving-product-supplied-modules-and-scripts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for z/OS", "Installing and configuring R4Z"]
---

# Receiving product-supplied modules and scripts

The following instructions explain how to download and receive the required modules and scripts.

To receive the load modules and installation components:

1. Download R4Z as described in [*Prerequisites*](../../../../Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-zos/prerequisites-zos.htm).
2. Unzip the file contents to your workstation.

   The zip file contains the following files:

   - `r4z.vxx.ryy.spzz.install.xmit` – JCLs; ISPF dialog components.

     Information note

     The version identifiers, namely: major release, minor release, and service pack, are indicated by `xx`, `yy` and `zz` respectively.
   - `r4z.vxx.ryy.spzz.load.xmit` – Executable load modules.
   - `version.txt` – A text file listing the version identifiers in this kit.
   - `r4zrrcv.txt` – A sample job for populating the INSTALL and LOAD libraries from the matching XMIT files.
3. Pre-allocate the following 1 cylinder datasets with LRECL=80,RECFM=FB,DSORG=PS:

   - <xmit-HLQ>.INSTALL
   - <xmit-HLQ>.LOAD
4. Perform a binary transfer of `r4z.vxx.ryy.spzz.load.xmit` to **<xmit-HLQ>.LOAD** and of `r4z.vxx.ryy.spzz.install.xmit`  to **<xmit-HLQ>.INSTALL**.
5. In TSO, use the RECEIVE command to create and populate the INSTALL and LOAD libraries from the matching xmit files, which should now exist in the host z/OS.

   You can do that in either of the following methods:

   - Use the sample job provided in r4zrrcv.txt (see below) to invoke the RECEIVE command.
   - Run the RECEIVE command directly under TSO:

     1. From the ISPF TSO command shell run the command bellow per each library <type>, INSTALL or LOAD:

        `Receive indsn('<xmit-HLQ>.<type>')`
     2. When prompted `INMR906A Enter restore parameters or 'DELETE' or 'END' +`, respond with the output dataset and other parameters; for example: `Receive dsn('<r4z-vnd-HLQ>.<type>').`

        These RECEIVE commands will populate the INSTALL and LOAD libraries.

## Sample Job

Below is the sample RECEIVE job found in the r4zrrcv.txt file. For non-SMS datasets, change `<volser>` to a valid volume serial number. For SMS datasets, delete **UNIT** and **VOLUME**.

//RECEIVE JOB NOTIFY=&SYSUID

//RECEIVE1 EXEC PGM=IKJEFT01,DYNAMNBR=11

//SYSTSPRT DD SYSOUT=\*

//SYSTSIN DD \*

RECEIVE INDSNAME(<xmit-HLQ>.INSTALL')

DSNAME('<r4z-vnd-HLQ>.INSTALL') UNIT(3390) VOLUME(<volser>)

RECEIVE INDSNAME('<xmit-HLQ>.LOAD')

DSNAME('<r4z-vnd-HLQ>.LOAD') UNIT(3390) VOLUME(<volser>)
