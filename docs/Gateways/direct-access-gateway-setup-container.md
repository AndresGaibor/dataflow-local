---
title: "Setting up Qlik Data Gateway - Direct Access in a container"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-setup-container.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Qlik Data Gateway - Direct Access", "Setting up Qlik Data Gateway - Direct Access"]
---

# Setting up Qlik Data Gateway - Direct Access in a container

Expand/Collapse all

# Setting up Qlik Data Gateway - Direct Access in a container

This topic outlines the how to set up containerized Direct Access gateway. It provides prerequisites and installation instructions, and describes the limitations and considerations you should be aware of when working with containerized Direct Access gateway.

Information noteSupported from Direct Access gateway 1.8.0.

## Supported data sources

The following connectors are supported for containerized installations:

- The following ODBC connectors are supported:
  - PostgreSQL
  - SQL Server
  - Oracle
  - Amazon Redshift, Snowflake, Databricks, Google BigQuery, and Amazon Athena

    Information noteSupported from Direct Access gateway 1.8.2.

  For more information about ODBC connectors, see [ODBC databases ‒ Qlik Cloud](https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Introduction/ODBC-connector.htm).
- REST connector (REST via Direct Access gateway). For more information about REST data sources, see [REST sources ‒ Qlik Cloud](https://help.qlik.com/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Connectors_REST/REST-connector.htm).
- MySQL connector.

  Information noteSupported from Direct Access gateway 1.8.1.
- SAP SQL, SAP BW, SAP ODP, and SAP Report connectors. For information about installing the SAP NetWeaver RFC SDK on the Qlik Data Gateway - Direct Access machine for containerized installations, see [Installing SAP NetWeaver RFC SDK for Qlik Data Gateway - Direct Access](/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Installation/Installing-sap-connectors-for-direct-access-gw.htm).

  Information noteSupported from Direct Access gateway 1.8.1.

## What is containerized Direct Access gateway?

You can deploy Direct Access gateway into a Docker container. This type of deployment is called containerized Direct Access gateway. Containerized Direct Access gateway deployments are supported for Linux, macOS, and Windows.

Containerized Direct Access gateway provides portability to your Direct Access gateway environment.

## Best practices when using Qlik Data Gateway - Direct Access

For a successful experience when using Qlik Data Gateway - Direct Access, it is strongly recommended to adhere to the following best practices:

- Do not use the same Direct Access gateway for development, user acceptance testing, and production, as this will increase the risk of overloading the available resources and impact system stability. From a business perspective, the combination of insufficient resources and decreased stability, might result in delayed updates to production application data.
- For optimal performance, install the Direct Access gateway in an environment that is as close as possible to your data source.

## System prerequisites

This section describes the requirements for using containerized Direct Access gateway.

### Software requirements

- Docker Engine version 20.9+ and the Docker Compose plugin (docker compose, v2 syntax) installed on the host.

### Required ports and protocols

For required ports and protocols, see [*Required ports and protocols*](direct-access-gateway-setting-up.htm#Ports).

### Recommended hardware

- Host: 8 cores, 32 GB memory, 5 GB storage available to Docker
- Optional: Set matching limits on the container in the compose file so the gateway has dedicated capacity rather than competing with other containers or processes on the host:

  ```
  direct-access-agent:
      image: ...
      deploy:
        resources:
          limits:
            cpus: "6"
            memory: 24G
  ...
  dcaas:
      image: ...
      deploy:
        resources:
          limits:
            cpus: "2"
  ```

#### Minimum hardware

The minimum hardware is only suitable for specific scenarios using smaller dedicated deployments (development, test, or production), with continuously low data volumes, and a limited number of concurrent reloads.

- Host: 4 cores, 8 GB memory, 5 GB storage available to Docker
- Optional: Set matching limits on the container in the compose file so the gateway has dedicated capacity rather than competing with other containers or processes on the host:

  ```
  direct-access-agent:
      image: ...
      deploy:
        resources:
          limits:
            cpus: "2"
            memory: 4G
  ...
  dcaas:
      image: ...
      deploy:
        resources:
          limits:
            cpus: "2"
  ```

## Installing Qlik Data Gateway - Direct Access

Setting up the Direct Access gateway involves procedures that need to be performed both in the Administration activity center and on the Direct Access gateway server.

Information noteData gateway procedures that need to be performed in the Administration activity center require tenant admin permission.

### Stage one: Download Qlik Data Gateway - Direct Access

1. In the Administration activity center, select Data gateways.

   Any existing data gateways will be listed in [a table showing basic information about each gateway](direct-access-gateway-managing-console.htm#gateprop).
2. Click the Deploy toolbar button.

   The Deploy Data Gateway dialog opens.
3. Select Data Gateway - Direct Access - Containerized Direct Access Gateway, accept the Qlik Customer Agreement, and click Download. The Direct Access gateway setup file (docker-compose.qlik-data-gateway-direct-access.yml) will be downloaded to your machine.

### Stage two: Start the deployment by running the Docker Compose file

To start the deployment of the Direct Access gateway, run the following command:

docker compose -f docker-compose.qlik-data-gateway-direct-access.yml up

#### Copying the SAP NetWeaver RFC SDK to the container

For SAP SQL, SAP BW, SAP ODP, and SAP Report connectors, copy the SAP NetWeaver RFC SDK files into the container.

From the directory that contains both the Linux and Windows SDK binary folders, run:

docker cp . direct-access-agent-1:/usr/share/Qlik/Gateway/sap-sdk

Restart the direct-access-agent-1 container after copying the files.

### Stage three: Setting up Direct Access gateway

For detailed setup instructions, see [*Stage three: Set up Direct Access gateway*](direct-access-gateway-setting-up.htm#Stage3).

### Stage four: Register the data gateway

The next step is to register the data gateway. This can be done either through the Administration activity center or on the command line.

Option 1: Via the Administration activity center

You can register the gateway using the Administration activity center. See [*Option 1: Via the Administration activity center*](direct-access-gateway-setting-up.htm#StageConsole).

Option 2: Automatic registration using the command line

You can also register Direct Access gateway automatically from the command line, without using the Administration activity center. This method uses a short-lived session token generated from an OAuth client.

Information note

To automatically register and remove automatically registered gateways, you need the following permissions:

- Automatic registration: You need the Register Direct Access gateway admin permission set to Allowed.
- Removing automatically registered gateways: You need the Register Direct Access gateway admin permission set to Allowed.

For more information about permissions, see [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm).

Information noteAutomatic registration is supported through the command line only. A REST API for automatic gateway registration is not currently available.

Prerequisites

An API key with tenant admin permission to create and manage OAuth clients.

Registering the gateway with automatic registration

1. First, you need to set up a Python environment to generate an OAuth client ID, as well as an assertion key (short-lived token) in the direct-access-agent container. Run the following commands separately, in this order:

   1. docker exec -it --user root direct-access-agent-1 bash
   2. apt-get update && apt-get install -y python3 python3-pip
   3. apt install python3.11-venv
   4. python3 -m venv .venv
   5. source .venv/bin/activate
   6. pip install cryptography pyjwt
   7. python3 generate\_gateway\_assertion.py --tenant-url <tenant-url>
2. For the [last command in the list above](#python3), follow the interactive prompts and copy the client\_id (OAuth client ID) and assertion when provided. Store these details on paper or in a temporary text file for now—they are required for later steps in the process.
3. When you have written down the client\_id and assertion, clean the Python environment with the following command:

   deactivate
4. Set the OAuth client's consent method to trusted.

   curl "https://<tenant-url>/api/v1/oauth-clients/<client-id>/connection-configs/me" -X PATCH -H 'accept: application/json' -H 'content-type: application/json' -H 'authorization: Bearer <api-key>' -d '[{"op":"replace","path":"/consentMethod","value":"trusted"}]'
5. Request an access token. This also triggers automatic creation of the bot user account used by the gateway.

   curl "https://<tenant-url>/oauth/token" -X POST -H 'content-type: application/x-www-form-urlencoded' -d "grant\_type=client\_credentials" -d "client\_id=<client-id>" -d "client\_assertion\_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer" -d "client\_assertion=<assertion>" -d "scope=admin.direct-access-gateways:register\_gateway admin.direct-access-gateways:delete\_gateway"

   Information note

   If the assertion has expired, re-run the script from the virtual environment.
6. Look up the auto-created bot user.

   curl "https://<tenant-url>/api/v1/users" -H 'accept: application/json' -H 'authorization: Bearer <API-key>'
7. Copy the ID of my-bot-client.
8. Create a "DAG Registration" role.

   curl "https://<tenant-url>/api/v1/roles" -X POST -H 'accept: application/json' -H 'content-type: application/json' -H  'authorization: Bearer <API-key>' -d '{"name":"DAG Registration","description":"Role for registering a gateway","assignedScopes":["admin.direct-access-gateways:register\_gateway", "admin.direct-access-gateways:delete\_gateway"]}'
9. Assign tenant-level roles to the bot user.

   curl "https://<tenant-url>/api/v1/users/<bot-user-ID>" -X PATCH  -H 'accept: application/json' -H 'content-type: application/json' -H  'authorization: Bearer <API-key>' -d ' [ { "op": "replace", "path": "/assignedRoles", "value": [ { "name": "DAG Registration" } ] } ]'
10. Get the Direct Access Gateway space.

    curl "https://<tenant-url>/api/v1/spaces" -H  'authorization: Bearer <API-key>'
11. Copy the Direct Access Gateway space ID.
12. Add the bot user to the space with Can edit permission.

    curl "https://<tenant-url>/api/v1/spaces/<DAG-space-ID>/assignments" -X POST -H 'accept: application/json' -H 'content-type: application/json' -H  'authorization: Bearer <API-key>' -d '{"assigneeId": "<bot-user-ID>","roles": ["consumer","dataconsumer","producer"], "type": "user"}'
13. In case the existing assertion has expired, generate a new one. Run the following command:

    python3 generate\_gateway\_assertion.py --tenant-url <tenant-url>
14. Follow the needed steps in the command prompt. Since the OAuth client is already created, there is a need to update JWK using this API call:

    curl "https://<tenant-url>/api/v1/oauth-clients/<client-ID>" -X PATCH -H 'accept: application/json' -H 'content-type: application/json' -H 'authorization: Bearer <API-key>' -d '[{"op":"replace","path":"/publicKeys/0/y","value":"<Y-value-from-JWK>"},{"op":"replace","path":"/publicKeys/0/x","value":"<X-value-from-JWK>"},{"op":"remove","path":"/publicKeys/0/use"},{"op":"replace","path":"/publicKeys/0/kid","value":"<kid-value-from-JWK>"}]'
15. Register the gateway:

    dotnet ConnectorAgent.dll qcs register\_gateway --tenant\_url <tenant-url> --gateway\_name <DAG-name> --gateway\_description <DAG-description> --space\_name <space-name> --client-id <client-ID> --assertion <assertion>

Removing an automatically registered gateway

Use the following steps to unregister a gateway that was registered using the automatic, session token-based method described above. These steps also remove the OAuth client, bot user, and role that were created for it.

1. Generate an assertion, as described in [the section above](#AutoRegister).
2. Delete the gateway:

   dotnet ConnectorAgent.dll qcs delete\_gateway --tenant\_url <tenant-url> --gateway\_name <gateway-name> --client-id <client-ID> --assertion <assertion>
3. Look up the bot user account that was created for the gateway.

   curl "https://<tenant-url>/api/v1/users" -H 'accept: application/json' -H 'authorization: Bearer <api-key>'
4. Copy the bot ID.
5. Delete this bot user account.

   curl -X DELETE "https://<tenant-url>/api/v1/users/<bot-user-ID>" -H "Authorization: Bearer <api-key>"
6. Look up the “DAG Registration” role that was created for the gateway.

   curl "https://<tenant-url>/api/v1/roles?limit=1&filter=(name%20eq%20%22DAG%20Registration%22)"  -H "Authorization: Bearer <api-key>"
7. Copy the role ID.
8. Delete this role.

   curl -X DELETE "https://<tenant-url>/api/v1/roles/<role-ID> -H "Authorization: Bearer <api-key>"
9. Delete the OAuth client.

   curl -X DELETE https://<tenant-url>/api/v1/oauth-clients/<OAuth-client-ID> -H "qlik-confirm-delete: <OAuth-client-ID>" -H "Authorization: Bearer <api-key>

### Stage five: Start the Qlik Data Gateway - Direct Access service on the Direct Access gateway server

To start the Qlik Data Gateway - Direct Access service, start the dcaas-dg and direct-access-agent containers.

### Stage six: Add a connection to your data source

See [*Stage six: Add a connection to your data source*](#Stage6).

## Environment settings

This section lists specific environment variables from the docker-compose.qlik-data-gateway-direct-access.yml file which you might need to configure to properly connect your data sources via the gateway.

- ALLOW\_SOURCES: A comma-separated allowlist of hostnames and IPs. When the gateway agent needs to connect to something on your own server or another host in the local or private network (for example, a database on localhost, a Docker service name, or a private-IP host), you add that address to ALLOW\_SOURCES — otherwise the connection attempt is refused.

## Learn more

- [*Setting up Qlik Data Gateway - Direct Access*](direct-access-gateway-setting-up.htm)
- [*Setting up Qlik Data Gateway - Direct Access on a Windows server*](direct-access-gateway-setup-win.htm)
