---
source: https://qlik.dev/changelog/73-api-updates-tabular-reporting/
last_updated: 2025-07-08T16:09:30Z
---

# New APIs and endpoints - tabular reporting

Tabular reporting enables Qlik Cloud customers to address common operational report
distribution requirements, such as providing:

- Custom and highly formatted Excel documents from Qlik data and Qlik visualizations
- Paginated tables of sales/transactional data
- Repeated sheets of departmental analysis

Qlik has published APIs and endpoints to support programmatically
managing, deploying, and maintaining this capability:

- The [Sharing Tasks](https://qlik.dev/apis/rest/sharing-tasks/) API supports the
  creation and management of Report Tasks.
- The [Report Templates](https://qlik.dev/apis/rest/report-templates/) API gives you
  access to the Excel templates used to generate tabular reporting output.
- The [Report Filters](https://qlik.dev/apis/rest/apps/#%23%2Fentries%2Fv1%2Fapps%2F-appId%2Freport-filters-get)
  endpoints provide access to filters used when configuring Report Tasks.
- The [Reports](https://qlik.dev/apis/rest/reports/) API can now be used to trigger
  tabular report generation via the `sense-excel-template-1.0` template type.

Learn more about:

- How to use these APIs to [programmatically deploy tabular reports between apps, spaces, and tenants](https://qlik.dev/manage/reports/deploy-tabular-reports/)
- How to create and configure reports with the [tabular reporting](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/cloud-tabular-reports-intro.htm)
  capability in your Qlik Cloud tenant
