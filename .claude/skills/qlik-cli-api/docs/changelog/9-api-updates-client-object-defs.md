---
source: https://qlik.dev/changelog/9-api-updates-client-object-defs/
last_updated: 2025-07-08T16:09:30Z
---

# SaaS API updates - 2021-03-24

## New Evaluation API Property - fileSizeMiB

The evaluations API now includes a property in the result schema and the
evaluation detail properties indicating the file size on disk of the evaluated
Qlik Sense application.

Learn more about [optimizing app performance](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/app-performance.htm#anchor-2)
and using the API in DevOps processes [here](https://qlik.dev/apis/rest/evaluations).

## Apps API Export App Response Update

The [export app](https://qlik.dev/apis/rest/apps#%23%2Fentries%2Fapps%2F-appId%2Fexport-post)
endpoint in the apps API now provides a location header
containing the URL of the exported application in the temporary content service
when the endpoint returns an `http 201` response.

## Sense Client Object Definitions Released

Developers have requested the schemas and property definitions
for the different objects created in Qlik Sense applications be made public. You
can now view this information [here](https://qlik.dev/apis/javascript/sense-client-objects).

You'll find all of the properties in each type of object available in Qlik
Sense, and you can download the specification for use in your own custom
applications.

## Webhooks API set to public/stable API status

The webhooks API is now a public and stable API in alignment with the public
release of tenant level webhooks in SaaS platform.
