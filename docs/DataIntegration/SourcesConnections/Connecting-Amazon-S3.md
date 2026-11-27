---
title: "Amazon S3"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Connecting-Amazon-S3.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to cloud storage"]
---

# Amazon S3

Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To connect to Amazon S3, you need permissions in AWS Identity Access Management (IAM) that allow you to create policies, create roles, and attach policies to roles. This is required to grant the authorization to your S3 bucket:

- [Creating an IAM policy](#Creating).
- [Creating an IAM Role](#Creating2).

### Creating an IAM policy

[An IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json) is JSON-based access policy language to manage permissions to bucket resources.

Amazon S3 permissions

| Permission name | Operation | Description |
| --- | --- | --- |
| **s3:GetObject** | **[GET Object](http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html)** | Allows for the retrieval of objects from Amazon S3. |
| **s3:GetObject** | **[HEAD Object](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectHEAD.html)** | Allows for the retrieval of metadata from an object without returning the object itself. |
| **s3:ListBucket** | **[GET Bucket (List Objects)](http://docs.aws.amazon.com/AmazonS3/latest/API/v2-RESTBucketGET.html)** | Allows for the return of some or all (up to 1,000) of the objects in a bucket. |
| **s3:ListBucket** | **[HEAD Bucket](http://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketHEAD.html)** | Used to determine if a bucket exists and access is allowed. |

To create the IAM policy:

1. In AWS, [navigate to the IAM service](https://console.aws.amazon.com/iam/home#/home) by clicking the **Services** menu and typing IAM.
2. Click IAM once it displays in the results.
3. Click Policies in the menu on the left side of the page.
4. Click Create Policy.
5. In the Create Policy page, click the JSON tab.
6. Select everything currently in the text field and delete it.
7. In the text field, paste the following JSON and replace MyBucketName by the name of your bucket:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "",
               "Effect": "Allow",
               "Action": [
               "s3:GetObject",
               "s3:ListBucket"
               ],
               "Resource": [
               "arn:aws:s3:::MyBucketName",
               "arn:aws:s3:::MyBucketName/*"
               ]
           }
       ]
   }
   ```
8. Click Review policy.
9. On the Review Policy page, give the policy a name. For example: `qlik_amazon_s3`.
10. Click Create policy.

### Creating an IAM role

Information note

To complete this step, you need the following AWS IAM permissions: `CreateRole` and `AttachRolePolicy`. Refer to [Amazon’s documentation](https://docs.aws.amazon.com/IAM/latest/APIReference/API_Operations.html) for more info.

If you are creating multiple Amazon S3 integrations, you need to complete this step for each integration you are connecting.

1. In AWS, navigate to the [IAM Roles](https://console.aws.amazon.com/iam/home#/roles) page.
2. Click Create Role.
3. On the Create Role page:
   1. In the Select type of trusted entity section, click the Another AWS account option.
   2. In the Account ID field, paste `338144066592`.
   3. In the Options section, select the Require external ID checkbox.
   4. In the External ID field that displays, paste `qlik_connection_<tenant-id>` and replace <tenant-id> by your tenant ID.

      To find your tenant ID, see [Finding tenant information](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/qcs-account-information.htm).
   5. Click Next: Permissions.
4. On the Attach permissions page:
   1. Search for the policy you created in the [Creating an IAM policy](#Creating).
   2. Once located, check the box next to it in the table.
   3. Click Next: Tags.
5. If you want to enter any tags, do so on the Add tags page. Otherwise, click Next: Review.
6. On the Review page:
   1. In the Role name field, paste `qlik_s3_<tenant-id>` and replace <tenant-id> by your tenant ID.

      To find your tenant ID, see [Finding tenant information](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/qcs-account-information.htm).
   2. Enter a description in the Role description field. For example: `Qlik role for Amazon S3 integration.`
   3. Click Create role.

### Defining the search pattern

The Search Pattern field defines the search criteria Qlik should use for selecting and replicating files. This field accepts regular expressions, which can be used to include a single file or multiple files.

When creating a search pattern, keep the following in mind:

- When including multiple files for a single table, each file should have the same header row values.
- Special characters such as periods (`.`) have special meaning in regular expressions. To match exactly, they will need to be escaped. For example: `.\`
- Qlik uses Python for regular expressions, which may vary in syntax from other varieties. Try using [PyRegex](http://www.pyregex.com/) to test your expressions before saving the integration.
- Parquet (`.parquet`) and Arvo (`.arvo`) search patterns are also supported.
- Search patterns should account for how data in files is updated. Consider these examples:

|  |  |  |
| --- | --- | --- |
| **Scenario** | Single file, periodically updated | Multiple files, generated daily |
| **How updates are made** | A single JSONL file is periodically updated with new and updated customer data. | A new CSV file is created every day that contains new and updated customer data. Old files are never updated after they're created. |
| **File name** | `customers.jsonl` | `customers-[STRING].csv`, where `[STRING]` is a unique, random string |
| **Search pattern** | Because there will only ever be one file, you could enter the exact name of the file in your S3 bucket:   ``` customers\.jsonl ``` | To ensure new and updated files are identified, you'd want to enter a search pattern that would match all files beginning with `customers`, regardless of the string in the file name:   ``` (customers-).*\.csv ``` |
| **Matches** | `customer.jsonl`, exactly | - `customers-reQDSwNG6U.csv` - `customers-xaPTXfN4tD.csv` - `customers-MBJMhCbNCp.csv` - etc. |

### File requirements

|  |  |
| --- | --- |
| First-row header (CSV files only) | - Every file must have a first-row header containing column names. The first row in any file is considered the header row, and will present these values as columns available for selection. - Files with the same first-row header values, if including multiple files in a table. Amazon S3 integration allows you to map several files to a single target table. Header row values are used to determine a table’s schema. For the best results, each file should have the same header row values. This is different from configuring multiple tables. See [Defining the search pattern](#Defining) for examples. |
| File types | - CSV (`.csv`) - Text (`.txt`) - JSONL (`.jsonl`) - Parquet (`.parquet`) - Arvo (`.arvo`) Arvo files must include a schema to be supported. |
| Compression types | These files must be correctly compressed or errors will surface during extraction.   - gzip compressed files (`.gz`) |
| Delimiters (CSV files only) | - Comma (`,`) - Tab (`/t`) - Pipe (`|`) - Semicolon (`;`) |
| Character encoding | UTF-8 (`.csv`, `.txt` and `.jsonl` only)  Information note`.parquet` and `.arvo` files are raw binary files. |

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Fill in the required connection properties.
2. Provide a name for the connection in Connection name.
3. Select Open connection metadata to define metadata for the connection when it has been created.
4. Click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| S3 Bucket | Name of the S3 bucket. |
| AWS Account ID | The AWS account ID of the account where the bucket exists.  You can find your AWS account ID in the AWS Management Console under Account details. |
| Search pattern | Enter the files to include in your table. You can enter a single file name or a regular expression. Example: `users\*.csv``products\*.jsonl`. |
| Directory | Limit the search in this directory path. When defined, only files in this location will be searched and wille be selected those that match the search pattern. You cannot use a regular expression. Example: csv-exports-folder or employee\_jsonl\_exports. |
| Table configuration Configure a table by specifying files you want to include.  You can configure multiple tables. | |
| Table name | Table name. Each target has its own rules for how tables can be named. For example, Amazon Redshift table names cannot exceed 127 characters. |
| Primary key | Enter the primary key to identify unique rows or records. When you enter more than one key, use comma to separate the values.  - For CSV files, enter the header fields or column names. - For JSONL files, enter the attribute names or object keys.   Example: id, name. |
| Specify datetime fields | Enter the values that must appear as datetime instead of string in your table. Example: created\_at, modified\_at. |
| Delimiter | Select the delimiter from the drop-down list. |
