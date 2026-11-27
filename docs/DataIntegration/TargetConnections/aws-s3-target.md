---
title: "Amazon S3"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/aws-s3-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to cloud storage"]
---

# Amazon S3

Amazon S3 can be used as:

- A cloud staging area when using Databricks (optional) or Amazon Redshift (required) as a data pipeline target. The cloud staging area is where data and changes are staged before being applied and stored.
- A cloud staging area when using Qlik Open Lakehouse projects with CDC sources. This requires the Data Movement gateway and clusters to be able to read from and write to the landing bucket. For more information, see [*Step 1: Create a network integration*](../Lakehouse/network-integration.htm).
- A cloud staging area when using Qlik Open Lakehouse projects with streaming sources. This requires the clusters to be able to read from and write to the landing bucket. For more information, see [*Step 1: Create a network integration*](../Lakehouse/network-integration.htm).
- A target in a replication task.

  - For an explanation of how to replicate data to Amazon S3 with Standard, Premium, and Enterprise subscriptions, see [*Landing data in a data lake with a Standard, Premium, or Enterprise subscription*](../Replicating/landing-datalakes.htm).
  - For an explanation of how to replicate data to Amazon S3 with a Starter subscription, see [*Replicating data with a Qlik Talend Cloud Starter subscription*](../Replicating/replicating-starter-subscription.htm).

## Permissions required for landing data

- You must have an Amazon S3 bucket that is accessible from the service or machine used to access it.

  For information on signing up for Amazon S3, see <http://aws.amazon.com/s3/>.
- Bucket access credentials: Make a note of the bucket name, access key and secret access key - you will need to provide them in the Amazon S3 connector settings.
- Bucket access permissions: The following bucket access permissions are required:

  ```
   
  ```

  ```
  {
  	"Version": "2012-10-17",
  	"Statement": [
  	    {
  	     "Sid": "Stmt1497347821000",
  	     "Effect": "Allow",
  	     "Action": [
                  "s3:GetBucketLocation",
                  "s3:ListBucket"
              ],
              "Resource": [
                  "arn:aws:s3:::YOUR_BUCKET_NAME"
              ]
          },
          {
              "Sid": "Stmt1497344984000",
              "Effect": "Allow",
              "Action": [
                  "s3:PutObject",
                  "s3:GetObject",
                  "s3:DeleteObject"
              ],
              "Resource": [
                  "arn:aws:s3:::YOUR_BUCKET_NAME/target_path",
                  "arn:aws:s3:::YOUR_BUCKET_NAME/target_path/*"
              ]
          }
      ]
  }
  ```

Where `YOUR_BUCKET_NAME` is the name of your bucket and `target_path` is the intended location of the target files in your bucket.

Information note

If the target path is the bucket root, just specify `“/target_path”` with an empty string.

## Qlik Data Gateway - Data Movement prerequisites

Data Movement gateway connects to AWS using SSL. This requires an appropriate CA certificate to reside on the Data Movement gateway machine; otherwise, the connection will fail. The purpose of the CA certificate is to authenticate the ownership of the AWS server certificate.

Make sure that the required CA certificate exists in the following location on the Linux machine:

/etc/pki/tls/certs/ca-bundle.crt

If it does not exist, the simplest solution is to copy the certificates bundle from another Linux machine.

## Setting Amazon S3 connection properties

To configure the connector, do the following:

1. In Connections, click Create connection.
2. Select the Amazon S3  target connector and then provide the following settings:

### Data target

Usage 

Select one of the following according to your usage:

- Data Movement: Select when using Data Movement gateway to access the Amazon S3 target.
- Network Integration: Select when using Amazon S3 to store the Qlik metadata files needed for [Qlik Open Lakehouse network integration](../Lakehouse/manual-integration.htm).
- Both: Select when both of the above are true.

Data gateway

When Data Movement or Both is selected, select the Data Movement gateway that you want to use to access the target.

