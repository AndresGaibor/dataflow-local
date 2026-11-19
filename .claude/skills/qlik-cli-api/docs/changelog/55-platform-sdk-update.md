---
source: https://qlik.dev/changelog/55-platform-sdk-update/
last_updated: 2025-07-08T16:09:30Z
---

# Platform SDKs Update - August 2023

## Typescript v0.24.0: New API Intakes and Maintenance

### feat: Intake Brands API

The \[`brands`] API supports the creation and management
of brands in the tenant. This allows you to provide a custom logo and
favicon to help you enhance the user experience for your users.
Below is an example of how you can use the API.

> **Important:** Use of the brands API is permitted for OEM use cases only.

```ts
const qlik = new Qlik({...});
// upload a new logo
const logo = fs.readFileSync(path.join(__dirname, 'assets/logo.png'));
const brand = await qlik.brands.create(logo, 'my_awesome_logo');
// activate/deactivate and delete
await qlik.brands.activate(brand.id);
await qlik.brands.deactivate(brand.id);
await qlik.brands.delete(brand.id);
```

See full API reference [here](https://qlik.dev/apis/rest/brands)

### feat: Intake Tenants API

```ts
const { tenants, users } = new Qlik({...});
// checks tenant/me
const { id } = await tenants.getMe();
const { tenantId } = await users.getMe();

// get a tenant & update settings
let tenant = await tenants.get(id);
const orgEnableAnalyticCreationSettings = tenant.enableAnalyticCreation;
await tenant.patch([{ op: 'replace', path: '/enableAnalyticCreation', value: !orgEnableAnalyticCreationSettings }]);
```

See full API reference [here](https://qlik.dev/apis/rest/tenants)

### Bugfixes

- ⚠️ Breaking - fix: method name fixes in various APIs

```ts
// example method name changes:
app.recommendInsightAnalyses(...); // was previously app.recommend(...)
automation.retryRun(...); // was previously automation.retry(...)
// & some plural/singular fixes
collections.getFavorites(); // was previously collections.getFavorite()
webhook.getDelivery(...); // was previously webhook.getDeliverie(...)
```

### Other Fixes

- fix: render inline response object
- fix: random nbr in group test by
- fix: bump spectacular.ts to latest

To get started with the Qlik Typescript SDK, [click here](https://www.npmjs.com/package/@qlik/sdk)

## Python v0.16.0: New API Intakes and Fixes

### feat: Intake for Brands API

```py
brands = Brands(config=config)
# create upload logo to your tenant
file_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(file_dir, "logo.png")
with open(logo_path, "rb") as logo_file:
    brand = brands.create(logo=logo_file, name="my_awesome_logo")
# get / activate / deactivate
brands.get(brand_id=brand.id)
brands.activate(brand_id=brand.id)
brands.deactivate(brand_id=brand.id)
```

See full API reference [here](https://qlik.dev/apis/rest/brands)

### feat: Tenants API

```py
tenants = Tenants(config=config)
# fetch information about your tenant
my_tenant = tenants.get_me()

# change settings
tenant_analytic_creation_setting = my_tenant.enableAnalyticCreation
my_tenant.patch(
    data=[
        {
            "op": "replace",
            "path": "/enableAnalyticCreation",
            "value": True,
        }
    ]
)
```

See full API reference [here](https://qlik.dev/apis/rest/tenants)

### feat: Intake for Notes API

```py
notes = Notes(config=config)
# fetch notes settings
notes_settings = notes.get_settings()
# set settings programmatically
notes.set_settings(data={"toggledOn": True, "snapshotRelations": True})
```

### fix: \[breaking change] variouse plurals/singular method names fixes

```py
# webhooks.get_deliverie(..) changed to:
webhooks.get_delivery(..)
# collections.get_favorite(..) is now:
collections.get_favorites(..)
# and more
```

See full API reference [here](https://qlik.dev/apis/rest/notes)

To get started with the Qlik Python SDK, [click here](https://pypi.org/project/qlik-sdk/)
