---
title: "Image and VM requirements"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/gcp-image-vm-requirements.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in GCP"]
---

# Image and VM requirements

Review the Compute Engine image and VM requirements for running Qlik Open Lakehouse in your Google Cloud environment.

Qlik deploys the network integration gateway and the lakehouse cluster from Compute Engine instance templates. The lakehouse cluster uses separate Managed Instance Groups (MIGs) for Standard and Spot VMs:

- Standard MIG: Provides a minimum capacity floor.
- Spot MIG: Provides additional capacity using Spot VMs. Spot VMs can be preempted with 30 seconds' notice.
