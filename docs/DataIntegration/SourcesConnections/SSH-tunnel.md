---
title: "SSH tunnel"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SSH-tunnel.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases"]
---

# SSH tunnel

Create an SSH tunnel connection to connect to supported data sources via an SSH tunnel. Tunneling allows you to securely access data sources located behind a firewall while also encrypting all data passing through the tunnel.

## Supported connectors and configuration

SSH tunnel is only supported with connectors that are configured without a Data Movement gateway, and with the following on-premises data sources only (cloud-based variants are not supported):

- MySQL
- PostgreSQL
- Microsoft SQL Server (Microsoft CDC based)

## Connection details

- SSH host

  The IP or host name of the SSH server.
- SSH port

  The port to use to access the SSH server.
- SSH user

  Your user name for accessing the SSH server.
- Encryption method

  Select an encryption method.
- Public key

  After selecting an encryption method, click Generate to generate the public key. Click the button at then end of the field to copy the key.

  You need to append the public key to the ~/.ssh/authorized\_keys file on the SSH host server, where it will be used to verify that the connection request was initiated from Qlik Cloud. There are several ways of doing this. One of them is to copy the key to a key.pem file, and then run the following command:

  ssh-copy-id -f -i key.pem user@remote-server
- Name

  The display name for the SSH connection. If you enable the SSH tunnel option in a supported connector, you need to select the name of an SSH connector from the SSH connection drop-down list.
