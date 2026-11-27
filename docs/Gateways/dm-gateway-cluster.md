---
title: "Setting up Data Movement gateway in a Linux cluster"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/dm-gateway-cluster.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Qlik Data Gateway - Data Movement"]
---

# Setting up Data Movement gateway in a Linux cluster

This section provides guidelines for setting up Data Movement gateway in a Linux cluster environment. There are several commercially available clustering solutions for Linux including Veritas Cluster Server, Red Hat Cluster Suite and IBM HACMP for Linux.

When one of the available clustering solutions is already in place, Data Movement gateway can be set up like any other cluster application while adhering to the following guidelines:

- Data Movement gateway should be installed on the participating cluster nodes.

  For information about setting up Data Movement gateway, see [*Data Movement gateway system requirements*](dm-gateway-prerequisites.htm) and  [*Setting up Data Movement gateway*](dm-gateway-setting-up.htm).
- Data Movement gateway only supports the failover cluster configuration (active-passive). This means that, at any given time, the Data Movement gateway service should be running on one of the cluster nodes only.

  Information note The failover cluster configuration is a "hard requirement" as it ensures that only one instance of Data Movement gateway can access the shared data folder (see below) at any given time. Any other configuration will result in unpredictable behavior.
- Make the Data Movement gateway data folder (/opt/qlik/gateway/movement/data) a mount-point.

  To do this, on each of the participating cluster nodes:

  1. Install Data Movement gateway according to the instructions in  [*Setting up Data Movement gateway*](dm-gateway-setting-up.htm)
  2. Issue the following command to stop the Data Movement gateway service:

     sudo systemctl stop repagent
  3. Check that the service has stopped by running the following command:

     sudo systemctl status repagent

     The output should be as follows:

     Active: inactive (dead) since <timestamp> ago
  4. Change the directory to /opt/qlik/gateway/movement and rename the data folder, as in the following example:

     mv data data-save
  5. Create an empty data directory as follows:

     mkdir data
  6. Mount the data directory on a shared block device (iSCSI), as in the following example:

     mount -t ext4 /dev/sdb1 /opt/qlik/gateway/movement/data

     Information noteNFS based mounts (such as EFS on AWS) are not supported.
  7. Copy the content of data-save to data.

  After performing steps 1-7 on the participating cluster nodes, start the application using the cluster management tool. A single instance of Data Movement gateway will start on one of the cluster nodes.
