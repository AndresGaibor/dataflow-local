---
title: "R4Z components and the associated environment"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/R4Z_Install_Config/r4z-components-and-the-associated-environment.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for z/OS", "Installing and configuring R4Z"]
---

# R4Z components and the associated environment

The relationship between all components involved in the moving process is described below.

- The IBM DB2 for z/OS connectoris associated with:
  - A z/OS host, which can be a single system (LPAR) or a Sysplex, via a TCP/IP address. Referring to a Sysplex requires defining a VIPA that points to a set of systems.
  - A DB2 location name active within the above z/OS host, which is the logical identification of a DB2 subsystem ID (non-data sharing) or a “group attach”, which may refer to several members of a data sharing DB2.

    The connector also allows you to set a **CDC reader UDTF** name. This is an external UDTF (User-Defined Table Function) which is referenced by a “SELECT … FROM TABLE(…)” statement issued from the moving task. The CDC reader UDTF is created in DB2, at the location name specified above, by SQL DDL, as part of the installation. This definition also specifies:

    - The name of the external program to be executed for serving the function call. This name must not be changed.
    - The name of the WLM APPLENV (application environment) through which the program is to be executed. This is defined as part of the installation.

      The WLM APPLENV specifies, as one of its attributes, the name of a JCL procedure for initiating a started task (STC) address space. Such STC address spaces (also known as WLM servers) are started and managed by WLM upon calls to the UDTF, to invoke the external program to be executed for serving the function call. The JCL procedure is stored in a PROCLIB library as part of the installation.
- The CDC reader UDTF name: If this name matches a specific pattern, it specifies a CDC service qualifier to be associated with the UDTF invocation. The CDC service, which is defined in the R4Z CONFIG library as part of the installation and may be altered later, designates certain system resources and configuration settings to be used during CDC processing. If the UDTF name does qualify for the said pattern, a default CDC service is associated with the UDTF.
