---
source: https://qlik.dev/changelog/92-nebula-v5-typings/
last_updated: 2025-07-08T16:09:30Z
---

# nebula.js version 5 released

The [nebula.js](https://qlik.dev/apis/javascript/nebula-js/) extension and mashup library
has been updated to version 5, the next major version.

Users of versions prior to 5.0.0 should be aware of important changes to:

- Type updates which align nebula with other Qlik tools
- Expanded support for multi-app mashups and web apps
- Updated OAuth support for Qlik Cloud

## Type updates

To improve compatibility with other Qlik tools, simplify developer onboarding,
and enhance the TypeScript experience,
Nebula now uses the [@qlik/api](https://qlik.dev/toolkits/qlik-api/) typings for QIX and Engine entities.

## Multi-app support fix

This update changes how Nebula handles its cache. Building mashups using
multiple app connections at the same time now works without interference. Previously, a
common cache was used between instances, which could cause issues if apps shared a data
model or if they where duplicates of each other.

## Nebula serve updates

The connection setup in nebula serve was updated to improve compatibility with
the Qlik Cloud OAuth setup. If you've used this capability before, you need to update
the redirect URL to `http://localhost:8000/auth/login/callback`.

See nebula.js on [npm](https://www.npmjs.com/package/@nebula.js/stardust).
