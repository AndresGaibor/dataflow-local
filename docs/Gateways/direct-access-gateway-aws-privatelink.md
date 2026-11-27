---
title: "Configuring AWS PrivateLink for Qlik Data Gateway - Direct Access"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-aws-privatelink.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Qlik Data Gateway - Direct Access"]
---

# Configuring AWS PrivateLink for Qlik Data Gateway - Direct Access

This topic describes the AWS PrivateLink workflow for connecting a Direct Access gateway in your Amazon Web Services (AWS) VPC to Qlik Cloud through private connectivity on the AWS network.

Warning note

Qlik does not provide the following:

- Any configuration help on the customer's AWS console, VPC, or PrivateLink setup. Qlik does not provide AWS consulting.
- If something goes wrong after setup is confirmed working and a technical issue arises, Qlik Support investigates the customer configuration to understand why the integration did not work as expected, but does not troubleshoot or help to configure the customer's AWS-side setup.

  Reference documentation for the customer's AWS-side setup will be shared with Support for context, but the scope of support is to the Direct Access Gateway operation on the customer side.

Information noteSupported from Direct Access gateway 1.8.0.

Govnote-not-inNot supported in Qlik Cloud Government.

Govnote-not-inNot supported in Qlik Cloud Government - DoD.

## Understand the pattern

The pattern uses an AWS interface VPC endpoint in your VPC to connect to a Qlik Cloud AWS endpoint service. The Direct Access gateway runs in your VPC. Route 53 private DNS can resolve the service name from the VPC, and traffic remains on the AWS backbone instead of traversing the public internet.

- Qlik provides and operates the Qlik Cloud endpoint service.
- You create and operate the interface VPC endpoint, private DNS, and network controls in your AWS account.
- You install and operate the Direct Access gateway in your VPC and keep its connection to your data sources available.

## Check the scope

- This pattern applies to AWS and to Direct Access gateway connectivity to Qlik Cloud.
- Azure private connectivity is out of scope for this topic.
- Availability must be confirmed for the requested tenant and AWS Region before implementation.

## Prepare your environment

Before implementation, coordinate with your AWS and Qlik Cloud administrators. Confirm the following for your tenant and AWS Region:

- The Direct Access gateway is installed on an EC2 instance, and the instance is running.
- You have AWS Console access with permission to create VPC endpoints and modify security groups.
- Qlik has confirmed PrivateLink availability for the tenant and region and has provided the exact regional service name and onboarding requirements.
- You can contact Qlik Support to provide the endpoint ID and request endpoint service acceptance.

## Configure the workflow

Do the following with your AWS and Qlik Cloud administrators:

