---
title: "R4Z product libraries"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/R4Z_Install_Config/r4z-product-libraries-standard.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for z/OS", "Installing and configuring R4Z"]
---

# R4Z product libraries

The following library types are required by the product:

- LOAD and INSTALL libraries - These libraries are received from the installation kit. Therefore, their content is version-dependent and cannot be reused by other versions.
- CONFIG and CNTL libraries - These libraries are created during the installation and configuration. As a result, their content can be reused by successive versions of the product (depending on the specific case).

Examples of LOAD and INSTALL library file names:

- LOAD: r4z.v2022r5.sp0.load.xmit
- INSTALL: r4z.v2022r5.sp0.install.xmit

To accommodate for these different use types, it is recommended to use separate high-level qualifiers for the R4Z product libraries:

- R4Z “version-specifc” high-level qualifier, with the following libraries:

  - **LOAD** - Found in the kit; contains executable load modules.
  - **INSTALL** - Found in the kit; contains installation scripts/JCLs and sample jobs.

  This qualifier will henceforth be referred to as `<r4z-vnd-hlq>`.
- R4Z "basic" high-level qualifier, independent of versions, with the following libraries:

  - **CONFIG** - Created during the installation; contains the CDC services configuration.
  - **CNTL** -To be created by the person performing the installation, for saving JCL components - jobs and Include members.It is possible to allocate several CNTL libraries, assigning them a name that contains the CDC service name. This is useful if the CDC services are to be managed independently of one another.

  This qualifier will be henceforth referred to as `<r4z-bsc-hlq>`.
