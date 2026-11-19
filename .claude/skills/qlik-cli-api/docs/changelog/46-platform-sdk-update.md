---
source: https://qlik.dev/changelog/46-platform-sdk-update/
last_updated: 2025-03-11T11:54:24Z
---

# Platform SDKs Update - June 2023

## Typescript 0.23.0: Browser friendly library

⚠️ Breaking - in this release all the data structures are now type aliases
previously they were data classes

```ts
// previously
import { GenericSheetProperties } from '@qlik/sdk';
const sheetProperties = new GenericSheetProperties({...});

// now
import type { GenericSheetProperties } from '@qlik/sdk';
const sheetProperties: GenericSheetProperties = {...};
```

This change reduces drastically the bundle size of the library making it more optimized for browsers.

- feat: notes settings API

```ts
import { Notes } from '@qlik/sdk';
const notes = new Notes({...});
await notes.setSettings({ toggledOn: true });
```

- feat: transport API email-config

```ts
import { Transports } from '@qlik/sdk';
const transports = new Transports({...});
const emailConfig = await transports.getEmailConfig();
const validated = await transports.validate();
```

- feat: apps API - change-owner on objects

```ts
// create a sheet
const sheet = await app.createSheet({ qMetaDef:{ title: 'temp sheet' } });
// change owner of the sheet
await app.changeOwner(sheet.id, { ownerId: anotherUser.id });
```

- feat: groups API - create groups

You can now create groups using directly the groups API

```ts
import Qlik from '@qlik/cli';

const { roles, groups } = new Qlik({...});
// fetch the tenant admin role
const [ tenantAdminRole ] = await roles.getRoles({ filter: 'name eq "TenantAdmin"' });
// create group named avengers with tenant admin role
await groups.create({name: 'avengers', assignedRoles:[{id: tenantAdminRole.id}]})
// fetch the groups
const groups = await groups.getGroups({ filter: 'name eq "avengers"' });
```

- feat: users API - invite user

```ts
const users = new Users({...});
// resend an invitation in swedish
await users.invite({ invitees:[{ email: 'tom.hanks@qlik.com', resend: true, language: 'sv' }] });
```

- fix: allow using limit from query param for pagination

## Python 0.15.0: API updates

- feat: users API - update

```py
qlik = Qlik(config=config)
# resend an invite to a user in your tenant
qlik.users.invite(
    InviteRequest(
        invitees=[{email: "tom_hanks@qlik.com", language: "sv", resend: true}]
    )
)
```

- feat: groups API - updates

You can now create a groups:

```py
qlik = Qlik(config=config)
tenant_admin_role = qlik.roles.get_roles(filter='name eq "TenantAdmin"')
# create group
data = GroupPostSchema(name="avengers", assignedRoles={ "id": tenant_admin_role[0].id})
new_group = qlik.groups.create(data=data)
# delete group
group = qlik.groups.get(groupId=new_group.id)
group.delete()
```

- feat: apps API - new features

insight analysis: you now can list ()`app.get_insight_analyses()`) and get recommendations (`recommend`)
from insight advisor through APIs

change the ownership of generic objects

```py
app.change_owner(objectId = 'objectId', data = { ownerId: 'userId' })
```

- feat: transport API email-config

```py
config = Config(
    host=self.base_url, auth_type=AuthType.APIKey, api_key=self.api_key
)
q = Qlik(config=config)
email_config = q.transports.get_email_config()
validation = q.transports.validate()
```

- fix: handle properties with leading numbers
- fix: response type as requests.response
