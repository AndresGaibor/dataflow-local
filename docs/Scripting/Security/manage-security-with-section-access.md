---
title: "Managing data security with Section Access"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data"]
---
# Managing data security with Section Access

Section Access is used to control the security of an application. It is basically a part of the data load script where you add a security table to define who gets to see what.  Qlik Cloud uses this information to reduce data to the appropriate scope when the user opens the application, that is, some of the data in the application is hidden from the user based on their identity. Section Access is tightly integrated with the data in the application and relies upon it to control access. This form of dynamic data reduction can target table rows, columns, or a combination of both. For more information, see [Trust and Security at Qlik](https://www.qlik.com/us/trust).

## Sections in the load script

Data access control is managed through one or more
security tables loaded in the same way that data is normally loaded.
This makes it possible to store these tables in a standard database or in a spreadsheet. The script
statements managing the security tables are given within an authorization section,
which in the script is initiated by the statement Section Access.

> **Note:** All the field names and field values listed in Section Access are always converted to uppercase. As a result, all fields that are part of a data reduction must be converted to upper case to match what is stated in the Section Access statement, even if they are located outside the Section Access Statement. You can convert any field name containing lowercase letters in the database to uppercase using the Upper function before reading the field by the LOAD or **SELECT** statement.
>
> For more information, see [*Upper Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Upper.htm).

If an authorization section is defined in the script,
the part of the script loading the application data must be put in a different
section, initiated by the statement Section
Application.

Example:

Section Access;
Load \* INLINE [
ACCESS, USER.EMAIL, REDUCTION
USER, USER1@EXAMPLE.COM, \*
USER, USER2@EXAMPLE.COM, 1
USER, USER3@EXAMPLE.COM, 2
ADMIN, USER4@EXAMPLE.COM,
];
Section Application;
T1:
Load \*,
NUM AS REDUCTION;
LOAD
Chr(RecNo()+ord('A')-1) AS ALPHA,
RecNo() AS NUM
AUTOGENERATE 3;

Note that after making changes to the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm#glossary-1 "Glossary term"), you must always reload the data for the changes to take effect.

### Section Access system fields

The access levels are assigned to users in one or more security tables loaded within the Section Access part of the script. These tables must contain, as a minimum, two system fields: ACCESS, which is the [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm#glossary-2 "Glossary term") defining the access level, and USERID or USER.EMAIL . Other optional system fields can be added depending on the use case. The full set of Section Access system fields is described below.

#### ACCESS

Defines what access the corresponding user should have.

Access to Qlik Sense applications can be authorized for specified users. In the security table, users can be assigned to the access levels ADMIN or USER. A user with ADMIN privileges has access to all data in the application unless limited by the security table. A user with USER privileges can only access data as defined in the security table. If no valid access level is assigned, the user cannot open the application.

#### USERID

Contains a string corresponding to a Qlik Cloud user name.
Qlik Cloud will get the login information from the IdP subject and compare it to the value in this field. For an alternate way to verify user identity using email address, see [*USER.EMAIL*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm#Email). For multi-cloud environments, the IdP subject can be mapped against your internal Windows identity. When using Qlik Account, the subject cannot be mapped against internal Windows identity. User IdP subject can be viewed in the **Manage users** section of the Administration activity center.

A wildcard character (\*) is interpreted as all users, subject to further conditions specified in the security table. For example, in the following security table, users who are in the Qlik Sense Tenant Admins can see all listed REDUCTION values.

Section Access;
LOAD \* INLINE [
ACCESS, USERID, GROUP, REDUCTION
ADMIN, \*, Qlik SENSE TENANT ADMINS, \*
USER, QLIK-POC\SOMEOTHERUSER1, \*, 1
USER, QLIK-POC\SOMEOTHERUSER2, \*, 2
...
];

> **Note:** 
> USERID and the NTNAME both use the same authentication information, so it is not necessary to check both on the same row in the security table. The difference between the two fields is that NTNAME checks groups also.

#### NTNAME

> **Note:** NTNAME is a legacy QlikView field and it is recommended to use USERID if QlikView is not using the same security table.

A field that should contain a string corresponding to the NetBIOS version of a Windows NT Domain user name or group name. If a different authentication system is used, it should contain the name of an authenticated user.

Qlik Cloud will fetch the logon information from the subject claim of the identity provider and compare it to the value in this field.

#### USER.EMAIL

Contains a string corresponding to a user email address. Qlik Cloud will get this information from the identity provider and compare it to the value in this field.

#### GROUP

Contains a string corresponding to a group in Qlik Cloud. Qlik Cloud will get the information from the “groups” claim of the identity provider or custom groups and compare it to the value in this field. Whether IdP groups, custom groups, or a combination of both are used is controlled by the system variable `QlikCloudGroupMode`. For more information, see [*Defining IdP or custom groups for GROUP*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm#Selectin).

> **Note:** This functionality is not available in Qlik Sense Business, Qlik Cloud Analytics Standard, or when using Qlik Identity Provider (IdP).

#### OMIT

Contains the name of the field that is to be omitted for this specific user. Wildcards may be used and the field may be empty.

> **Note:** It is recommended that you do not apply OMIT on key fields. Key fields that are omitted are visible in the data model viewer, but the content is not available, which can be confusing for a user. Additionally, applying OMIT on fields that are used in a [visualization](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm#glossary-3 "Glossary term") can result in an incomplete visualization for users that do not have access to the omitted fields.

## Managing user access to an application

A user with USERID AD\_DOMAIN\C would not be able to open the application at all because that user ID is not listed in the security table.

Section access, in its simplest form, can be used to restrict specific users from accessing an application. Users are denied access to an application through exclusion. In other words, if a specific user email address is not listed in the security table, they will not be able to access the application. The only exception to this rule is if a wildcard (\*) is assigned to the USER.EMAIL field in one of the rows in the security table. A wildcard, in this case, means that all authenticated users can access the application. Here is an example of a security table with a list of user IDs:

Section Access;
LOAD \* inline [
ACCESS, USER.EMAIL
ADMIN, USER1@EXAMPLE.COM
USER, USER2@EXAMPLE.COM
USER, USER3@EXAMPLE.COM
];
Section Application;

A user with USER.EMAIL USER4@example.com would not be able to open the application at all because that user email address is not listed in the security table.

## Managing user access to specific data in an application

Dynamic data reduction limits access to rows and columns in the data tables within Qlik Sense applications after a user has been authorized to access the application itself.

### Managing access to row-level data

Restrict access to row-level data by adding a data reduction column to the security table in the access section of the load script. Specific records (rows) can be hidden from users by linking the Section Access data with the real data. The selection of data to be shown or excluded is controlled by having one or more reduction fields with common names in Section Access and Section Application parts of the script. After user login, Qlik Sense matches the selections in reduction fields in the access section to any fields in the application section with exactly the same field names (the field names must be written in uppercase). After the selections have been made, Qlik Sense permanently hides all data excluded by these selections from the user. If a wildcard (\*) is used as a field value in the data reduction column, it is interpreted as allowing the user to access records associated with all selected reduction fields in the security table.

When Qlik Sense is comparing the reduction field in Section Access to fields in the data model, the following behaviors are expected:

- If a field value in the data model matches the reduction field in Section Access, the application will open showing data associated with the match for the specified user. Other data will be hidden.
- If the reducing field value does not match any of the values in the data model, the application will not open for a normal USER. It will, however, open unreduced for a user marked as ADMIN.

Using several reducing fields in Section Access is not recommended, since it will allow other access combinations than the intended ones.

> **Note:** The wildcard character \* in the data reduction column refers only to all values in the security table. If there are values in Section Application that are not available in the reduction column of the security table, they will be reduced.

> **Note:** All field names used in the transfer described above and all field values in these fields must be uppercase because all field names and field values are, by default, converted to uppercase in the access section.

Example: Row-level data reduction based on user identity

Section Access;
Authorization:
LOAD \* inline [
ACCESS, USER.EMAIL, REDUCTION
ADMIN, USER1@EXAMPLE.COM, \*
USER, USER2@EXAMPLE.COM, 1
USER, USER3@EXAMPLE.COM, 2
USER, USER4@EXAMPLE.COM, \*
];
Section Application;
T1:
LOAD \*,
NUM AS REDUCTION;
LOAD
RecNo() AS NUM
AUTOGENERATE 3;

In this example, the field REDUCTION (uppercase) now exists in both Section Access and Section Application (all field values are also uppercase). The two fields would normally be different and separated, but using Section Access, these fields are linked and the number of records displayed to the user is reduced.

The result will be:

- User USER1@EXAMPLE.COM can see all fields and only those records other users can see when REDUCTION = 1 or REDUCTION =2.
- User USER2@EXAMPLE.COM can see all fields, but only those records associated with REDUCTION=1.
- User USER3@EXAMPLE.COM can see all fields, but only those records associated with REDUCTION=2.
- User USER4@EXAMPLE.COM can see all fields and only those records other users can see when REDUCTION = 1 or REDUCTION =2.

### Managing access to column-level data

Restrict access to column-level data by adding the OMIT system field to the security table in the Section Access script. The following example builds on the previous example where row data reduction is already in place.

Example: Column data reduction based on user identity

Section Access;
LOAD \* inline [
ACCESS, USER.EMAIL, REDUCTION, OMIT
ADMIN, USER1@example.com, \*,
USER, USER2@example.com, 1,
USER, USER3@example.com, 2, NUM
USER, USER4@example.com, 3, ALPHA
];
Section Application;
T1:
LOAD \*,
NUM AS REDUCTION;
LOAD
Chr( RecNo()+ord('A')-1) AS ALPHA,
RecNo() AS NUM
AUTOGENERATE 3;

The field OMIT in Section Access defines the fields that should be hidden from the user.

The result will be:

- User USER1@example.com can see all fields and only those records other users can see in this example when REDUCTION is 1, 2, or 3.
- User USER2@example.com can see all fields, but only those records associated with REDUCTION=1.
- User USER3@example.com can see all fields except NUM, and only those records associated with REDUCTION=2.
- User USER4@example.com can see all fields except ALPHA, and only those records associated with REDUCTION=3.

> **Note:** Some visualizations have minimum data requirements that must be met in order to render. As a result, "Incomplete visualization" might be displayed when a column-level field is omitted from a user's data view.

### Managing access to user groups

Section Access offers you the option to limit the scope of data visible to users through group membership. To restrict your data using user groups, add the GROUP field name to the security table in the access section and define values for the GROUP field.

Example:  Data reduction based on user groups

Section Access;
LOAD \* inline [
ACCESS, USERID, GROUP, REDUCTION, OMIT
USER, \*, ADMIN, \*,
USER, \*, A, 1,
USER, \*, B, 2, NUM
USER, \*, C, 3, ALPHA
USER, \*, GROUP1, 3,
ADMIN, AD\_DOMAIN\DEV, \*, \*,
];
section application;
T1:
LOAD \*,
NUM AS REDUCTION;
LOAD
Chr( RecNo()+ord('A')-1) AS ALPHA,
RecNo() AS NUM
AUTOGENERATE 3;

The result will be:

- Users belonging to the ADMIN group are allowed to see all fields and only those records other users can see in this example when REDUCTION is 1, 2, or 3.
- Users belonging to the A group are allowed to see data associated with REDUCTION=1 across all fields.
- Users belonging to the B group are allowed to see data associated with REDUCTION=2, but not in the NUM field
- Users belonging to the C group are allowed to see data associated with REDUCTION=3, but not in the ALPHA field
- Users belonging to the GROUP1 group are allowed to see data associated with REDUCTION=3 across all fields
- The user AD\_DOMAIN\DEV is allowed to see all data in all fields.

Qlik Cloud compares the user with UserID and resolves the user against groups in the table. If the user belongs to a group that is allowed access, or the user matches, they can access the application.

#### Defining IdP or custom groups for GROUP

Section Access can use IdP groups, custom groups, or a combination of both groups.

By default, Section Access uses your IdP groups. You can choose which groups to use in your Section Access statement with the variable `QlikCloudGroupMode`. By setting `QlikCloudGroupMode` with the appropriate value before your Section Access statement, you can control what kind of groups are used with GROUP in the Section Access statement.

`QlikCloudGroupMode` values

| Value | Results |
| --- | --- |
| `0` | IdP groups |
| `1` | Custom groups |
| `2` | Both IdP and custom groups |

If you are using a combination of IdP and custom groups, IdP and custom groups that share a name will have the defined policies applied to members of both groups.

Example: Using custom groups

SET QlikCloudGroupMode = 1;
  
Section Access;
LOAD \* inline [
ACCESS, USERID, GROUP, REDUCTION, OMIT
USER, \*, ADMIN, \*,
USER, \*, A, 1,
USER, \*, B, 2, NUM
USER, \*, C, 3, ALPHA
USER, \*, GROUP1, 3,
];
section application;
T1:
LOAD \*,
NUM AS REDUCTION;
LOAD
Chr( RecNo()+ord('A')-1) AS ALPHA,
RecNo() AS NUM
AUTOGENERATE 3;

## Reloading data in Qlik Cloud

To reload an application without data reduction in Qlik Cloud, it is recommended to use the USER.EMAIL system field in the security table. The value for the USER.EMAIL field should be the email address of users who are able to edit and load the application. This applies to applications in both [shared](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm#glossary-4 "Glossary term") and [managed spaces](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm#glossary-5 "Glossary term"). For example:

Section Access;
LOAD \* inline [
ACCESS, USER.EMAIL, REDUCTION
ADMIN, TEST@EXAMPLE.COM, \*
];

In this example, the user with email address test@example.com is ADMIN and is able to reload the application.

If you are using groups, the following example would work equally for both Qlik Sense and Qlik Cloud:

Section Access;
LOAD \* inline [
ACCESS, GROUP, REDUCTION
ADMIN, DEVELOPERS, \*
];

You can also map the USERID in the security table to the subject claim of the Identity Provider, as shown in the following example. This configuration is suggested for migrating from Qlik Sense to Qlik Cloud and for multi-cloud environments. For more information about mapping the USERID to the subject claim, see [*Managing user access in a multi-cloud environment*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm#user_access)

Section Access;
LOAD \* inline [
ACCESS, USERID, REDUCTION
ADMIN, AD\_DOMAIN\DEV, \*
];

## Managing user access in a multi-cloud environment

A Qlik Sense multi-cloud environment involves a mix of user authentication mechanisms. Typically, with Qlik Sense Enterprise on Windows, the USERID in the Section Access security table is verified by the proxy service. In Qlik Cloud, an Identity Provider assumes that authentication role. Consequently, Section Access that is set up for an on-premises environment such as Qlik Sense Enterprise on Windows will not work in a cloud environment.

When using an OIDC or SAML identity provider (Qlik IdP or custom IdP) with Qlik Cloud, the subject claim is used to identify users when logging in.
With Section Access, the value of the USERID field in the security table is compared to the value of the subject claim. When you set up your [tenant](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm#glossary-6 "Glossary term"), make sure that the SAM account name is mapped to the subject claim of your identity provider. So, for example, if your SAM account name is AD\_DOMAIN\Dev, set the subject claim to AD\_DOMAIN\Dev. If you want to see the value of the subject claim of the IdP, append /api/v1/diagnose-claims to the tenant URL in the browser, for example, your-tenant.us.qlikcloud.com/api/v1/diagnose-claims. In the JSON response, the subject claim is called sub.

If you are unable to use the SAM account name, there is an alternate way to authenticate a user. Since e-mail addresses tend to remain the same in different environments, you can use the USER.EMAIL field instead of USERID in the security table. Here is an example of what the security table could look like:

| ACCESS | USERID | USER.EMAIL | Comment | COUNTRY |
| --- | --- | --- | --- | --- |
| USER | ABC\JOE | \* | Access-on-prem | United States |
| USER | \* | JOE.SMITH@EXAMPLE.COM | Access-in-cloud | United States |
| USER | ABC\URSULA | \* | Access-on-prem | Germany |
| USER | \* | URSULA.SCHULTZ@EXAMPLE.COM | Access-in-cloud | Germany |
| USER | ABC\STEFAN | \* | Access-on-prem | Sweden |
| USER | \* | STEFAN.SVENSSON@EXAMPLE.COM | Access-in-cloud | Sweden |

Authorization script:

Section Access;
LOAD \* INLINE [
ACCESS, USERID, USER.EMAIL, COUNTRY
USER, ABC\JOE, \*, UNITED STATES
USER, \*, JOE.SMITH@EXAMPLE.COM, UNITED STATES
USER, ABC\URSULA, \*, GERMANY
USER, \*, URSULA.SCHULTZ@EXAMPLE.COM, GERMANY
USER, ABC\STEFAN, \*, SWEDEN
USER, \*, STEFAN.SVENSSON@EXAMPLE.COM, SWEDEN
];

Note that each user has two records: One for on-premises access and one for cloud access. The wildcards ensure that only the relevant authenticating fields are used. In this example, COUNTRY is used as a data reduction field.

## QlikView authorizing fields

For backwards compatibility, Qlik Cloud recognizes the authorizing fields from QlikView. Although USERID is interpreted differently in QlikView and Qlik Cloud, it will in Qlik Cloud be interpreted the same way as in Qlik Sense: It will be matched against the name of the authenticated user.

#### PASSWORD, NTSID and NTDOMAINSID

If one of the fields PASSWORD, NTSID and NTDOMAINSID is used and it contains a relevant value, access to the document is denied. If the field contains a wildcard (\*), access might be granted, depending on the other fields in the authorization table.

#### SERIAL

If the field SERIAL is used and it contains a license number, the Section Access row will deny access to the document. If the field contains a wildcard (\*), access might be granted, depending on the other fields in the authorization table.

Further, in Qlik Cloud this field can also be used to define the environment. This means that if the field contains the string ‘QLIKCLOUD’, access might be granted, depending on the other fields in the authorization table.

## Mixed environments

If you plan to use the same security table in both QlikView and Qlik Cloud, be aware that:

• USERID has different meanings in QlikView and Qlik Cloud, and could, if used, cause security problems. Use NTNAME instead or combine it with SERIAL as described below.

• GROUP and fields beginning with ‘USER.’, such as 'USER.NAME' and 'USER.EMAIL', are (or will be) authorizing fields in Qlik Cloud. If you use these fields in your Section Access, access might be denied in Qlik Cloud.

• PASSWORD, NTSID and NTDOMAINSID cannot be used in Qlik Cloud. Access will be denied, unless a wildcard is used.

• SERIAL cannot be used to check license number in Qlik Cloud. However, if this field contains the string ‘QLIKCLOUD’, access might be granted. This means that it is possible to have a security table like the following, where line 1 will grant access in QlikView (but not in Qlik Cloud), and line 2 will grant access in Qlik Cloud (but not in QlikView).

Security table

| Line | SERIAL | USERID | Comment |
| --- | --- | --- | --- |
| 1 | 4600 0123 4567 8901 | \* | Grants access to correct license number in QlikView. |
| 2 | QLIKCLOUD | JOHN DOE | Grants access to correct user in Qlik Cloud. |

Authorization script:

Section Access;
LOAD \* INLINE [
ACCESS, USERID, SERIAL
USER, \*, 4600 0123 4567 8901
USER, JOHN DOE, QLIKCLOUD
];

## Using Section Access and Insight Advisor Chat

Applications using Section Access use an index user to determine how much information Insight Advisor Chat retrieves from the application. The index user should be the user with the highest level of access for the application in the Section Access script. Data provided to end users, however, is still controlled by the section access limitations.

For a visual demo of how to use section access and Insight Advisor Chat, see:

[Using Section Access and Insight Advisor Chat](https://share.vidyard.com/watch/8Xg1Eq9SyWYjQeTABijo1M)

> **Warning:** If you have sensitive information in application names, field names, or master item names, these may be exposed by making applications using Section Access available for Insight Advisor Chat. Application suggestions for queries include applications in spaces to which users have access. These may include applications to which users do not have access in an application's Section Access. Selecting these applications will do nothing, however. When clicking **Dimensions** or **Measures** to view the available items from an application using Section Access, users may see items to which they do not have access. Clicking on these items will not provide any data to the users, however.

By default, the application owner is the index user. You can change the index user in **Details**.

Do the following:

1. In Qlik Cloud, navigate to the application.
2. Click ![More](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select **Details**.
3. Under **Index user**, select the index user.
4. Click **Back**.
5. Click ![More](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select **Reload**.

## Using Section Access and Qlik Answers

Applications using Section Access use an index user to determine how much information Qlik Answers retrieves from the application.

Configure the indexing user with the broadest data access available, ideally a dedicated service account with ADMIN or ALL access in Section Access. This ensures that the index captures the full dataset and that individual user permissions are applied at query time. Data shown to end users is still controlled by the section access limitations.

### Indexing and section access

The indexing user determines the scope of the index. When Qlik Answers indexes a Section Access application, it builds the index based on what the indexing user can access. This means the indexing user's data permissions set the upper limit of what the index contains. Data the indexing user cannot see will not be indexed.

If the indexing user has full access, the index captures all application data. Section Access rules are still enforced at query time. The two layers are independent, so each user only receives results they are permitted to see.

If the indexing user has restricted access, the index will only contain data within that restriction. Users with broader permissions will still be limited to the data captured in the index, even if their Section Access rules would normally allow them to see more.

> **Note:** Incomplete indexing due to a restricted indexing user does not produce errors. Affected users will receive answers based on the reduced index without any indication that data is missing.

Example:

An application has two user types:

- Global users: Users with full data access.
- EMEA users: Users with only EMEA data access.

If the indexing user is an EMEA user, the index will only contain EMEA data. Global users querying through Qlik Answers will receive EMEA-scoped answers, even though their Section Access rules grant broader access.

If the indexing user has full access, the index contains all data. EMEA users querying through Qlik Answers will still receive only EMEA-scoped answers, because Section Access rules are applied at query time.

### Setting the index user

By default, the application owner is the index user. In managed spaces, the default index user is the space owner. You can change the index user in **Section access settings**.

Do the following:

1. In Qlik Cloud, navigate to the application.
2. Click ![More](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select **Manage** > **Section access settings**.

   > **Note:** Alternatively, in an open application, open the details area and click ![More](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > **Manage** > **Section access settings**.
3. Under **Index user**, select the index user.
4. Click **Save**.

## Using QVDs with Section Access

QVD files can be read as a regular load or as an optimized load. An optimized load is when no data transformations are made during loading and there are no filters in a WHERE clause.

Optimized loads do not work when using QVDs with Section Access. If you want to use a QVD file to load data into Section Access, you must expand the QVD file. The easiest way to expand the QVD file is to make a formatting change when loading the data.

In the following example, the QVD file is not expanded as no formatting is done to the data.

Example: Non-working example with no data formatting (optimized load)

section access;
LOAD
ACCESS,
USERID,
PASSWORD,
[GROUP]
FROM SAccess.qvd (qvd);

Instead, you can for example use the upper() function to format the data which will expand the QVD file.

Example: Working example with data formatting

section access;
LOAD
ACCESS,
USERID,
PASSWORD,
upper([GROUP]) as [GROUP]
FROM SAccess.qvd (qvd);

You can also add a Where 1=1 statement to the LOAD statement.

Example: Another working example with data formatting

section access;
LOAD
ACCESS,
USERID,
PASSWORD,
[GROUP]
FROM SAccess.qvd (qvd) where 1=1;

## Guidelines and tips for using Section Access

Here are some important facts and helpful hints to know about Section Access.

- All the field names and field values listed in Section Access are always converted to uppercase. As a result, all fields that are part of a data reduction must be converted to upper case to match what is stated in the Section Access statement, even if they are located outside the Section Access Statement. You can convert any field name containing lowercase letters in the database to uppercase using the Upper function before reading the field by the LOAD or **SELECT** statement.

  For more information, see [*Upper Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Upper.htm).
- You cannot use the Section Access system field names listed as field names in your data model.
- If you add, modify, or remove Section Access controls in application, different steps are required in order to apply the changes, depending on the space type of the application:
  - Personal and shared spaces: To apply the changed Section Access controls, reload the application.
  - Managed spaces: To apply the changed Section Access controls in the published copy of the application, do either of the following depending on your use case:

    - Reload the source application, and then republish the source application to the managed space with data.
    - Republish the source application without data and then reload the application.
- A snapshot shows data according to the access rights of the user who takes the snapshot, and the snapshot can then be shared in a story. However, when users return to a visualization from a story to see the live data in the application, they are restricted by their own access rights.
- Do not assign colors to master dimension values if you use section access or work with sensitive data, because the values might be exposed by the color configuration.
- To avoid exposing restricted data, remove all attached files with section access settings before publishing the application. Attached files are included when the application is published. If the published application is copied, the attached files are included in the copy. However, if section access restrictions have been applied to the attached data files, the section access settings are not retained when the files are copied, so users of the copied application will be able to see all the data in the attached files.
- A wildcard (\*) is interpreted as all (listed) values of the field in the table. If used in one of the system fields (USERID, GROUP) in a table loaded in the access section of the script, it is interpreted as all (also not listed) possible values of this field.
- Security fields can be put in different tables.
- When loading data from a QVD file, the Upper function slows down the loading speed.
