---
title: "Large application support"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/large-app-support.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Planning your Qlik Cloud deployment", "Qlik Cloud capacity-based subscriptions", "Qlik Cloud Analytics subscription options"]
---

# Large application support

With large application support, you can work with applications that are larger than the standard application size.
You can configure one or more spaces in Qlik Cloud to support large applications, ensuring they have the memory needed to run efficiently.

## How large application support works

Large application support provides additional memory through engines of different sizes in engine pools. Every application is loaded into an engine at runtime. An autoscaling mechanism dynamically allocates resources as needed and routes large applications to the best-suited engines. This ensures that you can work with an application even if it requires more resources than a single engine can provide.

The total large application capacity determines how many applications larger than the standard application size that you can have open at the same time. Only the in-memory size of the application is counted, not the number of user sessions on each application.

## Large application capacity options

Large application capacity is available in 20 GB and 100 GB packs for the following subscriptions:

- Qlik Cloud Analytics Premium
- Qlik Cloud Enterprise
- Qlik Sense Enterprise SaaS

You can mix and match capacity packs to allocate the right amount to your [tenant](#glossary-1 "Glossary term"). Qlik Cloud Enterprise includes 40 GB of large application capacity by default.

Qlik provides support for capacity planning and provisioning. Contact [Qlik Sales](https://www.qlik.com/us/try-or-buy/buy-now) for more information.

Information noteThe unit of measurement for Qlik Cloud capacity, usage, and limits is represented by binary gigabytes (GB), where 1 GB is 230 bytes (1,073,741,824). This is also known as a gibibyte (GiB), defined by the [International Electrotechnical Commission (IEC)](http://www.iec.ch/prefixes-binary-multiples). Similarly, 1 TB is 240 bytes (or 1,024 GBs).

Information note

Large application support is not available in Qlik Anonymous Access subscriptions.

## Supported application capacity

The maximum supported application size varies depending on your subscription level and the assigned large application capacity.

Application capacity

| Application type | Supported application size (in-memory) |
| --- | --- |
| Standard application for Qlik Sense Enterprise SaaS | Up to 5 GB |
| Standard application for Qlik Cloud Analytics Premium | Up to 10 GB |
| Standard application for Qlik Cloud Analytics Enterprise | Up to 15 GB |
| Large application | Up to 50 GB |

### Supported application size based on assigned capacity

If the large application capacity assigned to your tenant is less than 50 GB, the maximum supported application size is equal to the assigned capacity. The table shows the supported application size when the total large application capacity is 20, 40, or 50 GB.

Supported application size based on assigned capacity

| Assigned large application capacity | Supported application size (in-memory) |
| --- | --- |
| 1 pack of 20 GB | 20 GB |
| 2 packs of 20 GB | 40 GB |
| 50 GB or more | 50 GB |

## Estimating your large application capacity needs

To determine your required large application capacity:

- Count the in-memory size of the applications you need to have open at the same time.
- If you experience peak memory constraint errors when loading data into an application, consider increasing the capacity.

### Example: Calculating capacity needs

If you have five applications with the average size of 15 GB and you want to open them all at the same time, you need: 5 applications x 15 GB = 75 GB of capacity

To support this, you could:

- Assign four packs of 20 GB to your tenant (total 80 GB).
- Purchase one 100 GB pack to allow for future growth.

## Working with large applications

Administrators can define which spaces that allow large applications. You can see whether a space allows large applications in the Allow large apps column of the Spaces table.

### Enabling large application support for a new space

Do the following:

1. In the Administration activity center, select Spaces.
2. Click Create new.
3. Enter the space details and select the Allow large apps checkbox.
4. Click Create.

### Enabling large application support for an existing space

Do the following:

1. In the Administration activity center, select Spaces.
2. Locate the space, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and select Edit space.
3. Select the Allow large apps checkbox.
4. Click Save.

For more information about managing spaces, see [*Managing spaces*](mc-administer-spaces.htm).

## Considerations when using large applications

When using large applications, consider the following:

### Capacity usage

- The large application capacity is only used for applications that exceed the standard application size.
- Each open instance of an application counts toward the large application capacity. For example, if a source application is open in a shared space and a published copy of the application is open in a managed space, both count as separate instances.
- When you open a large application, it counts against your large application capacity, whether you open the application with or without data.

### Space behavior

- Spaces that allow large applications are not explicitly labeled in Qlik Cloud Catalog. To indicate that a space is intended for large applications, use the description field of the space.
- Applications can be moved between standard spaces and spaces with large application support. However:
  - If an application exceeds the standard in-memory limit and is moved to a standard space, it cannot be opened. You can still download the application and view its details in [activity centers](#glossary-2 "Glossary term").
  - If large application support is removed from a space, the application remains, but it cannot be opened it it exceeds the standard in-memory limit.

### Reloading large applications

- When you reload data from a space with large application support, the reload runs on that space.
- The peak reload size for applications in spaces without large application support is up to 34 GB. If a reload exceeds this limit, move the application to a space that allows large applications.

### Evaluating large applications

Performance evaluations use different rules depending on the selected engine settings:

- With automatic settings, the evaluation follows the default engine placement for the application's space.
- With custom settings, you can evaluate applications up to 50 GB on an available engine, regardless of the tenant's large application capacity or the space's large application settings.

All evaluations count against a separate evaluation quota. For more information, see [*Application performance evaluation*](../Apps/app-performance-evaluation.htm).

## Monitoring large application capacity

Administrators can track the usage of large application capacity from the Administration activity center.

### View total large application capacity

Go to Home > Capabilities to see the total large application capacity assigned to your tenant.

### Monitor current usage

The Large application utilization chart on the Home page shows current usage and peak capacity for the day. For more information, see [*Monitoring resource consumption*](mc-monitor-consumption.htm).

### Identify spaces allowing large applications

View the Allow large apps column on the Spaces page in Administration to see which spaces that allow large applications.

### Track application sizes

View application sizes from the Applications tab on the Content page.

### Monitor in-memory application size and memory usage

Use the App Analyzer monitoring application to track in-memory application size and memory usage over time.

The App Analyzer application is part of the Qlik Cloud Monitoring Apps, which are community-supported and not officially supported by Qlik. To quickly install and update these applications, use the Qlik Cloud Monitoring Apps Installer with Qlik Automate. For details on installation and support, see [*App Installers*](../../Sense_QlikAutomation/introduction/template-list.htm#App).

For more information, see:

- [Qlik Community: The Application Analyzer for Qlik Cloud Customers](https://community.qlik.com/t5/Support-Updates/The-App-Analyzer-for-Qlik-Cloud-Customers/ba-p/1734927)
- [GitHub: Qlik Cloud Application Analyzer](https://github.com/qlik-oss/qlik-cloud-app-analyzer)
