---
title: "Assigning engines to improve application performance"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/app-performance-select-engine.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing resources"]
---

# Assigning engines to improve application performance

When you open an application, Qlik Cloud automatically selects an engine based on application size, reload memory usage, and available system resources. You can manually assign a larger engine to gain more control or improve performance. Manual assignments use Large application capacity.

## Engine types and sizes

Qlik Cloud provides two types of engines: shared and dedicated.

### Shared engines

Shared engines can run multiple applications concurrently and the default for smaller or less complex applications. They cannot be assigned manually and do not require Large application capacity.

Example specification:

- 60 GB RAM
- Up to 14 CPU cores

### Dedicated engines

Dedicated engines run a single application at a time and are suited for larger or compute-intensive applications. They require Large application capacity and can be manually assigned.

Example specifications:

Engine specifications

| Engine type | Memory | Up to cores\* |
| --- | --- | --- |
| Large-40 | 40 GB | 10 cores |
| Large-60 | 60 GB | 14 cores |
| Large-80 | 80 GB | 20 cores |
| Large-120 | 120 GB | 30 cores |
| Large-160 | 160 GB | 40 cores |
| Large-200 | 200 GB | 50 cores |

\* “Up to” means resources are provisioned as needed. Not all CPU cores are used simultaneously for every calculation.

Information noteMemory and CPU specifications may change over time. This information reflects the current setup, but Qlik Cloud may update specifications as the platform evolves.

## When to manually assign a larger engine

You may want to override the default engine placement when:

- Your application has heavy visualizations or complex calculations that require more CPU.
- Your application size or complexity exceeds the default engine allocation.
- You want to test and validate performance gains using the built-in evaluation tool.

Manual assignments use Large application capacity, so always balance performance benefits against capacity usage. Assigning a larger engine does not necessarily resolve application-design or calculation problems.

Tip noteYou can test a larger engine temporarily during a performance evaluation before assigning it permanently. This lets you compare results and decide whether to assign the application to a larger engine or purchase Large application capacity. For details, see [*Application performance evaluation*](app-performance-evaluation.htm).

Information noteYou cannot assign an application to a smaller engine than the one Qlik Cloud selects automatically.

## Manually assigning engines to applications

You can manually assign a specific engine size to an application using the placement API. Manual overrides are available through API calls only.

Information noteAn engine size assigned through the placement API affects only the engine used for interactive consumption. It does not affect the engine used for reloads.

To assign engine sizes to applications, you need one of the following roles:

- Tenant Admin
- Analytics Admin
- A custom role including the Manage engine assignments for applications permission

With the placement API, you can:

- Assign an engine size to an application
- Check which engine size is currently assigned
- Remove an engine size override

Best practices:

- Grant engine assignment access only to trusted users responsible for performance and capacity management.
- Test engine changes in a development environment before applying changes to production applications.
- Review engine assignments regularly, especially for larger engine sizes.

For instructions and API details, see [Qlik Developer: Pin applications to engine sizes](https://qlik.dev/manage/reloads/analytics-engine-size-override/).

## Comparing application performance across engine sizes

The application performance evaluation tool in Qlik Cloud helps developers assess application performance during user interaction. It measures how efficiently application objects—such as charts, sheets, and KPIs—are calculated and rendered when the application is opened.

This tool is especially useful for testing whether a larger engine would improve performance. You can select a custom engine size for a single evaluation run without changing the application's default or permanently assigned engine size.

### What you can do with the evaluation tool

- Measure how long it takes for specific charts, sheets, or objects to calculate.
- Compare application performance across engine sizes to see whether assigning a larger engine improves speed and responsiveness.

Information noteThe application performance evaluation tool does not test reload performance. It focuses entirely on application usage.

### Assigning an engine during performance evaluation

Use a custom engine size to test how an application performs on a larger engine before assigning it permanently:

1. Run an evaluation with a custom engine size.
2. Compare the result with the default or another engine size.
3. If the results justify it, assign the engine size permanently using the placement API.

For detailed instructions, see [*Application performance evaluation*](app-performance-evaluation.htm).

### Temporary versus permanent assignments

- **Temporary selection**: Applies only to the current performance evaluation run. The selection is not retained after the evaluation.
- **Permanent assignment**: Assigns the application an engine size using the placement API. The assignment continues to affect future interactive use until it is removed.

Use a temporary selection to test and compare performance. Apply a permanent assignment only after you have confirmed that the larger engine improves performance.

Information noteYou can select a temporary engine that is smaller than the permanently assigned engine, provided it is not smaller than the engine size that Qlik Cloud would select automatically. For example, if an application is assigned to an 80 GB engine but Qlik Cloud would automatically select a 60 GB engine, you can run an evaluation on a 60 GB engine, but not on a 40 GB engine.

### Running a performance evaluation

You can run an application performance evaluation in several ways:

- Directly from the activity center
- As part of a Qlik Automate workflow
- Via the Qlik Cloud APIs

This makes the tool accessible to developers working interactively as well as to those automating application testing.

For more information, see [*Application performance evaluation*](app-performance-evaluation.htm).

## Capacity consumption considerations

Manual engine assignments affect how much Large application capacity your application uses. The following rules apply:

- Capacity used = engine size ÷ 4

  - Example: Assigning a 3 GB application to an 80 GB engine consumes 20 GB of Large application capacity at runtime.
- Qlik does not reduce usage if the application doesn’t fully use the assigned engine.
- If the application grows and is later automatically assigned to a larger engine, Qlik updates the capacity usage accordingly.

For more information, see [*Large application support*](../Admin/large-app-support.htm).