1. From the EC2 instance, identify the VPC where the Direct Access gateway runs.
2. In the AWS Console, go to VPC > PrivateLink and Lattice > Endpoints, and click Create endpoint.
3. Select the endpoint service option and enter the exact Qlik regional service name confirmed for your tenant.
4. Contact [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport) and share your AWS Account ID, and AWS region where the connection should be initiated from. Wait until Qlik Support confirms that Qlik has added your AWS Account ID.
5. Select the VPC identified for the EC2 instance. Leave Enable private DNS name clear until Qlik accepts the endpoint.
6. Select the subnet that matches the Availability Zone of the EC2 instance.
7. Assign a security group with inbound HTTPS on port `443`. Set the source to the security group itself; do not use the subnet or an open IP range as the source.
8. Click Create endpoint.

   - On the Create endpoint page:

     - Enter a Name tag for the endpoint (e.g., dmg-privatelink-test ).
     - Under Type, select Endpoint services that use NLBs and GWLBs.
   - Under Service settings:

     - Enter the Service name provided by Qlik for your region (e.g., com.amazonaws.vpce.us-east-1.vpce-svc-0afc69d0635aef748). For the list of service names by region, see [*List of service names (VPC IDs) per region*](#VPCIDs).
     - Click Verify service. You should see a green "Service name verified" confirmation banner.
   - Select your VPC:

     - Under Network settings, click the VPC dropdown and select the VPC that matches your EC2 instance's VPC ID (e.g., vpc-0abc1234def56789a).Contact [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport) with the endpoint ID so Qlik can accept the endpoint service connection.
9. After Qlik accepts the endpoint, enable private DNS. Before enabling it, confirm that the VPC has Enable DNS hostnames and Enable DNS support enabled.
10. Enable the private connection on the gateway by running one of the following, depending on your deployment method:

    - Windows server installation:

      connectoragent qcs set\_config --private\_connection true --tenant\_url https://<tenantName>.<region>.qlikcloud.com

      (Replace <tenantName> and <region> with the tenant values confirmed by Qlik.)
    - Containerized installation:

      dotnet ConnectorAgent.dll qcs set\_config --private\_connection true --tenant\_url https://<tenantName>.<region>.qlikcloud.com

      (Replace <tenantName> and <region> with the tenant values confirmed by Qlik.)
11. Run a load script through the DAG connection and confirm the traffic through the endpoint service monitoring.

## Validate and troubleshoot

First determine whether the issue is in the AWS endpoint path or in the Direct Access gateway application connection. Check endpoint state, private DNS resolution, routing, and security controls with your AWS administrator. Check gateway service status and logs with the Direct Access gateway administrator. For gateway-specific troubleshooting, see [*Configuring and troubleshooting Qlik Data Gateway - Direct Access*](direct-access-gateway-troubleshooting.htm).

Information note

PrivateLink connectivity does not by itself define all Qlik Cloud allowlisting requirements. Review [*Allowlisting domains and IP addresses*](../Introduction/qlik-cloud-dns-ip.htm) for general allowlisting guidance.

## List of service names (VPC IDs) per region

This section lists the service names corresponding to each region. You need the service name when configuring the AWS PrivateLink setup, as described in [*Configure the workflow*](#Configure).

Service names by region

| Region | Service name | Availability zones |
| --- | --- | --- |
| us-east-1 | com.amazonaws.vpce.us-east-1.vpce-svc-00a485f00a94df90d | - use1-az2 - use1-az4 - use1-az6 |
| eu-west-3 | com.amazonaws.vpce.eu-west-3.vpce-svc-0f914c285c80d92c1 | - euw3-az1 - euw3-az2 - euw3-az3 |
| ap-southeast-2 | com.amazonaws.vpce.ap-southeast-2.vpce-svc-084ba78d527a91749 | - apse2-az1 - apse2-az3 - apse2-az2 |
| eu-central-1 | com.amazonaws.vpce.eu-central-1.vpce-svc-0d184b720e97c3888 | - euc1-az2 - euc1-az3 - euc1-az1 |
| ap-south-1 | com.amazonaws.vpce.ap-south-1.vpce-svc-0baadb0cb3dd12848 | - aps1-az2 - aps1-az3 - aps1-az1 |
| ap-southeast-1 | com.amazonaws.vpce.ap-southeast-1.vpce-svc-0f808f9f48d12a6bf | - apse1-az2 - apse1-az3 - apse1-az1 |
| ap-northeast-1 | com.amazonaws.vpce.ap-northeast-1.vpce-svc-0291b1c14bd3353ce | - apne1-az4 - apne1-az1 - apne1-az2 |
| eu-west-1 | com.amazonaws.vpce.eu-west-1.vpce-svc-0a1084ab9a085760a | - euw1-az3 - euw1-az1 - euw1-az2 |
| eu-west-2 | com.amazonaws.vpce.eu-west-2.vpce-svc-0b29ae1d28b35237c | - euw2-az2 - euw2-az3 - euw2-az1 |
| eu-north-1 | com.amazonaws.vpce.eu-north-1.vpce-svc-095b4ac47699f0ef5 | - eun1-az1 - eun1-az2 - eun1-az3 |
| il-central-1 | com.amazonaws.vpce.il-central-1.vpce-svc-0d3e2075d594af3df | - ilc1-az1 - ilc1-az2 - ilc1-az3 |
| sa-east-1 | com.amazonaws.vpce.sa-east-1.vpce-svc-01916a7fa8fd86bfd | - sae1-az1 - sae1-az2 - sae1-az3 |

## Learn more

- [*Qlik Data Gateway - Direct Access*](direct-access-gateway.htm)
- [*Setting up Qlik Data Gateway - Direct Access*](direct-access-gateway-setting-up.htm)
