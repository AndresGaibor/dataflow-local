---
source: https://qlik.dev/changelog/39-api-updates-brands/
last_updated: 2025-07-08T16:09:30Z
---

# New API & tutorial - Brands

### Brands API

For Qlik customers deploying an OEM use case, Qlik Cloud can be branded to improve
alignment with your own portal, software, or brand, reducing friction for your
end users as they swap between experiences.

The [`brands`](https://qlik.dev/apis/rest/brands) API allows you to provide a custom logo and
favicon to help enhance this user experience for your users.

The new API at [`brands`](https://qlik.dev/apis/rest/brands) supports the creation and management
of brands in the tenant.

> **Important:** Use of the brands API is permitted for OEM use cases only.

- `POST/v1/brands` : Create a new brand

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/brands" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: multipart/form-data" \
 -F "logo=@/path/to/file" \
 -F "styles=@/path/to/file" \
 -F "favIcon=@/path/to/file"
```

See full API reference [here](https://qlik.dev/apis/rest/brands), or review
the full tutorial [here](https://qlik.dev/manage/platform-operations/brand-a-tenant).
