---
title: "Salesforce"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Salesforce_Connector_help/Content/Connectors_Salesforce/Introduction/Salesforce-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics"]
---

# Salesforce

The Salesforce Connector enables Qlik Sense to efficiently load data into an application from a Salesforce.com data set. You must have a Salesforce.com account with current access credentials to access data. Once a connection to a Salesforce.com account has been created, data can be selected from tables available to the user’s account and then loaded into an application where it can be used in visualizations.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Supported Salesforce API version

The Salesforce Connector supports up to Salesforce API version 56.

## Supported Salesforce data types

The following Salesforce.com data types are supported by the Salesforce Connector and are available for selection through the user interface. Fields containing unsupported data types are not displayed.

- Autonumber
- Checkbox
- Currency
- Date
- Date/Time
- Email
- Formula
- Geolocation
- Lookup Relationship
- Number
- Percent
- Phone
- Picklist
- Picklist (Multi-Select)
- Roll-Up Summary
- Text
- Text (Area)
- Text Area (Long)
- Text Area (Rich)
- Text (Encrypted)
- URL

Information note

Geolocation is composed of two primitive data types: longitude and latitude. The Salesforce Connector supports Geolocation by displaying each of its primitive types in separate fields. When a table contains a field with the Geolocation data type, the field displays as empty. The component values of the Geolocation field are then displayed in the table as two separate fields.
