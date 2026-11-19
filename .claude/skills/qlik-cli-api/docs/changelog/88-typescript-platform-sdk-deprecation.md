---
source: https://qlik.dev/changelog/88-typescript-platform-sdk-deprecation/
last_updated: 2025-07-08T16:09:30Z
---

# Typescript Platform SDK deprecation

This changelog provides 60 days' deprecation notice of the Typescript version of
the Platform SDK. The library is being replaced with the Qlik API.

The Qlik API offers the same capabilities and access to Qlik Cloud REST APIs
and the Analytics engine, with the addition of officially supported Typescript
types.

Switching from the Platform SDK to the Qlik API is straightforward, requiring only a few modifications
to your code. The major change is in handling authentication when connecting
to your Qlik Cloud tenant.

Authentication with @qlik/api:

```javascript

//Backend applications
import { auth } from "@qlik/api";
auth.setDefaultHostConfig({
    authType: "oauth2",
    host: "<hostname>.<region>.qlikcloud.com",
    clientId: "<OAuth2_Client_ID>",
    clientSecret: "<OAuth2_Client_Secret>",    
  });

```

Authentication with Typescript Platform SDK:

```javascript
const Qlik = require('@qlik/sdk').default;
const { AuthType } = require("@qlik/sdk");

const config =  {
  authType: AuthType.OAuth2,
  host: "<hostname>.<region>.qlikcloud.com",
  clientId: "<OAuth2_Client_ID>",
  clientSecret: "<OAuth2_Client_Secret>",
};

(async () => {
  const qlik = new Qlik(config);
  await qlik.auth.authorize();
})();

```

For more information about @qlik/api, refer to
the [release changelog](https://qlik.dev/changelog/87-qlik-api-introduction/)
for `@qlik/api` or visit the toolkit page
at [qlik-api](https://qlik.dev/toolkits/qlik-api/).
