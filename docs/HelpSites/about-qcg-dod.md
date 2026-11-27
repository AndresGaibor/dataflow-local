---
title: "Qlik Cloud Government - DoD"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/HelpSites/about-qcg-dod.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Introducing Qlik Cloud", "Qlik Cloud Government overview"]
---

# Qlik Cloud Government - DoD

Qlik Cloud Government - DoD is only available for the U.S. Department of Defense, Combat Support Agencies, Combatant Commands, and the U.S. Defense Industrial Base and has differences from both Qlik’s commercial Qlik Cloud offering and the Qlik Cloud Government offering due to the security protocols required to support the DoD. See [Qlik Cloud security, compliance, and privacy](security-compliance.htm) for a summary of compliance certifications and attestations.

Qlik keeps both platform offerings in sync for product features and capabilities wherever possible.

This topic notes feature differences between the Qlik Cloud Government version and Qlik Cloud Government - DoD. The Qlik Cloud documentation set supports both versions, and differences are noted.

Information note

For information about new and enhanced Qlik Cloud Government - DoD features, see [What's new in Qlik Cloud](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/saas-change-log.htm). Then, filter the items that to review specific Qlik Cloud Government - DoD-related information.

## Qlik Cloud Analytics

This section notes the Qlik Cloud Analytics feature differences between Qlik Cloud Government version and Qlik Cloud Government - DoD.

### Creating analytics and visualizing data

- In-application reporting is a set of features available in a Qlik Sense application, powered by the Qlik Reporting Service value-add subscription option. With in-application reporting, configure highly customizable Tabular, PixelPerfect, HTML, PowerPoint, and Word reports and distribute them to internal and external stakeholders.

  - Qlik add-ins for Microsoft Office are supported for developing report templates against applications in Qlik Cloud Government or Qlik Cloud Government - DoD tenants.
  - Qlik add-ins for Microsoft Office cannot be used in Office 365 U.S. Department of Defense (DoD).

    For more information, see [Managing installation manifests for Qlik add-ins for Microsoft Office](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-add-in.htm).
  - In Office 365 Government Community Cloud High (GCCH), Qlik add-ins for Microsoft Office can only be installed via [centralized deployment](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Install/reporting-install-add-ins.htm#Centrali). Installing via sideloading or network share is not supported.

  For more information about in-application reporting, see [In-application reporting with Qlik Cloud Analytics](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/cloud-in-app-reports-intro.htm).

## Qlik Cloud Administration

This section notes the administration difference between the Qlik Cloud Government version and Qlik Cloud Government - DoD.

### System management

- When configuring Microsoft 365 as an email provider, Qlik Cloud Government and Qlik Cloud Government - DoD tenants can select a cloud region to use the correct Microsoft endpoints for authentication and email sending.

  You cannot connect your Microsoft 365 email provider to Office 365 U.S. Department of Defense (DoD).

  For more information, see [Configuring email for reports and notifications](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-configure-email-support.htm).

### Internet and DODIN Network connectivity

- NIPRNet/DODIN Connectivity

  - Qlik Cloud Government - DoD is connected to the U.S. DoD information Network’s (DODIN) Non-Classified Internet Protocol Router Network (NIPRNet) via a DISA Boundary Cloud Access Point (BCAP) providing non-public connectivity to Qlik Cloud Government - DoD for DoD agencies.
  - Qlik Cloud Government - DoD's DISA BCAP routing is the only supported network traffic patter as per Qlik's DISA Provisional Authorization. Other component BCAPs are not able to route directly to Qlik Cloud Government - DoD.
  - While Qlik Cloud Government - DoD is whitelisted internally in NIPRNet, DoD agencies need to determine if their network security rules require egress permission to access Qlik Cloud Government - DoD
  - Qlik Cloud Government - DoD uses DISA's West BCAP
- Internet connectivity

  - Access to the internet from Qlik Cloud Government - DoD is via DISA Internet Access Point
  - Egress access from Qlik Cloud Government - DoD to the internet is whitelisted by DISA. Ingress access from the internet to Qlik Cloud Government - DoD tenants must be requested by the customer to and be approved by DISA.
  - All internet activity is controlled and monitored by DISA.

### Cyber Security Services Provider

- In order to meet DoD security requirements, customers that are authorized to use Qlik Cloud Government - DoD will work with Qlik and a DoD-accredited cyber security service provider (CSSP) provided by the customer, to perform defensive cyberspace operations (DCO) activities mandated by DoD.

### Encryption

- In order to meet DoD security requirements, customers that are authorized to use Qlik Cloud Government - DoD will need to use Qlik's Customer Managed Key capability.

## Qlik Automate

Qlik Automate is a no-code visual interface that lets Qlik Cloud users build automated analytics and data workflows by integrating applications and services from outside of your Qlik environment.

- Qlik Cloud Government - DoD supports a subset of Qlik-native and third-party connectors. For more information, see [Qlik Automate connectors](/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/connector-blocks/connectors-list.htm).
- The Custom Code block is not supported in Qlik Cloud Government - DoD tenants. For more information, see  [Custom Code in Qlik Automate](/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/advanced/custom-code.htm).
