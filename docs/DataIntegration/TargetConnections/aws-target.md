---
title: "Amazon S3 (Qlik Cloud)"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/aws-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to cloud storage"]
---

# Amazon S3 (Qlik Cloud)

The Amazon S3 (Qlik Cloud) target is used for storing data that is needed for QVD generation. The data is stored in an Amazon S3 bucket. You can either use Qlik managed storage or your own storage area.

For more information about connecting to Qlik Cloud, see [Amazon S3](/en-US/connectors/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Storage%20provider%20connectors/Amazon-S3-storage-provider-connector.htm).

Information noteThe maximum size of a generated QVD table is 5 GB.

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

You need to fulfill the following prerequisites on the Data Movement gateway machine.

- Make sure the time and time zone settings on the Data Movement gateway machine are accurate. This is required in order to ensure:

  - Proper synchronization of Full Load and CDC tasks.
  - Correlation of the transaction log time with the actual time.

- Data Movement gateway connects to AWS using SSL. This requires an appropriate CA certificate to reside on the Data Movement gateway machine; otherwise, the connection will fail. The purpose of the CA certificate is to authenticate the ownership of the AWS server certificate.

  Make sure that the required CA certificate exists in the following location on the Linux machine:

  /etc/pki/tls/certs/ca-bundle.crt

  If it does not exist, the simplest solution is to copy the certificates bundle from another Linux machine.
