---
source: https://qlik.dev/changelog/161-di-projects-events/
last_updated: 2025-10-31T14:06:52+01:00
---

# New events - Data integration project tasks

> Updated on September 8, 2025: Updated to reflect these events are also available in Audits.

New data integration project task events are now available through webhooks & audits.\
These events are emitted automatically when the corresponding task state change occurs, enabling real-time monitoring.

The following events are included in this release:

- **Data task completed**: `com.qlik.v1.di-projects.di-tasks.completed`
- **Data task failed**: `com.qlik.v1.di-projects.di-tasks.failed`
- **Data task started**: `com.qlik.v1.di-projects.di-tasks.started`
- **Data task stopped**: `com.qlik.v1.di-projects.di-tasks.stopped`

For more information, see:

- [Creating and managing webhooks for workflows](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-webhooks.htm)
  on Qlik Help.
- [Monitoring system events](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-events.htm)
  on Qlik Help.
- The [Data integration projects API reference documentation](https://qlik.dev/apis/event/di-projects/).
