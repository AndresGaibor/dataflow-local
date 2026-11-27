---
title: "AMI requirements"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/ami-requirements.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration", "Prerequisites in AWS"]
---

# AMI requirements

## Supported platforms

| Cloud provider | Supported Distribution | Notes |
| --- | --- | --- |
| AWS | Amazon Linux 2023 |  |

## Custom image requirements

Using custom images is optional. When using custom images, an x86 image is required, but using both arm and x86 images is recommended to maximize availability of spot instances.

The following requirements must be met to ensure proper functionality.

### Required utilities

The following utilities must be installed and available on the image:

| Utility | Notes |
| --- | --- |
| bash | Shell |
| docker | Container runtime |
| docker-compose | Container orchestration |
| curl | HTTP client |
| wget | HTTP client — planned for deprecation, but required for now |
| jq | JSON processor |
| socat | Socket relay utility |
| rsyslog | System logging daemon — start automatically at boot:  sudo systemctl enable rsyslog  sudo systemctl start rsyslog |
| awscli | AWS CLI |