Depending on your use case, this will either be the same Data Movement gateway deployed to land data from the data source, or a different one. For information about the possible Data Movement gateway deployment possibilities, see [*Common use cases*](../../Gateways/replication-gateway.htm#Common).

Information noteRequires Data Movement gateway 2023.5.10 or later.

Network Integration

When Network Integration or Both is selected, select the Qlik Open Lakehouse [Network Integration you created earlier](../Lakehouse/network-integration.htm).

### Connection properties

- Access options: Select one of the following:

  - Key pair (the default)

    Use a key pair to access your Amazon S3 bucket. When this option is selected, specify the following:

    - Access key: The access key for your Amazon S3 bucket.
    - Secret key: The secret key for your Amazon S3 bucket.- IAM Roles Anywhere
       (not supported when using Amazon S3 as a staging area for Databricks or Qlik Open Lakehouse):

      IAM Roles Anywhere can be set up in the [IAM Roles Anywhere console](https://console.aws.amazon.com/rolesanywhere/home/), via the AWS CLI, or using the AWS SDK. IAM Roles Anywhere allows you to use your private key infrastructure (PKI) to generate temporary credentials for accessing IAM roles from outside of AWS. This means you can securely access AWS resources from Qlik Talend Data Integration without having to manage long-term credentials.

      When this option is selected, specify the following:

      - Certificate file: Path to the Qlik Talend Data Integration public certificate on the Data Movement gateway machine in PEM format. This file needs to be signed with the CA certificate configured in the IAM Roles Anywhere console.
      - Private key file: Path to the Qlik Talend Data Integration private key file on the Data Movement gateway machine in PEM format.
      - Private key passphrase: The private key passphrase. Only required if the private key file is encrypted.
      - Trust anchor ARN: The ARN associated with the trust anchor you created in the IAM Roles Anywhere console. You establish trust between IAM Roles Anywhere and your certificate authority (CA) by creating a trust anchor. A trust anchor is a reference to either AWS Private CA or an external CA certificate. Your workloads outside of AWS authenticate with the trust anchor using certificates issued by the trusted CA in exchange for temporary AWS credentials.
      - Profile
        ARN: The ARN associated with the profile you created in the IAM Roles Anywhere console. To specify which roles IAM Roles Anywhere assumes and what your workloads can do with the temporary credentials, you create a profile. In a profile, you can define permissions with IAM managed policies to limit the permissions for a created session.
      - Role ARN: The ARN associated with the role you created in the IAM Roles Anywhere console. A role is an IAM identity that you create in your account with specific permissions. For IAM Roles Anywhere to be able to assume a role and deliver temporary AWS credentials, the role must trust the IAM Roles Anywhere service principal.

        The format should be as follows:

        arn:aws:iam::<account-id>:role/<role-name-with-path>

      For more information about IAM Roles Anywhere, see:

      [Extend AWS IAM roles to workloads outside of AWS with IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)
  - IAM Roles for EC2

    Select this method if the machine used to access Amazon S3 is configured to authenticate using an IAM role.

    For information on IAM roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html).

    - Assume role: Select this option to assume the target IAM role.

      This option is optional for Data Movement, Network Integration, and Both modes.

      When it is not selected, the connection uses the IAM role associated with the relevant EC2 machine.

      Configure the target role trust policy to trust the applicable Data Access and/or Data Movement role for the selected Usage mode.

      Specify the following:

      - Additional role ARN: The ARN associated with the target role.
      - Additional role external ID: When Assume role is selected and Usage is set to Network Integration or Both, click Load External ID to retrieve the external ID. Add the retrieved external ID to the trust policy of the additional target role.

      Configure the trust policy to trust the applicable role for your selected Usage mode:

      - Network Integration mode: Trust the Data Access role (server role) used by your network integration.
      - Data Movement mode: Trust the Data Movement role used by the Data Movement gateway.
      - Both mode: Trust both the Data Access role and the Data Movement role.
- Bucket name: The name of your Amazon S3 bucket.

  Information note

  The default bucket region setting is auto-detect, which eliminates the need to set a specific region. However, due to security considerations, for some regions (for example, AWS GovCloud), you might need to explicitly set the region. In such a case, you can set the region code using the regionCode internal property.

  For a list of region codes, see the Region availability section in:<https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html>

  For instructions on setting internal properties, see below.
- Use AWS PrivateLink (not supported as a landing target for Qlik Open Lakehouse ): Select this to connect to an Amazon VPC and then specify the VPC Endpoint URL (for example, https://bucket.vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com).

  Information noteThe Use AWS PrivateLink option is not supported when using an Amazon S3 bucket as the staging area for a Databricks target. For information on setting up connectivity to a Databricks target, see [*Databricks*](databricks-target.htm).

### Data encryption

Select one of the following Encryption options:

- Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3).

  This is the default.
- Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS)

  This option also requires you to specify your KMS key ID.

  For more information on the available server-side encryption methods, see:

  [Protecting data with server-side encryption](http://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html)
- None

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the connection.

## Data type mapping

The following table shows the default mapping from Qlik Cloud data types to Amazon S3 data types.

Information noteThe data type mappings are only relevant if the [Create metadata files in the target folder](../Replicating/landing-datalakes-settings.htm#Metadata) option in the "Land data in data lake" task settings is enabled.

### Mapping from Qlik Cloud data types to Amazon S3

Qlik Cloud and Amazon S3 data types

| Qlik Cloud data types | Amazon S3 Target data types |
| --- | --- |
| DATE | DATE |
| TIME | TIME |
| DATETIME | DATETIME |
| BYTES | BYTES (length) |
| BLOB | BLOB |
| REAL4 | REAL4 (7) |
| REAL8 | REAL8 (14) |
| INT1 | INT1 (3) |
| INT2 | INT2 (5) |
| INT4 | INT4 (10) |
| INT8 | INT8 (19) |
| UINT1 | UINT1 (3) |
| UINT2 | UINT2 (5) |
| UINT4 | UINT4 (10) |
| UINT8 | UINT8 (20) |
| NUMERIC | NUMERIC (p,s) |
| STRING | STRING (Length) |
| WSTRING | WSTRING (Length) |
| CLOB | CLOB |
| NCLOB | NCLOB |
| BOOLEAN | BOOLEAN (1) |

### Mapping from Qlik Cloud data types to Parquet

When Parquet is set as the file format, due to the limited number of data types supported by Parquet, the data type mappings will be as follows:

Parquet data type mappings

| Qlik Cloud Data Type | Parquet Primitive Type | Logical Type |
| --- | --- | --- |
| BOOLEAN | BOOLEAN |  |
| INT1 | INT32 | INT(8, true) |
| INT2 | INT32 | INT(16, true) |
| INT4 | INT32 |  |
| INT8 | INT64 |  |
| UINT1 | INT32 | INT(8, false) |
| UINT2 | INT32 | INT(16, false) |
| UINT4 | INT64 |  |
| UINT8 | INT64 | INT(64, false) |
| REAL4 | FLOAT |  |
| REAL8 | DOUBLE |  |
| NUMERIC | FIXED\_LEN\_BYTE\_ARRAY (16) | DECIMAL (precision, scale) |
| STRING | BYTE\_ARRAY | STRING |
| WSTRING | BYTE\_ARRAY | STRING |
| BYTES | BYTE\_ARRAY |  |
| BLOB | BYTE\_ARRAY |  |
| CLOB | BYTE\_ARRAY | STRING |
| NCLOB | BYTE\_ARRAY | STRING |
| DATE | INT32 | DATE |
| TIME | INT32 | TIME (UTC=true, unit=MILLIS) |
| DATETIME | INT64 | TIMESTAMP (UTC=true, unit=MICROS) |

## Learn more

- [Landing data in a data lake](../Replicating/landing-datalakes.htm)
- [Amazon Redshift target](redshift-target.htm)
- [Databricks target](databricks-target.htm)
