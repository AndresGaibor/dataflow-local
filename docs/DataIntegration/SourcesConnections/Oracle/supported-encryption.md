---
title: "Supported encryption methods"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Oracle/supported-encryption.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Oracle"]
---

# Supported encryption methods

This section describes which encryption methods Qlik Replicate supports when working with an Oracle source database, and details the requirements for HSM encryption support.

## TDE encryption

Both tablespace and column encryption is supported.

### Limitations and considerations

- NNE (Native Network Encryption) is supported as long as it is configured correctly, both on Oracle and in the Oracle client sqlnet.ora file.
- Moving of columns encrypted with the 3DES168 algorithm is not supported.

## HSM Encryption

Both tablespace and column encryption is supported.

### Prerequisites

- An Oracle DBA should install the PKCS #11 client on the Qlik Talend Data Integration machine and configure it to work with HSM.
- Define the AREP\_HSM\_LIB environment variable with a path to pkcs11 dll/so.

  Example:

  - set AREP\_HSM\_LIB=C:\Program Files\Vormetric\DataSecurityExpert\Agent\pkcs11\bin\vorpkcs11.dll
  - export AREP\_HSM\_LIB=/opt/cloudhsm/lib/libcloudhsm\_pkcs11.so

### Setup

1. Enter HSM in Names field.
2. In the Values field, set either crypto\_username:password or just password depending on your HSM. For Oracle Key Vault, the password should be the same as the one used to install the okvclient.jar. The password or crypto\_username:password combination are the same credentials that were used to create the TDE master key.

### Limitations and considerations

- When working with Oracle Key Vault for Oracle 19, Oracle 19.17 full client or later must be installed.

  Information noteOracle Key Vault can be used with any HSM using the PKCS#11 API. Using Oracle Vault in OCI (Oracle Cloud Infrastructure) is not supported, as it does not provide a public PKCS#11 API.
- Moving of columns encrypted with the 3DES168 algorithm is not supported.
