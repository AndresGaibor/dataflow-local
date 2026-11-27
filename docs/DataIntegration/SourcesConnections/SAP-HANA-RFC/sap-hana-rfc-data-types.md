---
title: "Source data types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA-RFC/sap-hana-rfc-data-types.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP HANA RFC"]
---

# Source data types

The SAP add-on discovers column types, lengths, and key flags from ABAP Dictionary (DDIC) metadata. Source type support and the target column representation are separate considerations.

## Review SAP column types

SAP HANA RFC source type families

| Source types | Considerations |
| --- | --- |
| CHAR, CLNT, LANG, NUMC, SSTRING, SSTR, CUKY, UNIT | Character-like values. Preserve leading zeros in numeric text such as NUMC when reviewing target metadata. |
| CURR, DEC, QUAN, INT1, INT2, INT4, INT8 | Review precision and scale in the data task metadata. A DEC column with scale zero has no decimal places. |
| FLTP, DF16\_DEC, DECFLOAT16, DF34\_DEC | Review floating-point and decimal-floating-point representation. FLTP values can arrive in scientific notation. |
| DATS, TIMS, DATN, TIMN, UTCLONG, ACCP and timestamp fields | Review date, time, and timestamp precision for the selected target. |
| RAW, STRING, RAWSTRING, RSTR | Review binary and large-object column handling before running the data task. |

D34R and VARC are listed as expected string mappings but are not yet tested. The same endpoint reference also lists VARC as unsupported. Confirm its status before selecting a table that uses it. LCHR, PREC, and GEOM\_EWKB are not supported.

## Review target mappings

Do not treat Replicate's internal type names as the final Cloud target column types. Review the data task metadata and the mappings supported by your target. See [*Managing data types*](../../Introduction/Managing-data-types.htm).

## Configure LOB handling

The source sends STRING and RAWSTRING values inline with the row; it does not provide a later lookup for the complete value. Full LOB mode is not supported by this endpoint.

For replication tasks, configure the available LOB settings for your target in [*LOB settings*](../../Replicating/replicating-settings.htm#LOB). Excluding LOB columns omits their values. With a size limit, longer values can be truncated, including multi-byte text. Review the task metadata and target limits before starting capture.
