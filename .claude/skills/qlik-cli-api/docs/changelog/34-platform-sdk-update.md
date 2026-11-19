---
source: https://qlik.dev/changelog/34-platform-sdk-update/
last_updated: 2025-07-08T16:09:30Z
---

# Platform SDKs Update

Since the release of the Qlik Cloud platform SDKs earlier this year, the packages have recently been updated.
The idea with the Qlik Platform SDKs is to let developers extend solutions without the need
to develop them from scratch.

## Python SDK (v0.11.0)

- Feat: Allow full path in RAW rest calls.
  This feature in combination with interceptors unlocks QRS communication,
  for example:

```python
def inject_csrf_token(req):
    csrf_token = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    req.headers["x-qlik-xrfkey"] = csrf_token
    req.params["xrfkey"] = csrf_token
    return req
win_auth_instance = Auth(config=Config(
    api_key=qseow_api_key, host=qseow_host, auth_type=AuthType.APIKey))
win_auth_instance.rest.interceptors["request"].use(inject_csrf_token)
apps = win_auth_instance.rest(path=f"{qseow_host}qrs/apps/full")
```

### Feat: Added new APIs

- api-keys API

```python
apiKeys = ApiKeys(config=config)
keys = apiKeys.get_api_keys()
```

- audits API

```python
audits = Audits(config=config)
sources = audits.get_sources()
```

- Webhooks API

```python
qlik = Webhooks(config=config)
name = "qlik-sdk-py-test"
url = "https://your-tenant.qlikcloud.com/api/v1/automations/{automationId}/actions/execute"
eventTypes = ["com.qlik.v1.app.created", "com.qlik.v1.app.reload.finished"]
headers = {
    "X-Execution-Token": "lXw9BRm1Ba1bb6MOcPDewNvk5WUmdre70bHljfv1KzNMuby9YXwkUExrCgapxoxn"
}
hook = webhooks.create(
    Webhook(name=name, url=url, eventTypes=eventTypes, headers=headers)
)
```

- Quotas API

```python
quotas = Quotas(config=config)
data = quotas.get_quotas()
```

- Collections API

```python
 qlik = Qlik(config=config)
# create collection
collection = qlik.collections.create({"name": col_name, "type": "public"})
app = qlik.apps.create({"attributes": {"name": app_name}})
items = qlik.items.get_items(resourceType="app", resourceId=app.attributes.id)
itemId = items[0].id
# add item to collection
collection.create_item({"id": itemId})
```

- Automations API

```python
qlik = Qlik(config=config)
name = "test-sdk-py-" + str(uuid.uuid1())
# create
automation = automations.create(data=AutomationDetailRequestObject(name=name))
# run
automation.create_run(RunDetailRequestObject(context="detail"))
# list runs
runs = automation.get_runs()
# delete
automation.delete()
```

- Reload-Tasks API

```python
qlik = Qlik(config=config)
app = qlik.apps.create({"attributes": {"name": "app name"}})
# create
task = qlik.reload_tasks.create(
    PostTaskBody(
        appId=app.attributes.id,
        timeZone="Europe/Zurich",
        recurrence=[
            "RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO;BYHOUR=14;BYMINUTE=16;BYSECOND=0",
        ],
    )
)
# list reload tasks
tasks = qlik.reload_tasks.get_reload_tasks(appId=app.attributes.id)
# delete
task.delete()
```

### Docs

- Cleaned up README and dded more dev documents
- New example for auth flows
- Added engima examples in README.md

### Fixes

- Inline return objects are generated as dataclasses
- Allow sending dynamic properties for RPC
- Support nested array object

## Typescript SDK (v0.16.0)

- Feat: Allow user to use full patch for RAW calls.
  This feature in combination with interceptors unlocks QRS communication,
  For example:

```javascript
const injectXrfKey = ([url, config]) => {
  const _url = new URL(url);
  _url.searchParams.append("xrfkey", "ichBinEinBerlinR");
  const res = [
    _url.toString(),
    {
      ...config,
      headers: {
        "x-qlik-xrfkey": "ichBinEinBerlinR",
        ...config.headers,
      },
    },
  ];
  return res;
};
auth.rest.interceptors.request.use([injectXrfKey]);

const apps = await auth
  .rest(`https://win-server/jwt/qrs/app/full?filter=name eq '${appName}'`)
  .then((resp) => resp.json());
```

- Feat: Expose session events

```javascript
const session = await auth.rpc(appId);
session.on("traffic:sent", onTrafficSent);
session.on("traffic:received", (data: any) => {
  /** ... */
});
session.on("opened", onOpened);
session.on("notification:*", onNotification);
```

- Feat: Added Relaod-Tasks API

```javascript
const task = await reloadTasks.create({
  appId: app.attributes.id,
  timeZone: "Europe/Zurich",
  recurrence: [
    "RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO;BYHOUR=14;BYMINUTE=16;BYSECOND=0",
  ],
});
// list
const tasks = await reloadTasks.getReloadTasks({ appId: app.id });
```

- Feat: Enum values in method and class props and parameters

- Docs: Added engine examples to README.md

- Fix: set session on Qix returned Object Classes

- Fix: allow initiated objects

- Fix: request and response interceptors promises

- Refactor: EnigmaSession renamed to the more generic RpcSession

For more information see the package links below:

- Typescript (link removed since this SDK is deprecated)
- [Python](https://pypi.org/project/qlik-sdk/)

Please note that the Platform SDK packages are early development releases. So,
please expect breaking changes as it updates and stabilize.
