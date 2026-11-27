---
title: "Deputy"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Deputy.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Deputy

Deputy is an employee scheduling, HR, workforce management and time clock software.

Deputy integration replicates data using the [Deputy API](https://www.deputy.com/api-doc/API/Getting_Started).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate your client ID and secret:

1. Log into your Deputy installation, for example: https://your-subdomain.region.deputy.com.
2. Navigate to your OAuth client settings, for example: https://your-subdomain.region.deputy.com/exec/devapp/oauth\_client.
3. To create your OAuth client, fill in:
   - Name: Your app’s display name.
   - Description: A description of your app.
   - Logo URL (optional): An image of your logo.
4. Make sure Authorized Redirect URIs is set to https://connector.qlik.com/auth/oauth/v3.htm.
5. Click Save this OAuth Client. The client ID and secret are displayed.
6. Copy and paste your client ID and secret into a secured file.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Click Authenticate when you have filled in the required connection settings.

   You may be asked to log in to the source application.

   A window is displayed with an authentication code.
2. Copy the code to the clipboard and return to the connection dialog.
3. Paste the code in Complete authentication with the code provided by the source and click Verify.

   Tip noteYou may need to scroll down to see this field.

   When status is Verified, the authentication is verified.
4. Provide a name for the connection in Connection name.
5. Select Open connection metadata to define metadata for the connection when it has been created.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### addresses

The `addresses` table contains info about addresses.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Address) |

addresses table foreign keys

| Join addresses with | on |
| --- | --- |
| [companies](#companies) | ``` addresses.Id = companies.Address ```  ``` addresses.Creator = companies.Creator ``` |
| [employee\_history](#employee-history) | ``` addresses.Id = employee_history.MainAddress ```  ``` addresses.Id = employee_history.PostalAddress ```  ``` addresses.Id = employee_history.EmergencyAddress ```  ``` addresses.Creator = employee_history.EmployeeId ```  ``` addresses.Creator = employee_history.Creator ``` |
| [operational\_units](#operational-units) | ``` addresses.Id = operational_units.Address ```  ``` addresses.Creator = operational_units.Creator ``` |
| [categories](#categories) | ``` addresses.Creator = categories.Creator ``` |
| [comments](#comments) | ``` addresses.Creator = comments.Creator ``` |
| [company\_periods](#company-periods) | ``` addresses.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` addresses.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` addresses.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` addresses.Creator = custom_app_data.Employee ```  ``` addresses.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` addresses.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` addresses.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` addresses.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` addresses.Creator = employee_agreements.EmployeeId ```  ``` addresses.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` addresses.Creator = employee_appraisal.Creator ```  ``` addresses.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` addresses.Creator = employee_availability.Employee ```  ``` addresses.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` addresses.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` addresses.Creator = employee_contracts.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` addresses.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` addresses.Creator = employee_paycycles.EmployeeId ```  ``` addresses.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` addresses.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` addresses.Creator = employee_salary_opunit_costing.Employee ```  ``` addresses.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` addresses.Creator = employee_workplaces.EmployeeId ```  ``` addresses.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` addresses.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` addresses.Creator = events.Creator ``` |
| [geo](#geo) | ``` addresses.Creator = geo.Creator ``` |
| [journal](#journal) | ``` addresses.Creator = journal.EmployeeId ```  ``` addresses.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` addresses.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` addresses.Creator = leave_accruals.Employee ```  ``` addresses.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` addresses.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` addresses.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` addresses.Creator = leaves.Employee ```  ``` addresses.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` addresses.Creator = memos.Creator ``` |
| [pay\_periods](#pay-periods) | ``` addresses.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` addresses.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` addresses.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` addresses.Creator = roster_opens.Employee ```  ``` addresses.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` addresses.Creator = roster_swaps.Employee ```  ``` addresses.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` addresses.Creator = rosters.Employee ```  ``` addresses.Creator = rosters.ConfirmBy ```  ``` addresses.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` addresses.Creator = sales_data.Employee ```  ``` addresses.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` addresses.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` addresses.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` addresses.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` addresses.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` addresses.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` addresses.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` addresses.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` addresses.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` addresses.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` addresses.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` addresses.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` addresses.Creator = teams.LeaderEmployee ```  ``` addresses.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` addresses.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` addresses.Creator = timesheets.Employee ```  ``` addresses.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` addresses.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` addresses.Creator = training_records.Employee ```  ``` addresses.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` addresses.Creator = webhooks.Creator ``` |

addresses table schema

|  |
| --- |
| **City**  STRING |
| **ContactName**  STRING |
| **Country**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Format**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Notes**  STRING |
| **Phone**  STRING |
| **PoBox**  STRING |
| **Postcode**  STRING |
| **Saved**  BOOLEAN |
| **State**  STRING |
| **Street1**  STRING |
| **Street2**  STRING |
| **StreetNo**  STRING |
| **SuiteNo**  STRING |
| **UnitNo**  STRING |

### categories

The `categories` table contains info about categories.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Category) |

categories table foreign keys

| Join categories with | on |
| --- | --- |
| [employee\_contracts](#employee-contracts) | ``` categories.Id = employee_contracts.EmploymentCategory ```  ``` categories.Creator = employee_contracts.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` categories.Id = employment_conditions.EmploymentCategory ```  ``` categories.Creator = employment_conditions.Creator ``` |
| [addresses](#addresses) | ``` categories.Creator = addresses.Creator ``` |
| [comments](#comments) | ``` categories.Creator = comments.Creator ``` |
| [companies](#companies) | ``` categories.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` categories.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` categories.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` categories.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` categories.Creator = custom_app_data.Employee ```  ``` categories.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` categories.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` categories.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` categories.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` categories.Creator = employee_agreements.EmployeeId ```  ``` categories.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` categories.Creator = employee_appraisal.Creator ```  ``` categories.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` categories.Creator = employee_availability.Employee ```  ``` categories.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` categories.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_history](#employee-history) | ``` categories.Creator = employee_history.EmployeeId ```  ``` categories.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` categories.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` categories.Creator = employee_paycycles.EmployeeId ```  ``` categories.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` categories.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` categories.Creator = employee_salary_opunit_costing.Employee ```  ``` categories.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` categories.Creator = employee_workplaces.EmployeeId ```  ``` categories.Creator = employee_workplaces.Creator ``` |
| [events](#events) | ``` categories.Creator = events.Creator ``` |
| [geo](#geo) | ``` categories.Creator = geo.Creator ``` |
| [journal](#journal) | ``` categories.Creator = journal.EmployeeId ```  ``` categories.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` categories.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` categories.Creator = leave_accruals.Employee ```  ``` categories.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` categories.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` categories.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` categories.Creator = leaves.Employee ```  ``` categories.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` categories.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` categories.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` categories.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` categories.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` categories.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` categories.Creator = roster_opens.Employee ```  ``` categories.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` categories.Creator = roster_swaps.Employee ```  ``` categories.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` categories.Creator = rosters.Employee ```  ``` categories.Creator = rosters.ConfirmBy ```  ``` categories.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` categories.Creator = sales_data.Employee ```  ``` categories.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` categories.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` categories.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` categories.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` categories.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` categories.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` categories.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` categories.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` categories.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` categories.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` categories.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` categories.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` categories.Creator = teams.LeaderEmployee ```  ``` categories.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` categories.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` categories.Creator = timesheets.Employee ```  ``` categories.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` categories.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` categories.Creator = training_records.Employee ```  ``` categories.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` categories.Creator = webhooks.Creator ``` |

categories table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **SortOrder**  INTEGER |
| **Stafflog**  BOOLEAN |
| **System**  BOOLEAN |
| **category**  STRING |
| **group**  STRING |

### comments

The `comments` table contains info about comments.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Comment) |

comments table foreign keys

| Join comments with | on |
| --- | --- |
| [addresses](#addresses) | ``` comments.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` comments.Creator = categories.Creator ``` |
| [companies](#companies) | ``` comments.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` comments.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` comments.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` comments.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` comments.Creator = custom_app_data.Employee ```  ``` comments.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` comments.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` comments.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` comments.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` comments.Creator = employee_agreements.EmployeeId ```  ``` comments.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` comments.Creator = employee_appraisal.Creator ```  ``` comments.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` comments.Creator = employee_availability.Employee ```  ``` comments.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` comments.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` comments.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` comments.Creator = employee_history.EmployeeId ```  ``` comments.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` comments.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` comments.Creator = employee_paycycles.EmployeeId ```  ``` comments.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` comments.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` comments.Creator = employee_salary_opunit_costing.Employee ```  ``` comments.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` comments.Creator = employee_workplaces.EmployeeId ```  ``` comments.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` comments.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` comments.Creator = events.Creator ``` |
| [geo](#geo) | ``` comments.Creator = geo.Creator ``` |
| [journal](#journal) | ``` comments.Creator = journal.EmployeeId ```  ``` comments.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` comments.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` comments.Creator = leave_accruals.Employee ```  ``` comments.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` comments.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` comments.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` comments.Creator = leaves.Employee ```  ``` comments.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` comments.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` comments.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` comments.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` comments.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` comments.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` comments.Creator = roster_opens.Employee ```  ``` comments.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` comments.Creator = roster_swaps.Employee ```  ``` comments.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` comments.Creator = rosters.Employee ```  ``` comments.Creator = rosters.ConfirmBy ```  ``` comments.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` comments.Creator = sales_data.Employee ```  ``` comments.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` comments.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` comments.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` comments.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` comments.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` comments.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` comments.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` comments.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` comments.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` comments.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` comments.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` comments.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` comments.Creator = teams.LeaderEmployee ```  ``` comments.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` comments.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` comments.Creator = timesheets.Employee ```  ``` comments.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` comments.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` comments.Creator = training_records.Employee ```  ``` comments.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` comments.Creator = webhooks.Creator ``` |

comments table schema

|  |
| --- |
| **Comment**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **IgnorePermission**  BOOLEAN |
| **InFeed**  BOOLEAN |
| **Modified**  DATE-TIME |
| **Orm**  STRING |
| **RecId**  INTEGER |

### companies

The `companies` table contains info about companies.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Company) |

companies table foreign keys

| Join companies with | on |
| --- | --- |
| [addresses](#addresses) | ``` companies.Address = addresses.Id ```  ``` companies.Creator = addresses.Creator ``` |
| [employee\_history](#employee-history) | ``` companies.Address = employee_history.MainAddress ```  ``` companies.Address = employee_history.PostalAddress ```  ``` companies.Address = employee_history.EmergencyAddress ```  ``` companies.Id = employee_history.Company ```  ``` companies.ParentCompany = employee_history.Company ```  ``` companies.Creator = employee_history.EmployeeId ```  ``` companies.Creator = employee_history.Creator ``` |
| [operational\_units](#operational-units) | ``` companies.Address = operational_units.Address ```  ``` companies.Contact = operational_units.Contact ```  ``` companies.Creator = operational_units.Creator ``` |
| [company\_periods](#company-periods) | ``` companies.Id = company_periods.Company ```  ``` companies.ParentCompany = company_periods.Company ```  ``` companies.Creator = company_periods.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` companies.Id = employee_workplaces.Company ```  ``` companies.ParentCompany = employee_workplaces.Company ```  ``` companies.Creator = employee_workplaces.EmployeeId ```  ``` companies.Creator = employee_workplaces.Creator ``` |
| [kiosks](#kiosks) | ``` companies.Id = kiosks.Company ```  ``` companies.ParentCompany = kiosks.Company ```  ``` companies.Creator = kiosks.Creator ``` |
| [leaves](#leaves) | ``` companies.Id = leaves.Company ```  ``` companies.ParentCompany = leaves.Company ```  ``` companies.Creator = leaves.Employee ```  ``` companies.Creator = leaves.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` companies.Id = system_usage_tracking.CompanyId ```  ``` companies.ParentCompany = system_usage_tracking.CompanyId ```  ``` companies.Creator = system_usage_tracking.Creator ``` |
| [contacts](#contacts) | ``` companies.Contact = contacts.Id ```  ``` companies.Creator = contacts.Creator ``` |
| [categories](#categories) | ``` companies.Creator = categories.Creator ``` |
| [comments](#comments) | ``` companies.Creator = comments.Creator ``` |
| [countries](#countries) | ``` companies.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` companies.Creator = custom_app_data.Employee ```  ``` companies.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` companies.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` companies.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` companies.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` companies.Creator = employee_agreements.EmployeeId ```  ``` companies.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` companies.Creator = employee_appraisal.Creator ```  ``` companies.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` companies.Creator = employee_availability.Employee ```  ``` companies.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` companies.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` companies.Creator = employee_contracts.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` companies.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` companies.Creator = employee_paycycles.EmployeeId ```  ``` companies.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` companies.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` companies.Creator = employee_salary_opunit_costing.Employee ```  ``` companies.Creator = employee_salary_opunit_costing.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` companies.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` companies.Creator = events.Creator ``` |
| [geo](#geo) | ``` companies.Creator = geo.Creator ``` |
| [journal](#journal) | ``` companies.Creator = journal.EmployeeId ```  ``` companies.Creator = journal.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` companies.Creator = leave_accruals.Employee ```  ``` companies.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` companies.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` companies.Creator = leave_rules.Creator ``` |
| [memos](#memos) | ``` companies.Creator = memos.Creator ``` |
| [pay\_periods](#pay-periods) | ``` companies.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` companies.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` companies.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` companies.Creator = roster_opens.Employee ```  ``` companies.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` companies.Creator = roster_swaps.Employee ```  ``` companies.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` companies.Creator = rosters.Employee ```  ``` companies.Creator = rosters.ConfirmBy ```  ``` companies.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` companies.Creator = sales_data.Employee ```  ``` companies.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` companies.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` companies.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` companies.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` companies.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` companies.Creator = system_usage_balances.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` companies.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` companies.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` companies.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` companies.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` companies.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` companies.Creator = teams.LeaderEmployee ```  ``` companies.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` companies.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` companies.Creator = timesheets.Employee ```  ``` companies.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` companies.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` companies.Creator = training_records.Employee ```  ``` companies.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` companies.Creator = webhooks.Creator ``` |

companies table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **Address**  INTEGER |
| **BusinessNumber**  STRING |
| **Code**  STRING |
| **CompanyName**  STRING |
| **CompanyNumber**  STRING |
| **Contact**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **IsPayrollEntity**  BOOLEAN |
| **IsWorkplace**  BOOLEAN |
| **Modified**  DATE-TIME |
| **ParentCompany**  INTEGER |
| **PayrollExportCode**  INTEGER |
| **Portfolio**  INTEGER |
| **TradingName**  STRING |

### company\_periods

The `company_periods` table contains info about company periods.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/CompanyPeriod) |

company\_periods table foreign keys

| Join company\_periods with | on |
| --- | --- |
| [companies](#companies) | ``` company_periods.Company = companies.Id ```  ``` company_periods.Company = companies.ParentCompany ```  ``` company_periods.Creator = companies.Creator ``` |
| [employee\_history](#employee-history) | ``` company_periods.Company = employee_history.Company ```  ``` company_periods.Creator = employee_history.EmployeeId ```  ``` company_periods.Creator = employee_history.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` company_periods.Company = employee_workplaces.Company ```  ``` company_periods.Creator = employee_workplaces.EmployeeId ```  ``` company_periods.Creator = employee_workplaces.Creator ``` |
| [kiosks](#kiosks) | ``` company_periods.Company = kiosks.Company ```  ``` company_periods.Creator = kiosks.Creator ``` |
| [leaves](#leaves) | ``` company_periods.Company = leaves.Company ```  ``` company_periods.Creator = leaves.Employee ```  ``` company_periods.Creator = leaves.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` company_periods.Company = system_usage_tracking.CompanyId ```  ``` company_periods.Creator = system_usage_tracking.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` company_periods.Id = employee_paycycles.PeriodId ```  ``` company_periods.Creator = employee_paycycles.EmployeeId ```  ``` company_periods.Creator = employee_paycycles.Creator ``` |
| [addresses](#addresses) | ``` company_periods.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` company_periods.Creator = categories.Creator ``` |
| [comments](#comments) | ``` company_periods.Creator = comments.Creator ``` |
| [contacts](#contacts) | ``` company_periods.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` company_periods.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` company_periods.Creator = custom_app_data.Employee ```  ``` company_periods.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` company_periods.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` company_periods.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` company_periods.Creator = employee_agreement_history.Creator ```  ``` company_periods.PayPeriod = employee_agreement_history.PayPeriod ``` |
| [employee\_agreements](#employee-agreements) | ``` company_periods.Creator = employee_agreements.EmployeeId ```  ``` company_periods.Creator = employee_agreements.Creator ```  ``` company_periods.PayPeriod = employee_agreements.PayPeriod ``` |
| [employee\_appraisal](#employee-appraisal) | ``` company_periods.Creator = employee_appraisal.Creator ```  ``` company_periods.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` company_periods.Creator = employee_availability.Employee ```  ``` company_periods.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` company_periods.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` company_periods.Creator = employee_contracts.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` company_periods.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_roles](#employee-roles) | ``` company_periods.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` company_periods.Creator = employee_salary_opunit_costing.Employee ```  ``` company_periods.Creator = employee_salary_opunit_costing.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` company_periods.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` company_periods.Creator = events.Creator ``` |
| [geo](#geo) | ``` company_periods.Creator = geo.Creator ``` |
| [journal](#journal) | ``` company_periods.Creator = journal.EmployeeId ```  ``` company_periods.Creator = journal.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` company_periods.Creator = leave_accruals.Employee ```  ``` company_periods.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` company_periods.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` company_periods.Creator = leave_rules.Creator ``` |
| [memos](#memos) | ``` company_periods.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` company_periods.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` company_periods.Creator = pay_periods.Creator ```  ``` company_periods.PayPeriod = pay_periods.Id ``` |
| [pay\_rules](#pay-rules) | ``` company_periods.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` company_periods.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` company_periods.Creator = roster_opens.Employee ```  ``` company_periods.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` company_periods.Creator = roster_swaps.Employee ```  ``` company_periods.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` company_periods.Creator = rosters.Employee ```  ``` company_periods.Creator = rosters.ConfirmBy ```  ``` company_periods.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` company_periods.Creator = sales_data.Employee ```  ``` company_periods.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` company_periods.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` company_periods.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` company_periods.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` company_periods.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` company_periods.Creator = system_usage_balances.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` company_periods.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` company_periods.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` company_periods.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` company_periods.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` company_periods.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` company_periods.Creator = teams.LeaderEmployee ```  ``` company_periods.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` company_periods.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` company_periods.Creator = timesheets.Employee ```  ``` company_periods.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` company_periods.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` company_periods.Creator = training_records.Employee ```  ``` company_periods.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` company_periods.Creator = webhooks.Creator ``` |

company\_periods table schema

|  |
| --- |
| **Company**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **DateEnd**  DATE |
| **DateStart**  DATE |
| **End**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **PayPeriod**  INTEGER |
| **Start**  INTEGER |

### contacts

The `contacts` table contains info about contacts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Contact) |

contacts table foreign keys

| Join contacts with | on |
| --- | --- |
| [companies](#companies) | ``` contacts.Id = companies.Contact ```  ``` contacts.Creator = companies.Creator ``` |
| [operational\_units](#operational-units) | ``` contacts.Id = operational_units.Contact ```  ``` contacts.Creator = operational_units.Creator ``` |
| [addresses](#addresses) | ``` contacts.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` contacts.Creator = categories.Creator ``` |
| [comments](#comments) | ``` contacts.Creator = comments.Creator ``` |
| [company\_periods](#company-periods) | ``` contacts.Creator = company_periods.Creator ``` |
| [countries](#countries) | ``` contacts.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` contacts.Creator = custom_app_data.Employee ```  ``` contacts.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` contacts.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` contacts.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` contacts.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` contacts.Creator = employee_agreements.EmployeeId ```  ``` contacts.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` contacts.Creator = employee_appraisal.Creator ```  ``` contacts.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` contacts.Creator = employee_availability.Employee ```  ``` contacts.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` contacts.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` contacts.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` contacts.Creator = employee_history.EmployeeId ```  ``` contacts.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` contacts.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` contacts.Creator = employee_paycycles.EmployeeId ```  ``` contacts.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` contacts.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` contacts.Creator = employee_salary_opunit_costing.Employee ```  ``` contacts.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` contacts.Creator = employee_workplaces.EmployeeId ```  ``` contacts.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` contacts.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` contacts.Creator = events.Creator ``` |
| [geo](#geo) | ``` contacts.Creator = geo.Creator ``` |
| [journal](#journal) | ``` contacts.Creator = journal.EmployeeId ```  ``` contacts.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` contacts.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` contacts.Creator = leave_accruals.Employee ```  ``` contacts.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` contacts.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` contacts.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` contacts.Creator = leaves.Employee ```  ``` contacts.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` contacts.Creator = memos.Creator ``` |
| [pay\_periods](#pay-periods) | ``` contacts.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` contacts.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` contacts.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` contacts.Creator = roster_opens.Employee ```  ``` contacts.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` contacts.Creator = roster_swaps.Employee ```  ``` contacts.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` contacts.Creator = rosters.Employee ```  ``` contacts.Creator = rosters.ConfirmBy ```  ``` contacts.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` contacts.Creator = sales_data.Employee ```  ``` contacts.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` contacts.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` contacts.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` contacts.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` contacts.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` contacts.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` contacts.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` contacts.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` contacts.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` contacts.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` contacts.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` contacts.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` contacts.Creator = teams.LeaderEmployee ```  ``` contacts.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` contacts.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` contacts.Creator = timesheets.Employee ```  ``` contacts.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` contacts.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` contacts.Creator = training_records.Employee ```  ``` contacts.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` contacts.Creator = webhooks.Creator ``` |

contacts table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Email1**  STRING |
| **Email1Type**  STRING |
| **Email2**  STRING |
| **Email2Type**  STRING |
| **Fax**  STRING |
| **Id**  INTEGER |
| **Im1**  STRING |
| **Im1Type**  STRING |
| **Im2**  STRING |
| **Im2Type**  STRING |
| **Modified**  DATE-TIME |
| **Notes**  STRING |
| **Phone1**  STRING |
| **Phone1Type**  STRING |
| **Phone2**  STRING |
| **Phone2Type**  STRING |
| **Phone3**  STRING |
| **Phone3Type**  STRING |
| **PrimaryEmail**  INTEGER |
| **PrimaryPhone**  INTEGER |
| **Saved**  BOOLEAN |
| **Web**  STRING |

### countries

The `countries` table contains info about countries.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Country) |

countries table foreign keys

| Join countries with | on |
| --- | --- |
| [geo](#geo) | ``` countries.Id = geo.Country ```  ``` countries.Creator = geo.Creator ``` |
| [states](#states) | ``` countries.Id = states.Country ```  ``` countries.Creator = states.Creator ``` |
| [addresses](#addresses) | ``` countries.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` countries.Creator = categories.Creator ``` |
| [comments](#comments) | ``` countries.Creator = comments.Creator ``` |
| [companies](#companies) | ``` countries.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` countries.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` countries.Creator = contacts.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` countries.Creator = custom_app_data.Employee ```  ``` countries.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` countries.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` countries.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` countries.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` countries.Creator = employee_agreements.EmployeeId ```  ``` countries.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` countries.Creator = employee_appraisal.Creator ```  ``` countries.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` countries.Creator = employee_availability.Employee ```  ``` countries.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` countries.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` countries.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` countries.Creator = employee_history.EmployeeId ```  ``` countries.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` countries.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` countries.Creator = employee_paycycles.EmployeeId ```  ``` countries.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` countries.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` countries.Creator = employee_salary_opunit_costing.Employee ```  ``` countries.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` countries.Creator = employee_workplaces.EmployeeId ```  ``` countries.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` countries.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` countries.Creator = events.Creator ``` |
| [journal](#journal) | ``` countries.Creator = journal.EmployeeId ```  ``` countries.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` countries.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` countries.Creator = leave_accruals.Employee ```  ``` countries.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` countries.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` countries.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` countries.Creator = leaves.Employee ```  ``` countries.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` countries.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` countries.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` countries.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` countries.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` countries.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` countries.Creator = roster_opens.Employee ```  ``` countries.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` countries.Creator = roster_swaps.Employee ```  ``` countries.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` countries.Creator = rosters.Employee ```  ``` countries.Creator = rosters.ConfirmBy ```  ``` countries.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` countries.Creator = sales_data.Employee ```  ``` countries.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` countries.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` countries.Creator = sms_logs.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` countries.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` countries.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` countries.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` countries.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` countries.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` countries.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` countries.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` countries.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` countries.Creator = teams.LeaderEmployee ```  ``` countries.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` countries.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` countries.Creator = timesheets.Employee ```  ``` countries.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` countries.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` countries.Creator = training_records.Employee ```  ``` countries.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` countries.Creator = webhooks.Creator ``` |

countries table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **Code**  STRING |
| **CodeA3**  STRING |
| **Country**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **PhoneDisplayPreg**  STRING |
| **Region**  STRING |
| **SortOrder**  INTEGER |
| **ZipVAlidatePreg**  STRING |

### custom\_app\_data

The `custom_app_data` table contains info about custom app data.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/CustomAppData) |

custom\_app\_data table foreign keys

| Join custom\_app\_data with | on |
| --- | --- |
| [addresses](#addresses) | ``` custom_app_data.Employee = addresses.Creator ```  ``` custom_app_data.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` custom_app_data.Employee = categories.Creator ```  ``` custom_app_data.Creator = categories.Creator ``` |
| [comments](#comments) | ``` custom_app_data.Employee = comments.Creator ```  ``` custom_app_data.Creator = comments.Creator ``` |
| [companies](#companies) | ``` custom_app_data.Employee = companies.Creator ```  ``` custom_app_data.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` custom_app_data.Employee = company_periods.Creator ```  ``` custom_app_data.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` custom_app_data.Employee = contacts.Creator ```  ``` custom_app_data.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` custom_app_data.Employee = countries.Creator ```  ``` custom_app_data.Creator = countries.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` custom_app_data.Employee = custom_field_data.Creator ```  ``` custom_app_data.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` custom_app_data.Employee = custom_fields.Creator ```  ``` custom_app_data.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` custom_app_data.Employee = employee_agreement_history.Creator ```  ``` custom_app_data.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` custom_app_data.Employee = employee_agreements.EmployeeId ```  ``` custom_app_data.Creator = employee_agreements.EmployeeId ```  ``` custom_app_data.Employee = employee_agreements.Creator ```  ``` custom_app_data.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` custom_app_data.Employee = employee_appraisal.Creator ```  ``` custom_app_data.Creator = employee_appraisal.Creator ```  ``` custom_app_data.Employee = employee_appraisal.Employee ```  ``` custom_app_data.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` custom_app_data.Employee = employee_availability.Employee ```  ``` custom_app_data.Creator = employee_availability.Employee ```  ``` custom_app_data.Employee = employee_availability.Creator ```  ``` custom_app_data.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` custom_app_data.Employee = employee_contract_leave_rules.Creator ```  ``` custom_app_data.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` custom_app_data.Employee = employee_contracts.Creator ```  ``` custom_app_data.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` custom_app_data.Employee = employee_history.EmployeeId ```  ``` custom_app_data.Creator = employee_history.EmployeeId ```  ``` custom_app_data.Employee = employee_history.Creator ```  ``` custom_app_data.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` custom_app_data.Employee = employee_paycycle_returns.Creator ```  ``` custom_app_data.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` custom_app_data.Employee = employee_paycycles.EmployeeId ```  ``` custom_app_data.Creator = employee_paycycles.EmployeeId ```  ``` custom_app_data.Employee = employee_paycycles.Creator ```  ``` custom_app_data.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` custom_app_data.Employee = employee_roles.Creator ```  ``` custom_app_data.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` custom_app_data.Employee = employee_salary_opunit_costing.Employee ```  ``` custom_app_data.Creator = employee_salary_opunit_costing.Employee ```  ``` custom_app_data.Employee = employee_salary_opunit_costing.Creator ```  ``` custom_app_data.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` custom_app_data.Employee = employee_workplaces.EmployeeId ```  ``` custom_app_data.Creator = employee_workplaces.EmployeeId ```  ``` custom_app_data.Employee = employee_workplaces.Creator ```  ``` custom_app_data.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` custom_app_data.Employee = employment_conditions.Creator ```  ``` custom_app_data.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` custom_app_data.Employee = events.Creator ```  ``` custom_app_data.Creator = events.Creator ``` |
| [geo](#geo) | ``` custom_app_data.Employee = geo.Creator ```  ``` custom_app_data.Creator = geo.Creator ``` |
| [journal](#journal) | ``` custom_app_data.Employee = journal.EmployeeId ```  ``` custom_app_data.Creator = journal.EmployeeId ```  ``` custom_app_data.Employee = journal.Creator ```  ``` custom_app_data.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` custom_app_data.Employee = kiosks.Creator ```  ``` custom_app_data.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` custom_app_data.Employee = leave_accruals.Employee ```  ``` custom_app_data.Creator = leave_accruals.Employee ```  ``` custom_app_data.Employee = leave_accruals.Creator ```  ``` custom_app_data.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` custom_app_data.Employee = leave_pay_lines.Creator ```  ``` custom_app_data.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` custom_app_data.Employee = leave_rules.Creator ```  ``` custom_app_data.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` custom_app_data.Employee = leaves.Employee ```  ``` custom_app_data.Creator = leaves.Employee ```  ``` custom_app_data.Employee = leaves.Creator ```  ``` custom_app_data.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` custom_app_data.Employee = memos.Creator ```  ``` custom_app_data.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` custom_app_data.Employee = operational_units.Creator ```  ``` custom_app_data.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` custom_app_data.Employee = pay_periods.Creator ```  ``` custom_app_data.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` custom_app_data.Employee = pay_rules.Creator ```  ``` custom_app_data.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` custom_app_data.Employee = public_holidays.Creator ```  ``` custom_app_data.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` custom_app_data.Employee = roster_opens.Employee ```  ``` custom_app_data.Creator = roster_opens.Employee ```  ``` custom_app_data.Employee = roster_opens.Creator ```  ``` custom_app_data.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` custom_app_data.Employee = roster_swaps.Employee ```  ``` custom_app_data.Creator = roster_swaps.Employee ```  ``` custom_app_data.Employee = roster_swaps.Creator ```  ``` custom_app_data.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` custom_app_data.Employee = rosters.Employee ```  ``` custom_app_data.Creator = rosters.Employee ```  ``` custom_app_data.Employee = rosters.ConfirmBy ```  ``` custom_app_data.Creator = rosters.ConfirmBy ```  ``` custom_app_data.Employee = rosters.Creator ```  ``` custom_app_data.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` custom_app_data.Employee = sales_data.Employee ```  ``` custom_app_data.Creator = sales_data.Employee ```  ``` custom_app_data.Employee = sales_data.Creator ```  ``` custom_app_data.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` custom_app_data.Employee = schedules.Creator ```  ``` custom_app_data.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` custom_app_data.Employee = sms_logs.Creator ```  ``` custom_app_data.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` custom_app_data.Employee = states.Creator ```  ``` custom_app_data.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` custom_app_data.Employee = stress_profiles.Creator ```  ``` custom_app_data.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` custom_app_data.Employee = system_usage_balances.Creator ```  ``` custom_app_data.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` custom_app_data.Employee = system_usage_tracking.Creator ```  ``` custom_app_data.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` custom_app_data.Employee = task_group_setups.Creator ```  ``` custom_app_data.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` custom_app_data.Employee = task_groups.Creator ```  ``` custom_app_data.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` custom_app_data.Employee = task_opunit_configs.Creator ```  ``` custom_app_data.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` custom_app_data.Employee = task_setups.Creator ```  ``` custom_app_data.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` custom_app_data.Employee = tasks.Creator ```  ``` custom_app_data.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` custom_app_data.Employee = teams.LeaderEmployee ```  ``` custom_app_data.Creator = teams.LeaderEmployee ```  ``` custom_app_data.Employee = teams.Creator ```  ``` custom_app_data.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` custom_app_data.Employee = timesheet_pay_returns.Creator ```  ``` custom_app_data.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` custom_app_data.Employee = timesheets.Employee ```  ``` custom_app_data.Creator = timesheets.Employee ```  ``` custom_app_data.Employee = timesheets.Creator ```  ``` custom_app_data.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` custom_app_data.Employee = training_modules.Creator ```  ``` custom_app_data.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` custom_app_data.Employee = training_records.Employee ```  ``` custom_app_data.Creator = training_records.Employee ```  ``` custom_app_data.Employee = training_records.Creator ```  ``` custom_app_data.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` custom_app_data.Employee = webhooks.Creator ```  ``` custom_app_data.Creator = webhooks.Creator ``` |

custom\_app\_data table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Data**  STRING |
| **Deleted**  BOOLEAN |
| **DocumentId**  STRING |
| **Employee**  INTEGER |
| **Id**  INTEGER |
| **KeyInt**  INTEGER |
| **KeyString**  STRING |
| **Label**  STRING |
| **Modified**  DATE-TIME |
| **OperationalUnit**  INTEGER |
| **Permission**  STRING |

### custom\_field\_data

The `custom_field_data` table contains info about custom field data.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/CustomFieldData) |

custom\_field\_data table foreign keys

| Join custom\_field\_data with | on |
| --- | --- |
| [timesheets](#timesheets) | ``` custom_field_data.Id = timesheets.CustomFieldData ```  ``` custom_field_data.Creator = timesheets.Employee ```  ``` custom_field_data.Creator = timesheets.Creator ``` |
| [addresses](#addresses) | ``` custom_field_data.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` custom_field_data.Creator = categories.Creator ``` |
| [comments](#comments) | ``` custom_field_data.Creator = comments.Creator ``` |
| [companies](#companies) | ``` custom_field_data.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` custom_field_data.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` custom_field_data.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` custom_field_data.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` custom_field_data.Creator = custom_app_data.Employee ```  ``` custom_field_data.Creator = custom_app_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` custom_field_data.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` custom_field_data.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` custom_field_data.Creator = employee_agreements.EmployeeId ```  ``` custom_field_data.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` custom_field_data.Creator = employee_appraisal.Creator ```  ``` custom_field_data.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` custom_field_data.Creator = employee_availability.Employee ```  ``` custom_field_data.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` custom_field_data.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` custom_field_data.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` custom_field_data.Creator = employee_history.EmployeeId ```  ``` custom_field_data.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` custom_field_data.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` custom_field_data.Creator = employee_paycycles.EmployeeId ```  ``` custom_field_data.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` custom_field_data.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` custom_field_data.Creator = employee_salary_opunit_costing.Employee ```  ``` custom_field_data.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` custom_field_data.Creator = employee_workplaces.EmployeeId ```  ``` custom_field_data.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` custom_field_data.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` custom_field_data.Creator = events.Creator ``` |
| [geo](#geo) | ``` custom_field_data.Creator = geo.Creator ``` |
| [journal](#journal) | ``` custom_field_data.Creator = journal.EmployeeId ```  ``` custom_field_data.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` custom_field_data.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` custom_field_data.Creator = leave_accruals.Employee ```  ``` custom_field_data.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` custom_field_data.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` custom_field_data.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` custom_field_data.Creator = leaves.Employee ```  ``` custom_field_data.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` custom_field_data.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` custom_field_data.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` custom_field_data.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` custom_field_data.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` custom_field_data.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` custom_field_data.Creator = roster_opens.Employee ```  ``` custom_field_data.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` custom_field_data.Creator = roster_swaps.Employee ```  ``` custom_field_data.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` custom_field_data.Creator = rosters.Employee ```  ``` custom_field_data.Creator = rosters.ConfirmBy ```  ``` custom_field_data.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` custom_field_data.Creator = sales_data.Employee ```  ``` custom_field_data.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` custom_field_data.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` custom_field_data.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` custom_field_data.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` custom_field_data.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` custom_field_data.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` custom_field_data.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` custom_field_data.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` custom_field_data.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` custom_field_data.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` custom_field_data.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` custom_field_data.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` custom_field_data.Creator = teams.LeaderEmployee ```  ``` custom_field_data.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` custom_field_data.Creator = timesheet_pay_returns.Creator ``` |
| [training\_modules](#training-modules) | ``` custom_field_data.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` custom_field_data.Creator = training_records.Employee ```  ``` custom_field_data.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` custom_field_data.Creator = webhooks.Creator ``` |

custom\_field\_data table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **F01**  STRING |
| **F02**  STRING |
| **F03**  STRING |
| **F04**  STRING |
| **F05**  STRING |
| **F06**  STRING |
| **F07**  STRING |
| **F08**  STRING |
| **F09**  STRING |
| **F10**  STRING |
| **F11**  STRING |
| **F12**  STRING |
| **F13**  STRING |
| **F14**  STRING |
| **F15**  STRING |
| **F16**  STRING |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **System**  STRING |

### custom\_fields

The `custom_fields` table contains info about

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/CustomField) |

custom\_fields table foreign keys

| Join custom\_fields with | on |
| --- | --- |
| [addresses](#addresses) | ``` custom_fields.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` custom_fields.Creator = categories.Creator ``` |
| [comments](#comments) | ``` custom_fields.Creator = comments.Creator ``` |
| [companies](#companies) | ``` custom_fields.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` custom_fields.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` custom_fields.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` custom_fields.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` custom_fields.Creator = custom_app_data.Employee ```  ``` custom_fields.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` custom_fields.Creator = custom_field_data.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` custom_fields.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` custom_fields.Creator = employee_agreements.EmployeeId ```  ``` custom_fields.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` custom_fields.Creator = employee_appraisal.Creator ```  ``` custom_fields.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` custom_fields.Creator = employee_availability.Employee ```  ``` custom_fields.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` custom_fields.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` custom_fields.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` custom_fields.Creator = employee_history.EmployeeId ```  ``` custom_fields.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` custom_fields.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` custom_fields.Creator = employee_paycycles.EmployeeId ```  ``` custom_fields.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` custom_fields.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` custom_fields.Creator = employee_salary_opunit_costing.Employee ```  ``` custom_fields.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` custom_fields.Creator = employee_workplaces.EmployeeId ```  ``` custom_fields.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` custom_fields.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` custom_fields.Creator = events.Creator ``` |
| [geo](#geo) | ``` custom_fields.Creator = geo.Creator ``` |
| [journal](#journal) | ``` custom_fields.Creator = journal.EmployeeId ```  ``` custom_fields.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` custom_fields.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` custom_fields.Creator = leave_accruals.Employee ```  ``` custom_fields.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` custom_fields.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` custom_fields.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` custom_fields.Creator = leaves.Employee ```  ``` custom_fields.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` custom_fields.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` custom_fields.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` custom_fields.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` custom_fields.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` custom_fields.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` custom_fields.Creator = roster_opens.Employee ```  ``` custom_fields.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` custom_fields.Creator = roster_swaps.Employee ```  ``` custom_fields.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` custom_fields.Creator = rosters.Employee ```  ``` custom_fields.Creator = rosters.ConfirmBy ```  ``` custom_fields.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` custom_fields.Creator = sales_data.Employee ```  ``` custom_fields.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` custom_fields.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` custom_fields.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` custom_fields.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` custom_fields.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` custom_fields.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` custom_fields.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` custom_fields.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` custom_fields.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` custom_fields.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` custom_fields.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` custom_fields.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` custom_fields.Creator = teams.LeaderEmployee ```  ``` custom_fields.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` custom_fields.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` custom_fields.Creator = timesheets.Employee ```  ``` custom_fields.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` custom_fields.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` custom_fields.Creator = training_records.Employee ```  ``` custom_fields.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` custom_fields.Creator = webhooks.Creator ``` |

custom\_fields table schema

|  |
| --- |
| **ApiName**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Default**  STRING |
| **DeputyField**  STRING |
| **Helptext**  STRING |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Name**  STRING |
| **SortOrder**  INTEGER |
| **System**  STRING |
| **Type**  INTEGER |
| **Validation**  STRING |
| **ValueList**  STRING |

### employee\_agreement\_history

The `employee_agreement_history` table contains info about

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/EmployeeAgreementHistory) |

employee\_agreement\_history table foreign keys

| Join employee\_agreement\_history with | on |
| --- | --- |
| [addresses](#addresses) | ``` employee_agreement_history.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` employee_agreement_history.Creator = categories.Creator ``` |
| [comments](#comments) | ``` employee_agreement_history.Creator = comments.Creator ``` |
| [companies](#companies) | ``` employee_agreement_history.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` employee_agreement_history.Creator = company_periods.Creator ```  ``` employee_agreement_history.PayPeriod = company_periods.PayPeriod ``` |
| [contacts](#contacts) | ``` employee_agreement_history.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` employee_agreement_history.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employee_agreement_history.Creator = custom_app_data.Employee ```  ``` employee_agreement_history.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employee_agreement_history.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employee_agreement_history.Creator = custom_fields.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` employee_agreement_history.Creator = employee_agreements.EmployeeId ```  ``` employee_agreement_history.Creator = employee_agreements.Creator ```  ``` employee_agreement_history.Id = employee_agreements.HistoryId ```  ``` employee_agreement_history.AgreementId = employee_agreements.Id ```  ``` employee_agreement_history.Contract = employee_agreements.Contract ```  ``` employee_agreement_history.PayPeriod = employee_agreements.PayPeriod ```  ``` employee_agreement_history.SalaryPayRule = employee_agreements.SalaryPayRule ``` |
| [employee\_appraisal](#employee-appraisal) | ``` employee_agreement_history.Creator = employee_appraisal.Creator ```  ``` employee_agreement_history.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` employee_agreement_history.Creator = employee_availability.Employee ```  ``` employee_agreement_history.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` employee_agreement_history.Creator = employee_contract_leave_rules.Creator ```  ``` employee_agreement_history.Contract = employee_contract_leave_rules.ContractId ```  ``` employee_agreement_history.SalaryPayRule = employee_contract_leave_rules.LoadingPayRule1 ```  ``` employee_agreement_history.SalaryPayRule = employee_contract_leave_rules.LoadingPayRule2 ```  ``` employee_agreement_history.SalaryPayRule = employee_contract_leave_rules.LoadingPayRule3 ``` |
| [employee\_contracts](#employee-contracts) | ``` employee_agreement_history.Creator = employee_contracts.Creator ```  ``` employee_agreement_history.Contract = employee_contracts.Id ```  ``` employee_agreement_history.SalaryPayRule = employee_contracts.BasePayRule ``` |
| [employee\_history](#employee-history) | ``` employee_agreement_history.Creator = employee_history.EmployeeId ```  ``` employee_agreement_history.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` employee_agreement_history.Creator = employee_paycycle_returns.Creator ```  ``` employee_agreement_history.SalaryPayRule = employee_paycycle_returns.PayRule ``` |
| [employee\_paycycles](#employee-paycycles) | ``` employee_agreement_history.Creator = employee_paycycles.EmployeeId ```  ``` employee_agreement_history.Creator = employee_paycycles.Creator ```  ``` employee_agreement_history.Id = employee_paycycles.EmployeeAgreementHistoryId ```  ``` employee_agreement_history.AgreementId = employee_paycycles.EmployeeAgreementId ``` |
| [employee\_roles](#employee-roles) | ``` employee_agreement_history.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` employee_agreement_history.Creator = employee_salary_opunit_costing.Employee ```  ``` employee_agreement_history.Creator = employee_salary_opunit_costing.Creator ```  ``` employee_agreement_history.AgreementId = employee_salary_opunit_costing.EmployeeAgreement ``` |
| [employee\_workplaces](#employee-workplaces) | ``` employee_agreement_history.Creator = employee_workplaces.EmployeeId ```  ``` employee_agreement_history.Creator = employee_workplaces.Creator ```  ``` employee_agreement_history.AgreementId = employee_workplaces.Agreement1 ```  ``` employee_agreement_history.AgreementId = employee_workplaces.Agreement2 ```  ``` employee_agreement_history.AgreementId = employee_workplaces.Agreement3 ``` |
| [employment\_conditions](#employment-conditions) | ``` employee_agreement_history.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` employee_agreement_history.Creator = events.Creator ``` |
| [geo](#geo) | ``` employee_agreement_history.Creator = geo.Creator ``` |
| [journal](#journal) | ``` employee_agreement_history.Creator = journal.EmployeeId ```  ``` employee_agreement_history.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` employee_agreement_history.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employee_agreement_history.Creator = leave_accruals.Employee ```  ``` employee_agreement_history.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employee_agreement_history.Creator = leave_pay_lines.Creator ```  ``` employee_agreement_history.AgreementId = leave_pay_lines.EmployeeAgreement ``` |
| [leave\_rules](#leave-rules) | ``` employee_agreement_history.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` employee_agreement_history.Creator = leaves.Employee ```  ``` employee_agreement_history.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` employee_agreement_history.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` employee_agreement_history.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` employee_agreement_history.Creator = pay_periods.Creator ```  ``` employee_agreement_history.PayPeriod = pay_periods.Id ``` |
| [pay\_rules](#pay-rules) | ``` employee_agreement_history.Creator = pay_rules.Creator ```  ``` employee_agreement_history.SalaryPayRule = pay_rules.Id ``` |
| [public\_holidays](#public-holidays) | ``` employee_agreement_history.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employee_agreement_history.Creator = roster_opens.Employee ```  ``` employee_agreement_history.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employee_agreement_history.Creator = roster_swaps.Employee ```  ``` employee_agreement_history.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employee_agreement_history.Creator = rosters.Employee ```  ``` employee_agreement_history.Creator = rosters.ConfirmBy ```  ``` employee_agreement_history.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` employee_agreement_history.Creator = sales_data.Employee ```  ``` employee_agreement_history.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` employee_agreement_history.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` employee_agreement_history.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` employee_agreement_history.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employee_agreement_history.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employee_agreement_history.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employee_agreement_history.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employee_agreement_history.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employee_agreement_history.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employee_agreement_history.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` employee_agreement_history.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` employee_agreement_history.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` employee_agreement_history.Creator = teams.LeaderEmployee ```  ``` employee_agreement_history.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employee_agreement_history.Creator = timesheet_pay_returns.Creator ```  ``` employee_agreement_history.SalaryPayRule = timesheet_pay_returns.PayRule ``` |
| [timesheets](#timesheets) | ``` employee_agreement_history.Creator = timesheets.Employee ```  ``` employee_agreement_history.Creator = timesheets.Creator ```  ``` employee_agreement_history.AgreementId = timesheets.EmployeeAgreement ``` |
| [training\_modules](#training-modules) | ``` employee_agreement_history.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employee_agreement_history.Creator = training_records.Employee ```  ``` employee_agreement_history.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employee_agreement_history.Creator = webhooks.Creator ``` |

employee\_agreement\_history table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **AgreementId**  INTEGER |
| **CompanyName**  STRING |
| **Contract**  INTEGER |
| **ContractFile**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **EmpType**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **PayPeriod**  INTEGER |
| **PayPoint**  INTEGER |
| **PayrollId**  INTEGER |
| **SalaryPayRule**  INTEGER |
| **StartDate**  DATE |

### employee\_agreements

The `employee_agreements` table contains info about employee agreements.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/EmployeeAgreement) |

employee\_agreements table foreign keys

| Join employee\_agreements with | on |
| --- | --- |
| [addresses](#addresses) | ``` employee_agreements.EmployeeId = addresses.Creator ```  ``` employee_agreements.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` employee_agreements.EmployeeId = categories.Creator ```  ``` employee_agreements.Creator = categories.Creator ``` |
| [comments](#comments) | ``` employee_agreements.EmployeeId = comments.Creator ```  ``` employee_agreements.Creator = comments.Creator ``` |
| [companies](#companies) | ``` employee_agreements.EmployeeId = companies.Creator ```  ``` employee_agreements.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` employee_agreements.EmployeeId = company_periods.Creator ```  ``` employee_agreements.Creator = company_periods.Creator ```  ``` employee_agreements.PayPeriod = company_periods.PayPeriod ``` |
| [contacts](#contacts) | ``` employee_agreements.EmployeeId = contacts.Creator ```  ``` employee_agreements.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` employee_agreements.EmployeeId = countries.Creator ```  ``` employee_agreements.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employee_agreements.EmployeeId = custom_app_data.Employee ```  ``` employee_agreements.Creator = custom_app_data.Employee ```  ``` employee_agreements.EmployeeId = custom_app_data.Creator ```  ``` employee_agreements.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employee_agreements.EmployeeId = custom_field_data.Creator ```  ``` employee_agreements.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employee_agreements.EmployeeId = custom_fields.Creator ```  ``` employee_agreements.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` employee_agreements.EmployeeId = employee_agreement_history.Creator ```  ``` employee_agreements.Creator = employee_agreement_history.Creator ```  ``` employee_agreements.HistoryId = employee_agreement_history.Id ```  ``` employee_agreements.Id = employee_agreement_history.AgreementId ```  ``` employee_agreements.Contract = employee_agreement_history.Contract ```  ``` employee_agreements.PayPeriod = employee_agreement_history.PayPeriod ```  ``` employee_agreements.SalaryPayRule = employee_agreement_history.SalaryPayRule ``` |
| [employee\_appraisal](#employee-appraisal) | ``` employee_agreements.EmployeeId = employee_appraisal.Creator ```  ``` employee_agreements.Creator = employee_appraisal.Creator ```  ``` employee_agreements.EmployeeId = employee_appraisal.Employee ```  ``` employee_agreements.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` employee_agreements.EmployeeId = employee_availability.Employee ```  ``` employee_agreements.Creator = employee_availability.Employee ```  ``` employee_agreements.EmployeeId = employee_availability.Creator ```  ``` employee_agreements.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` employee_agreements.EmployeeId = employee_contract_leave_rules.Creator ```  ``` employee_agreements.Creator = employee_contract_leave_rules.Creator ```  ``` employee_agreements.Contract = employee_contract_leave_rules.ContractId ```  ``` employee_agreements.SalaryPayRule = employee_contract_leave_rules.LoadingPayRule1 ```  ``` employee_agreements.SalaryPayRule = employee_contract_leave_rules.LoadingPayRule2 ```  ``` employee_agreements.SalaryPayRule = employee_contract_leave_rules.LoadingPayRule3 ``` |
| [employee\_contracts](#employee-contracts) | ``` employee_agreements.EmployeeId = employee_contracts.Creator ```  ``` employee_agreements.Creator = employee_contracts.Creator ```  ``` employee_agreements.Contract = employee_contracts.Id ```  ``` employee_agreements.SalaryPayRule = employee_contracts.BasePayRule ``` |
| [employee\_history](#employee-history) | ``` employee_agreements.EmployeeId = employee_history.EmployeeId ```  ``` employee_agreements.Creator = employee_history.EmployeeId ```  ``` employee_agreements.EmployeeId = employee_history.Creator ```  ``` employee_agreements.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` employee_agreements.EmployeeId = employee_paycycle_returns.Creator ```  ``` employee_agreements.Creator = employee_paycycle_returns.Creator ```  ``` employee_agreements.SalaryPayRule = employee_paycycle_returns.PayRule ``` |
| [employee\_paycycles](#employee-paycycles) | ``` employee_agreements.EmployeeId = employee_paycycles.EmployeeId ```  ``` employee_agreements.Creator = employee_paycycles.EmployeeId ```  ``` employee_agreements.EmployeeId = employee_paycycles.Creator ```  ``` employee_agreements.Creator = employee_paycycles.Creator ```  ``` employee_agreements.HistoryId = employee_paycycles.EmployeeAgreementHistoryId ```  ``` employee_agreements.Id = employee_paycycles.EmployeeAgreementId ``` |
| [employee\_roles](#employee-roles) | ``` employee_agreements.EmployeeId = employee_roles.Creator ```  ``` employee_agreements.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` employee_agreements.EmployeeId = employee_salary_opunit_costing.Employee ```  ``` employee_agreements.Creator = employee_salary_opunit_costing.Employee ```  ``` employee_agreements.EmployeeId = employee_salary_opunit_costing.Creator ```  ``` employee_agreements.Creator = employee_salary_opunit_costing.Creator ```  ``` employee_agreements.Id = employee_salary_opunit_costing.EmployeeAgreement ``` |
| [employee\_workplaces](#employee-workplaces) | ``` employee_agreements.EmployeeId = employee_workplaces.EmployeeId ```  ``` employee_agreements.Creator = employee_workplaces.EmployeeId ```  ``` employee_agreements.EmployeeId = employee_workplaces.Creator ```  ``` employee_agreements.Creator = employee_workplaces.Creator ```  ``` employee_agreements.Id = employee_workplaces.Agreement1 ```  ``` employee_agreements.Id = employee_workplaces.Agreement2 ```  ``` employee_agreements.Id = employee_workplaces.Agreement3 ``` |
| [employment\_conditions](#employment-conditions) | ``` employee_agreements.EmployeeId = employment_conditions.Creator ```  ``` employee_agreements.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` employee_agreements.EmployeeId = events.Creator ```  ``` employee_agreements.Creator = events.Creator ``` |
| [geo](#geo) | ``` employee_agreements.EmployeeId = geo.Creator ```  ``` employee_agreements.Creator = geo.Creator ``` |
| [journal](#journal) | ``` employee_agreements.EmployeeId = journal.EmployeeId ```  ``` employee_agreements.Creator = journal.EmployeeId ```  ``` employee_agreements.EmployeeId = journal.Creator ```  ``` employee_agreements.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` employee_agreements.EmployeeId = kiosks.Creator ```  ``` employee_agreements.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employee_agreements.EmployeeId = leave_accruals.Employee ```  ``` employee_agreements.Creator = leave_accruals.Employee ```  ``` employee_agreements.EmployeeId = leave_accruals.Creator ```  ``` employee_agreements.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employee_agreements.EmployeeId = leave_pay_lines.Creator ```  ``` employee_agreements.Creator = leave_pay_lines.Creator ```  ``` employee_agreements.Id = leave_pay_lines.EmployeeAgreement ``` |
| [leave\_rules](#leave-rules) | ``` employee_agreements.EmployeeId = leave_rules.Creator ```  ``` employee_agreements.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` employee_agreements.EmployeeId = leaves.Employee ```  ``` employee_agreements.Creator = leaves.Employee ```  ``` employee_agreements.EmployeeId = leaves.Creator ```  ``` employee_agreements.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` employee_agreements.EmployeeId = memos.Creator ```  ``` employee_agreements.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` employee_agreements.EmployeeId = operational_units.Creator ```  ``` employee_agreements.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` employee_agreements.EmployeeId = pay_periods.Creator ```  ``` employee_agreements.Creator = pay_periods.Creator ```  ``` employee_agreements.PayPeriod = pay_periods.Id ``` |
| [pay\_rules](#pay-rules) | ``` employee_agreements.EmployeeId = pay_rules.Creator ```  ``` employee_agreements.Creator = pay_rules.Creator ```  ``` employee_agreements.SalaryPayRule = pay_rules.Id ``` |
| [public\_holidays](#public-holidays) | ``` employee_agreements.EmployeeId = public_holidays.Creator ```  ``` employee_agreements.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employee_agreements.EmployeeId = roster_opens.Employee ```  ``` employee_agreements.Creator = roster_opens.Employee ```  ``` employee_agreements.EmployeeId = roster_opens.Creator ```  ``` employee_agreements.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employee_agreements.EmployeeId = roster_swaps.Employee ```  ``` employee_agreements.Creator = roster_swaps.Employee ```  ``` employee_agreements.EmployeeId = roster_swaps.Creator ```  ``` employee_agreements.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employee_agreements.EmployeeId = rosters.Employee ```  ``` employee_agreements.Creator = rosters.Employee ```  ``` employee_agreements.EmployeeId = rosters.ConfirmBy ```  ``` employee_agreements.Creator = rosters.ConfirmBy ```  ``` employee_agreements.EmployeeId = rosters.Creator ```  ``` employee_agreements.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` employee_agreements.EmployeeId = sales_data.Employee ```  ``` employee_agreements.Creator = sales_data.Employee ```  ``` employee_agreements.EmployeeId = sales_data.Creator ```  ``` employee_agreements.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` employee_agreements.EmployeeId = schedules.Creator ```  ``` employee_agreements.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` employee_agreements.EmployeeId = sms_logs.Creator ```  ``` employee_agreements.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` employee_agreements.EmployeeId = states.Creator ```  ``` employee_agreements.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employee_agreements.EmployeeId = stress_profiles.Creator ```  ``` employee_agreements.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employee_agreements.EmployeeId = system_usage_balances.Creator ```  ``` employee_agreements.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employee_agreements.EmployeeId = system_usage_tracking.Creator ```  ``` employee_agreements.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employee_agreements.EmployeeId = task_group_setups.Creator ```  ``` employee_agreements.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employee_agreements.EmployeeId = task_groups.Creator ```  ``` employee_agreements.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employee_agreements.EmployeeId = task_opunit_configs.Creator ```  ``` employee_agreements.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` employee_agreements.EmployeeId = task_setups.Creator ```  ``` employee_agreements.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` employee_agreements.EmployeeId = tasks.Creator ```  ``` employee_agreements.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` employee_agreements.EmployeeId = teams.LeaderEmployee ```  ``` employee_agreements.Creator = teams.LeaderEmployee ```  ``` employee_agreements.EmployeeId = teams.Creator ```  ``` employee_agreements.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employee_agreements.EmployeeId = timesheet_pay_returns.Creator ```  ``` employee_agreements.Creator = timesheet_pay_returns.Creator ```  ``` employee_agreements.SalaryPayRule = timesheet_pay_returns.PayRule ``` |
| [timesheets](#timesheets) | ``` employee_agreements.EmployeeId = timesheets.Employee ```  ``` employee_agreements.Creator = timesheets.Employee ```  ``` employee_agreements.EmployeeId = timesheets.Creator ```  ``` employee_agreements.Creator = timesheets.Creator ```  ``` employee_agreements.Id = timesheets.EmployeeAgreement ``` |
| [training\_modules](#training-modules) | ``` employee_agreements.EmployeeId = training_modules.Creator ```  ``` employee_agreements.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employee_agreements.EmployeeId = training_records.Employee ```  ``` employee_agreements.Creator = training_records.Employee ```  ``` employee_agreements.EmployeeId = training_records.Creator ```  ``` employee_agreements.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employee_agreements.EmployeeId = webhooks.Creator ```  ``` employee_agreements.Creator = webhooks.Creator ``` |

employee\_agreements table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **CompanyName**  STRING |
| **Contract**  INTEGER |
| **ContractFile**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **EmpType**  INTEGER |
| **EmployeeId**  INTEGER |
| **HistoryId**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **PayPeriod**  INTEGER |
| **PayPoint**  INTEGER |
| **PayrollId**  INTEGER |
| **SalaryPayRule**  INTEGER |
| **StartDate**  DATE |

### employee\_appraisal

The `employee_appraisal` table contains info about employee appraisals.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/EmployeeAppraisal) |

employee\_appraisal table foreign keys

| Join employee\_appraisal with | on |
| --- | --- |
| [addresses](#addresses) | ``` employee_appraisal.Creator = addresses.Creator ```  ``` employee_appraisal.Employee = addresses.Creator ``` |
| [categories](#categories) | ``` employee_appraisal.Creator = categories.Creator ```  ``` employee_appraisal.Employee = categories.Creator ``` |
| [comments](#comments) | ``` employee_appraisal.Creator = comments.Creator ```  ``` employee_appraisal.Employee = comments.Creator ``` |
| [companies](#companies) | ``` employee_appraisal.Creator = companies.Creator ```  ``` employee_appraisal.Employee = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` employee_appraisal.Creator = company_periods.Creator ```  ``` employee_appraisal.Employee = company_periods.Creator ``` |
| [contacts](#contacts) | ``` employee_appraisal.Creator = contacts.Creator ```  ``` employee_appraisal.Employee = contacts.Creator ``` |
| [countries](#countries) | ``` employee_appraisal.Creator = countries.Creator ```  ``` employee_appraisal.Employee = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employee_appraisal.Creator = custom_app_data.Employee ```  ``` employee_appraisal.Employee = custom_app_data.Employee ```  ``` employee_appraisal.Creator = custom_app_data.Creator ```  ``` employee_appraisal.Employee = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employee_appraisal.Creator = custom_field_data.Creator ```  ``` employee_appraisal.Employee = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employee_appraisal.Creator = custom_fields.Creator ```  ``` employee_appraisal.Employee = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` employee_appraisal.Creator = employee_agreement_history.Creator ```  ``` employee_appraisal.Employee = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` employee_appraisal.Creator = employee_agreements.EmployeeId ```  ``` employee_appraisal.Employee = employee_agreements.EmployeeId ```  ``` employee_appraisal.Creator = employee_agreements.Creator ```  ``` employee_appraisal.Employee = employee_agreements.Creator ``` |
| [employee\_availability](#employee-availability) | ``` employee_appraisal.Creator = employee_availability.Employee ```  ``` employee_appraisal.Employee = employee_availability.Employee ```  ``` employee_appraisal.Creator = employee_availability.Creator ```  ``` employee_appraisal.Employee = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` employee_appraisal.Creator = employee_contract_leave_rules.Creator ```  ``` employee_appraisal.Employee = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` employee_appraisal.Creator = employee_contracts.Creator ```  ``` employee_appraisal.Employee = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` employee_appraisal.Creator = employee_history.EmployeeId ```  ``` employee_appraisal.Employee = employee_history.EmployeeId ```  ``` employee_appraisal.Creator = employee_history.Creator ```  ``` employee_appraisal.Employee = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` employee_appraisal.Creator = employee_paycycle_returns.Creator ```  ``` employee_appraisal.Employee = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` employee_appraisal.Creator = employee_paycycles.EmployeeId ```  ``` employee_appraisal.Employee = employee_paycycles.EmployeeId ```  ``` employee_appraisal.Creator = employee_paycycles.Creator ```  ``` employee_appraisal.Employee = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` employee_appraisal.Creator = employee_roles.Creator ```  ``` employee_appraisal.Employee = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` employee_appraisal.Creator = employee_salary_opunit_costing.Employee ```  ``` employee_appraisal.Employee = employee_salary_opunit_costing.Employee ```  ``` employee_appraisal.Creator = employee_salary_opunit_costing.Creator ```  ``` employee_appraisal.Employee = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` employee_appraisal.Creator = employee_workplaces.EmployeeId ```  ``` employee_appraisal.Employee = employee_workplaces.EmployeeId ```  ``` employee_appraisal.Creator = employee_workplaces.Creator ```  ``` employee_appraisal.Employee = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` employee_appraisal.Creator = employment_conditions.Creator ```  ``` employee_appraisal.Employee = employment_conditions.Creator ``` |
| [events](#events) | ``` employee_appraisal.Creator = events.Creator ```  ``` employee_appraisal.Employee = events.Creator ``` |
| [geo](#geo) | ``` employee_appraisal.Creator = geo.Creator ```  ``` employee_appraisal.Employee = geo.Creator ``` |
| [journal](#journal) | ``` employee_appraisal.Creator = journal.EmployeeId ```  ``` employee_appraisal.Employee = journal.EmployeeId ```  ``` employee_appraisal.Creator = journal.Creator ```  ``` employee_appraisal.Employee = journal.Creator ``` |
| [kiosks](#kiosks) | ``` employee_appraisal.Creator = kiosks.Creator ```  ``` employee_appraisal.Employee = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employee_appraisal.Creator = leave_accruals.Employee ```  ``` employee_appraisal.Employee = leave_accruals.Employee ```  ``` employee_appraisal.Creator = leave_accruals.Creator ```  ``` employee_appraisal.Employee = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employee_appraisal.Creator = leave_pay_lines.Creator ```  ``` employee_appraisal.Employee = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` employee_appraisal.Creator = leave_rules.Creator ```  ``` employee_appraisal.Employee = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` employee_appraisal.Creator = leaves.Employee ```  ``` employee_appraisal.Employee = leaves.Employee ```  ``` employee_appraisal.Creator = leaves.Creator ```  ``` employee_appraisal.Employee = leaves.Creator ``` |
| [memos](#memos) | ``` employee_appraisal.Creator = memos.Creator ```  ``` employee_appraisal.Employee = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` employee_appraisal.Creator = operational_units.Creator ```  ``` employee_appraisal.Employee = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` employee_appraisal.Creator = pay_periods.Creator ```  ``` employee_appraisal.Employee = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` employee_appraisal.Creator = pay_rules.Creator ```  ``` employee_appraisal.Employee = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` employee_appraisal.Creator = public_holidays.Creator ```  ``` employee_appraisal.Employee = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employee_appraisal.Creator = roster_opens.Employee ```  ``` employee_appraisal.Employee = roster_opens.Employee ```  ``` employee_appraisal.Creator = roster_opens.Creator ```  ``` employee_appraisal.Employee = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employee_appraisal.Creator = roster_swaps.Employee ```  ``` employee_appraisal.Employee = roster_swaps.Employee ```  ``` employee_appraisal.Creator = roster_swaps.Creator ```  ``` employee_appraisal.Employee = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employee_appraisal.Creator = rosters.Employee ```  ``` employee_appraisal.Employee = rosters.Employee ```  ``` employee_appraisal.Creator = rosters.ConfirmBy ```  ``` employee_appraisal.Employee = rosters.ConfirmBy ```  ``` employee_appraisal.Creator = rosters.Creator ```  ``` employee_appraisal.Employee = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` employee_appraisal.Creator = sales_data.Employee ```  ``` employee_appraisal.Employee = sales_data.Employee ```  ``` employee_appraisal.Creator = sales_data.Creator ```  ``` employee_appraisal.Employee = sales_data.Creator ``` |
| [schedules](#schedules) | ``` employee_appraisal.Creator = schedules.Creator ```  ``` employee_appraisal.Employee = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` employee_appraisal.Creator = sms_logs.Creator ```  ``` employee_appraisal.Employee = sms_logs.Creator ``` |
| [states](#states) | ``` employee_appraisal.Creator = states.Creator ```  ``` employee_appraisal.Employee = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employee_appraisal.Creator = stress_profiles.Creator ```  ``` employee_appraisal.Employee = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employee_appraisal.Creator = system_usage_balances.Creator ```  ``` employee_appraisal.Employee = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employee_appraisal.Creator = system_usage_tracking.Creator ```  ``` employee_appraisal.Employee = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employee_appraisal.Creator = task_group_setups.Creator ```  ``` employee_appraisal.Employee = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employee_appraisal.Creator = task_groups.Creator ```  ``` employee_appraisal.Employee = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employee_appraisal.Creator = task_opunit_configs.Creator ```  ``` employee_appraisal.Employee = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` employee_appraisal.Creator = task_setups.Creator ```  ``` employee_appraisal.Employee = task_setups.Creator ``` |
| [tasks](#tasks) | ``` employee_appraisal.Creator = tasks.Creator ```  ``` employee_appraisal.Employee = tasks.Creator ``` |
| [teams](#teams) | ``` employee_appraisal.Creator = teams.LeaderEmployee ```  ``` employee_appraisal.Employee = teams.LeaderEmployee ```  ``` employee_appraisal.Creator = teams.Creator ```  ``` employee_appraisal.Employee = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employee_appraisal.Creator = timesheet_pay_returns.Creator ```  ``` employee_appraisal.Employee = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` employee_appraisal.Creator = timesheets.Employee ```  ``` employee_appraisal.Employee = timesheets.Employee ```  ``` employee_appraisal.Creator = timesheets.Creator ```  ``` employee_appraisal.Employee = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` employee_appraisal.Creator = training_modules.Creator ```  ``` employee_appraisal.Employee = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employee_appraisal.Creator = training_records.Employee ```  ``` employee_appraisal.Employee = training_records.Employee ```  ``` employee_appraisal.Creator = training_records.Creator ```  ``` employee_appraisal.Employee = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employee_appraisal.Creator = webhooks.Creator ```  ``` employee_appraisal.Employee = webhooks.Creator ``` |

employee\_appraisal table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Date**  DATE |
| **DayTimestamp**  INTEGER |
| **Employee**  INTEGER |
| **Id**  INTEGER |
| **Mark01**  NUMBER |
| **Mark02**  NUMBER |
| **Mark03**  NUMBER |
| **Mark04**  NUMBER |
| **Mark05**  NUMBER |
| **Modified**  DATE-TIME |

### employee\_availability

The `employee_availability` table contains info about employee availability.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/EmployeeAvailability) |

employee\_availability table foreign keys

| Join employee\_availability with | on |
| --- | --- |
| [addresses](#addresses) | ``` employee_availability.Employee = addresses.Creator ```  ``` employee_availability.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` employee_availability.Employee = categories.Creator ```  ``` employee_availability.Creator = categories.Creator ``` |
| [comments](#comments) | ``` employee_availability.Employee = comments.Creator ```  ``` employee_availability.Creator = comments.Creator ``` |
| [companies](#companies) | ``` employee_availability.Employee = companies.Creator ```  ``` employee_availability.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` employee_availability.Employee = company_periods.Creator ```  ``` employee_availability.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` employee_availability.Employee = contacts.Creator ```  ``` employee_availability.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` employee_availability.Employee = countries.Creator ```  ``` employee_availability.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employee_availability.Employee = custom_app_data.Employee ```  ``` employee_availability.Creator = custom_app_data.Employee ```  ``` employee_availability.Employee = custom_app_data.Creator ```  ``` employee_availability.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employee_availability.Employee = custom_field_data.Creator ```  ``` employee_availability.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employee_availability.Employee = custom_fields.Creator ```  ``` employee_availability.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` employee_availability.Employee = employee_agreement_history.Creator ```  ``` employee_availability.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` employee_availability.Employee = employee_agreements.EmployeeId ```  ``` employee_availability.Creator = employee_agreements.EmployeeId ```  ``` employee_availability.Employee = employee_agreements.Creator ```  ``` employee_availability.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` employee_availability.Employee = employee_appraisal.Creator ```  ``` employee_availability.Creator = employee_appraisal.Creator ```  ``` employee_availability.Employee = employee_appraisal.Employee ```  ``` employee_availability.Creator = employee_appraisal.Employee ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` employee_availability.Employee = employee_contract_leave_rules.Creator ```  ``` employee_availability.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` employee_availability.Employee = employee_contracts.Creator ```  ``` employee_availability.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` employee_availability.Employee = employee_history.EmployeeId ```  ``` employee_availability.Creator = employee_history.EmployeeId ```  ``` employee_availability.Employee = employee_history.Creator ```  ``` employee_availability.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` employee_availability.Employee = employee_paycycle_returns.Creator ```  ``` employee_availability.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` employee_availability.Employee = employee_paycycles.EmployeeId ```  ``` employee_availability.Creator = employee_paycycles.EmployeeId ```  ``` employee_availability.Employee = employee_paycycles.Creator ```  ``` employee_availability.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` employee_availability.Employee = employee_roles.Creator ```  ``` employee_availability.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` employee_availability.Employee = employee_salary_opunit_costing.Employee ```  ``` employee_availability.Creator = employee_salary_opunit_costing.Employee ```  ``` employee_availability.Employee = employee_salary_opunit_costing.Creator ```  ``` employee_availability.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` employee_availability.Employee = employee_workplaces.EmployeeId ```  ``` employee_availability.Creator = employee_workplaces.EmployeeId ```  ``` employee_availability.Employee = employee_workplaces.Creator ```  ``` employee_availability.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` employee_availability.Employee = employment_conditions.Creator ```  ``` employee_availability.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` employee_availability.Employee = events.Creator ```  ``` employee_availability.Creator = events.Creator ```  ``` employee_availability.Schedule = events.Schedule ``` |
| [geo](#geo) | ``` employee_availability.Employee = geo.Creator ```  ``` employee_availability.Creator = geo.Creator ``` |
| [journal](#journal) | ``` employee_availability.Employee = journal.EmployeeId ```  ``` employee_availability.Creator = journal.EmployeeId ```  ``` employee_availability.Employee = journal.Creator ```  ``` employee_availability.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` employee_availability.Employee = kiosks.Creator ```  ``` employee_availability.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employee_availability.Employee = leave_accruals.Employee ```  ``` employee_availability.Creator = leave_accruals.Employee ```  ``` employee_availability.Employee = leave_accruals.Creator ```  ``` employee_availability.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employee_availability.Employee = leave_pay_lines.Creator ```  ``` employee_availability.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` employee_availability.Employee = leave_rules.Creator ```  ``` employee_availability.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` employee_availability.Employee = leaves.Employee ```  ``` employee_availability.Creator = leaves.Employee ```  ``` employee_availability.Employee = leaves.Creator ```  ``` employee_availability.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` employee_availability.Employee = memos.Creator ```  ``` employee_availability.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` employee_availability.Employee = operational_units.Creator ```  ``` employee_availability.Creator = operational_units.Creator ```  ``` employee_availability.Schedule = operational_units.RosterActiveHoursSchedule ``` |
| [pay\_periods](#pay-periods) | ``` employee_availability.Employee = pay_periods.Creator ```  ``` employee_availability.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` employee_availability.Employee = pay_rules.Creator ```  ``` employee_availability.Creator = pay_rules.Creator ```  ``` employee_availability.Schedule = pay_rules.Schedule ``` |
| [public\_holidays](#public-holidays) | ``` employee_availability.Employee = public_holidays.Creator ```  ``` employee_availability.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employee_availability.Employee = roster_opens.Employee ```  ``` employee_availability.Creator = roster_opens.Employee ```  ``` employee_availability.Employee = roster_opens.Creator ```  ``` employee_availability.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employee_availability.Employee = roster_swaps.Employee ```  ``` employee_availability.Creator = roster_swaps.Employee ```  ``` employee_availability.Employee = roster_swaps.Creator ```  ``` employee_availability.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employee_availability.Employee = rosters.Employee ```  ``` employee_availability.Creator = rosters.Employee ```  ``` employee_availability.Employee = rosters.ConfirmBy ```  ``` employee_availability.Creator = rosters.ConfirmBy ```  ``` employee_availability.Employee = rosters.Creator ```  ``` employee_availability.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` employee_availability.Employee = sales_data.Employee ```  ``` employee_availability.Creator = sales_data.Employee ```  ``` employee_availability.Employee = sales_data.Creator ```  ``` employee_availability.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` employee_availability.Employee = schedules.Creator ```  ``` employee_availability.Creator = schedules.Creator ```  ``` employee_availability.Schedule = schedules.Id ``` |
| [sms\_logs](#sms-logs) | ``` employee_availability.Employee = sms_logs.Creator ```  ``` employee_availability.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` employee_availability.Employee = states.Creator ```  ``` employee_availability.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employee_availability.Employee = stress_profiles.Creator ```  ``` employee_availability.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employee_availability.Employee = system_usage_balances.Creator ```  ``` employee_availability.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employee_availability.Employee = system_usage_tracking.Creator ```  ``` employee_availability.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employee_availability.Employee = task_group_setups.Creator ```  ``` employee_availability.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employee_availability.Employee = task_groups.Creator ```  ``` employee_availability.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employee_availability.Employee = task_opunit_configs.Creator ```  ``` employee_availability.Creator = task_opunit_configs.Creator ```  ``` employee_availability.Schedule = task_opunit_configs.Schedule ``` |
| [task\_setups](#task-setups) | ``` employee_availability.Employee = task_setups.Creator ```  ``` employee_availability.Creator = task_setups.Creator ```  ``` employee_availability.Schedule = task_setups.Schedule ``` |
| [tasks](#tasks) | ``` employee_availability.Employee = tasks.Creator ```  ``` employee_availability.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` employee_availability.Employee = teams.LeaderEmployee ```  ``` employee_availability.Creator = teams.LeaderEmployee ```  ``` employee_availability.Employee = teams.Creator ```  ``` employee_availability.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employee_availability.Employee = timesheet_pay_returns.Creator ```  ``` employee_availability.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` employee_availability.Employee = timesheets.Employee ```  ``` employee_availability.Creator = timesheets.Employee ```  ``` employee_availability.Employee = timesheets.Creator ```  ``` employee_availability.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` employee_availability.Employee = training_modules.Creator ```  ``` employee_availability.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employee_availability.Employee = training_records.Employee ```  ``` employee_availability.Creator = training_records.Employee ```  ``` employee_availability.Employee = training_records.Creator ```  ``` employee_availability.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employee_availability.Employee = webhooks.Creator ```  ``` employee_availability.Creator = webhooks.Creator ``` |

employee\_availability table schema

|  |
| --- |
| **Comment**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Date**  DATE |
| **Employee**  INTEGER |
| **EndTime**  INTEGER |
| **Id**  INTEGER |
| **MaxDateRecurringGenerated**  DATE |
| **Modified**  DATE-TIME |
| **Schedule**  INTEGER |
| **StartTime**  INTEGER |
| **Type**  INTEGER |

### employee\_contract\_leave\_rules

The `employee_contract_leave_rules` table contains info about employment contract leave rules.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/EmploymentContractLeaveRules) |

employee\_contract\_leave\_rules table foreign keys

| Join employee\_contract\_leave\_rules with | on |
| --- | --- |
| [addresses](#addresses) | ``` employee_contract_leave_rules.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` employee_contract_leave_rules.Creator = categories.Creator ``` |
| [comments](#comments) | ``` employee_contract_leave_rules.Creator = comments.Creator ``` |
| [companies](#companies) | ``` employee_contract_leave_rules.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` employee_contract_leave_rules.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` employee_contract_leave_rules.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` employee_contract_leave_rules.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employee_contract_leave_rules.Creator = custom_app_data.Employee ```  ``` employee_contract_leave_rules.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employee_contract_leave_rules.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employee_contract_leave_rules.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` employee_contract_leave_rules.Creator = employee_agreement_history.Creator ```  ``` employee_contract_leave_rules.ContractId = employee_agreement_history.Contract ```  ``` employee_contract_leave_rules.LoadingPayRule1 = employee_agreement_history.SalaryPayRule ```  ``` employee_contract_leave_rules.LoadingPayRule2 = employee_agreement_history.SalaryPayRule ```  ``` employee_contract_leave_rules.LoadingPayRule3 = employee_agreement_history.SalaryPayRule ``` |
| [employee\_agreements](#employee-agreements) | ``` employee_contract_leave_rules.Creator = employee_agreements.EmployeeId ```  ``` employee_contract_leave_rules.Creator = employee_agreements.Creator ```  ``` employee_contract_leave_rules.ContractId = employee_agreements.Contract ```  ``` employee_contract_leave_rules.LoadingPayRule1 = employee_agreements.SalaryPayRule ```  ``` employee_contract_leave_rules.LoadingPayRule2 = employee_agreements.SalaryPayRule ```  ``` employee_contract_leave_rules.LoadingPayRule3 = employee_agreements.SalaryPayRule ``` |
| [employee\_appraisal](#employee-appraisal) | ``` employee_contract_leave_rules.Creator = employee_appraisal.Creator ```  ``` employee_contract_leave_rules.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` employee_contract_leave_rules.Creator = employee_availability.Employee ```  ``` employee_contract_leave_rules.Creator = employee_availability.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` employee_contract_leave_rules.Creator = employee_contracts.Creator ```  ``` employee_contract_leave_rules.ContractId = employee_contracts.Id ```  ``` employee_contract_leave_rules.LoadingPayRule1 = employee_contracts.BasePayRule ```  ``` employee_contract_leave_rules.LoadingPayRule2 = employee_contracts.BasePayRule ```  ``` employee_contract_leave_rules.LoadingPayRule3 = employee_contracts.BasePayRule ``` |
| [employee\_history](#employee-history) | ``` employee_contract_leave_rules.Creator = employee_history.EmployeeId ```  ``` employee_contract_leave_rules.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` employee_contract_leave_rules.Creator = employee_paycycle_returns.Creator ```  ``` employee_contract_leave_rules.LoadingPayRule1 = employee_paycycle_returns.PayRule ```  ``` employee_contract_leave_rules.LoadingPayRule2 = employee_paycycle_returns.PayRule ```  ``` employee_contract_leave_rules.LoadingPayRule3 = employee_paycycle_returns.PayRule ``` |
| [employee\_paycycles](#employee-paycycles) | ``` employee_contract_leave_rules.Creator = employee_paycycles.EmployeeId ```  ``` employee_contract_leave_rules.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` employee_contract_leave_rules.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` employee_contract_leave_rules.Creator = employee_salary_opunit_costing.Employee ```  ``` employee_contract_leave_rules.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` employee_contract_leave_rules.Creator = employee_workplaces.EmployeeId ```  ``` employee_contract_leave_rules.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` employee_contract_leave_rules.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` employee_contract_leave_rules.Creator = events.Creator ``` |
| [geo](#geo) | ``` employee_contract_leave_rules.Creator = geo.Creator ``` |
| [journal](#journal) | ``` employee_contract_leave_rules.Creator = journal.EmployeeId ```  ``` employee_contract_leave_rules.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` employee_contract_leave_rules.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employee_contract_leave_rules.Creator = leave_accruals.Employee ```  ``` employee_contract_leave_rules.Creator = leave_accruals.Creator ```  ``` employee_contract_leave_rules.LeaveRuleId = leave_accruals.LeaveRule ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employee_contract_leave_rules.Creator = leave_pay_lines.Creator ```  ``` employee_contract_leave_rules.LeaveRuleId = leave_pay_lines.LeaveRule ``` |
| [leave\_rules](#leave-rules) | ``` employee_contract_leave_rules.Creator = leave_rules.Creator ```  ``` employee_contract_leave_rules.LeaveRuleId = leave_rules.Id ``` |
| [leaves](#leaves) | ``` employee_contract_leave_rules.Creator = leaves.Employee ```  ``` employee_contract_leave_rules.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` employee_contract_leave_rules.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` employee_contract_leave_rules.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` employee_contract_leave_rules.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` employee_contract_leave_rules.Creator = pay_rules.Creator ```  ``` employee_contract_leave_rules.LoadingPayRule1 = pay_rules.Id ```  ``` employee_contract_leave_rules.LoadingPayRule2 = pay_rules.Id ```  ``` employee_contract_leave_rules.LoadingPayRule3 = pay_rules.Id ``` |
| [public\_holidays](#public-holidays) | ``` employee_contract_leave_rules.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employee_contract_leave_rules.Creator = roster_opens.Employee ```  ``` employee_contract_leave_rules.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employee_contract_leave_rules.Creator = roster_swaps.Employee ```  ``` employee_contract_leave_rules.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employee_contract_leave_rules.Creator = rosters.Employee ```  ``` employee_contract_leave_rules.Creator = rosters.ConfirmBy ```  ``` employee_contract_leave_rules.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` employee_contract_leave_rules.Creator = sales_data.Employee ```  ``` employee_contract_leave_rules.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` employee_contract_leave_rules.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` employee_contract_leave_rules.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` employee_contract_leave_rules.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employee_contract_leave_rules.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employee_contract_leave_rules.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employee_contract_leave_rules.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employee_contract_leave_rules.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employee_contract_leave_rules.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employee_contract_leave_rules.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` employee_contract_leave_rules.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` employee_contract_leave_rules.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` employee_contract_leave_rules.Creator = teams.LeaderEmployee ```  ``` employee_contract_leave_rules.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employee_contract_leave_rules.Creator = timesheet_pay_returns.Creator ```  ``` employee_contract_leave_rules.LoadingPayRule1 = timesheet_pay_returns.PayRule ```  ``` employee_contract_leave_rules.LoadingPayRule2 = timesheet_pay_returns.PayRule ```  ``` employee_contract_leave_rules.LoadingPayRule3 = timesheet_pay_returns.PayRule ``` |
| [timesheets](#timesheets) | ``` employee_contract_leave_rules.Creator = timesheets.Employee ```  ``` employee_contract_leave_rules.Creator = timesheets.Creator ```  ``` employee_contract_leave_rules.LeaveRuleId = timesheets.LeaveRule ``` |
| [training\_modules](#training-modules) | ``` employee_contract_leave_rules.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employee_contract_leave_rules.Creator = training_records.Employee ```  ``` employee_contract_leave_rules.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employee_contract_leave_rules.Creator = webhooks.Creator ``` |

employee\_contract\_leave\_rules table schema

|  |
| --- |
| **ContractId**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **LeaveRuleId**  INTEGER |
| **LoadingPayRule1**  INTEGER |
| **LoadingPayRule2**  INTEGER |
| **LoadingPayRule3**  INTEGER |
| **Modified**  DATE-TIME |

### employee\_contracts

The `employee_contracts` table contains info about employee contracts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
|

employee\_contracts table foreign keys

| Join employee\_contracts with | on |
| --- | --- |
| [categories](#categories) | ``` employee_contracts.EmploymentCategory = categories.Id ```  ``` employee_contracts.Creator = categories.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` employee_contracts.EmploymentCategory = employment_conditions.EmploymentCategory ```  ``` employee_contracts.Creator = employment_conditions.Creator ```  ``` employee_contracts.EmploymentCondition = employment_conditions.Id ``` |
| [addresses](#addresses) | ``` employee_contracts.Creator = addresses.Creator ``` |
| [comments](#comments) | ``` employee_contracts.Creator = comments.Creator ``` |
| [companies](#companies) | ``` employee_contracts.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` employee_contracts.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` employee_contracts.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` employee_contracts.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employee_contracts.Creator = custom_app_data.Employee ```  ``` employee_contracts.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employee_contracts.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employee_contracts.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` employee_contracts.Creator = employee_agreement_history.Creator ```  ``` employee_contracts.Id = employee_agreement_history.Contract ```  ``` employee_contracts.BasePayRule = employee_agreement_history.SalaryPayRule ``` |
| [employee\_agreements](#employee-agreements) | ``` employee_contracts.Creator = employee_agreements.EmployeeId ```  ``` employee_contracts.Creator = employee_agreements.Creator ```  ``` employee_contracts.Id = employee_agreements.Contract ```  ``` employee_contracts.BasePayRule = employee_agreements.SalaryPayRule ``` |
| [employee\_appraisal](#employee-appraisal) | ``` employee_contracts.Creator = employee_appraisal.Creator ```  ``` employee_contracts.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` employee_contracts.Creator = employee_availability.Employee ```  ``` employee_contracts.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` employee_contracts.Creator = employee_contract_leave_rules.Creator ```  ``` employee_contracts.Id = employee_contract_leave_rules.ContractId ```  ``` employee_contracts.BasePayRule = employee_contract_leave_rules.LoadingPayRule1 ```  ``` employee_contracts.BasePayRule = employee_contract_leave_rules.LoadingPayRule2 ```  ``` employee_contracts.BasePayRule = employee_contract_leave_rules.LoadingPayRule3 ``` |
| [employee\_history](#employee-history) | ``` employee_contracts.Creator = employee_history.EmployeeId ```  ``` employee_contracts.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` employee_contracts.Creator = employee_paycycle_returns.Creator ```  ``` employee_contracts.BasePayRule = employee_paycycle_returns.PayRule ``` |
| [employee\_paycycles](#employee-paycycles) | ``` employee_contracts.Creator = employee_paycycles.EmployeeId ```  ``` employee_contracts.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` employee_contracts.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` employee_contracts.Creator = employee_salary_opunit_costing.Employee ```  ``` employee_contracts.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` employee_contracts.Creator = employee_workplaces.EmployeeId ```  ``` employee_contracts.Creator = employee_workplaces.Creator ``` |
| [events](#events) | ``` employee_contracts.Creator = events.Creator ``` |
| [geo](#geo) | ``` employee_contracts.Creator = geo.Creator ``` |
| [journal](#journal) | ``` employee_contracts.Creator = journal.EmployeeId ```  ``` employee_contracts.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` employee_contracts.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employee_contracts.Creator = leave_accruals.Employee ```  ``` employee_contracts.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employee_contracts.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` employee_contracts.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` employee_contracts.Creator = leaves.Employee ```  ``` employee_contracts.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` employee_contracts.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` employee_contracts.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` employee_contracts.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` employee_contracts.Creator = pay_rules.Creator ```  ``` employee_contracts.BasePayRule = pay_rules.Id ``` |
| [public\_holidays](#public-holidays) | ``` employee_contracts.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employee_contracts.Creator = roster_opens.Employee ```  ``` employee_contracts.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employee_contracts.Creator = roster_swaps.Employee ```  ``` employee_contracts.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employee_contracts.Creator = rosters.Employee ```  ``` employee_contracts.Creator = rosters.ConfirmBy ```  ``` employee_contracts.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` employee_contracts.Creator = sales_data.Employee ```  ``` employee_contracts.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` employee_contracts.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` employee_contracts.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` employee_contracts.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employee_contracts.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employee_contracts.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employee_contracts.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employee_contracts.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employee_contracts.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employee_contracts.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` employee_contracts.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` employee_contracts.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` employee_contracts.Creator = teams.LeaderEmployee ```  ``` employee_contracts.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employee_contracts.Creator = timesheet_pay_returns.Creator ```  ``` employee_contracts.BasePayRule = timesheet_pay_returns.PayRule ``` |
| [timesheets](#timesheets) | ``` employee_contracts.Creator = timesheets.Employee ```  ``` employee_contracts.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` employee_contracts.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employee_contracts.Creator = training_records.Employee ```  ``` employee_contracts.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employee_contracts.Creator = webhooks.Creator ``` |

employee\_contracts table schema

|  |
| --- |
| **BasePayRule**  INTEGER |
| **Code**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Description**  STRING |
| **EmploymentBasis**  INTEGER |
| **EmploymentCategory**  INTEGER |
| **EmploymentCondition**  INTEGER |
| **EmploymentStatus**  INTEGER |
| **EndDate**  DATE |
| **File**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Name**  STRING |
| **PeriodType**  INTEGER |
| **StartDate**  DATE |

### employee\_history

The `employee_history` table contains info about employee histories.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/EmployeeHistory) |

employee\_history table foreign keys

| Join employee\_history with | on |
| --- | --- |
| [addresses](#addresses) | ``` employee_history.MainAddress = addresses.Id ```  ``` employee_history.PostalAddress = addresses.Id ```  ``` employee_history.EmergencyAddress = addresses.Id ```  ``` employee_history.EmployeeId = addresses.Creator ```  ``` employee_history.Creator = addresses.Creator ``` |
| [companies](#companies) | ``` employee_history.MainAddress = companies.Address ```  ``` employee_history.PostalAddress = companies.Address ```  ``` employee_history.EmergencyAddress = companies.Address ```  ``` employee_history.Company = companies.Id ```  ``` employee_history.Company = companies.ParentCompany ```  ``` employee_history.EmployeeId = companies.Creator ```  ``` employee_history.Creator = companies.Creator ``` |
| [operational\_units](#operational-units) | ``` employee_history.MainAddress = operational_units.Address ```  ``` employee_history.PostalAddress = operational_units.Address ```  ``` employee_history.EmergencyAddress = operational_units.Address ```  ``` employee_history.EmployeeId = operational_units.Creator ```  ``` employee_history.Creator = operational_units.Creator ``` |
| [company\_periods](#company-periods) | ``` employee_history.Company = company_periods.Company ```  ``` employee_history.EmployeeId = company_periods.Creator ```  ``` employee_history.Creator = company_periods.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` employee_history.Company = employee_workplaces.Company ```  ``` employee_history.EmployeeId = employee_workplaces.EmployeeId ```  ``` employee_history.Creator = employee_workplaces.EmployeeId ```  ``` employee_history.EmployeeId = employee_workplaces.Creator ```  ``` employee_history.Creator = employee_workplaces.Creator ``` |
| [kiosks](#kiosks) | ``` employee_history.Company = kiosks.Company ```  ``` employee_history.EmployeeId = kiosks.Creator ```  ``` employee_history.Creator = kiosks.Creator ``` |
| [leaves](#leaves) | ``` employee_history.Company = leaves.Company ```  ``` employee_history.EmployeeId = leaves.Employee ```  ``` employee_history.Creator = leaves.Employee ```  ``` employee_history.EmployeeId = leaves.Creator ```  ``` employee_history.Creator = leaves.Creator ```  ``` employee_history.Id = leaves.EmployeeHistory ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employee_history.Company = system_usage_tracking.CompanyId ```  ``` employee_history.EmployeeId = system_usage_tracking.Creator ```  ``` employee_history.Creator = system_usage_tracking.Creator ``` |
| [categories](#categories) | ``` employee_history.EmployeeId = categories.Creator ```  ``` employee_history.Creator = categories.Creator ``` |
| [comments](#comments) | ``` employee_history.EmployeeId = comments.Creator ```  ``` employee_history.Creator = comments.Creator ``` |
| [contacts](#contacts) | ``` employee_history.EmployeeId = contacts.Creator ```  ``` employee_history.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` employee_history.EmployeeId = countries.Creator ```  ``` employee_history.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employee_history.EmployeeId = custom_app_data.Employee ```  ``` employee_history.Creator = custom_app_data.Employee ```  ``` employee_history.EmployeeId = custom_app_data.Creator ```  ``` employee_history.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employee_history.EmployeeId = custom_field_data.Creator ```  ``` employee_history.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employee_history.EmployeeId = custom_fields.Creator ```  ``` employee_history.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` employee_history.EmployeeId = employee_agreement_history.Creator ```  ``` employee_history.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` employee_history.EmployeeId = employee_agreements.EmployeeId ```  ``` employee_history.Creator = employee_agreements.EmployeeId ```  ``` employee_history.EmployeeId = employee_agreements.Creator ```  ``` employee_history.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` employee_history.EmployeeId = employee_appraisal.Creator ```  ``` employee_history.Creator = employee_appraisal.Creator ```  ``` employee_history.EmployeeId = employee_appraisal.Employee ```  ``` employee_history.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` employee_history.EmployeeId = employee_availability.Employee ```  ``` employee_history.Creator = employee_availability.Employee ```  ``` employee_history.EmployeeId = employee_availability.Creator ```  ``` employee_history.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` employee_history.EmployeeId = employee_contract_leave_rules.Creator ```  ``` employee_history.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` employee_history.EmployeeId = employee_contracts.Creator ```  ``` employee_history.Creator = employee_contracts.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` employee_history.EmployeeId = employee_paycycle_returns.Creator ```  ``` employee_history.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` employee_history.EmployeeId = employee_paycycles.EmployeeId ```  ``` employee_history.Creator = employee_paycycles.EmployeeId ```  ``` employee_history.EmployeeId = employee_paycycles.Creator ```  ``` employee_history.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` employee_history.EmployeeId = employee_roles.Creator ```  ``` employee_history.Creator = employee_roles.Creator ```  ``` employee_history.Role = employee_roles.Id ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` employee_history.EmployeeId = employee_salary_opunit_costing.Employee ```  ``` employee_history.Creator = employee_salary_opunit_costing.Employee ```  ``` employee_history.EmployeeId = employee_salary_opunit_costing.Creator ```  ``` employee_history.Creator = employee_salary_opunit_costing.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` employee_history.EmployeeId = employment_conditions.Creator ```  ``` employee_history.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` employee_history.EmployeeId = events.Creator ```  ``` employee_history.Creator = events.Creator ``` |
| [geo](#geo) | ``` employee_history.EmployeeId = geo.Creator ```  ``` employee_history.Creator = geo.Creator ``` |
| [journal](#journal) | ``` employee_history.EmployeeId = journal.EmployeeId ```  ``` employee_history.Creator = journal.EmployeeId ```  ``` employee_history.EmployeeId = journal.Creator ```  ``` employee_history.Creator = journal.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employee_history.EmployeeId = leave_accruals.Employee ```  ``` employee_history.Creator = leave_accruals.Employee ```  ``` employee_history.EmployeeId = leave_accruals.Creator ```  ``` employee_history.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employee_history.EmployeeId = leave_pay_lines.Creator ```  ``` employee_history.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` employee_history.EmployeeId = leave_rules.Creator ```  ``` employee_history.Creator = leave_rules.Creator ``` |
| [memos](#memos) | ``` employee_history.EmployeeId = memos.Creator ```  ``` employee_history.Creator = memos.Creator ``` |
| [pay\_periods](#pay-periods) | ``` employee_history.EmployeeId = pay_periods.Creator ```  ``` employee_history.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` employee_history.EmployeeId = pay_rules.Creator ```  ``` employee_history.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` employee_history.EmployeeId = public_holidays.Creator ```  ``` employee_history.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employee_history.EmployeeId = roster_opens.Employee ```  ``` employee_history.Creator = roster_opens.Employee ```  ``` employee_history.EmployeeId = roster_opens.Creator ```  ``` employee_history.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employee_history.EmployeeId = roster_swaps.Employee ```  ``` employee_history.Creator = roster_swaps.Employee ```  ``` employee_history.EmployeeId = roster_swaps.Creator ```  ``` employee_history.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employee_history.EmployeeId = rosters.Employee ```  ``` employee_history.Creator = rosters.Employee ```  ``` employee_history.EmployeeId = rosters.ConfirmBy ```  ``` employee_history.Creator = rosters.ConfirmBy ```  ``` employee_history.EmployeeId = rosters.Creator ```  ``` employee_history.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` employee_history.EmployeeId = sales_data.Employee ```  ``` employee_history.Creator = sales_data.Employee ```  ``` employee_history.EmployeeId = sales_data.Creator ```  ``` employee_history.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` employee_history.EmployeeId = schedules.Creator ```  ``` employee_history.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` employee_history.EmployeeId = sms_logs.Creator ```  ``` employee_history.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` employee_history.EmployeeId = states.Creator ```  ``` employee_history.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employee_history.EmployeeId = stress_profiles.Creator ```  ``` employee_history.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employee_history.EmployeeId = system_usage_balances.Creator ```  ``` employee_history.Creator = system_usage_balances.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employee_history.EmployeeId = task_group_setups.Creator ```  ``` employee_history.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employee_history.EmployeeId = task_groups.Creator ```  ``` employee_history.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employee_history.EmployeeId = task_opunit_configs.Creator ```  ``` employee_history.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` employee_history.EmployeeId = task_setups.Creator ```  ``` employee_history.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` employee_history.EmployeeId = tasks.Creator ```  ``` employee_history.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` employee_history.EmployeeId = teams.LeaderEmployee ```  ``` employee_history.Creator = teams.LeaderEmployee ```  ``` employee_history.EmployeeId = teams.Creator ```  ``` employee_history.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employee_history.EmployeeId = timesheet_pay_returns.Creator ```  ``` employee_history.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` employee_history.EmployeeId = timesheets.Employee ```  ``` employee_history.Creator = timesheets.Employee ```  ``` employee_history.EmployeeId = timesheets.Creator ```  ``` employee_history.Creator = timesheets.Creator ```  ``` employee_history.Id = timesheets.EmployeeHistory ``` |
| [training\_modules](#training-modules) | ``` employee_history.EmployeeId = training_modules.Creator ```  ``` employee_history.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employee_history.EmployeeId = training_records.Employee ```  ``` employee_history.Creator = training_records.Employee ```  ``` employee_history.EmployeeId = training_records.Creator ```  ``` employee_history.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employee_history.EmployeeId = webhooks.Creator ```  ``` employee_history.Creator = webhooks.Creator ``` |

employee\_history table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **Company**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **DateOfBirth**  DATE |
| **DisplayName**  STRING |
| **EmergencyAddress**  STRING |
| **EmployeeId**  INTEGER |
| **FirstName**  STRING |
| **Gender**  INTEGER |
| **Id**  INTEGER |
| **JobAppId**  INTEGER |
| **LastName**  STRING |
| **MainAddress**  STRING |
| **Modified**  DATE-TIME |
| **OtherName**  STRING |
| **Photo**  INTEGER |
| **Position**  STRING |
| **PostalAddress**  STRING |
| **Role**  INTEGER |
| **Salutation**  STRING |
| **StartDate**  DATE |
| **TerminationDate**  DATE |

### employee\_paycycle\_returns

The `employee_paycycle_returns` table contains info about employee paycycle returns.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/EmployeePaycycleReturn) |

employee\_paycycle\_returns table foreign keys

| Join employee\_paycycle\_returns with | on |
| --- | --- |
| [addresses](#addresses) | ``` employee_paycycle_returns.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` employee_paycycle_returns.Creator = categories.Creator ``` |
| [comments](#comments) | ``` employee_paycycle_returns.Creator = comments.Creator ``` |
| [companies](#companies) | ``` employee_paycycle_returns.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` employee_paycycle_returns.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` employee_paycycle_returns.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` employee_paycycle_returns.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employee_paycycle_returns.Creator = custom_app_data.Employee ```  ``` employee_paycycle_returns.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employee_paycycle_returns.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employee_paycycle_returns.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` employee_paycycle_returns.Creator = employee_agreement_history.Creator ```  ``` employee_paycycle_returns.PayRule = employee_agreement_history.SalaryPayRule ``` |
| [employee\_agreements](#employee-agreements) | ``` employee_paycycle_returns.Creator = employee_agreements.EmployeeId ```  ``` employee_paycycle_returns.Creator = employee_agreements.Creator ```  ``` employee_paycycle_returns.PayRule = employee_agreements.SalaryPayRule ``` |
| [employee\_appraisal](#employee-appraisal) | ``` employee_paycycle_returns.Creator = employee_appraisal.Creator ```  ``` employee_paycycle_returns.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` employee_paycycle_returns.Creator = employee_availability.Employee ```  ``` employee_paycycle_returns.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` employee_paycycle_returns.Creator = employee_contract_leave_rules.Creator ```  ``` employee_paycycle_returns.PayRule = employee_contract_leave_rules.LoadingPayRule1 ```  ``` employee_paycycle_returns.PayRule = employee_contract_leave_rules.LoadingPayRule2 ```  ``` employee_paycycle_returns.PayRule = employee_contract_leave_rules.LoadingPayRule3 ``` |
| [employee\_contracts](#employee-contracts) | ``` employee_paycycle_returns.Creator = employee_contracts.Creator ```  ``` employee_paycycle_returns.PayRule = employee_contracts.BasePayRule ``` |
| [employee\_history](#employee-history) | ``` employee_paycycle_returns.Creator = employee_history.EmployeeId ```  ``` employee_paycycle_returns.Creator = employee_history.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` employee_paycycle_returns.Creator = employee_paycycles.EmployeeId ```  ``` employee_paycycle_returns.Creator = employee_paycycles.Creator ```  ``` employee_paycycle_returns.PaycycleId = employee_paycycles.Id ``` |
| [employee\_roles](#employee-roles) | ``` employee_paycycle_returns.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` employee_paycycle_returns.Creator = employee_salary_opunit_costing.Employee ```  ``` employee_paycycle_returns.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` employee_paycycle_returns.Creator = employee_workplaces.EmployeeId ```  ``` employee_paycycle_returns.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` employee_paycycle_returns.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` employee_paycycle_returns.Creator = events.Creator ``` |
| [geo](#geo) | ``` employee_paycycle_returns.Creator = geo.Creator ``` |
| [journal](#journal) | ``` employee_paycycle_returns.Creator = journal.EmployeeId ```  ``` employee_paycycle_returns.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` employee_paycycle_returns.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employee_paycycle_returns.Creator = leave_accruals.Employee ```  ``` employee_paycycle_returns.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employee_paycycle_returns.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` employee_paycycle_returns.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` employee_paycycle_returns.Creator = leaves.Employee ```  ``` employee_paycycle_returns.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` employee_paycycle_returns.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` employee_paycycle_returns.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` employee_paycycle_returns.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` employee_paycycle_returns.Creator = pay_rules.Creator ```  ``` employee_paycycle_returns.PayRule = pay_rules.Id ``` |
| [public\_holidays](#public-holidays) | ``` employee_paycycle_returns.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employee_paycycle_returns.Creator = roster_opens.Employee ```  ``` employee_paycycle_returns.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employee_paycycle_returns.Creator = roster_swaps.Employee ```  ``` employee_paycycle_returns.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employee_paycycle_returns.Creator = rosters.Employee ```  ``` employee_paycycle_returns.Creator = rosters.ConfirmBy ```  ``` employee_paycycle_returns.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` employee_paycycle_returns.Creator = sales_data.Employee ```  ``` employee_paycycle_returns.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` employee_paycycle_returns.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` employee_paycycle_returns.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` employee_paycycle_returns.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employee_paycycle_returns.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employee_paycycle_returns.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employee_paycycle_returns.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employee_paycycle_returns.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employee_paycycle_returns.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employee_paycycle_returns.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` employee_paycycle_returns.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` employee_paycycle_returns.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` employee_paycycle_returns.Creator = teams.LeaderEmployee ```  ``` employee_paycycle_returns.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employee_paycycle_returns.Creator = timesheet_pay_returns.Creator ```  ``` employee_paycycle_returns.PayRule = timesheet_pay_returns.PayRule ``` |
| [timesheets](#timesheets) | ``` employee_paycycle_returns.Creator = timesheets.Employee ```  ``` employee_paycycle_returns.Creator = timesheets.Creator ```  ``` employee_paycycle_returns.Id = timesheets.PaycycleId ``` |
| [training\_modules](#training-modules) | ``` employee_paycycle_returns.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employee_paycycle_returns.Creator = training_records.Employee ```  ``` employee_paycycle_returns.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employee_paycycle_returns.Creator = webhooks.Creator ``` |

employee\_paycycle\_returns table schema

|  |
| --- |
| **Approved**  BOOLEAN |
| **Cost**  NUMBER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Overridden**  BOOLEAN |
| **OverrideComment**  STRING |
| **PayRule**  INTEGER |
| **PaycycleId**  INTEGER |
| **Value**  NUMBER |

### employee\_paycycles

The `employee_paycycles` table contains info about employee paycycles.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/EmployeePaycycle) |

employee\_paycycles table foreign keys

| Join employee\_paycycles with | on |
| --- | --- |
| [company\_periods](#company-periods) | ``` employee_paycycles.PeriodId = company_periods.Id ```  ``` employee_paycycles.EmployeeId = company_periods.Creator ```  ``` employee_paycycles.Creator = company_periods.Creator ``` |
| [addresses](#addresses) | ``` employee_paycycles.EmployeeId = addresses.Creator ```  ``` employee_paycycles.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` employee_paycycles.EmployeeId = categories.Creator ```  ``` employee_paycycles.Creator = categories.Creator ``` |
| [comments](#comments) | ``` employee_paycycles.EmployeeId = comments.Creator ```  ``` employee_paycycles.Creator = comments.Creator ``` |
| [companies](#companies) | ``` employee_paycycles.EmployeeId = companies.Creator ```  ``` employee_paycycles.Creator = companies.Creator ``` |
| [contacts](#contacts) | ``` employee_paycycles.EmployeeId = contacts.Creator ```  ``` employee_paycycles.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` employee_paycycles.EmployeeId = countries.Creator ```  ``` employee_paycycles.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employee_paycycles.EmployeeId = custom_app_data.Employee ```  ``` employee_paycycles.Creator = custom_app_data.Employee ```  ``` employee_paycycles.EmployeeId = custom_app_data.Creator ```  ``` employee_paycycles.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employee_paycycles.EmployeeId = custom_field_data.Creator ```  ``` employee_paycycles.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employee_paycycles.EmployeeId = custom_fields.Creator ```  ``` employee_paycycles.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` employee_paycycles.EmployeeId = employee_agreement_history.Creator ```  ``` employee_paycycles.Creator = employee_agreement_history.Creator ```  ``` employee_paycycles.EmployeeAgreementHistoryId = employee_agreement_history.Id ```  ``` employee_paycycles.EmployeeAgreementId = employee_agreement_history.AgreementId ``` |
| [employee\_agreements](#employee-agreements) | ``` employee_paycycles.EmployeeId = employee_agreements.EmployeeId ```  ``` employee_paycycles.Creator = employee_agreements.EmployeeId ```  ``` employee_paycycles.EmployeeId = employee_agreements.Creator ```  ``` employee_paycycles.Creator = employee_agreements.Creator ```  ``` employee_paycycles.EmployeeAgreementHistoryId = employee_agreements.HistoryId ```  ``` employee_paycycles.EmployeeAgreementId = employee_agreements.Id ``` |
| [employee\_appraisal](#employee-appraisal) | ``` employee_paycycles.EmployeeId = employee_appraisal.Creator ```  ``` employee_paycycles.Creator = employee_appraisal.Creator ```  ``` employee_paycycles.EmployeeId = employee_appraisal.Employee ```  ``` employee_paycycles.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` employee_paycycles.EmployeeId = employee_availability.Employee ```  ``` employee_paycycles.Creator = employee_availability.Employee ```  ``` employee_paycycles.EmployeeId = employee_availability.Creator ```  ``` employee_paycycles.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` employee_paycycles.EmployeeId = employee_contract_leave_rules.Creator ```  ``` employee_paycycles.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` employee_paycycles.EmployeeId = employee_contracts.Creator ```  ``` employee_paycycles.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` employee_paycycles.EmployeeId = employee_history.EmployeeId ```  ``` employee_paycycles.Creator = employee_history.EmployeeId ```  ``` employee_paycycles.EmployeeId = employee_history.Creator ```  ``` employee_paycycles.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` employee_paycycles.EmployeeId = employee_paycycle_returns.Creator ```  ``` employee_paycycles.Creator = employee_paycycle_returns.Creator ```  ``` employee_paycycles.Id = employee_paycycle_returns.PaycycleId ``` |
| [employee\_roles](#employee-roles) | ``` employee_paycycles.EmployeeId = employee_roles.Creator ```  ``` employee_paycycles.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` employee_paycycles.EmployeeId = employee_salary_opunit_costing.Employee ```  ``` employee_paycycles.Creator = employee_salary_opunit_costing.Employee ```  ``` employee_paycycles.EmployeeId = employee_salary_opunit_costing.Creator ```  ``` employee_paycycles.Creator = employee_salary_opunit_costing.Creator ```  ``` employee_paycycles.EmployeeAgreementId = employee_salary_opunit_costing.EmployeeAgreement ``` |
| [employee\_workplaces](#employee-workplaces) | ``` employee_paycycles.EmployeeId = employee_workplaces.EmployeeId ```  ``` employee_paycycles.Creator = employee_workplaces.EmployeeId ```  ``` employee_paycycles.EmployeeId = employee_workplaces.Creator ```  ``` employee_paycycles.Creator = employee_workplaces.Creator ```  ``` employee_paycycles.EmployeeAgreementId = employee_workplaces.Agreement1 ```  ``` employee_paycycles.EmployeeAgreementId = employee_workplaces.Agreement2 ```  ``` employee_paycycles.EmployeeAgreementId = employee_workplaces.Agreement3 ``` |
| [employment\_conditions](#employment-conditions) | ``` employee_paycycles.EmployeeId = employment_conditions.Creator ```  ``` employee_paycycles.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` employee_paycycles.EmployeeId = events.Creator ```  ``` employee_paycycles.Creator = events.Creator ``` |
| [geo](#geo) | ``` employee_paycycles.EmployeeId = geo.Creator ```  ``` employee_paycycles.Creator = geo.Creator ``` |
| [journal](#journal) | ``` employee_paycycles.EmployeeId = journal.EmployeeId ```  ``` employee_paycycles.Creator = journal.EmployeeId ```  ``` employee_paycycles.EmployeeId = journal.Creator ```  ``` employee_paycycles.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` employee_paycycles.EmployeeId = kiosks.Creator ```  ``` employee_paycycles.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employee_paycycles.EmployeeId = leave_accruals.Employee ```  ``` employee_paycycles.Creator = leave_accruals.Employee ```  ``` employee_paycycles.EmployeeId = leave_accruals.Creator ```  ``` employee_paycycles.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employee_paycycles.EmployeeId = leave_pay_lines.Creator ```  ``` employee_paycycles.Creator = leave_pay_lines.Creator ```  ``` employee_paycycles.EmployeeAgreementId = leave_pay_lines.EmployeeAgreement ``` |
| [leave\_rules](#leave-rules) | ``` employee_paycycles.EmployeeId = leave_rules.Creator ```  ``` employee_paycycles.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` employee_paycycles.EmployeeId = leaves.Employee ```  ``` employee_paycycles.Creator = leaves.Employee ```  ``` employee_paycycles.EmployeeId = leaves.Creator ```  ``` employee_paycycles.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` employee_paycycles.EmployeeId = memos.Creator ```  ``` employee_paycycles.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` employee_paycycles.EmployeeId = operational_units.Creator ```  ``` employee_paycycles.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` employee_paycycles.EmployeeId = pay_periods.Creator ```  ``` employee_paycycles.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` employee_paycycles.EmployeeId = pay_rules.Creator ```  ``` employee_paycycles.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` employee_paycycles.EmployeeId = public_holidays.Creator ```  ``` employee_paycycles.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employee_paycycles.EmployeeId = roster_opens.Employee ```  ``` employee_paycycles.Creator = roster_opens.Employee ```  ``` employee_paycycles.EmployeeId = roster_opens.Creator ```  ``` employee_paycycles.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employee_paycycles.EmployeeId = roster_swaps.Employee ```  ``` employee_paycycles.Creator = roster_swaps.Employee ```  ``` employee_paycycles.EmployeeId = roster_swaps.Creator ```  ``` employee_paycycles.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employee_paycycles.EmployeeId = rosters.Employee ```  ``` employee_paycycles.Creator = rosters.Employee ```  ``` employee_paycycles.EmployeeId = rosters.ConfirmBy ```  ``` employee_paycycles.Creator = rosters.ConfirmBy ```  ``` employee_paycycles.EmployeeId = rosters.Creator ```  ``` employee_paycycles.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` employee_paycycles.EmployeeId = sales_data.Employee ```  ``` employee_paycycles.Creator = sales_data.Employee ```  ``` employee_paycycles.EmployeeId = sales_data.Creator ```  ``` employee_paycycles.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` employee_paycycles.EmployeeId = schedules.Creator ```  ``` employee_paycycles.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` employee_paycycles.EmployeeId = sms_logs.Creator ```  ``` employee_paycycles.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` employee_paycycles.EmployeeId = states.Creator ```  ``` employee_paycycles.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employee_paycycles.EmployeeId = stress_profiles.Creator ```  ``` employee_paycycles.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employee_paycycles.EmployeeId = system_usage_balances.Creator ```  ``` employee_paycycles.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employee_paycycles.EmployeeId = system_usage_tracking.Creator ```  ``` employee_paycycles.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employee_paycycles.EmployeeId = task_group_setups.Creator ```  ``` employee_paycycles.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employee_paycycles.EmployeeId = task_groups.Creator ```  ``` employee_paycycles.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employee_paycycles.EmployeeId = task_opunit_configs.Creator ```  ``` employee_paycycles.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` employee_paycycles.EmployeeId = task_setups.Creator ```  ``` employee_paycycles.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` employee_paycycles.EmployeeId = tasks.Creator ```  ``` employee_paycycles.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` employee_paycycles.EmployeeId = teams.LeaderEmployee ```  ``` employee_paycycles.Creator = teams.LeaderEmployee ```  ``` employee_paycycles.EmployeeId = teams.Creator ```  ``` employee_paycycles.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employee_paycycles.EmployeeId = timesheet_pay_returns.Creator ```  ``` employee_paycycles.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` employee_paycycles.EmployeeId = timesheets.Employee ```  ``` employee_paycycles.Creator = timesheets.Employee ```  ``` employee_paycycles.EmployeeId = timesheets.Creator ```  ``` employee_paycycles.Creator = timesheets.Creator ```  ``` employee_paycycles.EmployeeAgreementId = timesheets.EmployeeAgreement ``` |
| [training\_modules](#training-modules) | ``` employee_paycycles.EmployeeId = training_modules.Creator ```  ``` employee_paycycles.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employee_paycycles.EmployeeId = training_records.Employee ```  ``` employee_paycycles.Creator = training_records.Employee ```  ``` employee_paycycles.EmployeeId = training_records.Creator ```  ``` employee_paycycles.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employee_paycycles.EmployeeId = webhooks.Creator ```  ``` employee_paycycles.Creator = webhooks.Creator ``` |

employee\_paycycles table schema

|  |
| --- |
| **CostTotal**  NUMBER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **EmployeeAgreementHistoryId**  INTEGER |
| **EmployeeAgreementId**  INTEGER |
| **EmployeeId**  INTEGER |
| **ExportId**  INTEGER |
| **Exported**  BOOLEAN |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Paid**  BOOLEAN |
| **PaycycleRules**  INTEGER |
| **PaycycleRulesApproved**  INTEGER |
| **PeriodId**  INTEGER |
| **RecommendedLoadings**  BOOLEAN |
| **TimeTotal**  NUMBER |
| **Timesheets**  INTEGER |
| **TimesheetsPayApproved**  STRING |
| **TimesheetsTimeApproved**  INTEGER |

### employee\_roles

The `employee_roles` table contains info about employee roles.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/EmployeeRole) |

employee\_roles table foreign keys

| Join employee\_roles with | on |
| --- | --- |
| [addresses](#addresses) | ``` employee_roles.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` employee_roles.Creator = categories.Creator ``` |
| [comments](#comments) | ``` employee_roles.Creator = comments.Creator ``` |
| [companies](#companies) | ``` employee_roles.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` employee_roles.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` employee_roles.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` employee_roles.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employee_roles.Creator = custom_app_data.Employee ```  ``` employee_roles.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employee_roles.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employee_roles.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` employee_roles.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` employee_roles.Creator = employee_agreements.EmployeeId ```  ``` employee_roles.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` employee_roles.Creator = employee_appraisal.Creator ```  ``` employee_roles.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` employee_roles.Creator = employee_availability.Employee ```  ``` employee_roles.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` employee_roles.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` employee_roles.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` employee_roles.Creator = employee_history.EmployeeId ```  ``` employee_roles.Creator = employee_history.Creator ```  ``` employee_roles.Id = employee_history.Role ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` employee_roles.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` employee_roles.Creator = employee_paycycles.EmployeeId ```  ``` employee_roles.Creator = employee_paycycles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` employee_roles.Creator = employee_salary_opunit_costing.Employee ```  ``` employee_roles.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` employee_roles.Creator = employee_workplaces.EmployeeId ```  ``` employee_roles.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` employee_roles.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` employee_roles.Creator = events.Creator ``` |
| [geo](#geo) | ``` employee_roles.Creator = geo.Creator ``` |
| [journal](#journal) | ``` employee_roles.Creator = journal.EmployeeId ```  ``` employee_roles.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` employee_roles.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employee_roles.Creator = leave_accruals.Employee ```  ``` employee_roles.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employee_roles.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` employee_roles.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` employee_roles.Creator = leaves.Employee ```  ``` employee_roles.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` employee_roles.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` employee_roles.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` employee_roles.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` employee_roles.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` employee_roles.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employee_roles.Creator = roster_opens.Employee ```  ``` employee_roles.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employee_roles.Creator = roster_swaps.Employee ```  ``` employee_roles.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employee_roles.Creator = rosters.Employee ```  ``` employee_roles.Creator = rosters.ConfirmBy ```  ``` employee_roles.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` employee_roles.Creator = sales_data.Employee ```  ``` employee_roles.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` employee_roles.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` employee_roles.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` employee_roles.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employee_roles.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employee_roles.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employee_roles.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employee_roles.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employee_roles.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employee_roles.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` employee_roles.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` employee_roles.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` employee_roles.Creator = teams.LeaderEmployee ```  ``` employee_roles.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employee_roles.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` employee_roles.Creator = timesheets.Employee ```  ``` employee_roles.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` employee_roles.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employee_roles.Creator = training_records.Employee ```  ``` employee_roles.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employee_roles.Creator = webhooks.Creator ``` |

employee\_roles table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Permissions**  STRING |
| **Ranking**  INTEGER |
| **ReportTo**  INTEGER |
| **Require2fa**  BOOLEAN |
| **Role**  STRING |

### employee\_salary\_opunit\_costing

The `employee_salary_opunit_costing` table contains info about employee salary operational unit costs.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/EmployeeSalaryOpunitCosting) |

employee\_salary\_opunit\_costing table foreign keys

| Join employee\_salary\_opunit\_costing with | on |
| --- | --- |
| [addresses](#addresses) | ``` employee_salary_opunit_costing.Employee = addresses.Creator ```  ``` employee_salary_opunit_costing.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` employee_salary_opunit_costing.Employee = categories.Creator ```  ``` employee_salary_opunit_costing.Creator = categories.Creator ``` |
| [comments](#comments) | ``` employee_salary_opunit_costing.Employee = comments.Creator ```  ``` employee_salary_opunit_costing.Creator = comments.Creator ``` |
| [companies](#companies) | ``` employee_salary_opunit_costing.Employee = companies.Creator ```  ``` employee_salary_opunit_costing.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` employee_salary_opunit_costing.Employee = company_periods.Creator ```  ``` employee_salary_opunit_costing.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` employee_salary_opunit_costing.Employee = contacts.Creator ```  ``` employee_salary_opunit_costing.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` employee_salary_opunit_costing.Employee = countries.Creator ```  ``` employee_salary_opunit_costing.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employee_salary_opunit_costing.Employee = custom_app_data.Employee ```  ``` employee_salary_opunit_costing.Creator = custom_app_data.Employee ```  ``` employee_salary_opunit_costing.Employee = custom_app_data.Creator ```  ``` employee_salary_opunit_costing.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employee_salary_opunit_costing.Employee = custom_field_data.Creator ```  ``` employee_salary_opunit_costing.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employee_salary_opunit_costing.Employee = custom_fields.Creator ```  ``` employee_salary_opunit_costing.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` employee_salary_opunit_costing.Employee = employee_agreement_history.Creator ```  ``` employee_salary_opunit_costing.Creator = employee_agreement_history.Creator ```  ``` employee_salary_opunit_costing.EmployeeAgreement = employee_agreement_history.AgreementId ``` |
| [employee\_agreements](#employee-agreements) | ``` employee_salary_opunit_costing.Employee = employee_agreements.EmployeeId ```  ``` employee_salary_opunit_costing.Creator = employee_agreements.EmployeeId ```  ``` employee_salary_opunit_costing.Employee = employee_agreements.Creator ```  ``` employee_salary_opunit_costing.Creator = employee_agreements.Creator ```  ``` employee_salary_opunit_costing.EmployeeAgreement = employee_agreements.Id ``` |
| [employee\_appraisal](#employee-appraisal) | ``` employee_salary_opunit_costing.Employee = employee_appraisal.Creator ```  ``` employee_salary_opunit_costing.Creator = employee_appraisal.Creator ```  ``` employee_salary_opunit_costing.Employee = employee_appraisal.Employee ```  ``` employee_salary_opunit_costing.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` employee_salary_opunit_costing.Employee = employee_availability.Employee ```  ``` employee_salary_opunit_costing.Creator = employee_availability.Employee ```  ``` employee_salary_opunit_costing.Employee = employee_availability.Creator ```  ``` employee_salary_opunit_costing.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` employee_salary_opunit_costing.Employee = employee_contract_leave_rules.Creator ```  ``` employee_salary_opunit_costing.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` employee_salary_opunit_costing.Employee = employee_contracts.Creator ```  ``` employee_salary_opunit_costing.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` employee_salary_opunit_costing.Employee = employee_history.EmployeeId ```  ``` employee_salary_opunit_costing.Creator = employee_history.EmployeeId ```  ``` employee_salary_opunit_costing.Employee = employee_history.Creator ```  ``` employee_salary_opunit_costing.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` employee_salary_opunit_costing.Employee = employee_paycycle_returns.Creator ```  ``` employee_salary_opunit_costing.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` employee_salary_opunit_costing.Employee = employee_paycycles.EmployeeId ```  ``` employee_salary_opunit_costing.Creator = employee_paycycles.EmployeeId ```  ``` employee_salary_opunit_costing.Employee = employee_paycycles.Creator ```  ``` employee_salary_opunit_costing.Creator = employee_paycycles.Creator ```  ``` employee_salary_opunit_costing.EmployeeAgreement = employee_paycycles.EmployeeAgreementId ``` |
| [employee\_roles](#employee-roles) | ``` employee_salary_opunit_costing.Employee = employee_roles.Creator ```  ``` employee_salary_opunit_costing.Creator = employee_roles.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` employee_salary_opunit_costing.Employee = employee_workplaces.EmployeeId ```  ``` employee_salary_opunit_costing.Creator = employee_workplaces.EmployeeId ```  ``` employee_salary_opunit_costing.Employee = employee_workplaces.Creator ```  ``` employee_salary_opunit_costing.Creator = employee_workplaces.Creator ```  ``` employee_salary_opunit_costing.EmployeeAgreement = employee_workplaces.Agreement1 ```  ``` employee_salary_opunit_costing.EmployeeAgreement = employee_workplaces.Agreement2 ```  ``` employee_salary_opunit_costing.EmployeeAgreement = employee_workplaces.Agreement3 ``` |
| [employment\_conditions](#employment-conditions) | ``` employee_salary_opunit_costing.Employee = employment_conditions.Creator ```  ``` employee_salary_opunit_costing.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` employee_salary_opunit_costing.Employee = events.Creator ```  ``` employee_salary_opunit_costing.Creator = events.Creator ``` |
| [geo](#geo) | ``` employee_salary_opunit_costing.Employee = geo.Creator ```  ``` employee_salary_opunit_costing.Creator = geo.Creator ``` |
| [journal](#journal) | ``` employee_salary_opunit_costing.Employee = journal.EmployeeId ```  ``` employee_salary_opunit_costing.Creator = journal.EmployeeId ```  ``` employee_salary_opunit_costing.Employee = journal.Creator ```  ``` employee_salary_opunit_costing.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` employee_salary_opunit_costing.Employee = kiosks.Creator ```  ``` employee_salary_opunit_costing.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employee_salary_opunit_costing.Employee = leave_accruals.Employee ```  ``` employee_salary_opunit_costing.Creator = leave_accruals.Employee ```  ``` employee_salary_opunit_costing.Employee = leave_accruals.Creator ```  ``` employee_salary_opunit_costing.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employee_salary_opunit_costing.Employee = leave_pay_lines.Creator ```  ``` employee_salary_opunit_costing.Creator = leave_pay_lines.Creator ```  ``` employee_salary_opunit_costing.EmployeeAgreement = leave_pay_lines.EmployeeAgreement ``` |
| [leave\_rules](#leave-rules) | ``` employee_salary_opunit_costing.Employee = leave_rules.Creator ```  ``` employee_salary_opunit_costing.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` employee_salary_opunit_costing.Employee = leaves.Employee ```  ``` employee_salary_opunit_costing.Creator = leaves.Employee ```  ``` employee_salary_opunit_costing.Employee = leaves.Creator ```  ``` employee_salary_opunit_costing.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` employee_salary_opunit_costing.Employee = memos.Creator ```  ``` employee_salary_opunit_costing.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` employee_salary_opunit_costing.Employee = operational_units.Creator ```  ``` employee_salary_opunit_costing.Creator = operational_units.Creator ```  ``` employee_salary_opunit_costing.OpUnit = operational_units.Id ```  ``` employee_salary_opunit_costing.OpUnit = operational_units.ParentOperationalUnit ``` |
| [pay\_periods](#pay-periods) | ``` employee_salary_opunit_costing.Employee = pay_periods.Creator ```  ``` employee_salary_opunit_costing.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` employee_salary_opunit_costing.Employee = pay_rules.Creator ```  ``` employee_salary_opunit_costing.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` employee_salary_opunit_costing.Employee = public_holidays.Creator ```  ``` employee_salary_opunit_costing.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employee_salary_opunit_costing.Employee = roster_opens.Employee ```  ``` employee_salary_opunit_costing.Creator = roster_opens.Employee ```  ``` employee_salary_opunit_costing.Employee = roster_opens.Creator ```  ``` employee_salary_opunit_costing.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employee_salary_opunit_costing.Employee = roster_swaps.Employee ```  ``` employee_salary_opunit_costing.Creator = roster_swaps.Employee ```  ``` employee_salary_opunit_costing.Employee = roster_swaps.Creator ```  ``` employee_salary_opunit_costing.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employee_salary_opunit_costing.Employee = rosters.Employee ```  ``` employee_salary_opunit_costing.Creator = rosters.Employee ```  ``` employee_salary_opunit_costing.Employee = rosters.ConfirmBy ```  ``` employee_salary_opunit_costing.Creator = rosters.ConfirmBy ```  ``` employee_salary_opunit_costing.Employee = rosters.Creator ```  ``` employee_salary_opunit_costing.Creator = rosters.Creator ```  ``` employee_salary_opunit_costing.OpUnit = rosters.OperationalUnit ``` |
| [sales\_data](#sales-data) | ``` employee_salary_opunit_costing.Employee = sales_data.Employee ```  ``` employee_salary_opunit_costing.Creator = sales_data.Employee ```  ``` employee_salary_opunit_costing.Employee = sales_data.Creator ```  ``` employee_salary_opunit_costing.Creator = sales_data.Creator ```  ``` employee_salary_opunit_costing.OpUnit = sales_data.OperationalUnit ``` |
| [schedules](#schedules) | ``` employee_salary_opunit_costing.Employee = schedules.Creator ```  ``` employee_salary_opunit_costing.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` employee_salary_opunit_costing.Employee = sms_logs.Creator ```  ``` employee_salary_opunit_costing.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` employee_salary_opunit_costing.Employee = states.Creator ```  ``` employee_salary_opunit_costing.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employee_salary_opunit_costing.Employee = stress_profiles.Creator ```  ``` employee_salary_opunit_costing.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employee_salary_opunit_costing.Employee = system_usage_balances.Creator ```  ``` employee_salary_opunit_costing.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employee_salary_opunit_costing.Employee = system_usage_tracking.Creator ```  ``` employee_salary_opunit_costing.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employee_salary_opunit_costing.Employee = task_group_setups.Creator ```  ``` employee_salary_opunit_costing.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employee_salary_opunit_costing.Employee = task_groups.Creator ```  ``` employee_salary_opunit_costing.Creator = task_groups.Creator ```  ``` employee_salary_opunit_costing.OpUnit = task_groups.OpUnitId ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employee_salary_opunit_costing.Employee = task_opunit_configs.Creator ```  ``` employee_salary_opunit_costing.Creator = task_opunit_configs.Creator ```  ``` employee_salary_opunit_costing.OpUnit = task_opunit_configs.OpUnitId ``` |
| [task\_setups](#task-setups) | ``` employee_salary_opunit_costing.Employee = task_setups.Creator ```  ``` employee_salary_opunit_costing.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` employee_salary_opunit_costing.Employee = tasks.Creator ```  ``` employee_salary_opunit_costing.Creator = tasks.Creator ```  ``` employee_salary_opunit_costing.OpUnit = tasks.OpUnitId ``` |
| [teams](#teams) | ``` employee_salary_opunit_costing.Employee = teams.LeaderEmployee ```  ``` employee_salary_opunit_costing.Creator = teams.LeaderEmployee ```  ``` employee_salary_opunit_costing.Employee = teams.Creator ```  ``` employee_salary_opunit_costing.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employee_salary_opunit_costing.Employee = timesheet_pay_returns.Creator ```  ``` employee_salary_opunit_costing.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` employee_salary_opunit_costing.Employee = timesheets.Employee ```  ``` employee_salary_opunit_costing.Creator = timesheets.Employee ```  ``` employee_salary_opunit_costing.Employee = timesheets.Creator ```  ``` employee_salary_opunit_costing.Creator = timesheets.Creator ```  ``` employee_salary_opunit_costing.EmployeeAgreement = timesheets.EmployeeAgreement ```  ``` employee_salary_opunit_costing.OpUnit = timesheets.OperationalUnit ``` |
| [training\_modules](#training-modules) | ``` employee_salary_opunit_costing.Employee = training_modules.Creator ```  ``` employee_salary_opunit_costing.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employee_salary_opunit_costing.Employee = training_records.Employee ```  ``` employee_salary_opunit_costing.Creator = training_records.Employee ```  ``` employee_salary_opunit_costing.Employee = training_records.Creator ```  ``` employee_salary_opunit_costing.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employee_salary_opunit_costing.Employee = webhooks.Creator ```  ``` employee_salary_opunit_costing.Creator = webhooks.Creator ``` |

employee\_salary\_opunit\_costing table schema

|  |
| --- |
| **AgreementHistory**  INTEGER |
| **Cost**  NUMBER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Date**  DATE |
| **DayTimestamp**  STRING |
| **Employee**  INTEGER |
| **EmployeeAgreement**  INTEGER |
| **Final**  BOOLEAN |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **OpUnit**  INTEGER |

### employee\_workplaces

The `employee_workplaces` table contains info about employee workplaces.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/EmployeeWorkplace) |

employee\_workplaces table foreign keys

| Join employee\_workplaces with | on |
| --- | --- |
| [companies](#companies) | ``` employee_workplaces.Company = companies.Id ```  ``` employee_workplaces.Company = companies.ParentCompany ```  ``` employee_workplaces.EmployeeId = companies.Creator ```  ``` employee_workplaces.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` employee_workplaces.Company = company_periods.Company ```  ``` employee_workplaces.EmployeeId = company_periods.Creator ```  ``` employee_workplaces.Creator = company_periods.Creator ``` |
| [employee\_history](#employee-history) | ``` employee_workplaces.Company = employee_history.Company ```  ``` employee_workplaces.EmployeeId = employee_history.EmployeeId ```  ``` employee_workplaces.Creator = employee_history.EmployeeId ```  ``` employee_workplaces.EmployeeId = employee_history.Creator ```  ``` employee_workplaces.Creator = employee_history.Creator ``` |
| [kiosks](#kiosks) | ``` employee_workplaces.Company = kiosks.Company ```  ``` employee_workplaces.EmployeeId = kiosks.Creator ```  ``` employee_workplaces.Creator = kiosks.Creator ``` |
| [leaves](#leaves) | ``` employee_workplaces.Company = leaves.Company ```  ``` employee_workplaces.EmployeeId = leaves.Employee ```  ``` employee_workplaces.Creator = leaves.Employee ```  ``` employee_workplaces.EmployeeId = leaves.Creator ```  ``` employee_workplaces.Creator = leaves.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employee_workplaces.Company = system_usage_tracking.CompanyId ```  ``` employee_workplaces.EmployeeId = system_usage_tracking.Creator ```  ``` employee_workplaces.Creator = system_usage_tracking.Creator ``` |
| [addresses](#addresses) | ``` employee_workplaces.EmployeeId = addresses.Creator ```  ``` employee_workplaces.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` employee_workplaces.EmployeeId = categories.Creator ```  ``` employee_workplaces.Creator = categories.Creator ``` |
| [comments](#comments) | ``` employee_workplaces.EmployeeId = comments.Creator ```  ``` employee_workplaces.Creator = comments.Creator ``` |
| [contacts](#contacts) | ``` employee_workplaces.EmployeeId = contacts.Creator ```  ``` employee_workplaces.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` employee_workplaces.EmployeeId = countries.Creator ```  ``` employee_workplaces.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employee_workplaces.EmployeeId = custom_app_data.Employee ```  ``` employee_workplaces.Creator = custom_app_data.Employee ```  ``` employee_workplaces.EmployeeId = custom_app_data.Creator ```  ``` employee_workplaces.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employee_workplaces.EmployeeId = custom_field_data.Creator ```  ``` employee_workplaces.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employee_workplaces.EmployeeId = custom_fields.Creator ```  ``` employee_workplaces.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` employee_workplaces.EmployeeId = employee_agreement_history.Creator ```  ``` employee_workplaces.Creator = employee_agreement_history.Creator ```  ``` employee_workplaces.Agreement1 = employee_agreement_history.AgreementId ```  ``` employee_workplaces.Agreement2 = employee_agreement_history.AgreementId ```  ``` employee_workplaces.Agreement3 = employee_agreement_history.AgreementId ``` |
| [employee\_agreements](#employee-agreements) | ``` employee_workplaces.EmployeeId = employee_agreements.EmployeeId ```  ``` employee_workplaces.Creator = employee_agreements.EmployeeId ```  ``` employee_workplaces.EmployeeId = employee_agreements.Creator ```  ``` employee_workplaces.Creator = employee_agreements.Creator ```  ``` employee_workplaces.Agreement1 = employee_agreements.Id ```  ``` employee_workplaces.Agreement2 = employee_agreements.Id ```  ``` employee_workplaces.Agreement3 = employee_agreements.Id ``` |
| [employee\_appraisal](#employee-appraisal) | ``` employee_workplaces.EmployeeId = employee_appraisal.Creator ```  ``` employee_workplaces.Creator = employee_appraisal.Creator ```  ``` employee_workplaces.EmployeeId = employee_appraisal.Employee ```  ``` employee_workplaces.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` employee_workplaces.EmployeeId = employee_availability.Employee ```  ``` employee_workplaces.Creator = employee_availability.Employee ```  ``` employee_workplaces.EmployeeId = employee_availability.Creator ```  ``` employee_workplaces.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` employee_workplaces.EmployeeId = employee_contract_leave_rules.Creator ```  ``` employee_workplaces.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` employee_workplaces.EmployeeId = employee_contracts.Creator ```  ``` employee_workplaces.Creator = employee_contracts.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` employee_workplaces.EmployeeId = employee_paycycle_returns.Creator ```  ``` employee_workplaces.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` employee_workplaces.EmployeeId = employee_paycycles.EmployeeId ```  ``` employee_workplaces.Creator = employee_paycycles.EmployeeId ```  ``` employee_workplaces.EmployeeId = employee_paycycles.Creator ```  ``` employee_workplaces.Creator = employee_paycycles.Creator ```  ``` employee_workplaces.Agreement1 = employee_paycycles.EmployeeAgreementId ```  ``` employee_workplaces.Agreement2 = employee_paycycles.EmployeeAgreementId ```  ``` employee_workplaces.Agreement3 = employee_paycycles.EmployeeAgreementId ``` |
| [employee\_roles](#employee-roles) | ``` employee_workplaces.EmployeeId = employee_roles.Creator ```  ``` employee_workplaces.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` employee_workplaces.EmployeeId = employee_salary_opunit_costing.Employee ```  ``` employee_workplaces.Creator = employee_salary_opunit_costing.Employee ```  ``` employee_workplaces.EmployeeId = employee_salary_opunit_costing.Creator ```  ``` employee_workplaces.Creator = employee_salary_opunit_costing.Creator ```  ``` employee_workplaces.Agreement1 = employee_salary_opunit_costing.EmployeeAgreement ```  ``` employee_workplaces.Agreement2 = employee_salary_opunit_costing.EmployeeAgreement ```  ``` employee_workplaces.Agreement3 = employee_salary_opunit_costing.EmployeeAgreement ``` |
| [employment\_conditions](#employment-conditions) | ``` employee_workplaces.EmployeeId = employment_conditions.Creator ```  ``` employee_workplaces.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` employee_workplaces.EmployeeId = events.Creator ```  ``` employee_workplaces.Creator = events.Creator ``` |
| [geo](#geo) | ``` employee_workplaces.EmployeeId = geo.Creator ```  ``` employee_workplaces.Creator = geo.Creator ``` |
| [journal](#journal) | ``` employee_workplaces.EmployeeId = journal.EmployeeId ```  ``` employee_workplaces.Creator = journal.EmployeeId ```  ``` employee_workplaces.EmployeeId = journal.Creator ```  ``` employee_workplaces.Creator = journal.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employee_workplaces.EmployeeId = leave_accruals.Employee ```  ``` employee_workplaces.Creator = leave_accruals.Employee ```  ``` employee_workplaces.EmployeeId = leave_accruals.Creator ```  ``` employee_workplaces.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employee_workplaces.EmployeeId = leave_pay_lines.Creator ```  ``` employee_workplaces.Creator = leave_pay_lines.Creator ```  ``` employee_workplaces.Agreement1 = leave_pay_lines.EmployeeAgreement ```  ``` employee_workplaces.Agreement2 = leave_pay_lines.EmployeeAgreement ```  ``` employee_workplaces.Agreement3 = leave_pay_lines.EmployeeAgreement ``` |
| [leave\_rules](#leave-rules) | ``` employee_workplaces.EmployeeId = leave_rules.Creator ```  ``` employee_workplaces.Creator = leave_rules.Creator ``` |
| [memos](#memos) | ``` employee_workplaces.EmployeeId = memos.Creator ```  ``` employee_workplaces.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` employee_workplaces.EmployeeId = operational_units.Creator ```  ``` employee_workplaces.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` employee_workplaces.EmployeeId = pay_periods.Creator ```  ``` employee_workplaces.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` employee_workplaces.EmployeeId = pay_rules.Creator ```  ``` employee_workplaces.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` employee_workplaces.EmployeeId = public_holidays.Creator ```  ``` employee_workplaces.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employee_workplaces.EmployeeId = roster_opens.Employee ```  ``` employee_workplaces.Creator = roster_opens.Employee ```  ``` employee_workplaces.EmployeeId = roster_opens.Creator ```  ``` employee_workplaces.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employee_workplaces.EmployeeId = roster_swaps.Employee ```  ``` employee_workplaces.Creator = roster_swaps.Employee ```  ``` employee_workplaces.EmployeeId = roster_swaps.Creator ```  ``` employee_workplaces.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employee_workplaces.EmployeeId = rosters.Employee ```  ``` employee_workplaces.Creator = rosters.Employee ```  ``` employee_workplaces.EmployeeId = rosters.ConfirmBy ```  ``` employee_workplaces.Creator = rosters.ConfirmBy ```  ``` employee_workplaces.EmployeeId = rosters.Creator ```  ``` employee_workplaces.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` employee_workplaces.EmployeeId = sales_data.Employee ```  ``` employee_workplaces.Creator = sales_data.Employee ```  ``` employee_workplaces.EmployeeId = sales_data.Creator ```  ``` employee_workplaces.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` employee_workplaces.EmployeeId = schedules.Creator ```  ``` employee_workplaces.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` employee_workplaces.EmployeeId = sms_logs.Creator ```  ``` employee_workplaces.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` employee_workplaces.EmployeeId = states.Creator ```  ``` employee_workplaces.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employee_workplaces.EmployeeId = stress_profiles.Creator ```  ``` employee_workplaces.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employee_workplaces.EmployeeId = system_usage_balances.Creator ```  ``` employee_workplaces.Creator = system_usage_balances.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employee_workplaces.EmployeeId = task_group_setups.Creator ```  ``` employee_workplaces.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employee_workplaces.EmployeeId = task_groups.Creator ```  ``` employee_workplaces.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employee_workplaces.EmployeeId = task_opunit_configs.Creator ```  ``` employee_workplaces.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` employee_workplaces.EmployeeId = task_setups.Creator ```  ``` employee_workplaces.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` employee_workplaces.EmployeeId = tasks.Creator ```  ``` employee_workplaces.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` employee_workplaces.EmployeeId = teams.LeaderEmployee ```  ``` employee_workplaces.Creator = teams.LeaderEmployee ```  ``` employee_workplaces.EmployeeId = teams.Creator ```  ``` employee_workplaces.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employee_workplaces.EmployeeId = timesheet_pay_returns.Creator ```  ``` employee_workplaces.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` employee_workplaces.EmployeeId = timesheets.Employee ```  ``` employee_workplaces.Creator = timesheets.Employee ```  ``` employee_workplaces.EmployeeId = timesheets.Creator ```  ``` employee_workplaces.Creator = timesheets.Creator ```  ``` employee_workplaces.Agreement1 = timesheets.EmployeeAgreement ```  ``` employee_workplaces.Agreement2 = timesheets.EmployeeAgreement ```  ``` employee_workplaces.Agreement3 = timesheets.EmployeeAgreement ``` |
| [training\_modules](#training-modules) | ``` employee_workplaces.EmployeeId = training_modules.Creator ```  ``` employee_workplaces.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employee_workplaces.EmployeeId = training_records.Employee ```  ``` employee_workplaces.Creator = training_records.Employee ```  ``` employee_workplaces.EmployeeId = training_records.Creator ```  ``` employee_workplaces.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employee_workplaces.EmployeeId = webhooks.Creator ```  ``` employee_workplaces.Creator = webhooks.Creator ``` |

employee\_workplaces table schema

|  |
| --- |
| **Agreement1**  INTEGER |
| **Agreement2**  INTEGER |
| **Agreement3**  INTEGER |
| **Company**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **EmployeeId**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **SortOrder**  INTEGER |

### employment\_conditions

The `employment_conditions` table contains info about employment conditions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/EmploymentCondition) |

employment\_conditions table foreign keys

| Join employment\_conditions with | on |
| --- | --- |
| [categories](#categories) | ``` employment_conditions.EmploymentCategory = categories.Id ```  ``` employment_conditions.Creator = categories.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` employment_conditions.EmploymentCategory = employee_contracts.EmploymentCategory ```  ``` employment_conditions.Creator = employee_contracts.Creator ```  ``` employment_conditions.Id = employee_contracts.EmploymentCondition ``` |
| [addresses](#addresses) | ``` employment_conditions.Creator = addresses.Creator ``` |
| [comments](#comments) | ``` employment_conditions.Creator = comments.Creator ``` |
| [companies](#companies) | ``` employment_conditions.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` employment_conditions.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` employment_conditions.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` employment_conditions.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` employment_conditions.Creator = custom_app_data.Employee ```  ``` employment_conditions.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` employment_conditions.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` employment_conditions.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` employment_conditions.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` employment_conditions.Creator = employee_agreements.EmployeeId ```  ``` employment_conditions.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` employment_conditions.Creator = employee_appraisal.Creator ```  ``` employment_conditions.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` employment_conditions.Creator = employee_availability.Employee ```  ``` employment_conditions.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` employment_conditions.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_history](#employee-history) | ``` employment_conditions.Creator = employee_history.EmployeeId ```  ``` employment_conditions.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` employment_conditions.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` employment_conditions.Creator = employee_paycycles.EmployeeId ```  ``` employment_conditions.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` employment_conditions.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` employment_conditions.Creator = employee_salary_opunit_costing.Employee ```  ``` employment_conditions.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` employment_conditions.Creator = employee_workplaces.EmployeeId ```  ``` employment_conditions.Creator = employee_workplaces.Creator ``` |
| [events](#events) | ``` employment_conditions.Creator = events.Creator ``` |
| [geo](#geo) | ``` employment_conditions.Creator = geo.Creator ``` |
| [journal](#journal) | ``` employment_conditions.Creator = journal.EmployeeId ```  ``` employment_conditions.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` employment_conditions.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` employment_conditions.Creator = leave_accruals.Employee ```  ``` employment_conditions.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` employment_conditions.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` employment_conditions.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` employment_conditions.Creator = leaves.Employee ```  ``` employment_conditions.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` employment_conditions.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` employment_conditions.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` employment_conditions.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` employment_conditions.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` employment_conditions.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` employment_conditions.Creator = roster_opens.Employee ```  ``` employment_conditions.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` employment_conditions.Creator = roster_swaps.Employee ```  ``` employment_conditions.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` employment_conditions.Creator = rosters.Employee ```  ``` employment_conditions.Creator = rosters.ConfirmBy ```  ``` employment_conditions.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` employment_conditions.Creator = sales_data.Employee ```  ``` employment_conditions.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` employment_conditions.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` employment_conditions.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` employment_conditions.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` employment_conditions.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` employment_conditions.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` employment_conditions.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` employment_conditions.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` employment_conditions.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` employment_conditions.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` employment_conditions.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` employment_conditions.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` employment_conditions.Creator = teams.LeaderEmployee ```  ``` employment_conditions.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` employment_conditions.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` employment_conditions.Creator = timesheets.Employee ```  ``` employment_conditions.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` employment_conditions.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` employment_conditions.Creator = training_records.Employee ```  ``` employment_conditions.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` employment_conditions.Creator = webhooks.Creator ``` |

employment\_conditions table schema

|  |
| --- |
| **AvgHoursPerDay**  NUMBER |
| **AwardLevel**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Description**  STRING |
| **EmploymentBasis**  INTEGER |
| **EmploymentCategory**  INTEGER |
| **EmploymentPeriod**  INTEGER |
| **EmploymentStatus**  INTEGER |
| **Id**  INTEGER |
| **MinHoursForLeave**  NUMBER |
| **MinHoursPerDay**  NUMBER |
| **Modified**  DATE-TIME |
| **Name**  STRING |
| **ProbationaryPeriod**  INTEGER |
| **UsualFinishTime**  STRING |
| **UsualMealbreak**  STRING |
| **UsualStartTime**  STRING |
| **WorkingDaysPerPeriod**  NUMBER |

### events

The `events` table contains info about events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Event) |

events table foreign keys

| Join events with | on |
| --- | --- |
| [addresses](#addresses) | ``` events.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` events.Creator = categories.Creator ``` |
| [comments](#comments) | ``` events.Creator = comments.Creator ``` |
| [companies](#companies) | ``` events.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` events.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` events.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` events.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` events.Creator = custom_app_data.Employee ```  ``` events.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` events.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` events.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` events.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` events.Creator = employee_agreements.EmployeeId ```  ``` events.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` events.Creator = employee_appraisal.Creator ```  ``` events.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` events.Creator = employee_availability.Employee ```  ``` events.Creator = employee_availability.Creator ```  ``` events.Schedule = employee_availability.Schedule ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` events.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` events.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` events.Creator = employee_history.EmployeeId ```  ``` events.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` events.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` events.Creator = employee_paycycles.EmployeeId ```  ``` events.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` events.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` events.Creator = employee_salary_opunit_costing.Employee ```  ``` events.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` events.Creator = employee_workplaces.EmployeeId ```  ``` events.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` events.Creator = employment_conditions.Creator ``` |
| [geo](#geo) | ``` events.Creator = geo.Creator ``` |
| [journal](#journal) | ``` events.Creator = journal.EmployeeId ```  ``` events.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` events.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` events.Creator = leave_accruals.Employee ```  ``` events.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` events.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` events.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` events.Creator = leaves.Employee ```  ``` events.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` events.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` events.Creator = operational_units.Creator ```  ``` events.Schedule = operational_units.RosterActiveHoursSchedule ``` |
| [pay\_periods](#pay-periods) | ``` events.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` events.Creator = pay_rules.Creator ```  ``` events.Schedule = pay_rules.Schedule ``` |
| [public\_holidays](#public-holidays) | ``` events.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` events.Creator = roster_opens.Employee ```  ``` events.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` events.Creator = roster_swaps.Employee ```  ``` events.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` events.Creator = rosters.Employee ```  ``` events.Creator = rosters.ConfirmBy ```  ``` events.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` events.Creator = sales_data.Employee ```  ``` events.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` events.Creator = schedules.Creator ```  ``` events.Schedule = schedules.Id ``` |
| [sms\_logs](#sms-logs) | ``` events.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` events.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` events.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` events.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` events.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` events.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` events.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` events.Creator = task_opunit_configs.Creator ```  ``` events.Schedule = task_opunit_configs.Schedule ``` |
| [task\_setups](#task-setups) | ``` events.Creator = task_setups.Creator ```  ``` events.Schedule = task_setups.Schedule ``` |
| [tasks](#tasks) | ``` events.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` events.Creator = teams.LeaderEmployee ```  ``` events.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` events.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` events.Creator = timesheets.Employee ```  ``` events.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` events.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` events.Creator = training_records.Employee ```  ``` events.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` events.Creator = webhooks.Creator ``` |

events table schema

|  |
| --- |
| **AddToBudget**  NUMBER |
| **BlockTimeOff**  BOOLEAN |
| **Colour**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Schedule**  INTEGER |
| **ShowOnRoster**  BOOLEAN |
| **Title**  STRING |

### geo

The `geo` table contains info about geographic locations.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Geo) |

geo table foreign keys

| Join geo with | on |
| --- | --- |
| [countries](#countries) | ``` geo.Country = countries.Id ```  ``` geo.Creator = countries.Creator ``` |
| [states](#states) | ``` geo.Country = states.Country ```  ``` geo.Creator = states.Creator ``` |
| [addresses](#addresses) | ``` geo.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` geo.Creator = categories.Creator ``` |
| [comments](#comments) | ``` geo.Creator = comments.Creator ``` |
| [companies](#companies) | ``` geo.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` geo.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` geo.Creator = contacts.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` geo.Creator = custom_app_data.Employee ```  ``` geo.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` geo.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` geo.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` geo.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` geo.Creator = employee_agreements.EmployeeId ```  ``` geo.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` geo.Creator = employee_appraisal.Creator ```  ``` geo.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` geo.Creator = employee_availability.Employee ```  ``` geo.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` geo.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` geo.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` geo.Creator = employee_history.EmployeeId ```  ``` geo.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` geo.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` geo.Creator = employee_paycycles.EmployeeId ```  ``` geo.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` geo.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` geo.Creator = employee_salary_opunit_costing.Employee ```  ``` geo.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` geo.Creator = employee_workplaces.EmployeeId ```  ``` geo.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` geo.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` geo.Creator = events.Creator ``` |
| [journal](#journal) | ``` geo.Creator = journal.EmployeeId ```  ``` geo.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` geo.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` geo.Creator = leave_accruals.Employee ```  ``` geo.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` geo.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` geo.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` geo.Creator = leaves.Employee ```  ``` geo.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` geo.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` geo.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` geo.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` geo.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` geo.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` geo.Creator = roster_opens.Employee ```  ``` geo.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` geo.Creator = roster_swaps.Employee ```  ``` geo.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` geo.Creator = rosters.Employee ```  ``` geo.Creator = rosters.ConfirmBy ```  ``` geo.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` geo.Creator = sales_data.Employee ```  ``` geo.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` geo.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` geo.Creator = sms_logs.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` geo.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` geo.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` geo.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` geo.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` geo.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` geo.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` geo.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` geo.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` geo.Creator = teams.LeaderEmployee ```  ``` geo.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` geo.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` geo.Creator = timesheets.Employee ```  ``` geo.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` geo.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` geo.Creator = training_records.Employee ```  ``` geo.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` geo.Creator = webhooks.Creator ``` |

geo table schema

|  |
| --- |
| **Country**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **Latitude**  STRING |
| **Longitude**  STRING |
| **Modified**  DATE-TIME |
| **No**  STRING |
| **Orm**  STRING |
| **Postcode**  STRING |
| **RecId**  INTEGER |
| **State**  STRING |
| **Street**  STRING |
| **Suburb**  STRING |

### journal

The `journal` table contains info about journals.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Journal) |

journal table foreign keys

| Join journal with | on |
| --- | --- |
| [addresses](#addresses) | ``` journal.EmployeeId = addresses.Creator ```  ``` journal.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` journal.EmployeeId = categories.Creator ```  ``` journal.Creator = categories.Creator ``` |
| [comments](#comments) | ``` journal.EmployeeId = comments.Creator ```  ``` journal.Creator = comments.Creator ``` |
| [companies](#companies) | ``` journal.EmployeeId = companies.Creator ```  ``` journal.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` journal.EmployeeId = company_periods.Creator ```  ``` journal.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` journal.EmployeeId = contacts.Creator ```  ``` journal.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` journal.EmployeeId = countries.Creator ```  ``` journal.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` journal.EmployeeId = custom_app_data.Employee ```  ``` journal.Creator = custom_app_data.Employee ```  ``` journal.EmployeeId = custom_app_data.Creator ```  ``` journal.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` journal.EmployeeId = custom_field_data.Creator ```  ``` journal.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` journal.EmployeeId = custom_fields.Creator ```  ``` journal.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` journal.EmployeeId = employee_agreement_history.Creator ```  ``` journal.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` journal.EmployeeId = employee_agreements.EmployeeId ```  ``` journal.Creator = employee_agreements.EmployeeId ```  ``` journal.EmployeeId = employee_agreements.Creator ```  ``` journal.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` journal.EmployeeId = employee_appraisal.Creator ```  ``` journal.Creator = employee_appraisal.Creator ```  ``` journal.EmployeeId = employee_appraisal.Employee ```  ``` journal.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` journal.EmployeeId = employee_availability.Employee ```  ``` journal.Creator = employee_availability.Employee ```  ``` journal.EmployeeId = employee_availability.Creator ```  ``` journal.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` journal.EmployeeId = employee_contract_leave_rules.Creator ```  ``` journal.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` journal.EmployeeId = employee_contracts.Creator ```  ``` journal.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` journal.EmployeeId = employee_history.EmployeeId ```  ``` journal.Creator = employee_history.EmployeeId ```  ``` journal.EmployeeId = employee_history.Creator ```  ``` journal.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` journal.EmployeeId = employee_paycycle_returns.Creator ```  ``` journal.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` journal.EmployeeId = employee_paycycles.EmployeeId ```  ``` journal.Creator = employee_paycycles.EmployeeId ```  ``` journal.EmployeeId = employee_paycycles.Creator ```  ``` journal.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` journal.EmployeeId = employee_roles.Creator ```  ``` journal.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` journal.EmployeeId = employee_salary_opunit_costing.Employee ```  ``` journal.Creator = employee_salary_opunit_costing.Employee ```  ``` journal.EmployeeId = employee_salary_opunit_costing.Creator ```  ``` journal.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` journal.EmployeeId = employee_workplaces.EmployeeId ```  ``` journal.Creator = employee_workplaces.EmployeeId ```  ``` journal.EmployeeId = employee_workplaces.Creator ```  ``` journal.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` journal.EmployeeId = employment_conditions.Creator ```  ``` journal.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` journal.EmployeeId = events.Creator ```  ``` journal.Creator = events.Creator ``` |
| [geo](#geo) | ``` journal.EmployeeId = geo.Creator ```  ``` journal.Creator = geo.Creator ``` |
| [kiosks](#kiosks) | ``` journal.EmployeeId = kiosks.Creator ```  ``` journal.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` journal.EmployeeId = leave_accruals.Employee ```  ``` journal.Creator = leave_accruals.Employee ```  ``` journal.EmployeeId = leave_accruals.Creator ```  ``` journal.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` journal.EmployeeId = leave_pay_lines.Creator ```  ``` journal.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` journal.EmployeeId = leave_rules.Creator ```  ``` journal.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` journal.EmployeeId = leaves.Employee ```  ``` journal.Creator = leaves.Employee ```  ``` journal.EmployeeId = leaves.Creator ```  ``` journal.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` journal.EmployeeId = memos.Creator ```  ``` journal.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` journal.EmployeeId = operational_units.Creator ```  ``` journal.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` journal.EmployeeId = pay_periods.Creator ```  ``` journal.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` journal.EmployeeId = pay_rules.Creator ```  ``` journal.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` journal.EmployeeId = public_holidays.Creator ```  ``` journal.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` journal.EmployeeId = roster_opens.Employee ```  ``` journal.Creator = roster_opens.Employee ```  ``` journal.EmployeeId = roster_opens.Creator ```  ``` journal.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` journal.EmployeeId = roster_swaps.Employee ```  ``` journal.Creator = roster_swaps.Employee ```  ``` journal.EmployeeId = roster_swaps.Creator ```  ``` journal.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` journal.EmployeeId = rosters.Employee ```  ``` journal.Creator = rosters.Employee ```  ``` journal.EmployeeId = rosters.ConfirmBy ```  ``` journal.Creator = rosters.ConfirmBy ```  ``` journal.EmployeeId = rosters.Creator ```  ``` journal.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` journal.EmployeeId = sales_data.Employee ```  ``` journal.Creator = sales_data.Employee ```  ``` journal.EmployeeId = sales_data.Creator ```  ``` journal.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` journal.EmployeeId = schedules.Creator ```  ``` journal.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` journal.EmployeeId = sms_logs.Creator ```  ``` journal.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` journal.EmployeeId = states.Creator ```  ``` journal.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` journal.EmployeeId = stress_profiles.Creator ```  ``` journal.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` journal.EmployeeId = system_usage_balances.Creator ```  ``` journal.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` journal.EmployeeId = system_usage_tracking.Creator ```  ``` journal.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` journal.EmployeeId = task_group_setups.Creator ```  ``` journal.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` journal.EmployeeId = task_groups.Creator ```  ``` journal.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` journal.EmployeeId = task_opunit_configs.Creator ```  ``` journal.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` journal.EmployeeId = task_setups.Creator ```  ``` journal.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` journal.EmployeeId = tasks.Creator ```  ``` journal.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` journal.EmployeeId = teams.LeaderEmployee ```  ``` journal.Creator = teams.LeaderEmployee ```  ``` journal.EmployeeId = teams.Creator ```  ``` journal.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` journal.EmployeeId = timesheet_pay_returns.Creator ```  ``` journal.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` journal.EmployeeId = timesheets.Employee ```  ``` journal.Creator = timesheets.Employee ```  ``` journal.EmployeeId = timesheets.Creator ```  ``` journal.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` journal.EmployeeId = training_modules.Creator ```  ``` journal.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` journal.EmployeeId = training_records.Employee ```  ``` journal.Creator = training_records.Employee ```  ``` journal.EmployeeId = training_records.Creator ```  ``` journal.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` journal.EmployeeId = webhooks.Creator ```  ``` journal.Creator = webhooks.Creator ``` |

journal table schema

|  |
| --- |
| **Comment**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Date**  DATE |
| **EmployeeId**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |

### kiosks

The `kiosks` table contains info about kiosks.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Kiosk) |

kiosks table foreign keys

| Join kiosks with | on |
| --- | --- |
| [companies](#companies) | ``` kiosks.Company = companies.Id ```  ``` kiosks.Company = companies.ParentCompany ```  ``` kiosks.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` kiosks.Company = company_periods.Company ```  ``` kiosks.Creator = company_periods.Creator ``` |
| [employee\_history](#employee-history) | ``` kiosks.Company = employee_history.Company ```  ``` kiosks.Creator = employee_history.EmployeeId ```  ``` kiosks.Creator = employee_history.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` kiosks.Company = employee_workplaces.Company ```  ``` kiosks.Creator = employee_workplaces.EmployeeId ```  ``` kiosks.Creator = employee_workplaces.Creator ``` |
| [leaves](#leaves) | ``` kiosks.Company = leaves.Company ```  ``` kiosks.Creator = leaves.Employee ```  ``` kiosks.Creator = leaves.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` kiosks.Company = system_usage_tracking.CompanyId ```  ``` kiosks.Creator = system_usage_tracking.Creator ``` |
| [addresses](#addresses) | ``` kiosks.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` kiosks.Creator = categories.Creator ``` |
| [comments](#comments) | ``` kiosks.Creator = comments.Creator ``` |
| [contacts](#contacts) | ``` kiosks.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` kiosks.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` kiosks.Creator = custom_app_data.Employee ```  ``` kiosks.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` kiosks.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` kiosks.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` kiosks.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` kiosks.Creator = employee_agreements.EmployeeId ```  ``` kiosks.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` kiosks.Creator = employee_appraisal.Creator ```  ``` kiosks.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` kiosks.Creator = employee_availability.Employee ```  ``` kiosks.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` kiosks.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` kiosks.Creator = employee_contracts.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` kiosks.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` kiosks.Creator = employee_paycycles.EmployeeId ```  ``` kiosks.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` kiosks.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` kiosks.Creator = employee_salary_opunit_costing.Employee ```  ``` kiosks.Creator = employee_salary_opunit_costing.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` kiosks.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` kiosks.Creator = events.Creator ``` |
| [geo](#geo) | ``` kiosks.Creator = geo.Creator ``` |
| [journal](#journal) | ``` kiosks.Creator = journal.EmployeeId ```  ``` kiosks.Creator = journal.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` kiosks.Creator = leave_accruals.Employee ```  ``` kiosks.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` kiosks.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` kiosks.Creator = leave_rules.Creator ``` |
| [memos](#memos) | ``` kiosks.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` kiosks.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` kiosks.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` kiosks.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` kiosks.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` kiosks.Creator = roster_opens.Employee ```  ``` kiosks.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` kiosks.Creator = roster_swaps.Employee ```  ``` kiosks.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` kiosks.Creator = rosters.Employee ```  ``` kiosks.Creator = rosters.ConfirmBy ```  ``` kiosks.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` kiosks.Creator = sales_data.Employee ```  ``` kiosks.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` kiosks.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` kiosks.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` kiosks.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` kiosks.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` kiosks.Creator = system_usage_balances.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` kiosks.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` kiosks.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` kiosks.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` kiosks.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` kiosks.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` kiosks.Creator = teams.LeaderEmployee ```  ``` kiosks.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` kiosks.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` kiosks.Creator = timesheets.Employee ```  ``` kiosks.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` kiosks.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` kiosks.Creator = training_records.Employee ```  ``` kiosks.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` kiosks.Creator = webhooks.Creator ``` |

kiosks table schema

|  |
| --- |
| **AuthenticationMode**  INTEGER |
| **Company**  INTEGER |
| **ConnectionMode**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **InstallationId**  STRING |
| **IpAddress**  STRING |
| **LastActivity**  STRING |
| **Modified**  DATE-TIME |
| **Name**  STRING |
| **SubnetRestriction**  STRING |
| **UseBiometric**  BOOLEAN |

### leave\_accruals

The `leave_accruals` table contains info about employee leave balances.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/LeaveAccrual) |

leave\_accruals table foreign keys

| Join leave\_accruals with | on |
| --- | --- |
| [addresses](#addresses) | ``` leave_accruals.Employee = addresses.Creator ```  ``` leave_accruals.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` leave_accruals.Employee = categories.Creator ```  ``` leave_accruals.Creator = categories.Creator ``` |
| [comments](#comments) | ``` leave_accruals.Employee = comments.Creator ```  ``` leave_accruals.Creator = comments.Creator ``` |
| [companies](#companies) | ``` leave_accruals.Employee = companies.Creator ```  ``` leave_accruals.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` leave_accruals.Employee = company_periods.Creator ```  ``` leave_accruals.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` leave_accruals.Employee = contacts.Creator ```  ``` leave_accruals.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` leave_accruals.Employee = countries.Creator ```  ``` leave_accruals.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` leave_accruals.Employee = custom_app_data.Employee ```  ``` leave_accruals.Creator = custom_app_data.Employee ```  ``` leave_accruals.Employee = custom_app_data.Creator ```  ``` leave_accruals.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` leave_accruals.Employee = custom_field_data.Creator ```  ``` leave_accruals.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` leave_accruals.Employee = custom_fields.Creator ```  ``` leave_accruals.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` leave_accruals.Employee = employee_agreement_history.Creator ```  ``` leave_accruals.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` leave_accruals.Employee = employee_agreements.EmployeeId ```  ``` leave_accruals.Creator = employee_agreements.EmployeeId ```  ``` leave_accruals.Employee = employee_agreements.Creator ```  ``` leave_accruals.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` leave_accruals.Employee = employee_appraisal.Creator ```  ``` leave_accruals.Creator = employee_appraisal.Creator ```  ``` leave_accruals.Employee = employee_appraisal.Employee ```  ``` leave_accruals.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` leave_accruals.Employee = employee_availability.Employee ```  ``` leave_accruals.Creator = employee_availability.Employee ```  ``` leave_accruals.Employee = employee_availability.Creator ```  ``` leave_accruals.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` leave_accruals.Employee = employee_contract_leave_rules.Creator ```  ``` leave_accruals.Creator = employee_contract_leave_rules.Creator ```  ``` leave_accruals.LeaveRule = employee_contract_leave_rules.LeaveRuleId ``` |
| [employee\_contracts](#employee-contracts) | ``` leave_accruals.Employee = employee_contracts.Creator ```  ``` leave_accruals.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` leave_accruals.Employee = employee_history.EmployeeId ```  ``` leave_accruals.Creator = employee_history.EmployeeId ```  ``` leave_accruals.Employee = employee_history.Creator ```  ``` leave_accruals.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` leave_accruals.Employee = employee_paycycle_returns.Creator ```  ``` leave_accruals.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` leave_accruals.Employee = employee_paycycles.EmployeeId ```  ``` leave_accruals.Creator = employee_paycycles.EmployeeId ```  ``` leave_accruals.Employee = employee_paycycles.Creator ```  ``` leave_accruals.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` leave_accruals.Employee = employee_roles.Creator ```  ``` leave_accruals.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` leave_accruals.Employee = employee_salary_opunit_costing.Employee ```  ``` leave_accruals.Creator = employee_salary_opunit_costing.Employee ```  ``` leave_accruals.Employee = employee_salary_opunit_costing.Creator ```  ``` leave_accruals.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` leave_accruals.Employee = employee_workplaces.EmployeeId ```  ``` leave_accruals.Creator = employee_workplaces.EmployeeId ```  ``` leave_accruals.Employee = employee_workplaces.Creator ```  ``` leave_accruals.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` leave_accruals.Employee = employment_conditions.Creator ```  ``` leave_accruals.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` leave_accruals.Employee = events.Creator ```  ``` leave_accruals.Creator = events.Creator ``` |
| [geo](#geo) | ``` leave_accruals.Employee = geo.Creator ```  ``` leave_accruals.Creator = geo.Creator ``` |
| [journal](#journal) | ``` leave_accruals.Employee = journal.EmployeeId ```  ``` leave_accruals.Creator = journal.EmployeeId ```  ``` leave_accruals.Employee = journal.Creator ```  ``` leave_accruals.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` leave_accruals.Employee = kiosks.Creator ```  ``` leave_accruals.Creator = kiosks.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` leave_accruals.Employee = leave_pay_lines.Creator ```  ``` leave_accruals.Creator = leave_pay_lines.Creator ```  ``` leave_accruals.LeaveRule = leave_pay_lines.LeaveRule ``` |
| [leave\_rules](#leave-rules) | ``` leave_accruals.Employee = leave_rules.Creator ```  ``` leave_accruals.Creator = leave_rules.Creator ```  ``` leave_accruals.LeaveRule = leave_rules.Id ``` |
| [leaves](#leaves) | ``` leave_accruals.Employee = leaves.Employee ```  ``` leave_accruals.Creator = leaves.Employee ```  ``` leave_accruals.Employee = leaves.Creator ```  ``` leave_accruals.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` leave_accruals.Employee = memos.Creator ```  ``` leave_accruals.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` leave_accruals.Employee = operational_units.Creator ```  ``` leave_accruals.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` leave_accruals.Employee = pay_periods.Creator ```  ``` leave_accruals.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` leave_accruals.Employee = pay_rules.Creator ```  ``` leave_accruals.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` leave_accruals.Employee = public_holidays.Creator ```  ``` leave_accruals.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` leave_accruals.Employee = roster_opens.Employee ```  ``` leave_accruals.Creator = roster_opens.Employee ```  ``` leave_accruals.Employee = roster_opens.Creator ```  ``` leave_accruals.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` leave_accruals.Employee = roster_swaps.Employee ```  ``` leave_accruals.Creator = roster_swaps.Employee ```  ``` leave_accruals.Employee = roster_swaps.Creator ```  ``` leave_accruals.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` leave_accruals.Employee = rosters.Employee ```  ``` leave_accruals.Creator = rosters.Employee ```  ``` leave_accruals.Employee = rosters.ConfirmBy ```  ``` leave_accruals.Creator = rosters.ConfirmBy ```  ``` leave_accruals.Employee = rosters.Creator ```  ``` leave_accruals.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` leave_accruals.Employee = sales_data.Employee ```  ``` leave_accruals.Creator = sales_data.Employee ```  ``` leave_accruals.Employee = sales_data.Creator ```  ``` leave_accruals.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` leave_accruals.Employee = schedules.Creator ```  ``` leave_accruals.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` leave_accruals.Employee = sms_logs.Creator ```  ``` leave_accruals.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` leave_accruals.Employee = states.Creator ```  ``` leave_accruals.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` leave_accruals.Employee = stress_profiles.Creator ```  ``` leave_accruals.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` leave_accruals.Employee = system_usage_balances.Creator ```  ``` leave_accruals.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` leave_accruals.Employee = system_usage_tracking.Creator ```  ``` leave_accruals.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` leave_accruals.Employee = task_group_setups.Creator ```  ``` leave_accruals.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` leave_accruals.Employee = task_groups.Creator ```  ``` leave_accruals.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` leave_accruals.Employee = task_opunit_configs.Creator ```  ``` leave_accruals.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` leave_accruals.Employee = task_setups.Creator ```  ``` leave_accruals.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` leave_accruals.Employee = tasks.Creator ```  ``` leave_accruals.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` leave_accruals.Employee = teams.LeaderEmployee ```  ``` leave_accruals.Creator = teams.LeaderEmployee ```  ``` leave_accruals.Employee = teams.Creator ```  ``` leave_accruals.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` leave_accruals.Employee = timesheet_pay_returns.Creator ```  ``` leave_accruals.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` leave_accruals.Employee = timesheets.Employee ```  ``` leave_accruals.Creator = timesheets.Employee ```  ``` leave_accruals.Employee = timesheets.Creator ```  ``` leave_accruals.Creator = timesheets.Creator ```  ``` leave_accruals.LeaveRule = timesheets.LeaveRule ``` |
| [training\_modules](#training-modules) | ``` leave_accruals.Employee = training_modules.Creator ```  ``` leave_accruals.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` leave_accruals.Employee = training_records.Employee ```  ``` leave_accruals.Creator = training_records.Employee ```  ``` leave_accruals.Employee = training_records.Creator ```  ``` leave_accruals.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` leave_accruals.Employee = webhooks.Creator ```  ``` leave_accruals.Creator = webhooks.Creator ``` |

leave\_accruals table schema

|  |
| --- |
| **Comment**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Days**  NUMBER |
| **Employee**  INTEGER |
| **EmployeeHistory**  INTEGER |
| **FkId**  INTEGER |
| **Hours**  NUMBER |
| **Id**  INTEGER |
| **LeaveRule**  INTEGER |
| **Modified**  DATE-TIME |
| **TransactionDate**  DATE |
| **Type**  INTEGER |

### leave\_pay\_lines

The `leave_pay_lines` table contains info about employee leave pay lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/LeavePayLine) |

leave\_pay\_lines table foreign keys

| Join leave\_pay\_lines with | on |
| --- | --- |
| [addresses](#addresses) | ``` leave_pay_lines.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` leave_pay_lines.Creator = categories.Creator ``` |
| [comments](#comments) | ``` leave_pay_lines.Creator = comments.Creator ``` |
| [companies](#companies) | ``` leave_pay_lines.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` leave_pay_lines.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` leave_pay_lines.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` leave_pay_lines.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` leave_pay_lines.Creator = custom_app_data.Employee ```  ``` leave_pay_lines.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` leave_pay_lines.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` leave_pay_lines.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` leave_pay_lines.Creator = employee_agreement_history.Creator ```  ``` leave_pay_lines.EmployeeAgreement = employee_agreement_history.AgreementId ``` |
| [employee\_agreements](#employee-agreements) | ``` leave_pay_lines.Creator = employee_agreements.EmployeeId ```  ``` leave_pay_lines.Creator = employee_agreements.Creator ```  ``` leave_pay_lines.EmployeeAgreement = employee_agreements.Id ``` |
| [employee\_appraisal](#employee-appraisal) | ``` leave_pay_lines.Creator = employee_appraisal.Creator ```  ``` leave_pay_lines.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` leave_pay_lines.Creator = employee_availability.Employee ```  ``` leave_pay_lines.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` leave_pay_lines.Creator = employee_contract_leave_rules.Creator ```  ``` leave_pay_lines.LeaveRule = employee_contract_leave_rules.LeaveRuleId ``` |
| [employee\_contracts](#employee-contracts) | ``` leave_pay_lines.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` leave_pay_lines.Creator = employee_history.EmployeeId ```  ``` leave_pay_lines.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` leave_pay_lines.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` leave_pay_lines.Creator = employee_paycycles.EmployeeId ```  ``` leave_pay_lines.Creator = employee_paycycles.Creator ```  ``` leave_pay_lines.EmployeeAgreement = employee_paycycles.EmployeeAgreementId ``` |
| [employee\_roles](#employee-roles) | ``` leave_pay_lines.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` leave_pay_lines.Creator = employee_salary_opunit_costing.Employee ```  ``` leave_pay_lines.Creator = employee_salary_opunit_costing.Creator ```  ``` leave_pay_lines.EmployeeAgreement = employee_salary_opunit_costing.EmployeeAgreement ``` |
| [employee\_workplaces](#employee-workplaces) | ``` leave_pay_lines.Creator = employee_workplaces.EmployeeId ```  ``` leave_pay_lines.Creator = employee_workplaces.Creator ```  ``` leave_pay_lines.EmployeeAgreement = employee_workplaces.Agreement1 ```  ``` leave_pay_lines.EmployeeAgreement = employee_workplaces.Agreement2 ```  ``` leave_pay_lines.EmployeeAgreement = employee_workplaces.Agreement3 ``` |
| [employment\_conditions](#employment-conditions) | ``` leave_pay_lines.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` leave_pay_lines.Creator = events.Creator ``` |
| [geo](#geo) | ``` leave_pay_lines.Creator = geo.Creator ``` |
| [journal](#journal) | ``` leave_pay_lines.Creator = journal.EmployeeId ```  ``` leave_pay_lines.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` leave_pay_lines.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` leave_pay_lines.Creator = leave_accruals.Employee ```  ``` leave_pay_lines.Creator = leave_accruals.Creator ```  ``` leave_pay_lines.LeaveRule = leave_accruals.LeaveRule ``` |
| [leave\_rules](#leave-rules) | ``` leave_pay_lines.Creator = leave_rules.Creator ```  ``` leave_pay_lines.LeaveRule = leave_rules.Id ``` |
| [leaves](#leaves) | ``` leave_pay_lines.Creator = leaves.Employee ```  ``` leave_pay_lines.Creator = leaves.Creator ```  ``` leave_pay_lines.LeaveId = leaves.Id ``` |
| [memos](#memos) | ``` leave_pay_lines.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` leave_pay_lines.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` leave_pay_lines.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` leave_pay_lines.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` leave_pay_lines.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` leave_pay_lines.Creator = roster_opens.Employee ```  ``` leave_pay_lines.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` leave_pay_lines.Creator = roster_swaps.Employee ```  ``` leave_pay_lines.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` leave_pay_lines.Creator = rosters.Employee ```  ``` leave_pay_lines.Creator = rosters.ConfirmBy ```  ``` leave_pay_lines.Creator = rosters.Creator ```  ``` leave_pay_lines.TimesheetId = rosters.MatchedByTimesheet ``` |
| [sales\_data](#sales-data) | ``` leave_pay_lines.Creator = sales_data.Employee ```  ``` leave_pay_lines.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` leave_pay_lines.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` leave_pay_lines.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` leave_pay_lines.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` leave_pay_lines.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` leave_pay_lines.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` leave_pay_lines.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` leave_pay_lines.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` leave_pay_lines.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` leave_pay_lines.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` leave_pay_lines.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` leave_pay_lines.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` leave_pay_lines.Creator = teams.LeaderEmployee ```  ``` leave_pay_lines.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` leave_pay_lines.Creator = timesheet_pay_returns.Creator ```  ``` leave_pay_lines.TimesheetId = timesheet_pay_returns.Timesheet ``` |
| [timesheets](#timesheets) | ``` leave_pay_lines.Creator = timesheets.Employee ```  ``` leave_pay_lines.Creator = timesheets.Creator ```  ``` leave_pay_lines.EmployeeAgreement = timesheets.EmployeeAgreement ```  ``` leave_pay_lines.LeaveId = timesheets.LeaveId ```  ``` leave_pay_lines.LeaveRule = timesheets.LeaveRule ```  ``` leave_pay_lines.TimesheetId = timesheets.Id ``` |
| [training\_modules](#training-modules) | ``` leave_pay_lines.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` leave_pay_lines.Creator = training_records.Employee ```  ``` leave_pay_lines.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` leave_pay_lines.Creator = webhooks.Creator ``` |

leave\_pay\_lines table schema

|  |
| --- |
| **Comment**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Date**  DATE |
| **EmployeeAgreement**  INTEGER |
| **EndTime**  STRING |
| **Hours**  STRING |
| **Id**  INTEGER |
| **LeaveId**  INTEGER |
| **LeaveRule**  INTEGER |
| **Modified**  DATE-TIME |
| **StartTime**  STRING |
| **TimesheetId**  INTEGER |

### leave\_rules

The `leave_rules` table contains info about employee leave rules.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/LeaveRules) |

leave\_rules table foreign keys

| Join leave\_rules with | on |
| --- | --- |
| [addresses](#addresses) | ``` leave_rules.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` leave_rules.Creator = categories.Creator ``` |
| [comments](#comments) | ``` leave_rules.Creator = comments.Creator ``` |
| [companies](#companies) | ``` leave_rules.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` leave_rules.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` leave_rules.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` leave_rules.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` leave_rules.Creator = custom_app_data.Employee ```  ``` leave_rules.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` leave_rules.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` leave_rules.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` leave_rules.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` leave_rules.Creator = employee_agreements.EmployeeId ```  ``` leave_rules.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` leave_rules.Creator = employee_appraisal.Creator ```  ``` leave_rules.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` leave_rules.Creator = employee_availability.Employee ```  ``` leave_rules.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` leave_rules.Creator = employee_contract_leave_rules.Creator ```  ``` leave_rules.Id = employee_contract_leave_rules.LeaveRuleId ``` |
| [employee\_contracts](#employee-contracts) | ``` leave_rules.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` leave_rules.Creator = employee_history.EmployeeId ```  ``` leave_rules.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` leave_rules.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` leave_rules.Creator = employee_paycycles.EmployeeId ```  ``` leave_rules.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` leave_rules.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` leave_rules.Creator = employee_salary_opunit_costing.Employee ```  ``` leave_rules.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` leave_rules.Creator = employee_workplaces.EmployeeId ```  ``` leave_rules.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` leave_rules.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` leave_rules.Creator = events.Creator ``` |
| [geo](#geo) | ``` leave_rules.Creator = geo.Creator ``` |
| [journal](#journal) | ``` leave_rules.Creator = journal.EmployeeId ```  ``` leave_rules.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` leave_rules.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` leave_rules.Creator = leave_accruals.Employee ```  ``` leave_rules.Creator = leave_accruals.Creator ```  ``` leave_rules.Id = leave_accruals.LeaveRule ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` leave_rules.Creator = leave_pay_lines.Creator ```  ``` leave_rules.Id = leave_pay_lines.LeaveRule ``` |
| [leaves](#leaves) | ``` leave_rules.Creator = leaves.Employee ```  ``` leave_rules.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` leave_rules.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` leave_rules.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` leave_rules.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` leave_rules.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` leave_rules.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` leave_rules.Creator = roster_opens.Employee ```  ``` leave_rules.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` leave_rules.Creator = roster_swaps.Employee ```  ``` leave_rules.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` leave_rules.Creator = rosters.Employee ```  ``` leave_rules.Creator = rosters.ConfirmBy ```  ``` leave_rules.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` leave_rules.Creator = sales_data.Employee ```  ``` leave_rules.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` leave_rules.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` leave_rules.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` leave_rules.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` leave_rules.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` leave_rules.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` leave_rules.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` leave_rules.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` leave_rules.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` leave_rules.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` leave_rules.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` leave_rules.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` leave_rules.Creator = teams.LeaderEmployee ```  ``` leave_rules.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` leave_rules.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` leave_rules.Creator = timesheets.Employee ```  ``` leave_rules.Creator = timesheets.Creator ```  ``` leave_rules.Id = timesheets.LeaveRule ``` |
| [training\_modules](#training-modules) | ``` leave_rules.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` leave_rules.Creator = training_records.Employee ```  ``` leave_rules.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` leave_rules.Creator = webhooks.Creator ``` |

leave\_rules table schema

|  |
| --- |
| **AnnualRollOver**  BOOLEAN |
| **Calc**  STRING |
| **CalcType**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Description**  STRING |
| **EntitlementAfterMonth**  INTEGER |
| **ExportType**  INTEGER |
| **Id**  INTEGER |
| **MaxAllowedAnnually**  NUMBER |
| **Modified**  DATE-TIME |
| **Name**  STRING |
| **PaidLeave**  BOOLEAN |
| **PayoutOnTermination**  BOOLEAN |
| **PayrollCategory**  STRING |
| **ResetType**  INTEGER |
| **Type**  STRING |
| **UnitType**  INTEGER |
| **Visible**  BOOLEAN |

### leaves

The `leaves` table contains info about employee leave.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Leave) |

leaves table foreign keys

| Join leaves with | on |
| --- | --- |
| [companies](#companies) | ``` leaves.Company = companies.Id ```  ``` leaves.Company = companies.ParentCompany ```  ``` leaves.Employee = companies.Creator ```  ``` leaves.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` leaves.Company = company_periods.Company ```  ``` leaves.Employee = company_periods.Creator ```  ``` leaves.Creator = company_periods.Creator ``` |
| [employee\_history](#employee-history) | ``` leaves.Company = employee_history.Company ```  ``` leaves.Employee = employee_history.EmployeeId ```  ``` leaves.Creator = employee_history.EmployeeId ```  ``` leaves.Employee = employee_history.Creator ```  ``` leaves.Creator = employee_history.Creator ```  ``` leaves.EmployeeHistory = employee_history.Id ``` |
| [employee\_workplaces](#employee-workplaces) | ``` leaves.Company = employee_workplaces.Company ```  ``` leaves.Employee = employee_workplaces.EmployeeId ```  ``` leaves.Creator = employee_workplaces.EmployeeId ```  ``` leaves.Employee = employee_workplaces.Creator ```  ``` leaves.Creator = employee_workplaces.Creator ``` |
| [kiosks](#kiosks) | ``` leaves.Company = kiosks.Company ```  ``` leaves.Employee = kiosks.Creator ```  ``` leaves.Creator = kiosks.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` leaves.Company = system_usage_tracking.CompanyId ```  ``` leaves.Employee = system_usage_tracking.Creator ```  ``` leaves.Creator = system_usage_tracking.Creator ``` |
| [addresses](#addresses) | ``` leaves.Employee = addresses.Creator ```  ``` leaves.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` leaves.Employee = categories.Creator ```  ``` leaves.Creator = categories.Creator ``` |
| [comments](#comments) | ``` leaves.Employee = comments.Creator ```  ``` leaves.Creator = comments.Creator ``` |
| [contacts](#contacts) | ``` leaves.Employee = contacts.Creator ```  ``` leaves.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` leaves.Employee = countries.Creator ```  ``` leaves.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` leaves.Employee = custom_app_data.Employee ```  ``` leaves.Creator = custom_app_data.Employee ```  ``` leaves.Employee = custom_app_data.Creator ```  ``` leaves.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` leaves.Employee = custom_field_data.Creator ```  ``` leaves.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` leaves.Employee = custom_fields.Creator ```  ``` leaves.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` leaves.Employee = employee_agreement_history.Creator ```  ``` leaves.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` leaves.Employee = employee_agreements.EmployeeId ```  ``` leaves.Creator = employee_agreements.EmployeeId ```  ``` leaves.Employee = employee_agreements.Creator ```  ``` leaves.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` leaves.Employee = employee_appraisal.Creator ```  ``` leaves.Creator = employee_appraisal.Creator ```  ``` leaves.Employee = employee_appraisal.Employee ```  ``` leaves.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` leaves.Employee = employee_availability.Employee ```  ``` leaves.Creator = employee_availability.Employee ```  ``` leaves.Employee = employee_availability.Creator ```  ``` leaves.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` leaves.Employee = employee_contract_leave_rules.Creator ```  ``` leaves.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` leaves.Employee = employee_contracts.Creator ```  ``` leaves.Creator = employee_contracts.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` leaves.Employee = employee_paycycle_returns.Creator ```  ``` leaves.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` leaves.Employee = employee_paycycles.EmployeeId ```  ``` leaves.Creator = employee_paycycles.EmployeeId ```  ``` leaves.Employee = employee_paycycles.Creator ```  ``` leaves.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` leaves.Employee = employee_roles.Creator ```  ``` leaves.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` leaves.Employee = employee_salary_opunit_costing.Employee ```  ``` leaves.Creator = employee_salary_opunit_costing.Employee ```  ``` leaves.Employee = employee_salary_opunit_costing.Creator ```  ``` leaves.Creator = employee_salary_opunit_costing.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` leaves.Employee = employment_conditions.Creator ```  ``` leaves.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` leaves.Employee = events.Creator ```  ``` leaves.Creator = events.Creator ``` |
| [geo](#geo) | ``` leaves.Employee = geo.Creator ```  ``` leaves.Creator = geo.Creator ``` |
| [journal](#journal) | ``` leaves.Employee = journal.EmployeeId ```  ``` leaves.Creator = journal.EmployeeId ```  ``` leaves.Employee = journal.Creator ```  ``` leaves.Creator = journal.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` leaves.Employee = leave_accruals.Employee ```  ``` leaves.Creator = leave_accruals.Employee ```  ``` leaves.Employee = leave_accruals.Creator ```  ``` leaves.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` leaves.Employee = leave_pay_lines.Creator ```  ``` leaves.Creator = leave_pay_lines.Creator ```  ``` leaves.Id = leave_pay_lines.LeaveId ``` |
| [leave\_rules](#leave-rules) | ``` leaves.Employee = leave_rules.Creator ```  ``` leaves.Creator = leave_rules.Creator ``` |
| [memos](#memos) | ``` leaves.Employee = memos.Creator ```  ``` leaves.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` leaves.Employee = operational_units.Creator ```  ``` leaves.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` leaves.Employee = pay_periods.Creator ```  ``` leaves.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` leaves.Employee = pay_rules.Creator ```  ``` leaves.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` leaves.Employee = public_holidays.Creator ```  ``` leaves.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` leaves.Employee = roster_opens.Employee ```  ``` leaves.Creator = roster_opens.Employee ```  ``` leaves.Employee = roster_opens.Creator ```  ``` leaves.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` leaves.Employee = roster_swaps.Employee ```  ``` leaves.Creator = roster_swaps.Employee ```  ``` leaves.Employee = roster_swaps.Creator ```  ``` leaves.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` leaves.Employee = rosters.Employee ```  ``` leaves.Creator = rosters.Employee ```  ``` leaves.Employee = rosters.ConfirmBy ```  ``` leaves.Creator = rosters.ConfirmBy ```  ``` leaves.Employee = rosters.Creator ```  ``` leaves.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` leaves.Employee = sales_data.Employee ```  ``` leaves.Creator = sales_data.Employee ```  ``` leaves.Employee = sales_data.Creator ```  ``` leaves.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` leaves.Employee = schedules.Creator ```  ``` leaves.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` leaves.Employee = sms_logs.Creator ```  ``` leaves.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` leaves.Employee = states.Creator ```  ``` leaves.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` leaves.Employee = stress_profiles.Creator ```  ``` leaves.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` leaves.Employee = system_usage_balances.Creator ```  ``` leaves.Creator = system_usage_balances.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` leaves.Employee = task_group_setups.Creator ```  ``` leaves.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` leaves.Employee = task_groups.Creator ```  ``` leaves.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` leaves.Employee = task_opunit_configs.Creator ```  ``` leaves.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` leaves.Employee = task_setups.Creator ```  ``` leaves.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` leaves.Employee = tasks.Creator ```  ``` leaves.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` leaves.Employee = teams.LeaderEmployee ```  ``` leaves.Creator = teams.LeaderEmployee ```  ``` leaves.Employee = teams.Creator ```  ``` leaves.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` leaves.Employee = timesheet_pay_returns.Creator ```  ``` leaves.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` leaves.Employee = timesheets.Employee ```  ``` leaves.Creator = timesheets.Employee ```  ``` leaves.Employee = timesheets.Creator ```  ``` leaves.Creator = timesheets.Creator ```  ``` leaves.EmployeeHistory = timesheets.EmployeeHistory ```  ``` leaves.Id = timesheets.LeaveId ``` |
| [training\_modules](#training-modules) | ``` leaves.Employee = training_modules.Creator ```  ``` leaves.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` leaves.Employee = training_records.Employee ```  ``` leaves.Creator = training_records.Employee ```  ``` leaves.Employee = training_records.Creator ```  ``` leaves.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` leaves.Employee = webhooks.Creator ```  ``` leaves.Creator = webhooks.Creator ``` |

leaves table schema

|  |
| --- |
| **ApprovalComment**  STRING |
| **ApproverPay**  INTEGER |
| **ApproverTime**  INTEGER |
| **Comment**  STRING |
| **Company**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **DateEnd**  DATE |
| **Days**  NUMBER |
| **Employee**  INTEGER |
| **EmployeeHistory**  INTEGER |
| **End**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Start**  INTEGER |
| **Status**  INTEGER |
| **TotalHours**  NUMBER |

### memos

The `memos` table contains info about memos.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Memo) |

memos table foreign keys

| Join memos with | on |
| --- | --- |
| [addresses](#addresses) | ``` memos.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` memos.Creator = categories.Creator ``` |
| [comments](#comments) | ``` memos.Creator = comments.Creator ``` |
| [companies](#companies) | ``` memos.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` memos.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` memos.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` memos.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` memos.Creator = custom_app_data.Employee ```  ``` memos.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` memos.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` memos.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` memos.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` memos.Creator = employee_agreements.EmployeeId ```  ``` memos.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` memos.Creator = employee_appraisal.Creator ```  ``` memos.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` memos.Creator = employee_availability.Employee ```  ``` memos.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` memos.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` memos.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` memos.Creator = employee_history.EmployeeId ```  ``` memos.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` memos.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` memos.Creator = employee_paycycles.EmployeeId ```  ``` memos.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` memos.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` memos.Creator = employee_salary_opunit_costing.Employee ```  ``` memos.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` memos.Creator = employee_workplaces.EmployeeId ```  ``` memos.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` memos.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` memos.Creator = events.Creator ``` |
| [geo](#geo) | ``` memos.Creator = geo.Creator ``` |
| [journal](#journal) | ``` memos.Creator = journal.EmployeeId ```  ``` memos.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` memos.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` memos.Creator = leave_accruals.Employee ```  ``` memos.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` memos.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` memos.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` memos.Creator = leaves.Employee ```  ``` memos.Creator = leaves.Creator ``` |
| [operational\_units](#operational-units) | ``` memos.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` memos.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` memos.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` memos.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` memos.Creator = roster_opens.Employee ```  ``` memos.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` memos.Creator = roster_swaps.Employee ```  ``` memos.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` memos.Creator = rosters.Employee ```  ``` memos.Creator = rosters.ConfirmBy ```  ``` memos.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` memos.Creator = sales_data.Employee ```  ``` memos.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` memos.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` memos.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` memos.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` memos.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` memos.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` memos.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` memos.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` memos.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` memos.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` memos.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` memos.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` memos.Creator = teams.LeaderEmployee ```  ``` memos.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` memos.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` memos.Creator = timesheets.Employee ```  ``` memos.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` memos.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` memos.Creator = training_records.Employee ```  ``` memos.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` memos.Creator = webhooks.Creator ``` |

memos table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **ConfirmText**  STRING |
| **Content**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **File**  INTEGER |
| **Id**  INTEGER |
| **Keyword**  STRING |
| **Modified**  DATE-TIME |
| **ShowFrom**  DATE |
| **ShowTill**  DATE |
| **Title**  STRING |
| **Type**  INTEGER |
| **Url**  STRING |

### operational\_units

The `operational_units` table contains info about operational units.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/OperationalUnit) |

operational\_units table foreign keys

| Join operational\_units with | on |
| --- | --- |
| [addresses](#addresses) | ``` operational_units.Address = addresses.Id ```  ``` operational_units.Creator = addresses.Creator ``` |
| [companies](#companies) | ``` operational_units.Address = companies.Address ```  ``` operational_units.Contact = companies.Contact ```  ``` operational_units.Creator = companies.Creator ``` |
| [employee\_history](#employee-history) | ``` operational_units.Address = employee_history.MainAddress ```  ``` operational_units.Address = employee_history.PostalAddress ```  ``` operational_units.Address = employee_history.EmergencyAddress ```  ``` operational_units.Creator = employee_history.EmployeeId ```  ``` operational_units.Creator = employee_history.Creator ``` |
| [contacts](#contacts) | ``` operational_units.Contact = contacts.Id ```  ``` operational_units.Creator = contacts.Creator ``` |
| [categories](#categories) | ``` operational_units.Creator = categories.Creator ``` |
| [comments](#comments) | ``` operational_units.Creator = comments.Creator ``` |
| [company\_periods](#company-periods) | ``` operational_units.Creator = company_periods.Creator ``` |
| [countries](#countries) | ``` operational_units.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` operational_units.Creator = custom_app_data.Employee ```  ``` operational_units.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` operational_units.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` operational_units.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` operational_units.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` operational_units.Creator = employee_agreements.EmployeeId ```  ``` operational_units.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` operational_units.Creator = employee_appraisal.Creator ```  ``` operational_units.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` operational_units.Creator = employee_availability.Employee ```  ``` operational_units.Creator = employee_availability.Creator ```  ``` operational_units.RosterActiveHoursSchedule = employee_availability.Schedule ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` operational_units.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` operational_units.Creator = employee_contracts.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` operational_units.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` operational_units.Creator = employee_paycycles.EmployeeId ```  ``` operational_units.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` operational_units.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` operational_units.Creator = employee_salary_opunit_costing.Employee ```  ``` operational_units.Creator = employee_salary_opunit_costing.Creator ```  ``` operational_units.Id = employee_salary_opunit_costing.OpUnit ```  ``` operational_units.ParentOperationalUnit = employee_salary_opunit_costing.OpUnit ``` |
| [employee\_workplaces](#employee-workplaces) | ``` operational_units.Creator = employee_workplaces.EmployeeId ```  ``` operational_units.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` operational_units.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` operational_units.Creator = events.Creator ```  ``` operational_units.RosterActiveHoursSchedule = events.Schedule ``` |
| [geo](#geo) | ``` operational_units.Creator = geo.Creator ``` |
| [journal](#journal) | ``` operational_units.Creator = journal.EmployeeId ```  ``` operational_units.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` operational_units.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` operational_units.Creator = leave_accruals.Employee ```  ``` operational_units.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` operational_units.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` operational_units.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` operational_units.Creator = leaves.Employee ```  ``` operational_units.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` operational_units.Creator = memos.Creator ``` |
| [pay\_periods](#pay-periods) | ``` operational_units.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` operational_units.Creator = pay_rules.Creator ```  ``` operational_units.RosterActiveHoursSchedule = pay_rules.Schedule ``` |
| [public\_holidays](#public-holidays) | ``` operational_units.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` operational_units.Creator = roster_opens.Employee ```  ``` operational_units.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` operational_units.Creator = roster_swaps.Employee ```  ``` operational_units.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` operational_units.Creator = rosters.Employee ```  ``` operational_units.Creator = rosters.ConfirmBy ```  ``` operational_units.Creator = rosters.Creator ```  ``` operational_units.Id = rosters.OperationalUnit ```  ``` operational_units.ParentOperationalUnit = rosters.OperationalUnit ``` |
| [sales\_data](#sales-data) | ``` operational_units.Creator = sales_data.Employee ```  ``` operational_units.Creator = sales_data.Creator ```  ``` operational_units.Id = sales_data.OperationalUnit ```  ``` operational_units.ParentOperationalUnit = sales_data.OperationalUnit ``` |
| [schedules](#schedules) | ``` operational_units.Creator = schedules.Creator ```  ``` operational_units.RosterActiveHoursSchedule = schedules.Id ``` |
| [sms\_logs](#sms-logs) | ``` operational_units.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` operational_units.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` operational_units.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` operational_units.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` operational_units.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` operational_units.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` operational_units.Creator = task_groups.Creator ```  ``` operational_units.Id = task_groups.OpUnitId ```  ``` operational_units.ParentOperationalUnit = task_groups.OpUnitId ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` operational_units.Creator = task_opunit_configs.Creator ```  ``` operational_units.Id = task_opunit_configs.OpUnitId ```  ``` operational_units.ParentOperationalUnit = task_opunit_configs.OpUnitId ```  ``` operational_units.RosterActiveHoursSchedule = task_opunit_configs.Schedule ``` |
| [task\_setups](#task-setups) | ``` operational_units.Creator = task_setups.Creator ```  ``` operational_units.RosterActiveHoursSchedule = task_setups.Schedule ``` |
| [tasks](#tasks) | ``` operational_units.Creator = tasks.Creator ```  ``` operational_units.Id = tasks.OpUnitId ```  ``` operational_units.ParentOperationalUnit = tasks.OpUnitId ``` |
| [teams](#teams) | ``` operational_units.Creator = teams.LeaderEmployee ```  ``` operational_units.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` operational_units.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` operational_units.Creator = timesheets.Employee ```  ``` operational_units.Creator = timesheets.Creator ```  ``` operational_units.Id = timesheets.OperationalUnit ```  ``` operational_units.ParentOperationalUnit = timesheets.OperationalUnit ``` |
| [training\_modules](#training-modules) | ``` operational_units.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` operational_units.Creator = training_records.Employee ```  ``` operational_units.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` operational_units.Creator = webhooks.Creator ``` |

operational\_units table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **Address**  INTEGER |
| **Company**  INTEGER |
| **Contact**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **DailyRosterBudget**  NUMBER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **OperationalUnitName**  STRING |
| **ParentOperationalUnit**  INTEGER |
| **PayrollExportName**  STRING |
| **RosterActiveHoursSchedule**  INTEGER |
| **RosterSortOrder**  INTEGER |
| **ShowOnRoster**  BOOLEAN |

### pay\_periods

The `pay_periods` table contains info about pay periods.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/PayPeriod) |

pay\_periods table foreign keys

| Join pay\_periods with | on |
| --- | --- |
| [addresses](#addresses) | ``` pay_periods.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` pay_periods.Creator = categories.Creator ``` |
| [comments](#comments) | ``` pay_periods.Creator = comments.Creator ``` |
| [companies](#companies) | ``` pay_periods.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` pay_periods.Creator = company_periods.Creator ```  ``` pay_periods.Id = company_periods.PayPeriod ``` |
| [contacts](#contacts) | ``` pay_periods.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` pay_periods.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` pay_periods.Creator = custom_app_data.Employee ```  ``` pay_periods.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` pay_periods.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` pay_periods.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` pay_periods.Creator = employee_agreement_history.Creator ```  ``` pay_periods.Id = employee_agreement_history.PayPeriod ``` |
| [employee\_agreements](#employee-agreements) | ``` pay_periods.Creator = employee_agreements.EmployeeId ```  ``` pay_periods.Creator = employee_agreements.Creator ```  ``` pay_periods.Id = employee_agreements.PayPeriod ``` |
| [employee\_appraisal](#employee-appraisal) | ``` pay_periods.Creator = employee_appraisal.Creator ```  ``` pay_periods.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` pay_periods.Creator = employee_availability.Employee ```  ``` pay_periods.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` pay_periods.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` pay_periods.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` pay_periods.Creator = employee_history.EmployeeId ```  ``` pay_periods.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` pay_periods.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` pay_periods.Creator = employee_paycycles.EmployeeId ```  ``` pay_periods.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` pay_periods.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` pay_periods.Creator = employee_salary_opunit_costing.Employee ```  ``` pay_periods.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` pay_periods.Creator = employee_workplaces.EmployeeId ```  ``` pay_periods.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` pay_periods.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` pay_periods.Creator = events.Creator ``` |
| [geo](#geo) | ``` pay_periods.Creator = geo.Creator ``` |
| [journal](#journal) | ``` pay_periods.Creator = journal.EmployeeId ```  ``` pay_periods.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` pay_periods.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` pay_periods.Creator = leave_accruals.Employee ```  ``` pay_periods.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` pay_periods.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` pay_periods.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` pay_periods.Creator = leaves.Employee ```  ``` pay_periods.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` pay_periods.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` pay_periods.Creator = operational_units.Creator ``` |
| [pay\_rules](#pay-rules) | ``` pay_periods.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` pay_periods.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` pay_periods.Creator = roster_opens.Employee ```  ``` pay_periods.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` pay_periods.Creator = roster_swaps.Employee ```  ``` pay_periods.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` pay_periods.Creator = rosters.Employee ```  ``` pay_periods.Creator = rosters.ConfirmBy ```  ``` pay_periods.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` pay_periods.Creator = sales_data.Employee ```  ``` pay_periods.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` pay_periods.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` pay_periods.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` pay_periods.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` pay_periods.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` pay_periods.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` pay_periods.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` pay_periods.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` pay_periods.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` pay_periods.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` pay_periods.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` pay_periods.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` pay_periods.Creator = teams.LeaderEmployee ```  ``` pay_periods.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` pay_periods.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` pay_periods.Creator = timesheets.Employee ```  ``` pay_periods.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` pay_periods.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` pay_periods.Creator = training_records.Employee ```  ``` pay_periods.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` pay_periods.Creator = webhooks.Creator ``` |

pay\_periods table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Cycle**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Name**  STRING |
| **StartDate**  DATE |

### pay\_rules

The `pay_rules` table contains info about pay rules.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/PayRules) |

pay\_rules table foreign keys

| Join pay\_rules with | on |
| --- | --- |
| [addresses](#addresses) | ``` pay_rules.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` pay_rules.Creator = categories.Creator ``` |
| [comments](#comments) | ``` pay_rules.Creator = comments.Creator ``` |
| [companies](#companies) | ``` pay_rules.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` pay_rules.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` pay_rules.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` pay_rules.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` pay_rules.Creator = custom_app_data.Employee ```  ``` pay_rules.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` pay_rules.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` pay_rules.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` pay_rules.Creator = employee_agreement_history.Creator ```  ``` pay_rules.Id = employee_agreement_history.SalaryPayRule ``` |
| [employee\_agreements](#employee-agreements) | ``` pay_rules.Creator = employee_agreements.EmployeeId ```  ``` pay_rules.Creator = employee_agreements.Creator ```  ``` pay_rules.Id = employee_agreements.SalaryPayRule ``` |
| [employee\_appraisal](#employee-appraisal) | ``` pay_rules.Creator = employee_appraisal.Creator ```  ``` pay_rules.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` pay_rules.Creator = employee_availability.Employee ```  ``` pay_rules.Creator = employee_availability.Creator ```  ``` pay_rules.Schedule = employee_availability.Schedule ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` pay_rules.Creator = employee_contract_leave_rules.Creator ```  ``` pay_rules.Id = employee_contract_leave_rules.LoadingPayRule1 ```  ``` pay_rules.Id = employee_contract_leave_rules.LoadingPayRule2 ```  ``` pay_rules.Id = employee_contract_leave_rules.LoadingPayRule3 ``` |
| [employee\_contracts](#employee-contracts) | ``` pay_rules.Creator = employee_contracts.Creator ```  ``` pay_rules.Id = employee_contracts.BasePayRule ``` |
| [employee\_history](#employee-history) | ``` pay_rules.Creator = employee_history.EmployeeId ```  ``` pay_rules.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` pay_rules.Creator = employee_paycycle_returns.Creator ```  ``` pay_rules.Id = employee_paycycle_returns.PayRule ``` |
| [employee\_paycycles](#employee-paycycles) | ``` pay_rules.Creator = employee_paycycles.EmployeeId ```  ``` pay_rules.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` pay_rules.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` pay_rules.Creator = employee_salary_opunit_costing.Employee ```  ``` pay_rules.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` pay_rules.Creator = employee_workplaces.EmployeeId ```  ``` pay_rules.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` pay_rules.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` pay_rules.Creator = events.Creator ```  ``` pay_rules.Schedule = events.Schedule ``` |
| [geo](#geo) | ``` pay_rules.Creator = geo.Creator ``` |
| [journal](#journal) | ``` pay_rules.Creator = journal.EmployeeId ```  ``` pay_rules.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` pay_rules.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` pay_rules.Creator = leave_accruals.Employee ```  ``` pay_rules.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` pay_rules.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` pay_rules.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` pay_rules.Creator = leaves.Employee ```  ``` pay_rules.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` pay_rules.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` pay_rules.Creator = operational_units.Creator ```  ``` pay_rules.Schedule = operational_units.RosterActiveHoursSchedule ``` |
| [pay\_periods](#pay-periods) | ``` pay_rules.Creator = pay_periods.Creator ``` |
| [public\_holidays](#public-holidays) | ``` pay_rules.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` pay_rules.Creator = roster_opens.Employee ```  ``` pay_rules.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` pay_rules.Creator = roster_swaps.Employee ```  ``` pay_rules.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` pay_rules.Creator = rosters.Employee ```  ``` pay_rules.Creator = rosters.ConfirmBy ```  ``` pay_rules.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` pay_rules.Creator = sales_data.Employee ```  ``` pay_rules.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` pay_rules.Creator = schedules.Creator ```  ``` pay_rules.Schedule = schedules.Id ``` |
| [sms\_logs](#sms-logs) | ``` pay_rules.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` pay_rules.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` pay_rules.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` pay_rules.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` pay_rules.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` pay_rules.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` pay_rules.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` pay_rules.Creator = task_opunit_configs.Creator ```  ``` pay_rules.Schedule = task_opunit_configs.Schedule ``` |
| [task\_setups](#task-setups) | ``` pay_rules.Creator = task_setups.Creator ```  ``` pay_rules.Schedule = task_setups.Schedule ``` |
| [tasks](#tasks) | ``` pay_rules.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` pay_rules.Creator = teams.LeaderEmployee ```  ``` pay_rules.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` pay_rules.Creator = timesheet_pay_returns.Creator ```  ``` pay_rules.Id = timesheet_pay_returns.PayRule ``` |
| [timesheets](#timesheets) | ``` pay_rules.Creator = timesheets.Employee ```  ``` pay_rules.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` pay_rules.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` pay_rules.Creator = training_records.Employee ```  ``` pay_rules.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` pay_rules.Creator = webhooks.Creator ``` |

pay\_rules table schema

|  |
| --- |
| **AdvancedCalculation**  STRING |
| **AnnualSalary**  NUMBER |
| **Comment**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **DexmlScript**  INTEGER |
| **DexmlScriptParam**  STRING |
| **HourlyRate**  NUMBER |
| **Id**  INTEGER |
| **IsExported**  BOOLEAN |
| **IsMultiplier**  BOOLEAN |
| **MaximumShiftLength**  STRING |
| **MaximumType**  INTEGER |
| **MaximumValue**  INTEGER |
| **MinimumShiftLength**  STRING |
| **MinimumType**  INTEGER |
| **MinimumValue**  INTEGER |
| **Modified**  DATE-TIME |
| **MultiplierBaseRate**  INTEGER |
| **MultiplierValue**  NUMBER |
| **PayPortionRule**  INTEGER |
| **PayTitle**  STRING |
| **PayrollCategory**  STRING |
| **PeriodType**  INTEGER |
| **RecommendWith**  INTEGER |
| **RenumerationBy**  INTEGER |
| **RenumerationType**  INTEGER |
| **Schedule**  INTEGER |
| **UnitValue**  NUMBER |

### public\_holidays

The `public_holidays` table contains info about public holidays.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/PublicHoliday) |

public\_holidays table foreign keys

| Join public\_holidays with | on |
| --- | --- |
| [addresses](#addresses) | ``` public_holidays.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` public_holidays.Creator = categories.Creator ``` |
| [comments](#comments) | ``` public_holidays.Creator = comments.Creator ``` |
| [companies](#companies) | ``` public_holidays.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` public_holidays.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` public_holidays.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` public_holidays.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` public_holidays.Creator = custom_app_data.Employee ```  ``` public_holidays.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` public_holidays.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` public_holidays.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` public_holidays.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` public_holidays.Creator = employee_agreements.EmployeeId ```  ``` public_holidays.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` public_holidays.Creator = employee_appraisal.Creator ```  ``` public_holidays.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` public_holidays.Creator = employee_availability.Employee ```  ``` public_holidays.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` public_holidays.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` public_holidays.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` public_holidays.Creator = employee_history.EmployeeId ```  ``` public_holidays.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` public_holidays.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` public_holidays.Creator = employee_paycycles.EmployeeId ```  ``` public_holidays.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` public_holidays.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` public_holidays.Creator = employee_salary_opunit_costing.Employee ```  ``` public_holidays.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` public_holidays.Creator = employee_workplaces.EmployeeId ```  ``` public_holidays.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` public_holidays.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` public_holidays.Creator = events.Creator ``` |
| [geo](#geo) | ``` public_holidays.Creator = geo.Creator ``` |
| [journal](#journal) | ``` public_holidays.Creator = journal.EmployeeId ```  ``` public_holidays.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` public_holidays.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` public_holidays.Creator = leave_accruals.Employee ```  ``` public_holidays.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` public_holidays.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` public_holidays.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` public_holidays.Creator = leaves.Employee ```  ``` public_holidays.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` public_holidays.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` public_holidays.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` public_holidays.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` public_holidays.Creator = pay_rules.Creator ``` |
| [roster\_opens](#roster-opens) | ``` public_holidays.Creator = roster_opens.Employee ```  ``` public_holidays.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` public_holidays.Creator = roster_swaps.Employee ```  ``` public_holidays.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` public_holidays.Creator = rosters.Employee ```  ``` public_holidays.Creator = rosters.ConfirmBy ```  ``` public_holidays.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` public_holidays.Creator = sales_data.Employee ```  ``` public_holidays.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` public_holidays.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` public_holidays.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` public_holidays.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` public_holidays.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` public_holidays.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` public_holidays.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` public_holidays.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` public_holidays.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` public_holidays.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` public_holidays.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` public_holidays.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` public_holidays.Creator = teams.LeaderEmployee ```  ``` public_holidays.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` public_holidays.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` public_holidays.Creator = timesheets.Employee ```  ``` public_holidays.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` public_holidays.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` public_holidays.Creator = training_records.Employee ```  ``` public_holidays.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` public_holidays.Creator = webhooks.Creator ``` |

public\_holidays table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Schedule**  INTEGER |
| **Title**  STRING |

### roster\_opens

The `roster_opens` table contains info about roster opens.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/RosterOpen) |

roster\_opens table foreign keys

| Join roster\_opens with | on |
| --- | --- |
| [addresses](#addresses) | ``` roster_opens.Employee = addresses.Creator ```  ``` roster_opens.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` roster_opens.Employee = categories.Creator ```  ``` roster_opens.Creator = categories.Creator ``` |
| [comments](#comments) | ``` roster_opens.Employee = comments.Creator ```  ``` roster_opens.Creator = comments.Creator ``` |
| [companies](#companies) | ``` roster_opens.Employee = companies.Creator ```  ``` roster_opens.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` roster_opens.Employee = company_periods.Creator ```  ``` roster_opens.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` roster_opens.Employee = contacts.Creator ```  ``` roster_opens.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` roster_opens.Employee = countries.Creator ```  ``` roster_opens.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` roster_opens.Employee = custom_app_data.Employee ```  ``` roster_opens.Creator = custom_app_data.Employee ```  ``` roster_opens.Employee = custom_app_data.Creator ```  ``` roster_opens.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` roster_opens.Employee = custom_field_data.Creator ```  ``` roster_opens.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` roster_opens.Employee = custom_fields.Creator ```  ``` roster_opens.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` roster_opens.Employee = employee_agreement_history.Creator ```  ``` roster_opens.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` roster_opens.Employee = employee_agreements.EmployeeId ```  ``` roster_opens.Creator = employee_agreements.EmployeeId ```  ``` roster_opens.Employee = employee_agreements.Creator ```  ``` roster_opens.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` roster_opens.Employee = employee_appraisal.Creator ```  ``` roster_opens.Creator = employee_appraisal.Creator ```  ``` roster_opens.Employee = employee_appraisal.Employee ```  ``` roster_opens.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` roster_opens.Employee = employee_availability.Employee ```  ``` roster_opens.Creator = employee_availability.Employee ```  ``` roster_opens.Employee = employee_availability.Creator ```  ``` roster_opens.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` roster_opens.Employee = employee_contract_leave_rules.Creator ```  ``` roster_opens.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` roster_opens.Employee = employee_contracts.Creator ```  ``` roster_opens.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` roster_opens.Employee = employee_history.EmployeeId ```  ``` roster_opens.Creator = employee_history.EmployeeId ```  ``` roster_opens.Employee = employee_history.Creator ```  ``` roster_opens.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` roster_opens.Employee = employee_paycycle_returns.Creator ```  ``` roster_opens.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` roster_opens.Employee = employee_paycycles.EmployeeId ```  ``` roster_opens.Creator = employee_paycycles.EmployeeId ```  ``` roster_opens.Employee = employee_paycycles.Creator ```  ``` roster_opens.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` roster_opens.Employee = employee_roles.Creator ```  ``` roster_opens.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` roster_opens.Employee = employee_salary_opunit_costing.Employee ```  ``` roster_opens.Creator = employee_salary_opunit_costing.Employee ```  ``` roster_opens.Employee = employee_salary_opunit_costing.Creator ```  ``` roster_opens.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` roster_opens.Employee = employee_workplaces.EmployeeId ```  ``` roster_opens.Creator = employee_workplaces.EmployeeId ```  ``` roster_opens.Employee = employee_workplaces.Creator ```  ``` roster_opens.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` roster_opens.Employee = employment_conditions.Creator ```  ``` roster_opens.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` roster_opens.Employee = events.Creator ```  ``` roster_opens.Creator = events.Creator ``` |
| [geo](#geo) | ``` roster_opens.Employee = geo.Creator ```  ``` roster_opens.Creator = geo.Creator ``` |
| [journal](#journal) | ``` roster_opens.Employee = journal.EmployeeId ```  ``` roster_opens.Creator = journal.EmployeeId ```  ``` roster_opens.Employee = journal.Creator ```  ``` roster_opens.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` roster_opens.Employee = kiosks.Creator ```  ``` roster_opens.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` roster_opens.Employee = leave_accruals.Employee ```  ``` roster_opens.Creator = leave_accruals.Employee ```  ``` roster_opens.Employee = leave_accruals.Creator ```  ``` roster_opens.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` roster_opens.Employee = leave_pay_lines.Creator ```  ``` roster_opens.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` roster_opens.Employee = leave_rules.Creator ```  ``` roster_opens.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` roster_opens.Employee = leaves.Employee ```  ``` roster_opens.Creator = leaves.Employee ```  ``` roster_opens.Employee = leaves.Creator ```  ``` roster_opens.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` roster_opens.Employee = memos.Creator ```  ``` roster_opens.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` roster_opens.Employee = operational_units.Creator ```  ``` roster_opens.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` roster_opens.Employee = pay_periods.Creator ```  ``` roster_opens.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` roster_opens.Employee = pay_rules.Creator ```  ``` roster_opens.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` roster_opens.Employee = public_holidays.Creator ```  ``` roster_opens.Creator = public_holidays.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` roster_opens.Employee = roster_swaps.Employee ```  ``` roster_opens.Creator = roster_swaps.Employee ```  ``` roster_opens.Employee = roster_swaps.Creator ```  ``` roster_opens.Creator = roster_swaps.Creator ```  ``` roster_opens.Roster = roster_swaps.SourceRoster ```  ``` roster_opens.Roster = roster_swaps.TargetRoster ``` |
| [rosters](#rosters) | ``` roster_opens.Employee = rosters.Employee ```  ``` roster_opens.Creator = rosters.Employee ```  ``` roster_opens.Employee = rosters.ConfirmBy ```  ``` roster_opens.Creator = rosters.ConfirmBy ```  ``` roster_opens.Employee = rosters.Creator ```  ``` roster_opens.Creator = rosters.Creator ```  ``` roster_opens.Roster = rosters.Id ``` |
| [sales\_data](#sales-data) | ``` roster_opens.Employee = sales_data.Employee ```  ``` roster_opens.Creator = sales_data.Employee ```  ``` roster_opens.Employee = sales_data.Creator ```  ``` roster_opens.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` roster_opens.Employee = schedules.Creator ```  ``` roster_opens.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` roster_opens.Employee = sms_logs.Creator ```  ``` roster_opens.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` roster_opens.Employee = states.Creator ```  ``` roster_opens.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` roster_opens.Employee = stress_profiles.Creator ```  ``` roster_opens.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` roster_opens.Employee = system_usage_balances.Creator ```  ``` roster_opens.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` roster_opens.Employee = system_usage_tracking.Creator ```  ``` roster_opens.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` roster_opens.Employee = task_group_setups.Creator ```  ``` roster_opens.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` roster_opens.Employee = task_groups.Creator ```  ``` roster_opens.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` roster_opens.Employee = task_opunit_configs.Creator ```  ``` roster_opens.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` roster_opens.Employee = task_setups.Creator ```  ``` roster_opens.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` roster_opens.Employee = tasks.Creator ```  ``` roster_opens.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` roster_opens.Employee = teams.LeaderEmployee ```  ``` roster_opens.Creator = teams.LeaderEmployee ```  ``` roster_opens.Employee = teams.Creator ```  ``` roster_opens.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` roster_opens.Employee = timesheet_pay_returns.Creator ```  ``` roster_opens.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` roster_opens.Employee = timesheets.Employee ```  ``` roster_opens.Creator = timesheets.Employee ```  ``` roster_opens.Employee = timesheets.Creator ```  ``` roster_opens.Creator = timesheets.Creator ```  ``` roster_opens.Roster = timesheets.Roster ``` |
| [training\_modules](#training-modules) | ``` roster_opens.Employee = training_modules.Creator ```  ``` roster_opens.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` roster_opens.Employee = training_records.Employee ```  ``` roster_opens.Creator = training_records.Employee ```  ``` roster_opens.Employee = training_records.Creator ```  ``` roster_opens.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` roster_opens.Employee = webhooks.Creator ```  ``` roster_opens.Creator = webhooks.Creator ``` |

roster\_opens table schema

|  |
| --- |
| **Accepted**  BOOLEAN |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Declined**  BOOLEAN |
| **Employee**  INTEGER |
| **Id**  INTEGER |
| **Link**  STRING |
| **Message**  STRING |
| **Modified**  DATE-TIME |
| **Roster**  INTEGER |
| **Seen**  BOOLEAN |

### roster\_swaps

The `roster_swaps` table contains info about roster swaps.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/RosterSwap) |

roster\_swaps table foreign keys

| Join roster\_swaps with | on |
| --- | --- |
| [addresses](#addresses) | ``` roster_swaps.Employee = addresses.Creator ```  ``` roster_swaps.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` roster_swaps.Employee = categories.Creator ```  ``` roster_swaps.Creator = categories.Creator ``` |
| [comments](#comments) | ``` roster_swaps.Employee = comments.Creator ```  ``` roster_swaps.Creator = comments.Creator ``` |
| [companies](#companies) | ``` roster_swaps.Employee = companies.Creator ```  ``` roster_swaps.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` roster_swaps.Employee = company_periods.Creator ```  ``` roster_swaps.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` roster_swaps.Employee = contacts.Creator ```  ``` roster_swaps.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` roster_swaps.Employee = countries.Creator ```  ``` roster_swaps.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` roster_swaps.Employee = custom_app_data.Employee ```  ``` roster_swaps.Creator = custom_app_data.Employee ```  ``` roster_swaps.Employee = custom_app_data.Creator ```  ``` roster_swaps.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` roster_swaps.Employee = custom_field_data.Creator ```  ``` roster_swaps.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` roster_swaps.Employee = custom_fields.Creator ```  ``` roster_swaps.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` roster_swaps.Employee = employee_agreement_history.Creator ```  ``` roster_swaps.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` roster_swaps.Employee = employee_agreements.EmployeeId ```  ``` roster_swaps.Creator = employee_agreements.EmployeeId ```  ``` roster_swaps.Employee = employee_agreements.Creator ```  ``` roster_swaps.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` roster_swaps.Employee = employee_appraisal.Creator ```  ``` roster_swaps.Creator = employee_appraisal.Creator ```  ``` roster_swaps.Employee = employee_appraisal.Employee ```  ``` roster_swaps.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` roster_swaps.Employee = employee_availability.Employee ```  ``` roster_swaps.Creator = employee_availability.Employee ```  ``` roster_swaps.Employee = employee_availability.Creator ```  ``` roster_swaps.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` roster_swaps.Employee = employee_contract_leave_rules.Creator ```  ``` roster_swaps.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` roster_swaps.Employee = employee_contracts.Creator ```  ``` roster_swaps.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` roster_swaps.Employee = employee_history.EmployeeId ```  ``` roster_swaps.Creator = employee_history.EmployeeId ```  ``` roster_swaps.Employee = employee_history.Creator ```  ``` roster_swaps.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` roster_swaps.Employee = employee_paycycle_returns.Creator ```  ``` roster_swaps.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` roster_swaps.Employee = employee_paycycles.EmployeeId ```  ``` roster_swaps.Creator = employee_paycycles.EmployeeId ```  ``` roster_swaps.Employee = employee_paycycles.Creator ```  ``` roster_swaps.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` roster_swaps.Employee = employee_roles.Creator ```  ``` roster_swaps.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` roster_swaps.Employee = employee_salary_opunit_costing.Employee ```  ``` roster_swaps.Creator = employee_salary_opunit_costing.Employee ```  ``` roster_swaps.Employee = employee_salary_opunit_costing.Creator ```  ``` roster_swaps.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` roster_swaps.Employee = employee_workplaces.EmployeeId ```  ``` roster_swaps.Creator = employee_workplaces.EmployeeId ```  ``` roster_swaps.Employee = employee_workplaces.Creator ```  ``` roster_swaps.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` roster_swaps.Employee = employment_conditions.Creator ```  ``` roster_swaps.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` roster_swaps.Employee = events.Creator ```  ``` roster_swaps.Creator = events.Creator ``` |
| [geo](#geo) | ``` roster_swaps.Employee = geo.Creator ```  ``` roster_swaps.Creator = geo.Creator ``` |
| [journal](#journal) | ``` roster_swaps.Employee = journal.EmployeeId ```  ``` roster_swaps.Creator = journal.EmployeeId ```  ``` roster_swaps.Employee = journal.Creator ```  ``` roster_swaps.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` roster_swaps.Employee = kiosks.Creator ```  ``` roster_swaps.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` roster_swaps.Employee = leave_accruals.Employee ```  ``` roster_swaps.Creator = leave_accruals.Employee ```  ``` roster_swaps.Employee = leave_accruals.Creator ```  ``` roster_swaps.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` roster_swaps.Employee = leave_pay_lines.Creator ```  ``` roster_swaps.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` roster_swaps.Employee = leave_rules.Creator ```  ``` roster_swaps.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` roster_swaps.Employee = leaves.Employee ```  ``` roster_swaps.Creator = leaves.Employee ```  ``` roster_swaps.Employee = leaves.Creator ```  ``` roster_swaps.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` roster_swaps.Employee = memos.Creator ```  ``` roster_swaps.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` roster_swaps.Employee = operational_units.Creator ```  ``` roster_swaps.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` roster_swaps.Employee = pay_periods.Creator ```  ``` roster_swaps.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` roster_swaps.Employee = pay_rules.Creator ```  ``` roster_swaps.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` roster_swaps.Employee = public_holidays.Creator ```  ``` roster_swaps.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` roster_swaps.Employee = roster_opens.Employee ```  ``` roster_swaps.Creator = roster_opens.Employee ```  ``` roster_swaps.Employee = roster_opens.Creator ```  ``` roster_swaps.Creator = roster_opens.Creator ```  ``` roster_swaps.SourceRoster = roster_opens.Roster ```  ``` roster_swaps.TargetRoster = roster_opens.Roster ``` |
| [rosters](#rosters) | ``` roster_swaps.Employee = rosters.Employee ```  ``` roster_swaps.Creator = rosters.Employee ```  ``` roster_swaps.Employee = rosters.ConfirmBy ```  ``` roster_swaps.Creator = rosters.ConfirmBy ```  ``` roster_swaps.Employee = rosters.Creator ```  ``` roster_swaps.Creator = rosters.Creator ```  ``` roster_swaps.SourceRoster = rosters.Id ```  ``` roster_swaps.TargetRoster = rosters.Id ``` |
| [sales\_data](#sales-data) | ``` roster_swaps.Employee = sales_data.Employee ```  ``` roster_swaps.Creator = sales_data.Employee ```  ``` roster_swaps.Employee = sales_data.Creator ```  ``` roster_swaps.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` roster_swaps.Employee = schedules.Creator ```  ``` roster_swaps.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` roster_swaps.Employee = sms_logs.Creator ```  ``` roster_swaps.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` roster_swaps.Employee = states.Creator ```  ``` roster_swaps.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` roster_swaps.Employee = stress_profiles.Creator ```  ``` roster_swaps.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` roster_swaps.Employee = system_usage_balances.Creator ```  ``` roster_swaps.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` roster_swaps.Employee = system_usage_tracking.Creator ```  ``` roster_swaps.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` roster_swaps.Employee = task_group_setups.Creator ```  ``` roster_swaps.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` roster_swaps.Employee = task_groups.Creator ```  ``` roster_swaps.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` roster_swaps.Employee = task_opunit_configs.Creator ```  ``` roster_swaps.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` roster_swaps.Employee = task_setups.Creator ```  ``` roster_swaps.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` roster_swaps.Employee = tasks.Creator ```  ``` roster_swaps.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` roster_swaps.Employee = teams.LeaderEmployee ```  ``` roster_swaps.Creator = teams.LeaderEmployee ```  ``` roster_swaps.Employee = teams.Creator ```  ``` roster_swaps.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` roster_swaps.Employee = timesheet_pay_returns.Creator ```  ``` roster_swaps.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` roster_swaps.Employee = timesheets.Employee ```  ``` roster_swaps.Creator = timesheets.Employee ```  ``` roster_swaps.Employee = timesheets.Creator ```  ``` roster_swaps.Creator = timesheets.Creator ```  ``` roster_swaps.SourceRoster = timesheets.Roster ```  ``` roster_swaps.TargetRoster = timesheets.Roster ``` |
| [training\_modules](#training-modules) | ``` roster_swaps.Employee = training_modules.Creator ```  ``` roster_swaps.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` roster_swaps.Employee = training_records.Employee ```  ``` roster_swaps.Creator = training_records.Employee ```  ``` roster_swaps.Employee = training_records.Creator ```  ``` roster_swaps.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` roster_swaps.Employee = webhooks.Creator ```  ``` roster_swaps.Creator = webhooks.Creator ``` |

roster\_swaps table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Employee**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **RequestMessage**  STRING |
| **ResponseMessage**  STRING |
| **SourceRoster**  INTEGER |
| **Status**  INTEGER |
| **TargetRoster**  INTEGER |

### rosters

The `rosters` table contains info about rosters.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Roster) |

rosters table foreign keys

| Join rosters with | on |
| --- | --- |
| [addresses](#addresses) | ``` rosters.Employee = addresses.Creator ```  ``` rosters.ConfirmBy = addresses.Creator ```  ``` rosters.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` rosters.Employee = categories.Creator ```  ``` rosters.ConfirmBy = categories.Creator ```  ``` rosters.Creator = categories.Creator ``` |
| [comments](#comments) | ``` rosters.Employee = comments.Creator ```  ``` rosters.ConfirmBy = comments.Creator ```  ``` rosters.Creator = comments.Creator ``` |
| [companies](#companies) | ``` rosters.Employee = companies.Creator ```  ``` rosters.ConfirmBy = companies.Creator ```  ``` rosters.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` rosters.Employee = company_periods.Creator ```  ``` rosters.ConfirmBy = company_periods.Creator ```  ``` rosters.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` rosters.Employee = contacts.Creator ```  ``` rosters.ConfirmBy = contacts.Creator ```  ``` rosters.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` rosters.Employee = countries.Creator ```  ``` rosters.ConfirmBy = countries.Creator ```  ``` rosters.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` rosters.Employee = custom_app_data.Employee ```  ``` rosters.ConfirmBy = custom_app_data.Employee ```  ``` rosters.Creator = custom_app_data.Employee ```  ``` rosters.Employee = custom_app_data.Creator ```  ``` rosters.ConfirmBy = custom_app_data.Creator ```  ``` rosters.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` rosters.Employee = custom_field_data.Creator ```  ``` rosters.ConfirmBy = custom_field_data.Creator ```  ``` rosters.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` rosters.Employee = custom_fields.Creator ```  ``` rosters.ConfirmBy = custom_fields.Creator ```  ``` rosters.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` rosters.Employee = employee_agreement_history.Creator ```  ``` rosters.ConfirmBy = employee_agreement_history.Creator ```  ``` rosters.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` rosters.Employee = employee_agreements.EmployeeId ```  ``` rosters.ConfirmBy = employee_agreements.EmployeeId ```  ``` rosters.Creator = employee_agreements.EmployeeId ```  ``` rosters.Employee = employee_agreements.Creator ```  ``` rosters.ConfirmBy = employee_agreements.Creator ```  ``` rosters.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` rosters.Employee = employee_appraisal.Creator ```  ``` rosters.ConfirmBy = employee_appraisal.Creator ```  ``` rosters.Creator = employee_appraisal.Creator ```  ``` rosters.Employee = employee_appraisal.Employee ```  ``` rosters.ConfirmBy = employee_appraisal.Employee ```  ``` rosters.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` rosters.Employee = employee_availability.Employee ```  ``` rosters.ConfirmBy = employee_availability.Employee ```  ``` rosters.Creator = employee_availability.Employee ```  ``` rosters.Employee = employee_availability.Creator ```  ``` rosters.ConfirmBy = employee_availability.Creator ```  ``` rosters.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` rosters.Employee = employee_contract_leave_rules.Creator ```  ``` rosters.ConfirmBy = employee_contract_leave_rules.Creator ```  ``` rosters.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` rosters.Employee = employee_contracts.Creator ```  ``` rosters.ConfirmBy = employee_contracts.Creator ```  ``` rosters.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` rosters.Employee = employee_history.EmployeeId ```  ``` rosters.ConfirmBy = employee_history.EmployeeId ```  ``` rosters.Creator = employee_history.EmployeeId ```  ``` rosters.Employee = employee_history.Creator ```  ``` rosters.ConfirmBy = employee_history.Creator ```  ``` rosters.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` rosters.Employee = employee_paycycle_returns.Creator ```  ``` rosters.ConfirmBy = employee_paycycle_returns.Creator ```  ``` rosters.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` rosters.Employee = employee_paycycles.EmployeeId ```  ``` rosters.ConfirmBy = employee_paycycles.EmployeeId ```  ``` rosters.Creator = employee_paycycles.EmployeeId ```  ``` rosters.Employee = employee_paycycles.Creator ```  ``` rosters.ConfirmBy = employee_paycycles.Creator ```  ``` rosters.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` rosters.Employee = employee_roles.Creator ```  ``` rosters.ConfirmBy = employee_roles.Creator ```  ``` rosters.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` rosters.Employee = employee_salary_opunit_costing.Employee ```  ``` rosters.ConfirmBy = employee_salary_opunit_costing.Employee ```  ``` rosters.Creator = employee_salary_opunit_costing.Employee ```  ``` rosters.Employee = employee_salary_opunit_costing.Creator ```  ``` rosters.ConfirmBy = employee_salary_opunit_costing.Creator ```  ``` rosters.Creator = employee_salary_opunit_costing.Creator ```  ``` rosters.OperationalUnit = employee_salary_opunit_costing.OpUnit ``` |
| [employee\_workplaces](#employee-workplaces) | ``` rosters.Employee = employee_workplaces.EmployeeId ```  ``` rosters.ConfirmBy = employee_workplaces.EmployeeId ```  ``` rosters.Creator = employee_workplaces.EmployeeId ```  ``` rosters.Employee = employee_workplaces.Creator ```  ``` rosters.ConfirmBy = employee_workplaces.Creator ```  ``` rosters.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` rosters.Employee = employment_conditions.Creator ```  ``` rosters.ConfirmBy = employment_conditions.Creator ```  ``` rosters.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` rosters.Employee = events.Creator ```  ``` rosters.ConfirmBy = events.Creator ```  ``` rosters.Creator = events.Creator ``` |
| [geo](#geo) | ``` rosters.Employee = geo.Creator ```  ``` rosters.ConfirmBy = geo.Creator ```  ``` rosters.Creator = geo.Creator ``` |
| [journal](#journal) | ``` rosters.Employee = journal.EmployeeId ```  ``` rosters.ConfirmBy = journal.EmployeeId ```  ``` rosters.Creator = journal.EmployeeId ```  ``` rosters.Employee = journal.Creator ```  ``` rosters.ConfirmBy = journal.Creator ```  ``` rosters.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` rosters.Employee = kiosks.Creator ```  ``` rosters.ConfirmBy = kiosks.Creator ```  ``` rosters.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` rosters.Employee = leave_accruals.Employee ```  ``` rosters.ConfirmBy = leave_accruals.Employee ```  ``` rosters.Creator = leave_accruals.Employee ```  ``` rosters.Employee = leave_accruals.Creator ```  ``` rosters.ConfirmBy = leave_accruals.Creator ```  ``` rosters.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` rosters.Employee = leave_pay_lines.Creator ```  ``` rosters.ConfirmBy = leave_pay_lines.Creator ```  ``` rosters.Creator = leave_pay_lines.Creator ```  ``` rosters.MatchedByTimesheet = leave_pay_lines.TimesheetId ``` |
| [leave\_rules](#leave-rules) | ``` rosters.Employee = leave_rules.Creator ```  ``` rosters.ConfirmBy = leave_rules.Creator ```  ``` rosters.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` rosters.Employee = leaves.Employee ```  ``` rosters.ConfirmBy = leaves.Employee ```  ``` rosters.Creator = leaves.Employee ```  ``` rosters.Employee = leaves.Creator ```  ``` rosters.ConfirmBy = leaves.Creator ```  ``` rosters.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` rosters.Employee = memos.Creator ```  ``` rosters.ConfirmBy = memos.Creator ```  ``` rosters.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` rosters.Employee = operational_units.Creator ```  ``` rosters.ConfirmBy = operational_units.Creator ```  ``` rosters.Creator = operational_units.Creator ```  ``` rosters.OperationalUnit = operational_units.Id ```  ``` rosters.OperationalUnit = operational_units.ParentOperationalUnit ``` |
| [pay\_periods](#pay-periods) | ``` rosters.Employee = pay_periods.Creator ```  ``` rosters.ConfirmBy = pay_periods.Creator ```  ``` rosters.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` rosters.Employee = pay_rules.Creator ```  ``` rosters.ConfirmBy = pay_rules.Creator ```  ``` rosters.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` rosters.Employee = public_holidays.Creator ```  ``` rosters.ConfirmBy = public_holidays.Creator ```  ``` rosters.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` rosters.Employee = roster_opens.Employee ```  ``` rosters.ConfirmBy = roster_opens.Employee ```  ``` rosters.Creator = roster_opens.Employee ```  ``` rosters.Employee = roster_opens.Creator ```  ``` rosters.ConfirmBy = roster_opens.Creator ```  ``` rosters.Creator = roster_opens.Creator ```  ``` rosters.Id = roster_opens.Roster ``` |
| [roster\_swaps](#roster-swaps) | ``` rosters.Employee = roster_swaps.Employee ```  ``` rosters.ConfirmBy = roster_swaps.Employee ```  ``` rosters.Creator = roster_swaps.Employee ```  ``` rosters.Employee = roster_swaps.Creator ```  ``` rosters.ConfirmBy = roster_swaps.Creator ```  ``` rosters.Creator = roster_swaps.Creator ```  ``` rosters.Id = roster_swaps.SourceRoster ```  ``` rosters.Id = roster_swaps.TargetRoster ``` |
| [sales\_data](#sales-data) | ``` rosters.Employee = sales_data.Employee ```  ``` rosters.ConfirmBy = sales_data.Employee ```  ``` rosters.Creator = sales_data.Employee ```  ``` rosters.Employee = sales_data.Creator ```  ``` rosters.ConfirmBy = sales_data.Creator ```  ``` rosters.Creator = sales_data.Creator ```  ``` rosters.OperationalUnit = sales_data.OperationalUnit ``` |
| [schedules](#schedules) | ``` rosters.Employee = schedules.Creator ```  ``` rosters.ConfirmBy = schedules.Creator ```  ``` rosters.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` rosters.Employee = sms_logs.Creator ```  ``` rosters.ConfirmBy = sms_logs.Creator ```  ``` rosters.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` rosters.Employee = states.Creator ```  ``` rosters.ConfirmBy = states.Creator ```  ``` rosters.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` rosters.Employee = stress_profiles.Creator ```  ``` rosters.ConfirmBy = stress_profiles.Creator ```  ``` rosters.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` rosters.Employee = system_usage_balances.Creator ```  ``` rosters.ConfirmBy = system_usage_balances.Creator ```  ``` rosters.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` rosters.Employee = system_usage_tracking.Creator ```  ``` rosters.ConfirmBy = system_usage_tracking.Creator ```  ``` rosters.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` rosters.Employee = task_group_setups.Creator ```  ``` rosters.ConfirmBy = task_group_setups.Creator ```  ``` rosters.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` rosters.Employee = task_groups.Creator ```  ``` rosters.ConfirmBy = task_groups.Creator ```  ``` rosters.Creator = task_groups.Creator ```  ``` rosters.OperationalUnit = task_groups.OpUnitId ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` rosters.Employee = task_opunit_configs.Creator ```  ``` rosters.ConfirmBy = task_opunit_configs.Creator ```  ``` rosters.Creator = task_opunit_configs.Creator ```  ``` rosters.OperationalUnit = task_opunit_configs.OpUnitId ``` |
| [task\_setups](#task-setups) | ``` rosters.Employee = task_setups.Creator ```  ``` rosters.ConfirmBy = task_setups.Creator ```  ``` rosters.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` rosters.Employee = tasks.Creator ```  ``` rosters.ConfirmBy = tasks.Creator ```  ``` rosters.Creator = tasks.Creator ```  ``` rosters.OperationalUnit = tasks.OpUnitId ``` |
| [teams](#teams) | ``` rosters.Employee = teams.LeaderEmployee ```  ``` rosters.ConfirmBy = teams.LeaderEmployee ```  ``` rosters.Creator = teams.LeaderEmployee ```  ``` rosters.Employee = teams.Creator ```  ``` rosters.ConfirmBy = teams.Creator ```  ``` rosters.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` rosters.Employee = timesheet_pay_returns.Creator ```  ``` rosters.ConfirmBy = timesheet_pay_returns.Creator ```  ``` rosters.Creator = timesheet_pay_returns.Creator ```  ``` rosters.MatchedByTimesheet = timesheet_pay_returns.Timesheet ``` |
| [timesheets](#timesheets) | ``` rosters.Employee = timesheets.Employee ```  ``` rosters.ConfirmBy = timesheets.Employee ```  ``` rosters.Creator = timesheets.Employee ```  ``` rosters.Employee = timesheets.Creator ```  ``` rosters.ConfirmBy = timesheets.Creator ```  ``` rosters.Creator = timesheets.Creator ```  ``` rosters.OperationalUnit = timesheets.OperationalUnit ```  ``` rosters.Id = timesheets.Roster ```  ``` rosters.MatchedByTimesheet = timesheets.Id ``` |
| [training\_modules](#training-modules) | ``` rosters.Employee = training_modules.Creator ```  ``` rosters.ConfirmBy = training_modules.Creator ```  ``` rosters.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` rosters.Employee = training_records.Employee ```  ``` rosters.ConfirmBy = training_records.Employee ```  ``` rosters.Creator = training_records.Employee ```  ``` rosters.Employee = training_records.Creator ```  ``` rosters.ConfirmBy = training_records.Creator ```  ``` rosters.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` rosters.Employee = webhooks.Creator ```  ``` rosters.ConfirmBy = webhooks.Creator ```  ``` rosters.Creator = webhooks.Creator ``` |

rosters table schema

|  |
| --- |
| **Comment**  STRING |
| **ConfirmBy**  INTEGER |
| **ConfirmComment**  STRING |
| **ConfirmStatus**  INTEGER |
| **ConfirmTime**  INTEGER |
| **Cost**  NUMBER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Date**  DATE |
| **Employee**  INTEGER |
| **EndTime**  INTEGER |
| **Id**  INTEGER |
| **MatchedByTimesheet**  INTEGER |
| **Mealbreak**  STRING |
| **Modified**  DATE-TIME |
| **Open**  BOOLEAN |
| **OperationalUnit**  INTEGER |
| **Published**  BOOLEAN |
| **StartTime**  INTEGER |
| **SwapManageBy**  INTEGER |
| **SwapStatus**  INTEGER |
| **TotalTime**  NUMBER |
| **Warning**  STRING |
| **WarningOverrideComment**  STRING |

### sales\_data

The `sales_data` table contains info about sales data.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/SalesData) |

sales\_data table foreign keys

| Join sales\_data with | on |
| --- | --- |
| [addresses](#addresses) | ``` sales_data.Employee = addresses.Creator ```  ``` sales_data.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` sales_data.Employee = categories.Creator ```  ``` sales_data.Creator = categories.Creator ``` |
| [comments](#comments) | ``` sales_data.Employee = comments.Creator ```  ``` sales_data.Creator = comments.Creator ``` |
| [companies](#companies) | ``` sales_data.Employee = companies.Creator ```  ``` sales_data.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` sales_data.Employee = company_periods.Creator ```  ``` sales_data.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` sales_data.Employee = contacts.Creator ```  ``` sales_data.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` sales_data.Employee = countries.Creator ```  ``` sales_data.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` sales_data.Employee = custom_app_data.Employee ```  ``` sales_data.Creator = custom_app_data.Employee ```  ``` sales_data.Employee = custom_app_data.Creator ```  ``` sales_data.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` sales_data.Employee = custom_field_data.Creator ```  ``` sales_data.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` sales_data.Employee = custom_fields.Creator ```  ``` sales_data.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` sales_data.Employee = employee_agreement_history.Creator ```  ``` sales_data.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` sales_data.Employee = employee_agreements.EmployeeId ```  ``` sales_data.Creator = employee_agreements.EmployeeId ```  ``` sales_data.Employee = employee_agreements.Creator ```  ``` sales_data.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` sales_data.Employee = employee_appraisal.Creator ```  ``` sales_data.Creator = employee_appraisal.Creator ```  ``` sales_data.Employee = employee_appraisal.Employee ```  ``` sales_data.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` sales_data.Employee = employee_availability.Employee ```  ``` sales_data.Creator = employee_availability.Employee ```  ``` sales_data.Employee = employee_availability.Creator ```  ``` sales_data.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` sales_data.Employee = employee_contract_leave_rules.Creator ```  ``` sales_data.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` sales_data.Employee = employee_contracts.Creator ```  ``` sales_data.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` sales_data.Employee = employee_history.EmployeeId ```  ``` sales_data.Creator = employee_history.EmployeeId ```  ``` sales_data.Employee = employee_history.Creator ```  ``` sales_data.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` sales_data.Employee = employee_paycycle_returns.Creator ```  ``` sales_data.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` sales_data.Employee = employee_paycycles.EmployeeId ```  ``` sales_data.Creator = employee_paycycles.EmployeeId ```  ``` sales_data.Employee = employee_paycycles.Creator ```  ``` sales_data.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` sales_data.Employee = employee_roles.Creator ```  ``` sales_data.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` sales_data.Employee = employee_salary_opunit_costing.Employee ```  ``` sales_data.Creator = employee_salary_opunit_costing.Employee ```  ``` sales_data.Employee = employee_salary_opunit_costing.Creator ```  ``` sales_data.Creator = employee_salary_opunit_costing.Creator ```  ``` sales_data.OperationalUnit = employee_salary_opunit_costing.OpUnit ``` |
| [employee\_workplaces](#employee-workplaces) | ``` sales_data.Employee = employee_workplaces.EmployeeId ```  ``` sales_data.Creator = employee_workplaces.EmployeeId ```  ``` sales_data.Employee = employee_workplaces.Creator ```  ``` sales_data.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` sales_data.Employee = employment_conditions.Creator ```  ``` sales_data.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` sales_data.Employee = events.Creator ```  ``` sales_data.Creator = events.Creator ``` |
| [geo](#geo) | ``` sales_data.Employee = geo.Creator ```  ``` sales_data.Creator = geo.Creator ``` |
| [journal](#journal) | ``` sales_data.Employee = journal.EmployeeId ```  ``` sales_data.Creator = journal.EmployeeId ```  ``` sales_data.Employee = journal.Creator ```  ``` sales_data.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` sales_data.Employee = kiosks.Creator ```  ``` sales_data.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` sales_data.Employee = leave_accruals.Employee ```  ``` sales_data.Creator = leave_accruals.Employee ```  ``` sales_data.Employee = leave_accruals.Creator ```  ``` sales_data.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` sales_data.Employee = leave_pay_lines.Creator ```  ``` sales_data.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` sales_data.Employee = leave_rules.Creator ```  ``` sales_data.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` sales_data.Employee = leaves.Employee ```  ``` sales_data.Creator = leaves.Employee ```  ``` sales_data.Employee = leaves.Creator ```  ``` sales_data.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` sales_data.Employee = memos.Creator ```  ``` sales_data.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` sales_data.Employee = operational_units.Creator ```  ``` sales_data.Creator = operational_units.Creator ```  ``` sales_data.OperationalUnit = operational_units.Id ```  ``` sales_data.OperationalUnit = operational_units.ParentOperationalUnit ``` |
| [pay\_periods](#pay-periods) | ``` sales_data.Employee = pay_periods.Creator ```  ``` sales_data.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` sales_data.Employee = pay_rules.Creator ```  ``` sales_data.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` sales_data.Employee = public_holidays.Creator ```  ``` sales_data.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` sales_data.Employee = roster_opens.Employee ```  ``` sales_data.Creator = roster_opens.Employee ```  ``` sales_data.Employee = roster_opens.Creator ```  ``` sales_data.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` sales_data.Employee = roster_swaps.Employee ```  ``` sales_data.Creator = roster_swaps.Employee ```  ``` sales_data.Employee = roster_swaps.Creator ```  ``` sales_data.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` sales_data.Employee = rosters.Employee ```  ``` sales_data.Creator = rosters.Employee ```  ``` sales_data.Employee = rosters.ConfirmBy ```  ``` sales_data.Creator = rosters.ConfirmBy ```  ``` sales_data.Employee = rosters.Creator ```  ``` sales_data.Creator = rosters.Creator ```  ``` sales_data.OperationalUnit = rosters.OperationalUnit ``` |
| [schedules](#schedules) | ``` sales_data.Employee = schedules.Creator ```  ``` sales_data.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` sales_data.Employee = sms_logs.Creator ```  ``` sales_data.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` sales_data.Employee = states.Creator ```  ``` sales_data.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` sales_data.Employee = stress_profiles.Creator ```  ``` sales_data.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` sales_data.Employee = system_usage_balances.Creator ```  ``` sales_data.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` sales_data.Employee = system_usage_tracking.Creator ```  ``` sales_data.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` sales_data.Employee = task_group_setups.Creator ```  ``` sales_data.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` sales_data.Employee = task_groups.Creator ```  ``` sales_data.Creator = task_groups.Creator ```  ``` sales_data.OperationalUnit = task_groups.OpUnitId ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` sales_data.Employee = task_opunit_configs.Creator ```  ``` sales_data.Creator = task_opunit_configs.Creator ```  ``` sales_data.OperationalUnit = task_opunit_configs.OpUnitId ``` |
| [task\_setups](#task-setups) | ``` sales_data.Employee = task_setups.Creator ```  ``` sales_data.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` sales_data.Employee = tasks.Creator ```  ``` sales_data.Creator = tasks.Creator ```  ``` sales_data.OperationalUnit = tasks.OpUnitId ``` |
| [teams](#teams) | ``` sales_data.Employee = teams.LeaderEmployee ```  ``` sales_data.Creator = teams.LeaderEmployee ```  ``` sales_data.Employee = teams.Creator ```  ``` sales_data.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` sales_data.Employee = timesheet_pay_returns.Creator ```  ``` sales_data.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` sales_data.Employee = timesheets.Employee ```  ``` sales_data.Creator = timesheets.Employee ```  ``` sales_data.Employee = timesheets.Creator ```  ``` sales_data.Creator = timesheets.Creator ```  ``` sales_data.OperationalUnit = timesheets.OperationalUnit ``` |
| [training\_modules](#training-modules) | ``` sales_data.Employee = training_modules.Creator ```  ``` sales_data.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` sales_data.Employee = training_records.Employee ```  ``` sales_data.Creator = training_records.Employee ```  ``` sales_data.Employee = training_records.Creator ```  ``` sales_data.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` sales_data.Employee = webhooks.Creator ```  ``` sales_data.Creator = webhooks.Creator ``` |

sales\_data table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Date**  DATE |
| **Employee**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **OperationalUnit**  INTEGER |
| **SalesAmount**  NUMBER |
| **SalesPayload**  STRING |
| **SalesQty**  NUMBER |
| **SalesRef**  STRING |
| **Timestamp**  INTEGER |

### schedules

The `schedules` table contains info about schedules.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Schedule) |

schedules table foreign keys

| Join schedules with | on |
| --- | --- |
| [addresses](#addresses) | ``` schedules.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` schedules.Creator = categories.Creator ``` |
| [comments](#comments) | ``` schedules.Creator = comments.Creator ``` |
| [companies](#companies) | ``` schedules.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` schedules.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` schedules.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` schedules.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` schedules.Creator = custom_app_data.Employee ```  ``` schedules.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` schedules.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` schedules.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` schedules.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` schedules.Creator = employee_agreements.EmployeeId ```  ``` schedules.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` schedules.Creator = employee_appraisal.Creator ```  ``` schedules.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` schedules.Creator = employee_availability.Employee ```  ``` schedules.Creator = employee_availability.Creator ```  ``` schedules.Id = employee_availability.Schedule ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` schedules.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` schedules.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` schedules.Creator = employee_history.EmployeeId ```  ``` schedules.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` schedules.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` schedules.Creator = employee_paycycles.EmployeeId ```  ``` schedules.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` schedules.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` schedules.Creator = employee_salary_opunit_costing.Employee ```  ``` schedules.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` schedules.Creator = employee_workplaces.EmployeeId ```  ``` schedules.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` schedules.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` schedules.Creator = events.Creator ```  ``` schedules.Id = events.Schedule ``` |
| [geo](#geo) | ``` schedules.Creator = geo.Creator ``` |
| [journal](#journal) | ``` schedules.Creator = journal.EmployeeId ```  ``` schedules.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` schedules.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` schedules.Creator = leave_accruals.Employee ```  ``` schedules.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` schedules.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` schedules.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` schedules.Creator = leaves.Employee ```  ``` schedules.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` schedules.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` schedules.Creator = operational_units.Creator ```  ``` schedules.Id = operational_units.RosterActiveHoursSchedule ``` |
| [pay\_periods](#pay-periods) | ``` schedules.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` schedules.Creator = pay_rules.Creator ```  ``` schedules.Id = pay_rules.Schedule ``` |
| [public\_holidays](#public-holidays) | ``` schedules.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` schedules.Creator = roster_opens.Employee ```  ``` schedules.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` schedules.Creator = roster_swaps.Employee ```  ``` schedules.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` schedules.Creator = rosters.Employee ```  ``` schedules.Creator = rosters.ConfirmBy ```  ``` schedules.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` schedules.Creator = sales_data.Employee ```  ``` schedules.Creator = sales_data.Creator ``` |
| [sms\_logs](#sms-logs) | ``` schedules.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` schedules.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` schedules.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` schedules.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` schedules.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` schedules.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` schedules.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` schedules.Creator = task_opunit_configs.Creator ```  ``` schedules.Id = task_opunit_configs.Schedule ``` |
| [task\_setups](#task-setups) | ``` schedules.Creator = task_setups.Creator ```  ``` schedules.Id = task_setups.Schedule ``` |
| [tasks](#tasks) | ``` schedules.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` schedules.Creator = teams.LeaderEmployee ```  ``` schedules.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` schedules.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` schedules.Creator = timesheets.Employee ```  ``` schedules.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` schedules.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` schedules.Creator = training_records.Employee ```  ``` schedules.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` schedules.Creator = webhooks.Creator ``` |

schedules table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **EndDate**  DATE |
| **EndTime**  STRING |
| **Exception**  STRING |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **MonthlyOnDates**  STRING |
| **MonthlyOnDays**  STRING |
| **Name**  STRING |
| **Orm**  STRING |
| **RepeatEvery**  INTEGER |
| **RepeatType**  INTEGER |
| **Saved**  BOOLEAN |
| **StartDate**  DATE |
| **StartTime**  STRING |
| **Template**  BOOLEAN |
| **WeeklyOnDays**  STRING |

### sms\_logs

The `sms_logs` table contains info about SMS logs.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/SmsLog) |

sms\_logs table foreign keys

| Join sms\_logs with | on |
| --- | --- |
| [addresses](#addresses) | ``` sms_logs.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` sms_logs.Creator = categories.Creator ``` |
| [comments](#comments) | ``` sms_logs.Creator = comments.Creator ``` |
| [companies](#companies) | ``` sms_logs.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` sms_logs.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` sms_logs.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` sms_logs.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` sms_logs.Creator = custom_app_data.Employee ```  ``` sms_logs.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` sms_logs.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` sms_logs.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` sms_logs.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` sms_logs.Creator = employee_agreements.EmployeeId ```  ``` sms_logs.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` sms_logs.Creator = employee_appraisal.Creator ```  ``` sms_logs.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` sms_logs.Creator = employee_availability.Employee ```  ``` sms_logs.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` sms_logs.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` sms_logs.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` sms_logs.Creator = employee_history.EmployeeId ```  ``` sms_logs.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` sms_logs.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` sms_logs.Creator = employee_paycycles.EmployeeId ```  ``` sms_logs.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` sms_logs.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` sms_logs.Creator = employee_salary_opunit_costing.Employee ```  ``` sms_logs.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` sms_logs.Creator = employee_workplaces.EmployeeId ```  ``` sms_logs.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` sms_logs.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` sms_logs.Creator = events.Creator ``` |
| [geo](#geo) | ``` sms_logs.Creator = geo.Creator ``` |
| [journal](#journal) | ``` sms_logs.Creator = journal.EmployeeId ```  ``` sms_logs.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` sms_logs.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` sms_logs.Creator = leave_accruals.Employee ```  ``` sms_logs.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` sms_logs.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` sms_logs.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` sms_logs.Creator = leaves.Employee ```  ``` sms_logs.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` sms_logs.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` sms_logs.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` sms_logs.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` sms_logs.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` sms_logs.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` sms_logs.Creator = roster_opens.Employee ```  ``` sms_logs.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` sms_logs.Creator = roster_swaps.Employee ```  ``` sms_logs.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` sms_logs.Creator = rosters.Employee ```  ``` sms_logs.Creator = rosters.ConfirmBy ```  ``` sms_logs.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` sms_logs.Creator = sales_data.Employee ```  ``` sms_logs.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` sms_logs.Creator = schedules.Creator ``` |
| [states](#states) | ``` sms_logs.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` sms_logs.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` sms_logs.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` sms_logs.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` sms_logs.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` sms_logs.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` sms_logs.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` sms_logs.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` sms_logs.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` sms_logs.Creator = teams.LeaderEmployee ```  ``` sms_logs.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` sms_logs.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` sms_logs.Creator = timesheets.Employee ```  ``` sms_logs.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` sms_logs.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` sms_logs.Creator = training_records.Employee ```  ``` sms_logs.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` sms_logs.Creator = webhooks.Creator ``` |

sms\_logs table schema

|  |
| --- |
| **Count**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **DeliveryReport**  STRING |
| **Destination**  STRING |
| **Id**  INTEGER |
| **Message**  STRING |
| **Modified**  DATE-TIME |
| **SmsId**  STRING |

### states

The `states` table contains info about states.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/State) |

states table foreign keys

| Join states with | on |
| --- | --- |
| [countries](#countries) | ``` states.Country = countries.Id ```  ``` states.Creator = countries.Creator ``` |
| [geo](#geo) | ``` states.Country = geo.Country ```  ``` states.Creator = geo.Creator ``` |
| [addresses](#addresses) | ``` states.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` states.Creator = categories.Creator ``` |
| [comments](#comments) | ``` states.Creator = comments.Creator ``` |
| [companies](#companies) | ``` states.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` states.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` states.Creator = contacts.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` states.Creator = custom_app_data.Employee ```  ``` states.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` states.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` states.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` states.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` states.Creator = employee_agreements.EmployeeId ```  ``` states.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` states.Creator = employee_appraisal.Creator ```  ``` states.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` states.Creator = employee_availability.Employee ```  ``` states.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` states.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` states.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` states.Creator = employee_history.EmployeeId ```  ``` states.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` states.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` states.Creator = employee_paycycles.EmployeeId ```  ``` states.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` states.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` states.Creator = employee_salary_opunit_costing.Employee ```  ``` states.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` states.Creator = employee_workplaces.EmployeeId ```  ``` states.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` states.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` states.Creator = events.Creator ``` |
| [journal](#journal) | ``` states.Creator = journal.EmployeeId ```  ``` states.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` states.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` states.Creator = leave_accruals.Employee ```  ``` states.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` states.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` states.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` states.Creator = leaves.Employee ```  ``` states.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` states.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` states.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` states.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` states.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` states.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` states.Creator = roster_opens.Employee ```  ``` states.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` states.Creator = roster_swaps.Employee ```  ``` states.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` states.Creator = rosters.Employee ```  ``` states.Creator = rosters.ConfirmBy ```  ``` states.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` states.Creator = sales_data.Employee ```  ``` states.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` states.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` states.Creator = sms_logs.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` states.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` states.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` states.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` states.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` states.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` states.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` states.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` states.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` states.Creator = teams.LeaderEmployee ```  ``` states.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` states.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` states.Creator = timesheets.Employee ```  ``` states.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` states.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` states.Creator = training_records.Employee ```  ``` states.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` states.Creator = webhooks.Creator ``` |

states table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **Code**  STRING |
| **Country**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **SortOrder**  INTEGER |
| **State**  STRING |

### stress\_profiles

The `stress_profiles` table contains info about stress profiles.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/StressProfile) |

stress\_profiles table foreign keys

| Join stress\_profiles with | on |
| --- | --- |
| [addresses](#addresses) | ``` stress_profiles.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` stress_profiles.Creator = categories.Creator ``` |
| [comments](#comments) | ``` stress_profiles.Creator = comments.Creator ``` |
| [companies](#companies) | ``` stress_profiles.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` stress_profiles.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` stress_profiles.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` stress_profiles.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` stress_profiles.Creator = custom_app_data.Employee ```  ``` stress_profiles.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` stress_profiles.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` stress_profiles.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` stress_profiles.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` stress_profiles.Creator = employee_agreements.EmployeeId ```  ``` stress_profiles.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` stress_profiles.Creator = employee_appraisal.Creator ```  ``` stress_profiles.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` stress_profiles.Creator = employee_availability.Employee ```  ``` stress_profiles.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` stress_profiles.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` stress_profiles.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` stress_profiles.Creator = employee_history.EmployeeId ```  ``` stress_profiles.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` stress_profiles.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` stress_profiles.Creator = employee_paycycles.EmployeeId ```  ``` stress_profiles.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` stress_profiles.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` stress_profiles.Creator = employee_salary_opunit_costing.Employee ```  ``` stress_profiles.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` stress_profiles.Creator = employee_workplaces.EmployeeId ```  ``` stress_profiles.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` stress_profiles.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` stress_profiles.Creator = events.Creator ``` |
| [geo](#geo) | ``` stress_profiles.Creator = geo.Creator ``` |
| [journal](#journal) | ``` stress_profiles.Creator = journal.EmployeeId ```  ``` stress_profiles.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` stress_profiles.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` stress_profiles.Creator = leave_accruals.Employee ```  ``` stress_profiles.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` stress_profiles.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` stress_profiles.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` stress_profiles.Creator = leaves.Employee ```  ``` stress_profiles.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` stress_profiles.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` stress_profiles.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` stress_profiles.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` stress_profiles.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` stress_profiles.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` stress_profiles.Creator = roster_opens.Employee ```  ``` stress_profiles.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` stress_profiles.Creator = roster_swaps.Employee ```  ``` stress_profiles.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` stress_profiles.Creator = rosters.Employee ```  ``` stress_profiles.Creator = rosters.ConfirmBy ```  ``` stress_profiles.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` stress_profiles.Creator = sales_data.Employee ```  ``` stress_profiles.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` stress_profiles.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` stress_profiles.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` stress_profiles.Creator = states.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` stress_profiles.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` stress_profiles.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` stress_profiles.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` stress_profiles.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` stress_profiles.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` stress_profiles.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` stress_profiles.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` stress_profiles.Creator = teams.LeaderEmployee ```  ``` stress_profiles.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` stress_profiles.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` stress_profiles.Creator = timesheets.Employee ```  ``` stress_profiles.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` stress_profiles.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` stress_profiles.Creator = training_records.Employee ```  ``` stress_profiles.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` stress_profiles.Creator = webhooks.Creator ``` |

stress\_profiles table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **CustomRules**  STRING |
| **GapHoursBetweenShifts**  NUMBER |
| **Id**  INTEGER |
| **MaxDaysPerPeriod**  NUMBER |
| **MaxHoursPerDay**  NUMBER |
| **MaxHoursPerPeriod**  NUMBER |
| **MaxHoursPerShift**  NUMBER |
| **Modified**  DATE-TIME |
| **Name**  STRING |

### system\_usage\_balances

The `system_usage_balances` table contains info about system usage balances.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/SystemUsageBalance) |

system\_usage\_balances table foreign keys

| Join system\_usage\_balances with | on |
| --- | --- |
| [addresses](#addresses) | ``` system_usage_balances.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` system_usage_balances.Creator = categories.Creator ``` |
| [comments](#comments) | ``` system_usage_balances.Creator = comments.Creator ``` |
| [companies](#companies) | ``` system_usage_balances.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` system_usage_balances.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` system_usage_balances.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` system_usage_balances.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` system_usage_balances.Creator = custom_app_data.Employee ```  ``` system_usage_balances.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` system_usage_balances.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` system_usage_balances.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` system_usage_balances.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` system_usage_balances.Creator = employee_agreements.EmployeeId ```  ``` system_usage_balances.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` system_usage_balances.Creator = employee_appraisal.Creator ```  ``` system_usage_balances.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` system_usage_balances.Creator = employee_availability.Employee ```  ``` system_usage_balances.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` system_usage_balances.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` system_usage_balances.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` system_usage_balances.Creator = employee_history.EmployeeId ```  ``` system_usage_balances.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` system_usage_balances.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` system_usage_balances.Creator = employee_paycycles.EmployeeId ```  ``` system_usage_balances.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` system_usage_balances.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` system_usage_balances.Creator = employee_salary_opunit_costing.Employee ```  ``` system_usage_balances.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` system_usage_balances.Creator = employee_workplaces.EmployeeId ```  ``` system_usage_balances.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` system_usage_balances.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` system_usage_balances.Creator = events.Creator ``` |
| [geo](#geo) | ``` system_usage_balances.Creator = geo.Creator ``` |
| [journal](#journal) | ``` system_usage_balances.Creator = journal.EmployeeId ```  ``` system_usage_balances.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` system_usage_balances.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` system_usage_balances.Creator = leave_accruals.Employee ```  ``` system_usage_balances.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` system_usage_balances.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` system_usage_balances.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` system_usage_balances.Creator = leaves.Employee ```  ``` system_usage_balances.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` system_usage_balances.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` system_usage_balances.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` system_usage_balances.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` system_usage_balances.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` system_usage_balances.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` system_usage_balances.Creator = roster_opens.Employee ```  ``` system_usage_balances.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` system_usage_balances.Creator = roster_swaps.Employee ```  ``` system_usage_balances.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` system_usage_balances.Creator = rosters.Employee ```  ``` system_usage_balances.Creator = rosters.ConfirmBy ```  ``` system_usage_balances.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` system_usage_balances.Creator = sales_data.Employee ```  ``` system_usage_balances.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` system_usage_balances.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` system_usage_balances.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` system_usage_balances.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` system_usage_balances.Creator = stress_profiles.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` system_usage_balances.Creator = system_usage_tracking.Creator ```  ``` system_usage_balances.Id = system_usage_tracking.BalanceId ``` |
| [task\_group\_setups](#task-group-setups) | ``` system_usage_balances.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` system_usage_balances.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` system_usage_balances.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` system_usage_balances.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` system_usage_balances.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` system_usage_balances.Creator = teams.LeaderEmployee ```  ``` system_usage_balances.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` system_usage_balances.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` system_usage_balances.Creator = timesheets.Employee ```  ``` system_usage_balances.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` system_usage_balances.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` system_usage_balances.Creator = training_records.Employee ```  ``` system_usage_balances.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` system_usage_balances.Creator = webhooks.Creator ``` |

system\_usage\_balances table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Credit**  NUMBER |
| **Date**  DATE |
| **Description**  STRING |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Type**  INTEGER |

### system\_usage\_tracking

The `system_usage_tracking` table contains info about system usage tracking.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/SystemUsageTracking) |

system\_usage\_tracking table foreign keys

| Join system\_usage\_tracking with | on |
| --- | --- |
| [companies](#companies) | ``` system_usage_tracking.CompanyId = companies.Id ```  ``` system_usage_tracking.CompanyId = companies.ParentCompany ```  ``` system_usage_tracking.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` system_usage_tracking.CompanyId = company_periods.Company ```  ``` system_usage_tracking.Creator = company_periods.Creator ``` |
| [employee\_history](#employee-history) | ``` system_usage_tracking.CompanyId = employee_history.Company ```  ``` system_usage_tracking.Creator = employee_history.EmployeeId ```  ``` system_usage_tracking.Creator = employee_history.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` system_usage_tracking.CompanyId = employee_workplaces.Company ```  ``` system_usage_tracking.Creator = employee_workplaces.EmployeeId ```  ``` system_usage_tracking.Creator = employee_workplaces.Creator ``` |
| [kiosks](#kiosks) | ``` system_usage_tracking.CompanyId = kiosks.Company ```  ``` system_usage_tracking.Creator = kiosks.Creator ``` |
| [leaves](#leaves) | ``` system_usage_tracking.CompanyId = leaves.Company ```  ``` system_usage_tracking.Creator = leaves.Employee ```  ``` system_usage_tracking.Creator = leaves.Creator ``` |
| [addresses](#addresses) | ``` system_usage_tracking.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` system_usage_tracking.Creator = categories.Creator ``` |
| [comments](#comments) | ``` system_usage_tracking.Creator = comments.Creator ``` |
| [contacts](#contacts) | ``` system_usage_tracking.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` system_usage_tracking.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` system_usage_tracking.Creator = custom_app_data.Employee ```  ``` system_usage_tracking.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` system_usage_tracking.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` system_usage_tracking.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` system_usage_tracking.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` system_usage_tracking.Creator = employee_agreements.EmployeeId ```  ``` system_usage_tracking.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` system_usage_tracking.Creator = employee_appraisal.Creator ```  ``` system_usage_tracking.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` system_usage_tracking.Creator = employee_availability.Employee ```  ``` system_usage_tracking.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` system_usage_tracking.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` system_usage_tracking.Creator = employee_contracts.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` system_usage_tracking.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` system_usage_tracking.Creator = employee_paycycles.EmployeeId ```  ``` system_usage_tracking.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` system_usage_tracking.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` system_usage_tracking.Creator = employee_salary_opunit_costing.Employee ```  ``` system_usage_tracking.Creator = employee_salary_opunit_costing.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` system_usage_tracking.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` system_usage_tracking.Creator = events.Creator ``` |
| [geo](#geo) | ``` system_usage_tracking.Creator = geo.Creator ``` |
| [journal](#journal) | ``` system_usage_tracking.Creator = journal.EmployeeId ```  ``` system_usage_tracking.Creator = journal.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` system_usage_tracking.Creator = leave_accruals.Employee ```  ``` system_usage_tracking.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` system_usage_tracking.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` system_usage_tracking.Creator = leave_rules.Creator ``` |
| [memos](#memos) | ``` system_usage_tracking.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` system_usage_tracking.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` system_usage_tracking.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` system_usage_tracking.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` system_usage_tracking.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` system_usage_tracking.Creator = roster_opens.Employee ```  ``` system_usage_tracking.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` system_usage_tracking.Creator = roster_swaps.Employee ```  ``` system_usage_tracking.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` system_usage_tracking.Creator = rosters.Employee ```  ``` system_usage_tracking.Creator = rosters.ConfirmBy ```  ``` system_usage_tracking.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` system_usage_tracking.Creator = sales_data.Employee ```  ``` system_usage_tracking.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` system_usage_tracking.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` system_usage_tracking.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` system_usage_tracking.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` system_usage_tracking.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` system_usage_tracking.Creator = system_usage_balances.Creator ```  ``` system_usage_tracking.BalanceId = system_usage_balances.Id ``` |
| [task\_group\_setups](#task-group-setups) | ``` system_usage_tracking.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` system_usage_tracking.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` system_usage_tracking.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` system_usage_tracking.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` system_usage_tracking.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` system_usage_tracking.Creator = teams.LeaderEmployee ```  ``` system_usage_tracking.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` system_usage_tracking.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` system_usage_tracking.Creator = timesheets.Employee ```  ``` system_usage_tracking.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` system_usage_tracking.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` system_usage_tracking.Creator = training_records.Employee ```  ``` system_usage_tracking.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` system_usage_tracking.Creator = webhooks.Creator ``` |

system\_usage\_tracking table schema

|  |
| --- |
| **BalanceId**  INTEGER |
| **CompanyId**  INTEGER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Date**  DATE |
| **Description**  STRING |
| **EmpId**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Usage**  NUMBER |
| **UsageRecordId**  INTEGER |
| **UsageType**  INTEGER |

### task\_group\_setups

The `task_group_setups` table contains info about task group setups.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/TaskGroupSetup) |

task\_group\_setups table foreign keys

| Join task\_group\_setups with | on |
| --- | --- |
| [addresses](#addresses) | ``` task_group_setups.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` task_group_setups.Creator = categories.Creator ``` |
| [comments](#comments) | ``` task_group_setups.Creator = comments.Creator ``` |
| [companies](#companies) | ``` task_group_setups.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` task_group_setups.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` task_group_setups.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` task_group_setups.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` task_group_setups.Creator = custom_app_data.Employee ```  ``` task_group_setups.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` task_group_setups.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` task_group_setups.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` task_group_setups.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` task_group_setups.Creator = employee_agreements.EmployeeId ```  ``` task_group_setups.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` task_group_setups.Creator = employee_appraisal.Creator ```  ``` task_group_setups.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` task_group_setups.Creator = employee_availability.Employee ```  ``` task_group_setups.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` task_group_setups.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` task_group_setups.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` task_group_setups.Creator = employee_history.EmployeeId ```  ``` task_group_setups.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` task_group_setups.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` task_group_setups.Creator = employee_paycycles.EmployeeId ```  ``` task_group_setups.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` task_group_setups.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` task_group_setups.Creator = employee_salary_opunit_costing.Employee ```  ``` task_group_setups.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` task_group_setups.Creator = employee_workplaces.EmployeeId ```  ``` task_group_setups.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` task_group_setups.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` task_group_setups.Creator = events.Creator ``` |
| [geo](#geo) | ``` task_group_setups.Creator = geo.Creator ``` |
| [journal](#journal) | ``` task_group_setups.Creator = journal.EmployeeId ```  ``` task_group_setups.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` task_group_setups.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` task_group_setups.Creator = leave_accruals.Employee ```  ``` task_group_setups.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` task_group_setups.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` task_group_setups.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` task_group_setups.Creator = leaves.Employee ```  ``` task_group_setups.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` task_group_setups.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` task_group_setups.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` task_group_setups.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` task_group_setups.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` task_group_setups.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` task_group_setups.Creator = roster_opens.Employee ```  ``` task_group_setups.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` task_group_setups.Creator = roster_swaps.Employee ```  ``` task_group_setups.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` task_group_setups.Creator = rosters.Employee ```  ``` task_group_setups.Creator = rosters.ConfirmBy ```  ``` task_group_setups.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` task_group_setups.Creator = sales_data.Employee ```  ``` task_group_setups.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` task_group_setups.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` task_group_setups.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` task_group_setups.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` task_group_setups.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` task_group_setups.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` task_group_setups.Creator = system_usage_tracking.Creator ``` |
| [task\_groups](#task-groups) | ``` task_group_setups.Creator = task_groups.Creator ```  ``` task_group_setups.Id = task_groups.GroupSetupId ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` task_group_setups.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` task_group_setups.Creator = task_setups.Creator ```  ``` task_group_setups.Id = task_setups.GroupId ``` |
| [tasks](#tasks) | ``` task_group_setups.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` task_group_setups.Creator = teams.LeaderEmployee ```  ``` task_group_setups.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` task_group_setups.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` task_group_setups.Creator = timesheets.Employee ```  ``` task_group_setups.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` task_group_setups.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` task_group_setups.Creator = training_records.Employee ```  ``` task_group_setups.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` task_group_setups.Creator = webhooks.Creator ``` |

task\_group\_setups table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **Comment**  STRING |
| **Compulsory**  BOOLEAN |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Deadline**  NUMBER |
| **Id**  INTEGER |
| **Key**  STRING |
| **Modified**  DATE-TIME |
| **Name**  STRING |
| **Notification**  STRING |
| **Oncreate**  STRING |
| **Onsubmit**  STRING |
| **Plugins**  STRING |

### task\_groups

The `task_groups` table contains info about task groups.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/TaskGroup) |

task\_groups table foreign keys

| Join task\_groups with | on |
| --- | --- |
| [addresses](#addresses) | ``` task_groups.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` task_groups.Creator = categories.Creator ``` |
| [comments](#comments) | ``` task_groups.Creator = comments.Creator ``` |
| [companies](#companies) | ``` task_groups.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` task_groups.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` task_groups.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` task_groups.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` task_groups.Creator = custom_app_data.Employee ```  ``` task_groups.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` task_groups.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` task_groups.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` task_groups.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` task_groups.Creator = employee_agreements.EmployeeId ```  ``` task_groups.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` task_groups.Creator = employee_appraisal.Creator ```  ``` task_groups.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` task_groups.Creator = employee_availability.Employee ```  ``` task_groups.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` task_groups.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` task_groups.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` task_groups.Creator = employee_history.EmployeeId ```  ``` task_groups.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` task_groups.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` task_groups.Creator = employee_paycycles.EmployeeId ```  ``` task_groups.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` task_groups.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` task_groups.Creator = employee_salary_opunit_costing.Employee ```  ``` task_groups.Creator = employee_salary_opunit_costing.Creator ```  ``` task_groups.OpUnitId = employee_salary_opunit_costing.OpUnit ``` |
| [employee\_workplaces](#employee-workplaces) | ``` task_groups.Creator = employee_workplaces.EmployeeId ```  ``` task_groups.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` task_groups.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` task_groups.Creator = events.Creator ``` |
| [geo](#geo) | ``` task_groups.Creator = geo.Creator ``` |
| [journal](#journal) | ``` task_groups.Creator = journal.EmployeeId ```  ``` task_groups.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` task_groups.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` task_groups.Creator = leave_accruals.Employee ```  ``` task_groups.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` task_groups.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` task_groups.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` task_groups.Creator = leaves.Employee ```  ``` task_groups.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` task_groups.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` task_groups.Creator = operational_units.Creator ```  ``` task_groups.OpUnitId = operational_units.Id ```  ``` task_groups.OpUnitId = operational_units.ParentOperationalUnit ``` |
| [pay\_periods](#pay-periods) | ``` task_groups.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` task_groups.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` task_groups.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` task_groups.Creator = roster_opens.Employee ```  ``` task_groups.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` task_groups.Creator = roster_swaps.Employee ```  ``` task_groups.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` task_groups.Creator = rosters.Employee ```  ``` task_groups.Creator = rosters.ConfirmBy ```  ``` task_groups.Creator = rosters.Creator ```  ``` task_groups.OpUnitId = rosters.OperationalUnit ``` |
| [sales\_data](#sales-data) | ``` task_groups.Creator = sales_data.Employee ```  ``` task_groups.Creator = sales_data.Creator ```  ``` task_groups.OpUnitId = sales_data.OperationalUnit ``` |
| [schedules](#schedules) | ``` task_groups.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` task_groups.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` task_groups.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` task_groups.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` task_groups.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` task_groups.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` task_groups.Creator = task_group_setups.Creator ```  ``` task_groups.GroupSetupId = task_group_setups.Id ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` task_groups.Creator = task_opunit_configs.Creator ```  ``` task_groups.OpUnitId = task_opunit_configs.OpUnitId ```  ``` task_groups.Id = task_opunit_configs.TaskGroupId ``` |
| [task\_setups](#task-setups) | ``` task_groups.Creator = task_setups.Creator ```  ``` task_groups.GroupSetupId = task_setups.GroupId ``` |
| [tasks](#tasks) | ``` task_groups.Creator = tasks.Creator ```  ``` task_groups.OpUnitId = tasks.OpUnitId ```  ``` task_groups.Id = tasks.GroupId ``` |
| [teams](#teams) | ``` task_groups.Creator = teams.LeaderEmployee ```  ``` task_groups.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` task_groups.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` task_groups.Creator = timesheets.Employee ```  ``` task_groups.Creator = timesheets.Creator ```  ``` task_groups.OpUnitId = timesheets.OperationalUnit ``` |
| [training\_modules](#training-modules) | ``` task_groups.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` task_groups.Creator = training_records.Employee ```  ``` task_groups.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` task_groups.Creator = webhooks.Creator ``` |

task\_groups table schema

|  |
| --- |
| **Comment**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Date**  DATE |
| **DayTimestamp**  INTEGER |
| **GroupSetupId**  INTEGER |
| **Id**  INTEGER |
| **Key**  STRING |
| **Modified**  DATE-TIME |
| **Name**  STRING |
| **OpUnitId**  INTEGER |
| **OrigDate**  DATE |
| **OrigDayTimestamp**  INTEGER |
| **SortOrder**  INTEGER |

### task\_opunit\_configs

The `task_opunit_configs` table contains info about task operational unit configurations.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/TaskOpunitConfig) |

task\_opunit\_configs table foreign keys

| Join task\_opunit\_configs with | on |
| --- | --- |
| [addresses](#addresses) | ``` task_opunit_configs.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` task_opunit_configs.Creator = categories.Creator ``` |
| [comments](#comments) | ``` task_opunit_configs.Creator = comments.Creator ``` |
| [companies](#companies) | ``` task_opunit_configs.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` task_opunit_configs.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` task_opunit_configs.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` task_opunit_configs.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` task_opunit_configs.Creator = custom_app_data.Employee ```  ``` task_opunit_configs.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` task_opunit_configs.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` task_opunit_configs.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` task_opunit_configs.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` task_opunit_configs.Creator = employee_agreements.EmployeeId ```  ``` task_opunit_configs.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` task_opunit_configs.Creator = employee_appraisal.Creator ```  ``` task_opunit_configs.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` task_opunit_configs.Creator = employee_availability.Employee ```  ``` task_opunit_configs.Creator = employee_availability.Creator ```  ``` task_opunit_configs.Schedule = employee_availability.Schedule ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` task_opunit_configs.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` task_opunit_configs.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` task_opunit_configs.Creator = employee_history.EmployeeId ```  ``` task_opunit_configs.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` task_opunit_configs.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` task_opunit_configs.Creator = employee_paycycles.EmployeeId ```  ``` task_opunit_configs.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` task_opunit_configs.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` task_opunit_configs.Creator = employee_salary_opunit_costing.Employee ```  ``` task_opunit_configs.Creator = employee_salary_opunit_costing.Creator ```  ``` task_opunit_configs.OpUnitId = employee_salary_opunit_costing.OpUnit ``` |
| [employee\_workplaces](#employee-workplaces) | ``` task_opunit_configs.Creator = employee_workplaces.EmployeeId ```  ``` task_opunit_configs.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` task_opunit_configs.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` task_opunit_configs.Creator = events.Creator ```  ``` task_opunit_configs.Schedule = events.Schedule ``` |
| [geo](#geo) | ``` task_opunit_configs.Creator = geo.Creator ``` |
| [journal](#journal) | ``` task_opunit_configs.Creator = journal.EmployeeId ```  ``` task_opunit_configs.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` task_opunit_configs.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` task_opunit_configs.Creator = leave_accruals.Employee ```  ``` task_opunit_configs.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` task_opunit_configs.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` task_opunit_configs.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` task_opunit_configs.Creator = leaves.Employee ```  ``` task_opunit_configs.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` task_opunit_configs.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` task_opunit_configs.Creator = operational_units.Creator ```  ``` task_opunit_configs.OpUnitId = operational_units.Id ```  ``` task_opunit_configs.OpUnitId = operational_units.ParentOperationalUnit ```  ``` task_opunit_configs.Schedule = operational_units.RosterActiveHoursSchedule ``` |
| [pay\_periods](#pay-periods) | ``` task_opunit_configs.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` task_opunit_configs.Creator = pay_rules.Creator ```  ``` task_opunit_configs.Schedule = pay_rules.Schedule ``` |
| [public\_holidays](#public-holidays) | ``` task_opunit_configs.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` task_opunit_configs.Creator = roster_opens.Employee ```  ``` task_opunit_configs.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` task_opunit_configs.Creator = roster_swaps.Employee ```  ``` task_opunit_configs.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` task_opunit_configs.Creator = rosters.Employee ```  ``` task_opunit_configs.Creator = rosters.ConfirmBy ```  ``` task_opunit_configs.Creator = rosters.Creator ```  ``` task_opunit_configs.OpUnitId = rosters.OperationalUnit ``` |
| [sales\_data](#sales-data) | ``` task_opunit_configs.Creator = sales_data.Employee ```  ``` task_opunit_configs.Creator = sales_data.Creator ```  ``` task_opunit_configs.OpUnitId = sales_data.OperationalUnit ``` |
| [schedules](#schedules) | ``` task_opunit_configs.Creator = schedules.Creator ```  ``` task_opunit_configs.Schedule = schedules.Id ``` |
| [sms\_logs](#sms-logs) | ``` task_opunit_configs.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` task_opunit_configs.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` task_opunit_configs.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` task_opunit_configs.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` task_opunit_configs.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` task_opunit_configs.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` task_opunit_configs.Creator = task_groups.Creator ```  ``` task_opunit_configs.OpUnitId = task_groups.OpUnitId ```  ``` task_opunit_configs.TaskGroupId = task_groups.Id ``` |
| [task\_setups](#task-setups) | ``` task_opunit_configs.Creator = task_setups.Creator ```  ``` task_opunit_configs.Schedule = task_setups.Schedule ```  ``` task_opunit_configs.TaskSetupId = task_setups.Id ``` |
| [tasks](#tasks) | ``` task_opunit_configs.Creator = tasks.Creator ```  ``` task_opunit_configs.OpUnitId = tasks.OpUnitId ```  ``` task_opunit_configs.TaskGroupId = tasks.GroupId ```  ``` task_opunit_configs.TaskSetupId = tasks.TaskSetupId ``` |
| [teams](#teams) | ``` task_opunit_configs.Creator = teams.LeaderEmployee ```  ``` task_opunit_configs.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` task_opunit_configs.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` task_opunit_configs.Creator = timesheets.Employee ```  ``` task_opunit_configs.Creator = timesheets.Creator ```  ``` task_opunit_configs.OpUnitId = timesheets.OperationalUnit ``` |
| [training\_modules](#training-modules) | ``` task_opunit_configs.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` task_opunit_configs.Creator = training_records.Employee ```  ``` task_opunit_configs.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` task_opunit_configs.Creator = webhooks.Creator ``` |

task\_opunit\_configs table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **AvailableAfter**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **OpUnitId**  INTEGER |
| **Schedule**  INTEGER |
| **SortOrder**  INTEGER |
| **TaskGroupId**  INTEGER |
| **TaskSetupId**  INTEGER |
| **Type**  INTEGER |

### task\_setups

The `task_setups` table contains info about task setups.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/TaskSetup) |

task\_setups table foreign keys

| Join task\_setups with | on |
| --- | --- |
| [addresses](#addresses) | ``` task_setups.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` task_setups.Creator = categories.Creator ``` |
| [comments](#comments) | ``` task_setups.Creator = comments.Creator ``` |
| [companies](#companies) | ``` task_setups.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` task_setups.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` task_setups.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` task_setups.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` task_setups.Creator = custom_app_data.Employee ```  ``` task_setups.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` task_setups.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` task_setups.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` task_setups.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` task_setups.Creator = employee_agreements.EmployeeId ```  ``` task_setups.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` task_setups.Creator = employee_appraisal.Creator ```  ``` task_setups.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` task_setups.Creator = employee_availability.Employee ```  ``` task_setups.Creator = employee_availability.Creator ```  ``` task_setups.Schedule = employee_availability.Schedule ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` task_setups.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` task_setups.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` task_setups.Creator = employee_history.EmployeeId ```  ``` task_setups.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` task_setups.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` task_setups.Creator = employee_paycycles.EmployeeId ```  ``` task_setups.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` task_setups.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` task_setups.Creator = employee_salary_opunit_costing.Employee ```  ``` task_setups.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` task_setups.Creator = employee_workplaces.EmployeeId ```  ``` task_setups.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` task_setups.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` task_setups.Creator = events.Creator ```  ``` task_setups.Schedule = events.Schedule ``` |
| [geo](#geo) | ``` task_setups.Creator = geo.Creator ``` |
| [journal](#journal) | ``` task_setups.Creator = journal.EmployeeId ```  ``` task_setups.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` task_setups.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` task_setups.Creator = leave_accruals.Employee ```  ``` task_setups.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` task_setups.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` task_setups.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` task_setups.Creator = leaves.Employee ```  ``` task_setups.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` task_setups.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` task_setups.Creator = operational_units.Creator ```  ``` task_setups.Schedule = operational_units.RosterActiveHoursSchedule ``` |
| [pay\_periods](#pay-periods) | ``` task_setups.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` task_setups.Creator = pay_rules.Creator ```  ``` task_setups.Schedule = pay_rules.Schedule ``` |
| [public\_holidays](#public-holidays) | ``` task_setups.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` task_setups.Creator = roster_opens.Employee ```  ``` task_setups.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` task_setups.Creator = roster_swaps.Employee ```  ``` task_setups.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` task_setups.Creator = rosters.Employee ```  ``` task_setups.Creator = rosters.ConfirmBy ```  ``` task_setups.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` task_setups.Creator = sales_data.Employee ```  ``` task_setups.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` task_setups.Creator = schedules.Creator ```  ``` task_setups.Schedule = schedules.Id ``` |
| [sms\_logs](#sms-logs) | ``` task_setups.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` task_setups.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` task_setups.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` task_setups.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` task_setups.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` task_setups.Creator = task_group_setups.Creator ```  ``` task_setups.GroupId = task_group_setups.Id ``` |
| [task\_groups](#task-groups) | ``` task_setups.Creator = task_groups.Creator ```  ``` task_setups.GroupId = task_groups.GroupSetupId ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` task_setups.Creator = task_opunit_configs.Creator ```  ``` task_setups.Schedule = task_opunit_configs.Schedule ```  ``` task_setups.Id = task_opunit_configs.TaskSetupId ``` |
| [tasks](#tasks) | ``` task_setups.Creator = tasks.Creator ```  ``` task_setups.Id = tasks.TaskSetupId ``` |
| [teams](#teams) | ``` task_setups.Creator = teams.LeaderEmployee ```  ``` task_setups.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` task_setups.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` task_setups.Creator = timesheets.Employee ```  ``` task_setups.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` task_setups.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` task_setups.Creator = training_records.Employee ```  ``` task_setups.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` task_setups.Creator = webhooks.Creator ``` |

task\_setups table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **AvailableAfter**  STRING |
| **Colour**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Default**  STRING |
| **GroupId**  INTEGER |
| **Helptext**  STRING |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **OnNo**  STRING |
| **OnStart**  STRING |
| **OnSubmit**  STRING |
| **OnYes**  STRING |
| **Parent**  INTEGER |
| **Priority**  STRING |
| **Question**  STRING |
| **RenderFunc**  STRING |
| **RepeatIfNotCompleted**  BOOLEAN |
| **Schedule**  INTEGER |
| **Section**  STRING |
| **SortOrder**  INTEGER |
| **SupercedePrev**  BOOLEAN |
| **Time**  STRING |
| **Type**  INTEGER |

### tasks

The `tasks` table contains info about tasks.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Task) |

tasks table foreign keys

| Join tasks with | on |
| --- | --- |
| [addresses](#addresses) | ``` tasks.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` tasks.Creator = categories.Creator ``` |
| [comments](#comments) | ``` tasks.Creator = comments.Creator ``` |
| [companies](#companies) | ``` tasks.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` tasks.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` tasks.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` tasks.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` tasks.Creator = custom_app_data.Employee ```  ``` tasks.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` tasks.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` tasks.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` tasks.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` tasks.Creator = employee_agreements.EmployeeId ```  ``` tasks.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` tasks.Creator = employee_appraisal.Creator ```  ``` tasks.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` tasks.Creator = employee_availability.Employee ```  ``` tasks.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` tasks.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` tasks.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` tasks.Creator = employee_history.EmployeeId ```  ``` tasks.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` tasks.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` tasks.Creator = employee_paycycles.EmployeeId ```  ``` tasks.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` tasks.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` tasks.Creator = employee_salary_opunit_costing.Employee ```  ``` tasks.Creator = employee_salary_opunit_costing.Creator ```  ``` tasks.OpUnitId = employee_salary_opunit_costing.OpUnit ``` |
| [employee\_workplaces](#employee-workplaces) | ``` tasks.Creator = employee_workplaces.EmployeeId ```  ``` tasks.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` tasks.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` tasks.Creator = events.Creator ``` |
| [geo](#geo) | ``` tasks.Creator = geo.Creator ``` |
| [journal](#journal) | ``` tasks.Creator = journal.EmployeeId ```  ``` tasks.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` tasks.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` tasks.Creator = leave_accruals.Employee ```  ``` tasks.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` tasks.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` tasks.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` tasks.Creator = leaves.Employee ```  ``` tasks.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` tasks.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` tasks.Creator = operational_units.Creator ```  ``` tasks.OpUnitId = operational_units.Id ```  ``` tasks.OpUnitId = operational_units.ParentOperationalUnit ``` |
| [pay\_periods](#pay-periods) | ``` tasks.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` tasks.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` tasks.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` tasks.Creator = roster_opens.Employee ```  ``` tasks.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` tasks.Creator = roster_swaps.Employee ```  ``` tasks.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` tasks.Creator = rosters.Employee ```  ``` tasks.Creator = rosters.ConfirmBy ```  ``` tasks.Creator = rosters.Creator ```  ``` tasks.OpUnitId = rosters.OperationalUnit ``` |
| [sales\_data](#sales-data) | ``` tasks.Creator = sales_data.Employee ```  ``` tasks.Creator = sales_data.Creator ```  ``` tasks.OpUnitId = sales_data.OperationalUnit ``` |
| [schedules](#schedules) | ``` tasks.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` tasks.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` tasks.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` tasks.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` tasks.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` tasks.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` tasks.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` tasks.Creator = task_groups.Creator ```  ``` tasks.OpUnitId = task_groups.OpUnitId ```  ``` tasks.GroupId = task_groups.Id ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` tasks.Creator = task_opunit_configs.Creator ```  ``` tasks.OpUnitId = task_opunit_configs.OpUnitId ```  ``` tasks.GroupId = task_opunit_configs.TaskGroupId ```  ``` tasks.TaskSetupId = task_opunit_configs.TaskSetupId ``` |
| [task\_setups](#task-setups) | ``` tasks.Creator = task_setups.Creator ```  ``` tasks.TaskSetupId = task_setups.Id ``` |
| [teams](#teams) | ``` tasks.Creator = teams.LeaderEmployee ```  ``` tasks.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` tasks.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` tasks.Creator = timesheets.Employee ```  ``` tasks.Creator = timesheets.Creator ```  ``` tasks.OpUnitId = timesheets.OperationalUnit ``` |
| [training\_modules](#training-modules) | ``` tasks.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` tasks.Creator = training_records.Employee ```  ``` tasks.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` tasks.Creator = webhooks.Creator ``` |

tasks table schema

|  |
| --- |
| **Answer**  STRING |
| **AvailableAfterTimestamp**  INTEGER |
| **Comment**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Date**  DATE |
| **DayTimestamp**  INTEGER |
| **DueDate**  DATE |
| **DueTimestamp**  INTEGER |
| **End**  INTEGER |
| **GroupId**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **OpUnitId**  INTEGER |
| **OrigDate**  DATE |
| **OrigDayTimestamp**  INTEGER |
| **Question**  STRING |
| **RepeatIfNotCompleted**  BOOLEAN |
| **SortOrder**  INTEGER |
| **Start**  INTEGER |
| **TaskSetupId**  INTEGER |
| **TsCompleted**  INTEGER |
| **Type**  INTEGER |
| **UserEntry**  INTEGER |
| **UserPerformTask**  INTEGER |
| **UserResponsible**  INTEGER |

### teams

The `teams` table contains info about teams.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Team) |

teams table foreign keys

| Join teams with | on |
| --- | --- |
| [addresses](#addresses) | ``` teams.LeaderEmployee = addresses.Creator ```  ``` teams.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` teams.LeaderEmployee = categories.Creator ```  ``` teams.Creator = categories.Creator ``` |
| [comments](#comments) | ``` teams.LeaderEmployee = comments.Creator ```  ``` teams.Creator = comments.Creator ``` |
| [companies](#companies) | ``` teams.LeaderEmployee = companies.Creator ```  ``` teams.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` teams.LeaderEmployee = company_periods.Creator ```  ``` teams.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` teams.LeaderEmployee = contacts.Creator ```  ``` teams.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` teams.LeaderEmployee = countries.Creator ```  ``` teams.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` teams.LeaderEmployee = custom_app_data.Employee ```  ``` teams.Creator = custom_app_data.Employee ```  ``` teams.LeaderEmployee = custom_app_data.Creator ```  ``` teams.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` teams.LeaderEmployee = custom_field_data.Creator ```  ``` teams.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` teams.LeaderEmployee = custom_fields.Creator ```  ``` teams.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` teams.LeaderEmployee = employee_agreement_history.Creator ```  ``` teams.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` teams.LeaderEmployee = employee_agreements.EmployeeId ```  ``` teams.Creator = employee_agreements.EmployeeId ```  ``` teams.LeaderEmployee = employee_agreements.Creator ```  ``` teams.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` teams.LeaderEmployee = employee_appraisal.Creator ```  ``` teams.Creator = employee_appraisal.Creator ```  ``` teams.LeaderEmployee = employee_appraisal.Employee ```  ``` teams.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` teams.LeaderEmployee = employee_availability.Employee ```  ``` teams.Creator = employee_availability.Employee ```  ``` teams.LeaderEmployee = employee_availability.Creator ```  ``` teams.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` teams.LeaderEmployee = employee_contract_leave_rules.Creator ```  ``` teams.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` teams.LeaderEmployee = employee_contracts.Creator ```  ``` teams.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` teams.LeaderEmployee = employee_history.EmployeeId ```  ``` teams.Creator = employee_history.EmployeeId ```  ``` teams.LeaderEmployee = employee_history.Creator ```  ``` teams.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` teams.LeaderEmployee = employee_paycycle_returns.Creator ```  ``` teams.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` teams.LeaderEmployee = employee_paycycles.EmployeeId ```  ``` teams.Creator = employee_paycycles.EmployeeId ```  ``` teams.LeaderEmployee = employee_paycycles.Creator ```  ``` teams.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` teams.LeaderEmployee = employee_roles.Creator ```  ``` teams.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` teams.LeaderEmployee = employee_salary_opunit_costing.Employee ```  ``` teams.Creator = employee_salary_opunit_costing.Employee ```  ``` teams.LeaderEmployee = employee_salary_opunit_costing.Creator ```  ``` teams.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` teams.LeaderEmployee = employee_workplaces.EmployeeId ```  ``` teams.Creator = employee_workplaces.EmployeeId ```  ``` teams.LeaderEmployee = employee_workplaces.Creator ```  ``` teams.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` teams.LeaderEmployee = employment_conditions.Creator ```  ``` teams.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` teams.LeaderEmployee = events.Creator ```  ``` teams.Creator = events.Creator ``` |
| [geo](#geo) | ``` teams.LeaderEmployee = geo.Creator ```  ``` teams.Creator = geo.Creator ``` |
| [journal](#journal) | ``` teams.LeaderEmployee = journal.EmployeeId ```  ``` teams.Creator = journal.EmployeeId ```  ``` teams.LeaderEmployee = journal.Creator ```  ``` teams.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` teams.LeaderEmployee = kiosks.Creator ```  ``` teams.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` teams.LeaderEmployee = leave_accruals.Employee ```  ``` teams.Creator = leave_accruals.Employee ```  ``` teams.LeaderEmployee = leave_accruals.Creator ```  ``` teams.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` teams.LeaderEmployee = leave_pay_lines.Creator ```  ``` teams.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` teams.LeaderEmployee = leave_rules.Creator ```  ``` teams.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` teams.LeaderEmployee = leaves.Employee ```  ``` teams.Creator = leaves.Employee ```  ``` teams.LeaderEmployee = leaves.Creator ```  ``` teams.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` teams.LeaderEmployee = memos.Creator ```  ``` teams.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` teams.LeaderEmployee = operational_units.Creator ```  ``` teams.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` teams.LeaderEmployee = pay_periods.Creator ```  ``` teams.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` teams.LeaderEmployee = pay_rules.Creator ```  ``` teams.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` teams.LeaderEmployee = public_holidays.Creator ```  ``` teams.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` teams.LeaderEmployee = roster_opens.Employee ```  ``` teams.Creator = roster_opens.Employee ```  ``` teams.LeaderEmployee = roster_opens.Creator ```  ``` teams.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` teams.LeaderEmployee = roster_swaps.Employee ```  ``` teams.Creator = roster_swaps.Employee ```  ``` teams.LeaderEmployee = roster_swaps.Creator ```  ``` teams.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` teams.LeaderEmployee = rosters.Employee ```  ``` teams.Creator = rosters.Employee ```  ``` teams.LeaderEmployee = rosters.ConfirmBy ```  ``` teams.Creator = rosters.ConfirmBy ```  ``` teams.LeaderEmployee = rosters.Creator ```  ``` teams.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` teams.LeaderEmployee = sales_data.Employee ```  ``` teams.Creator = sales_data.Employee ```  ``` teams.LeaderEmployee = sales_data.Creator ```  ``` teams.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` teams.LeaderEmployee = schedules.Creator ```  ``` teams.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` teams.LeaderEmployee = sms_logs.Creator ```  ``` teams.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` teams.LeaderEmployee = states.Creator ```  ``` teams.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` teams.LeaderEmployee = stress_profiles.Creator ```  ``` teams.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` teams.LeaderEmployee = system_usage_balances.Creator ```  ``` teams.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` teams.LeaderEmployee = system_usage_tracking.Creator ```  ``` teams.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` teams.LeaderEmployee = task_group_setups.Creator ```  ``` teams.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` teams.LeaderEmployee = task_groups.Creator ```  ``` teams.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` teams.LeaderEmployee = task_opunit_configs.Creator ```  ``` teams.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` teams.LeaderEmployee = task_setups.Creator ```  ``` teams.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` teams.LeaderEmployee = tasks.Creator ```  ``` teams.Creator = tasks.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` teams.LeaderEmployee = timesheet_pay_returns.Creator ```  ``` teams.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` teams.LeaderEmployee = timesheets.Employee ```  ``` teams.Creator = timesheets.Employee ```  ``` teams.LeaderEmployee = timesheets.Creator ```  ``` teams.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` teams.LeaderEmployee = training_modules.Creator ```  ``` teams.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` teams.LeaderEmployee = training_records.Employee ```  ``` teams.Creator = training_records.Employee ```  ``` teams.LeaderEmployee = training_records.Creator ```  ``` teams.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` teams.LeaderEmployee = webhooks.Creator ```  ``` teams.Creator = webhooks.Creator ``` |

teams table schema

|  |
| --- |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **LeaderEmployee**  INTEGER |
| **Modified**  DATE-TIME |
| **Name**  STRING |

### timesheet\_pay\_returns

The `timesheet_pay_returns` table contains info about timesheet pay returns.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/TimesheetPayReturn) |

timesheet\_pay\_returns table foreign keys

| Join timesheet\_pay\_returns with | on |
| --- | --- |
| [addresses](#addresses) | ``` timesheet_pay_returns.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` timesheet_pay_returns.Creator = categories.Creator ``` |
| [comments](#comments) | ``` timesheet_pay_returns.Creator = comments.Creator ``` |
| [companies](#companies) | ``` timesheet_pay_returns.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` timesheet_pay_returns.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` timesheet_pay_returns.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` timesheet_pay_returns.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` timesheet_pay_returns.Creator = custom_app_data.Employee ```  ``` timesheet_pay_returns.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` timesheet_pay_returns.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` timesheet_pay_returns.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` timesheet_pay_returns.Creator = employee_agreement_history.Creator ```  ``` timesheet_pay_returns.PayRule = employee_agreement_history.SalaryPayRule ``` |
| [employee\_agreements](#employee-agreements) | ``` timesheet_pay_returns.Creator = employee_agreements.EmployeeId ```  ``` timesheet_pay_returns.Creator = employee_agreements.Creator ```  ``` timesheet_pay_returns.PayRule = employee_agreements.SalaryPayRule ``` |
| [employee\_appraisal](#employee-appraisal) | ``` timesheet_pay_returns.Creator = employee_appraisal.Creator ```  ``` timesheet_pay_returns.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` timesheet_pay_returns.Creator = employee_availability.Employee ```  ``` timesheet_pay_returns.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` timesheet_pay_returns.Creator = employee_contract_leave_rules.Creator ```  ``` timesheet_pay_returns.PayRule = employee_contract_leave_rules.LoadingPayRule1 ```  ``` timesheet_pay_returns.PayRule = employee_contract_leave_rules.LoadingPayRule2 ```  ``` timesheet_pay_returns.PayRule = employee_contract_leave_rules.LoadingPayRule3 ``` |
| [employee\_contracts](#employee-contracts) | ``` timesheet_pay_returns.Creator = employee_contracts.Creator ```  ``` timesheet_pay_returns.PayRule = employee_contracts.BasePayRule ``` |
| [employee\_history](#employee-history) | ``` timesheet_pay_returns.Creator = employee_history.EmployeeId ```  ``` timesheet_pay_returns.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` timesheet_pay_returns.Creator = employee_paycycle_returns.Creator ```  ``` timesheet_pay_returns.PayRule = employee_paycycle_returns.PayRule ``` |
| [employee\_paycycles](#employee-paycycles) | ``` timesheet_pay_returns.Creator = employee_paycycles.EmployeeId ```  ``` timesheet_pay_returns.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` timesheet_pay_returns.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` timesheet_pay_returns.Creator = employee_salary_opunit_costing.Employee ```  ``` timesheet_pay_returns.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` timesheet_pay_returns.Creator = employee_workplaces.EmployeeId ```  ``` timesheet_pay_returns.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` timesheet_pay_returns.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` timesheet_pay_returns.Creator = events.Creator ``` |
| [geo](#geo) | ``` timesheet_pay_returns.Creator = geo.Creator ``` |
| [journal](#journal) | ``` timesheet_pay_returns.Creator = journal.EmployeeId ```  ``` timesheet_pay_returns.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` timesheet_pay_returns.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` timesheet_pay_returns.Creator = leave_accruals.Employee ```  ``` timesheet_pay_returns.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` timesheet_pay_returns.Creator = leave_pay_lines.Creator ```  ``` timesheet_pay_returns.Timesheet = leave_pay_lines.TimesheetId ``` |
| [leave\_rules](#leave-rules) | ``` timesheet_pay_returns.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` timesheet_pay_returns.Creator = leaves.Employee ```  ``` timesheet_pay_returns.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` timesheet_pay_returns.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` timesheet_pay_returns.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` timesheet_pay_returns.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` timesheet_pay_returns.Creator = pay_rules.Creator ```  ``` timesheet_pay_returns.PayRule = pay_rules.Id ``` |
| [public\_holidays](#public-holidays) | ``` timesheet_pay_returns.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` timesheet_pay_returns.Creator = roster_opens.Employee ```  ``` timesheet_pay_returns.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` timesheet_pay_returns.Creator = roster_swaps.Employee ```  ``` timesheet_pay_returns.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` timesheet_pay_returns.Creator = rosters.Employee ```  ``` timesheet_pay_returns.Creator = rosters.ConfirmBy ```  ``` timesheet_pay_returns.Creator = rosters.Creator ```  ``` timesheet_pay_returns.Timesheet = rosters.MatchedByTimesheet ``` |
| [sales\_data](#sales-data) | ``` timesheet_pay_returns.Creator = sales_data.Employee ```  ``` timesheet_pay_returns.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` timesheet_pay_returns.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` timesheet_pay_returns.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` timesheet_pay_returns.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` timesheet_pay_returns.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` timesheet_pay_returns.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` timesheet_pay_returns.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` timesheet_pay_returns.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` timesheet_pay_returns.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` timesheet_pay_returns.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` timesheet_pay_returns.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` timesheet_pay_returns.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` timesheet_pay_returns.Creator = teams.LeaderEmployee ```  ``` timesheet_pay_returns.Creator = teams.Creator ``` |
| [timesheets](#timesheets) | ``` timesheet_pay_returns.Creator = timesheets.Employee ```  ``` timesheet_pay_returns.Creator = timesheets.Creator ```  ``` timesheet_pay_returns.Timesheet = timesheets.Id ``` |
| [training\_modules](#training-modules) | ``` timesheet_pay_returns.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` timesheet_pay_returns.Creator = training_records.Employee ```  ``` timesheet_pay_returns.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` timesheet_pay_returns.Creator = webhooks.Creator ``` |

timesheet\_pay\_returns table schema

|  |
| --- |
| **Cost**  NUMBER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Overridden**  BOOLEAN |
| **OverrideComment**  STRING |
| **PayRule**  INTEGER |
| **Timesheet**  INTEGER |
| **Value**  NUMBER |

### timesheets

The `timesheets` table contains info about timesheets.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Timesheet) |

timesheets table foreign keys

| Join timesheets with | on |
| --- | --- |
| [custom\_field\_data](#custom-field-data) | ``` timesheets.CustomFieldData = custom_field_data.Id ```  ``` timesheets.Employee = custom_field_data.Creator ```  ``` timesheets.Creator = custom_field_data.Creator ``` |
| [addresses](#addresses) | ``` timesheets.Employee = addresses.Creator ```  ``` timesheets.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` timesheets.Employee = categories.Creator ```  ``` timesheets.Creator = categories.Creator ``` |
| [comments](#comments) | ``` timesheets.Employee = comments.Creator ```  ``` timesheets.Creator = comments.Creator ``` |
| [companies](#companies) | ``` timesheets.Employee = companies.Creator ```  ``` timesheets.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` timesheets.Employee = company_periods.Creator ```  ``` timesheets.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` timesheets.Employee = contacts.Creator ```  ``` timesheets.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` timesheets.Employee = countries.Creator ```  ``` timesheets.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` timesheets.Employee = custom_app_data.Employee ```  ``` timesheets.Creator = custom_app_data.Employee ```  ``` timesheets.Employee = custom_app_data.Creator ```  ``` timesheets.Creator = custom_app_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` timesheets.Employee = custom_fields.Creator ```  ``` timesheets.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` timesheets.Employee = employee_agreement_history.Creator ```  ``` timesheets.Creator = employee_agreement_history.Creator ```  ``` timesheets.EmployeeAgreement = employee_agreement_history.AgreementId ``` |
| [employee\_agreements](#employee-agreements) | ``` timesheets.Employee = employee_agreements.EmployeeId ```  ``` timesheets.Creator = employee_agreements.EmployeeId ```  ``` timesheets.Employee = employee_agreements.Creator ```  ``` timesheets.Creator = employee_agreements.Creator ```  ``` timesheets.EmployeeAgreement = employee_agreements.Id ``` |
| [employee\_appraisal](#employee-appraisal) | ``` timesheets.Employee = employee_appraisal.Creator ```  ``` timesheets.Creator = employee_appraisal.Creator ```  ``` timesheets.Employee = employee_appraisal.Employee ```  ``` timesheets.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` timesheets.Employee = employee_availability.Employee ```  ``` timesheets.Creator = employee_availability.Employee ```  ``` timesheets.Employee = employee_availability.Creator ```  ``` timesheets.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` timesheets.Employee = employee_contract_leave_rules.Creator ```  ``` timesheets.Creator = employee_contract_leave_rules.Creator ```  ``` timesheets.LeaveRule = employee_contract_leave_rules.LeaveRuleId ``` |
| [employee\_contracts](#employee-contracts) | ``` timesheets.Employee = employee_contracts.Creator ```  ``` timesheets.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` timesheets.Employee = employee_history.EmployeeId ```  ``` timesheets.Creator = employee_history.EmployeeId ```  ``` timesheets.Employee = employee_history.Creator ```  ``` timesheets.Creator = employee_history.Creator ```  ``` timesheets.EmployeeHistory = employee_history.Id ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` timesheets.Employee = employee_paycycle_returns.Creator ```  ``` timesheets.Creator = employee_paycycle_returns.Creator ```  ``` timesheets.PaycycleId = employee_paycycle_returns.Id ``` |
| [employee\_paycycles](#employee-paycycles) | ``` timesheets.Employee = employee_paycycles.EmployeeId ```  ``` timesheets.Creator = employee_paycycles.EmployeeId ```  ``` timesheets.Employee = employee_paycycles.Creator ```  ``` timesheets.Creator = employee_paycycles.Creator ```  ``` timesheets.EmployeeAgreement = employee_paycycles.EmployeeAgreementId ``` |
| [employee\_roles](#employee-roles) | ``` timesheets.Employee = employee_roles.Creator ```  ``` timesheets.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` timesheets.Employee = employee_salary_opunit_costing.Employee ```  ``` timesheets.Creator = employee_salary_opunit_costing.Employee ```  ``` timesheets.Employee = employee_salary_opunit_costing.Creator ```  ``` timesheets.Creator = employee_salary_opunit_costing.Creator ```  ``` timesheets.EmployeeAgreement = employee_salary_opunit_costing.EmployeeAgreement ```  ``` timesheets.OperationalUnit = employee_salary_opunit_costing.OpUnit ``` |
| [employee\_workplaces](#employee-workplaces) | ``` timesheets.Employee = employee_workplaces.EmployeeId ```  ``` timesheets.Creator = employee_workplaces.EmployeeId ```  ``` timesheets.Employee = employee_workplaces.Creator ```  ``` timesheets.Creator = employee_workplaces.Creator ```  ``` timesheets.EmployeeAgreement = employee_workplaces.Agreement1 ```  ``` timesheets.EmployeeAgreement = employee_workplaces.Agreement2 ```  ``` timesheets.EmployeeAgreement = employee_workplaces.Agreement3 ``` |
| [employment\_conditions](#employment-conditions) | ``` timesheets.Employee = employment_conditions.Creator ```  ``` timesheets.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` timesheets.Employee = events.Creator ```  ``` timesheets.Creator = events.Creator ``` |
| [geo](#geo) | ``` timesheets.Employee = geo.Creator ```  ``` timesheets.Creator = geo.Creator ``` |
| [journal](#journal) | ``` timesheets.Employee = journal.EmployeeId ```  ``` timesheets.Creator = journal.EmployeeId ```  ``` timesheets.Employee = journal.Creator ```  ``` timesheets.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` timesheets.Employee = kiosks.Creator ```  ``` timesheets.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` timesheets.Employee = leave_accruals.Employee ```  ``` timesheets.Creator = leave_accruals.Employee ```  ``` timesheets.Employee = leave_accruals.Creator ```  ``` timesheets.Creator = leave_accruals.Creator ```  ``` timesheets.LeaveRule = leave_accruals.LeaveRule ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` timesheets.Employee = leave_pay_lines.Creator ```  ``` timesheets.Creator = leave_pay_lines.Creator ```  ``` timesheets.EmployeeAgreement = leave_pay_lines.EmployeeAgreement ```  ``` timesheets.LeaveId = leave_pay_lines.LeaveId ```  ``` timesheets.LeaveRule = leave_pay_lines.LeaveRule ```  ``` timesheets.Id = leave_pay_lines.TimesheetId ``` |
| [leave\_rules](#leave-rules) | ``` timesheets.Employee = leave_rules.Creator ```  ``` timesheets.Creator = leave_rules.Creator ```  ``` timesheets.LeaveRule = leave_rules.Id ``` |
| [leaves](#leaves) | ``` timesheets.Employee = leaves.Employee ```  ``` timesheets.Creator = leaves.Employee ```  ``` timesheets.Employee = leaves.Creator ```  ``` timesheets.Creator = leaves.Creator ```  ``` timesheets.EmployeeHistory = leaves.EmployeeHistory ```  ``` timesheets.LeaveId = leaves.Id ``` |
| [memos](#memos) | ``` timesheets.Employee = memos.Creator ```  ``` timesheets.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` timesheets.Employee = operational_units.Creator ```  ``` timesheets.Creator = operational_units.Creator ```  ``` timesheets.OperationalUnit = operational_units.Id ```  ``` timesheets.OperationalUnit = operational_units.ParentOperationalUnit ``` |
| [pay\_periods](#pay-periods) | ``` timesheets.Employee = pay_periods.Creator ```  ``` timesheets.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` timesheets.Employee = pay_rules.Creator ```  ``` timesheets.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` timesheets.Employee = public_holidays.Creator ```  ``` timesheets.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` timesheets.Employee = roster_opens.Employee ```  ``` timesheets.Creator = roster_opens.Employee ```  ``` timesheets.Employee = roster_opens.Creator ```  ``` timesheets.Creator = roster_opens.Creator ```  ``` timesheets.Roster = roster_opens.Roster ``` |
| [roster\_swaps](#roster-swaps) | ``` timesheets.Employee = roster_swaps.Employee ```  ``` timesheets.Creator = roster_swaps.Employee ```  ``` timesheets.Employee = roster_swaps.Creator ```  ``` timesheets.Creator = roster_swaps.Creator ```  ``` timesheets.Roster = roster_swaps.SourceRoster ```  ``` timesheets.Roster = roster_swaps.TargetRoster ``` |
| [rosters](#rosters) | ``` timesheets.Employee = rosters.Employee ```  ``` timesheets.Creator = rosters.Employee ```  ``` timesheets.Employee = rosters.ConfirmBy ```  ``` timesheets.Creator = rosters.ConfirmBy ```  ``` timesheets.Employee = rosters.Creator ```  ``` timesheets.Creator = rosters.Creator ```  ``` timesheets.OperationalUnit = rosters.OperationalUnit ```  ``` timesheets.Roster = rosters.Id ```  ``` timesheets.Id = rosters.MatchedByTimesheet ``` |
| [sales\_data](#sales-data) | ``` timesheets.Employee = sales_data.Employee ```  ``` timesheets.Creator = sales_data.Employee ```  ``` timesheets.Employee = sales_data.Creator ```  ``` timesheets.Creator = sales_data.Creator ```  ``` timesheets.OperationalUnit = sales_data.OperationalUnit ``` |
| [schedules](#schedules) | ``` timesheets.Employee = schedules.Creator ```  ``` timesheets.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` timesheets.Employee = sms_logs.Creator ```  ``` timesheets.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` timesheets.Employee = states.Creator ```  ``` timesheets.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` timesheets.Employee = stress_profiles.Creator ```  ``` timesheets.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` timesheets.Employee = system_usage_balances.Creator ```  ``` timesheets.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` timesheets.Employee = system_usage_tracking.Creator ```  ``` timesheets.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` timesheets.Employee = task_group_setups.Creator ```  ``` timesheets.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` timesheets.Employee = task_groups.Creator ```  ``` timesheets.Creator = task_groups.Creator ```  ``` timesheets.OperationalUnit = task_groups.OpUnitId ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` timesheets.Employee = task_opunit_configs.Creator ```  ``` timesheets.Creator = task_opunit_configs.Creator ```  ``` timesheets.OperationalUnit = task_opunit_configs.OpUnitId ``` |
| [task\_setups](#task-setups) | ``` timesheets.Employee = task_setups.Creator ```  ``` timesheets.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` timesheets.Employee = tasks.Creator ```  ``` timesheets.Creator = tasks.Creator ```  ``` timesheets.OperationalUnit = tasks.OpUnitId ``` |
| [teams](#teams) | ``` timesheets.Employee = teams.LeaderEmployee ```  ``` timesheets.Creator = teams.LeaderEmployee ```  ``` timesheets.Employee = teams.Creator ```  ``` timesheets.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` timesheets.Employee = timesheet_pay_returns.Creator ```  ``` timesheets.Creator = timesheet_pay_returns.Creator ```  ``` timesheets.Id = timesheet_pay_returns.Timesheet ``` |
| [training\_modules](#training-modules) | ``` timesheets.Employee = training_modules.Creator ```  ``` timesheets.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` timesheets.Employee = training_records.Employee ```  ``` timesheets.Creator = training_records.Employee ```  ``` timesheets.Employee = training_records.Creator ```  ``` timesheets.Creator = training_records.Creator ``` |
| [webhooks](#webhooks) | ``` timesheets.Employee = webhooks.Creator ```  ``` timesheets.Creator = webhooks.Creator ``` |

timesheets table schema

|  |
| --- |
| **AutoPayRuleApproved**  BOOLEAN |
| **AutoProcessed**  BOOLEAN |
| **AutoRounded**  BOOLEAN |
| **AutoTimeApproved**  BOOLEAN |
| **Cost**  NUMBER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **CustomFieldData**  INTEGER |
| **Date**  DATE |
| **Disputed**  BOOLEAN |
| **Employee**  INTEGER |
| **EmployeeAgreement**  INTEGER |
| **EmployeeComment**  STRING |
| **EmployeeHistory**  INTEGER |
| **EndTime**  INTEGER |
| **Exported**  BOOLEAN |
| **File**  INTEGER |
| **Id**  INTEGER |
| **InvoiceComment**  STRING |
| **Invoiced**  BOOLEAN |
| **IsInProgress**  BOOLEAN |
| **IsLeave**  BOOLEAN |
| **LeaveId**  INTEGER |
| **LeaveRule**  INTEGER |
| **Mealbreak**  TIME |
| **MealbreakSlots**  STRING |
| **Modified**  DATE-TIME |
| **OperationalUnit**  INTEGER |
| **PayRuleApproved**  BOOLEAN |
| **PayStaged**  BOOLEAN |
| **PaycycleId**  INTEGER |
| **RealTime**  BOOLEAN |
| **Roster**  INTEGER |
| **StagingId**  INTEGER |
| **StartTime**  INTEGER |
| **Supervisor**  INTEGER |
| **SupervisorComment**  STRING |
| **TotalTime**  NUMBER |
| **TotalTimeInv**  NUMBER |
| **ValidationFlag**  INTEGER |

### training\_modules

The `training_modules` table contains info about training modules.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/TrainingModule) |

training\_modules table foreign keys

| Join training\_modules with | on |
| --- | --- |
| [addresses](#addresses) | ``` training_modules.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` training_modules.Creator = categories.Creator ``` |
| [comments](#comments) | ``` training_modules.Creator = comments.Creator ``` |
| [companies](#companies) | ``` training_modules.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` training_modules.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` training_modules.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` training_modules.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` training_modules.Creator = custom_app_data.Employee ```  ``` training_modules.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` training_modules.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` training_modules.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` training_modules.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` training_modules.Creator = employee_agreements.EmployeeId ```  ``` training_modules.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` training_modules.Creator = employee_appraisal.Creator ```  ``` training_modules.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` training_modules.Creator = employee_availability.Employee ```  ``` training_modules.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` training_modules.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` training_modules.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` training_modules.Creator = employee_history.EmployeeId ```  ``` training_modules.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` training_modules.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` training_modules.Creator = employee_paycycles.EmployeeId ```  ``` training_modules.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` training_modules.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` training_modules.Creator = employee_salary_opunit_costing.Employee ```  ``` training_modules.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` training_modules.Creator = employee_workplaces.EmployeeId ```  ``` training_modules.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` training_modules.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` training_modules.Creator = events.Creator ``` |
| [geo](#geo) | ``` training_modules.Creator = geo.Creator ``` |
| [journal](#journal) | ``` training_modules.Creator = journal.EmployeeId ```  ``` training_modules.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` training_modules.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` training_modules.Creator = leave_accruals.Employee ```  ``` training_modules.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` training_modules.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` training_modules.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` training_modules.Creator = leaves.Employee ```  ``` training_modules.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` training_modules.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` training_modules.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` training_modules.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` training_modules.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` training_modules.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` training_modules.Creator = roster_opens.Employee ```  ``` training_modules.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` training_modules.Creator = roster_swaps.Employee ```  ``` training_modules.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` training_modules.Creator = rosters.Employee ```  ``` training_modules.Creator = rosters.ConfirmBy ```  ``` training_modules.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` training_modules.Creator = sales_data.Employee ```  ``` training_modules.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` training_modules.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` training_modules.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` training_modules.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` training_modules.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` training_modules.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` training_modules.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` training_modules.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` training_modules.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` training_modules.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` training_modules.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` training_modules.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` training_modules.Creator = teams.LeaderEmployee ```  ``` training_modules.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` training_modules.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` training_modules.Creator = timesheets.Employee ```  ``` training_modules.Creator = timesheets.Creator ``` |
| [training\_records](#training-records) | ``` training_modules.Creator = training_records.Employee ```  ``` training_modules.Creator = training_records.Creator ```  ``` training_modules.Id = training_records.Module ``` |
| [webhooks](#webhooks) | ``` training_modules.Creator = webhooks.Creator ``` |

training\_modules table schema

|  |
| --- |
| **Comment**  STRING |
| **Cost**  NUMBER |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Provider**  STRING |
| **ProviderAddress**  STRING |
| **RenewalPeriodMonths**  INTEGER |
| **TimeRequiredDays**  INTEGER |
| **Title**  STRING |

### training\_records

The `training_records` table contains info about training records.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/TrainingRecord) |

training\_records table foreign keys

| Join training\_records with | on |
| --- | --- |
| [addresses](#addresses) | ``` training_records.Employee = addresses.Creator ```  ``` training_records.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` training_records.Employee = categories.Creator ```  ``` training_records.Creator = categories.Creator ``` |
| [comments](#comments) | ``` training_records.Employee = comments.Creator ```  ``` training_records.Creator = comments.Creator ``` |
| [companies](#companies) | ``` training_records.Employee = companies.Creator ```  ``` training_records.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` training_records.Employee = company_periods.Creator ```  ``` training_records.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` training_records.Employee = contacts.Creator ```  ``` training_records.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` training_records.Employee = countries.Creator ```  ``` training_records.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` training_records.Employee = custom_app_data.Employee ```  ``` training_records.Creator = custom_app_data.Employee ```  ``` training_records.Employee = custom_app_data.Creator ```  ``` training_records.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` training_records.Employee = custom_field_data.Creator ```  ``` training_records.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` training_records.Employee = custom_fields.Creator ```  ``` training_records.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` training_records.Employee = employee_agreement_history.Creator ```  ``` training_records.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` training_records.Employee = employee_agreements.EmployeeId ```  ``` training_records.Creator = employee_agreements.EmployeeId ```  ``` training_records.Employee = employee_agreements.Creator ```  ``` training_records.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` training_records.Employee = employee_appraisal.Creator ```  ``` training_records.Creator = employee_appraisal.Creator ```  ``` training_records.Employee = employee_appraisal.Employee ```  ``` training_records.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` training_records.Employee = employee_availability.Employee ```  ``` training_records.Creator = employee_availability.Employee ```  ``` training_records.Employee = employee_availability.Creator ```  ``` training_records.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` training_records.Employee = employee_contract_leave_rules.Creator ```  ``` training_records.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` training_records.Employee = employee_contracts.Creator ```  ``` training_records.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` training_records.Employee = employee_history.EmployeeId ```  ``` training_records.Creator = employee_history.EmployeeId ```  ``` training_records.Employee = employee_history.Creator ```  ``` training_records.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` training_records.Employee = employee_paycycle_returns.Creator ```  ``` training_records.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` training_records.Employee = employee_paycycles.EmployeeId ```  ``` training_records.Creator = employee_paycycles.EmployeeId ```  ``` training_records.Employee = employee_paycycles.Creator ```  ``` training_records.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` training_records.Employee = employee_roles.Creator ```  ``` training_records.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` training_records.Employee = employee_salary_opunit_costing.Employee ```  ``` training_records.Creator = employee_salary_opunit_costing.Employee ```  ``` training_records.Employee = employee_salary_opunit_costing.Creator ```  ``` training_records.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` training_records.Employee = employee_workplaces.EmployeeId ```  ``` training_records.Creator = employee_workplaces.EmployeeId ```  ``` training_records.Employee = employee_workplaces.Creator ```  ``` training_records.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` training_records.Employee = employment_conditions.Creator ```  ``` training_records.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` training_records.Employee = events.Creator ```  ``` training_records.Creator = events.Creator ``` |
| [geo](#geo) | ``` training_records.Employee = geo.Creator ```  ``` training_records.Creator = geo.Creator ``` |
| [journal](#journal) | ``` training_records.Employee = journal.EmployeeId ```  ``` training_records.Creator = journal.EmployeeId ```  ``` training_records.Employee = journal.Creator ```  ``` training_records.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` training_records.Employee = kiosks.Creator ```  ``` training_records.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` training_records.Employee = leave_accruals.Employee ```  ``` training_records.Creator = leave_accruals.Employee ```  ``` training_records.Employee = leave_accruals.Creator ```  ``` training_records.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` training_records.Employee = leave_pay_lines.Creator ```  ``` training_records.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` training_records.Employee = leave_rules.Creator ```  ``` training_records.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` training_records.Employee = leaves.Employee ```  ``` training_records.Creator = leaves.Employee ```  ``` training_records.Employee = leaves.Creator ```  ``` training_records.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` training_records.Employee = memos.Creator ```  ``` training_records.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` training_records.Employee = operational_units.Creator ```  ``` training_records.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` training_records.Employee = pay_periods.Creator ```  ``` training_records.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` training_records.Employee = pay_rules.Creator ```  ``` training_records.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` training_records.Employee = public_holidays.Creator ```  ``` training_records.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` training_records.Employee = roster_opens.Employee ```  ``` training_records.Creator = roster_opens.Employee ```  ``` training_records.Employee = roster_opens.Creator ```  ``` training_records.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` training_records.Employee = roster_swaps.Employee ```  ``` training_records.Creator = roster_swaps.Employee ```  ``` training_records.Employee = roster_swaps.Creator ```  ``` training_records.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` training_records.Employee = rosters.Employee ```  ``` training_records.Creator = rosters.Employee ```  ``` training_records.Employee = rosters.ConfirmBy ```  ``` training_records.Creator = rosters.ConfirmBy ```  ``` training_records.Employee = rosters.Creator ```  ``` training_records.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` training_records.Employee = sales_data.Employee ```  ``` training_records.Creator = sales_data.Employee ```  ``` training_records.Employee = sales_data.Creator ```  ``` training_records.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` training_records.Employee = schedules.Creator ```  ``` training_records.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` training_records.Employee = sms_logs.Creator ```  ``` training_records.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` training_records.Employee = states.Creator ```  ``` training_records.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` training_records.Employee = stress_profiles.Creator ```  ``` training_records.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` training_records.Employee = system_usage_balances.Creator ```  ``` training_records.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` training_records.Employee = system_usage_tracking.Creator ```  ``` training_records.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` training_records.Employee = task_group_setups.Creator ```  ``` training_records.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` training_records.Employee = task_groups.Creator ```  ``` training_records.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` training_records.Employee = task_opunit_configs.Creator ```  ``` training_records.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` training_records.Employee = task_setups.Creator ```  ``` training_records.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` training_records.Employee = tasks.Creator ```  ``` training_records.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` training_records.Employee = teams.LeaderEmployee ```  ``` training_records.Creator = teams.LeaderEmployee ```  ``` training_records.Employee = teams.Creator ```  ``` training_records.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` training_records.Employee = timesheet_pay_returns.Creator ```  ``` training_records.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` training_records.Employee = timesheets.Employee ```  ``` training_records.Creator = timesheets.Employee ```  ``` training_records.Employee = timesheets.Creator ```  ``` training_records.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` training_records.Employee = training_modules.Creator ```  ``` training_records.Creator = training_modules.Creator ```  ``` training_records.Module = training_modules.Id ``` |
| [webhooks](#webhooks) | ``` training_records.Employee = webhooks.Creator ```  ``` training_records.Creator = webhooks.Creator ``` |

training\_records table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **Comment**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Employee**  INTEGER |
| **ExpiryDate**  DATE |
| **File**  STRING |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Module**  INTEGER |
| **TrainingDate**  DATE |

### webhooks

The `webhooks` table contains info about webhooks.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Modified |
| **Replication Key** | Modified |
| **Useful links** | [Deputy documentation](https://www.deputy.com/api-doc/Resources/Webhook) |

webhooks table foreign keys

| Join webhooks with | on |
| --- | --- |
| [addresses](#addresses) | ``` webhooks.Creator = addresses.Creator ``` |
| [categories](#categories) | ``` webhooks.Creator = categories.Creator ``` |
| [comments](#comments) | ``` webhooks.Creator = comments.Creator ``` |
| [companies](#companies) | ``` webhooks.Creator = companies.Creator ``` |
| [company\_periods](#company-periods) | ``` webhooks.Creator = company_periods.Creator ``` |
| [contacts](#contacts) | ``` webhooks.Creator = contacts.Creator ``` |
| [countries](#countries) | ``` webhooks.Creator = countries.Creator ``` |
| [custom\_app\_data](#custom-app-data) | ``` webhooks.Creator = custom_app_data.Employee ```  ``` webhooks.Creator = custom_app_data.Creator ``` |
| [custom\_field\_data](#custom-field-data) | ``` webhooks.Creator = custom_field_data.Creator ``` |
| [custom\_fields](#custom-fields) | ``` webhooks.Creator = custom_fields.Creator ``` |
| [employee\_agreement\_history](#employee-agreement-history) | ``` webhooks.Creator = employee_agreement_history.Creator ``` |
| [employee\_agreements](#employee-agreements) | ``` webhooks.Creator = employee_agreements.EmployeeId ```  ``` webhooks.Creator = employee_agreements.Creator ``` |
| [employee\_appraisal](#employee-appraisal) | ``` webhooks.Creator = employee_appraisal.Creator ```  ``` webhooks.Creator = employee_appraisal.Employee ``` |
| [employee\_availability](#employee-availability) | ``` webhooks.Creator = employee_availability.Employee ```  ``` webhooks.Creator = employee_availability.Creator ``` |
| [employee\_contract\_leave\_rules](#employee-contract-leave-rules) | ``` webhooks.Creator = employee_contract_leave_rules.Creator ``` |
| [employee\_contracts](#employee-contracts) | ``` webhooks.Creator = employee_contracts.Creator ``` |
| [employee\_history](#employee-history) | ``` webhooks.Creator = employee_history.EmployeeId ```  ``` webhooks.Creator = employee_history.Creator ``` |
| [employee\_paycycle\_returns](#employee-paycycle-returns) | ``` webhooks.Creator = employee_paycycle_returns.Creator ``` |
| [employee\_paycycles](#employee-paycycles) | ``` webhooks.Creator = employee_paycycles.EmployeeId ```  ``` webhooks.Creator = employee_paycycles.Creator ``` |
| [employee\_roles](#employee-roles) | ``` webhooks.Creator = employee_roles.Creator ``` |
| [employee\_salary\_opunit\_costing](#employee-salary-opunit-costing) | ``` webhooks.Creator = employee_salary_opunit_costing.Employee ```  ``` webhooks.Creator = employee_salary_opunit_costing.Creator ``` |
| [employee\_workplaces](#employee-workplaces) | ``` webhooks.Creator = employee_workplaces.EmployeeId ```  ``` webhooks.Creator = employee_workplaces.Creator ``` |
| [employment\_conditions](#employment-conditions) | ``` webhooks.Creator = employment_conditions.Creator ``` |
| [events](#events) | ``` webhooks.Creator = events.Creator ``` |
| [geo](#geo) | ``` webhooks.Creator = geo.Creator ``` |
| [journal](#journal) | ``` webhooks.Creator = journal.EmployeeId ```  ``` webhooks.Creator = journal.Creator ``` |
| [kiosks](#kiosks) | ``` webhooks.Creator = kiosks.Creator ``` |
| [leave\_accruals](#leave-accruals) | ``` webhooks.Creator = leave_accruals.Employee ```  ``` webhooks.Creator = leave_accruals.Creator ``` |
| [leave\_pay\_lines](#leave-pay-lines) | ``` webhooks.Creator = leave_pay_lines.Creator ``` |
| [leave\_rules](#leave-rules) | ``` webhooks.Creator = leave_rules.Creator ``` |
| [leaves](#leaves) | ``` webhooks.Creator = leaves.Employee ```  ``` webhooks.Creator = leaves.Creator ``` |
| [memos](#memos) | ``` webhooks.Creator = memos.Creator ``` |
| [operational\_units](#operational-units) | ``` webhooks.Creator = operational_units.Creator ``` |
| [pay\_periods](#pay-periods) | ``` webhooks.Creator = pay_periods.Creator ``` |
| [pay\_rules](#pay-rules) | ``` webhooks.Creator = pay_rules.Creator ``` |
| [public\_holidays](#public-holidays) | ``` webhooks.Creator = public_holidays.Creator ``` |
| [roster\_opens](#roster-opens) | ``` webhooks.Creator = roster_opens.Employee ```  ``` webhooks.Creator = roster_opens.Creator ``` |
| [roster\_swaps](#roster-swaps) | ``` webhooks.Creator = roster_swaps.Employee ```  ``` webhooks.Creator = roster_swaps.Creator ``` |
| [rosters](#rosters) | ``` webhooks.Creator = rosters.Employee ```  ``` webhooks.Creator = rosters.ConfirmBy ```  ``` webhooks.Creator = rosters.Creator ``` |
| [sales\_data](#sales-data) | ``` webhooks.Creator = sales_data.Employee ```  ``` webhooks.Creator = sales_data.Creator ``` |
| [schedules](#schedules) | ``` webhooks.Creator = schedules.Creator ``` |
| [sms\_logs](#sms-logs) | ``` webhooks.Creator = sms_logs.Creator ``` |
| [states](#states) | ``` webhooks.Creator = states.Creator ``` |
| [stress\_profiles](#stress-profiles) | ``` webhooks.Creator = stress_profiles.Creator ``` |
| [system\_usage\_balances](#system-usage-balances) | ``` webhooks.Creator = system_usage_balances.Creator ``` |
| [system\_usage\_tracking](#system-usage-tracking) | ``` webhooks.Creator = system_usage_tracking.Creator ``` |
| [task\_group\_setups](#task-group-setups) | ``` webhooks.Creator = task_group_setups.Creator ``` |
| [task\_groups](#task-groups) | ``` webhooks.Creator = task_groups.Creator ``` |
| [task\_opunit\_configs](#task-opunit-configs) | ``` webhooks.Creator = task_opunit_configs.Creator ``` |
| [task\_setups](#task-setups) | ``` webhooks.Creator = task_setups.Creator ``` |
| [tasks](#tasks) | ``` webhooks.Creator = tasks.Creator ``` |
| [teams](#teams) | ``` webhooks.Creator = teams.LeaderEmployee ```  ``` webhooks.Creator = teams.Creator ``` |
| [timesheet\_pay\_returns](#timesheet-pay-returns) | ``` webhooks.Creator = timesheet_pay_returns.Creator ``` |
| [timesheets](#timesheets) | ``` webhooks.Creator = timesheets.Employee ```  ``` webhooks.Creator = timesheets.Creator ``` |
| [training\_modules](#training-modules) | ``` webhooks.Creator = training_modules.Creator ``` |
| [training\_records](#training-records) | ``` webhooks.Creator = training_records.Employee ```  ``` webhooks.Creator = training_records.Creator ``` |

webhooks table schema

|  |
| --- |
| **Address**  STRING |
| **Created**  DATE-TIME |
| **Creator**  INTEGER |
| **Enabled**  BOOLEAN |
| **Filters**  STRING |
| **Headers**  STRING |
| **Id**  INTEGER |
| **Modified**  DATE-TIME |
| **Topic**  STRING |
| **Type**  STRING |
