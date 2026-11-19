---
source: https://qlik.dev/apis/versioning/
last_updated: 2026-11-10T16:53:24+01:00
---

# API versioning

Qlik Cloud REST APIs and system events follow a quarterly, date-based versioning policy to help you manage
changes to your integrations.
API versions are released in February, May, August, and November, and use the `YYYY-MM` format.

REST APIs use the `qlik-api-version` header to indicate which API release an integration is aware of.
Deprecation warnings are communicated through response headers.
For system events, deprecations are documented in the AsyncAPI specs.

## How API versioning works

For REST APIs, specifying an API version does not select a different API request or response structure.
Instead, it tells Qlik which API release your integration is aware of, so Qlik can provide relevant deprecation
warnings.

Non-breaking changes, such as new endpoints, optional request parameters, and response properties, can be introduced at
any time. These changes are available to all REST API consumers, regardless of the version specified in their requests.

When existing functionality is deprecated, Qlik communicates the deprecation and its sunset date so you can update your
integration before the functionality is removed. Deprecated functionality may be removed on or after its sunset date,
regardless of the API version specified.

## Specify a REST API version

To specify an API version, include the `qlik-api-version` header in your request:

```bash
curl -i "https://<TENANT>.<REGION>.qlikcloud.com/api/core/auth-settings" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "qlik-api-version: 2026-11"
```

The header accepts a supported dated release, such as `2026-11`, or the special value `latest`.

Versioning applies to both namespaced APIs (`/api/<namespace>/...`) and legacy APIs (`/api/v1/...`).

Specify a dated API version rather than the `latest` value for all integrations.
This allows Qlik to identify deprecations introduced after the release your integration is aware of.

By default, `qlik-cli` and `@qlik/api` use the latest dated API version available when each tool version is released.
They do not use the `latest` header value.

### The `latest` header value

Set `qlik-api-version` to `latest` to acknowledge the most recent API release:

```bash
curl -i "https://<TENANT>.<REGION>.qlikcloud.com/api/core/auth-settings" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "qlik-api-version: latest"
```

When you use `latest`, your integration is considered aware of the most recent release.
You won't receive version-dependent deprecation warnings for response properties, but you can still receive warnings
when using deprecated endpoints or request parameters.

Using `latest` does not prevent deprecated functionality from being removed after its sunset date.

## Available versions and release schedule

Qlik releases API versions quarterly, in February, May, August, and November.

Each release is supported for 12 months, unless otherwise specified.

The following versions are supported from the November 2026 release:

| Version   | Supported until      |
| --------- | -------------------- |
| `2026-05` | Release of `2027-05` |
| `2026-08` | Release of `2027-08` |
| `2026-11` | Release of `2027-11` |

For REST APIs, a supported version does not guarantee that the API's request or response structure remains unchanged
throughout the support period.
Non-breaking changes can still be introduced, and deprecated functionality can be removed after its sunset date.

### Default and unsupported REST API versions

If you don't include the `qlik-api-version` header, Qlik uses the oldest supported release.

The same behavior applies when the requested version is malformed, unknown, not yet available, or no longer supported.

Requests are not rejected because of an invalid or unsupported version.
Instead, Qlik uses the oldest supported release as the acknowledged version.

For example, if `2026-05` is the oldest supported release, a request specifying `2026-02` falls back to `2026-05`.

### Check the accepted REST API version

REST API responses include the `qlik-api-version` header.
You can use it to check whether Qlik accepted your requested version or fell back to the oldest supported release.

For example, a request specifying an unsupported version might return:

```http
HTTP/1.1 200 OK
qlik-api-version: 2026-05
```

The status code depends on the API operation. An unsupported version does not itself cause an error.

When you request `latest`, the response header contains the corresponding dated release.

Check the response header, particularly when using an older version that may no longer be supported.

## Deprecation and sunset

Qlik uses deprecation periods to give you time to update integrations before functionality is removed.

For stable APIs, the deprecation period is at least 12 months, unless a shorter period is necessary for security
reasons.

Deprecated functionality remains available during the deprecation period. It may be removed on or after its sunset date.

### Deprecation information in API references and specs

Deprecated REST endpoints, parameters, response properties, and system events are identified in the API references.

For REST APIs, deprecation information may include a description and sunset release. For [system events](#system-events),
check the AsyncAPI spec for deprecation and sunset details that aren't displayed in the API reference.

You can download the OpenAPI or AsyncAPI spec from each API reference page. Deprecations are described using
the following extensions:

| Extension                       | Description                                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------- |
| `x-qlik-deprecated`             | Indicates that the endpoint, parameter, property, or event is deprecated.                |
| `x-qlik-deprecated-version`     | The API release (`YYYY-MM`) in which the deprecation period begins.                      |
| `x-qlik-deprecated-sunset`      | The earliest release (`YYYY-MM`) from which the deprecated functionality may be removed. |
| `x-qlik-deprecated-description` | The reason for the deprecation and replacement information, where provided.              |

Not all deprecated items currently include all four extensions. Check the relevant deprecation notices in the
[changelog](https://qlik.dev/changelog/) for additional information.

### REST API deprecation response headers

REST APIs use the following response headers to communicate deprecations:

| Header        | Description                                                                                                       |
| ------------- | ----------------------------------------------------------------------------------------------------------------- |
| `deprecation` | The date when the deprecation period begins, expressed as a Unix timestamp in HTTP Structured Fields date format. |
| `sunset`      | The earliest date from which deprecated functionality may be removed, expressed as an HTTP date.                  |
| `link`        | A link to more information about the deprecation, including migration guidance where available.                   |

The `sunset` header does not mean that functionality will be removed on that exact date. Removal may happen later.

### When deprecation headers are returned

For REST APIs, whether deprecation headers appear depends on what is deprecated:

- **Endpoint:** Headers are returned when you call a deprecated endpoint.
- **Request parameter:** Headers are returned when you use a deprecated parameter.
- **Response property:** Headers are returned when the API version your integration acknowledges predates the release
  in which the property was deprecated.

For response properties, Qlik uses the version header to determine whether your integration has acknowledged the
deprecation.

### Example: Response property deprecation

Consider an API response containing a `legacyName` property that is deprecated in the `2026-11` release, with a sunset
of `2027-11`.

The property remains available during the deprecation period, but the deprecation headers depend on which release your
integration acknowledges.

|                      | Older release         | Deprecation release   |
| -------------------- | --------------------- | --------------------- |
| Request version      | `2026-08`             | `2026-11`             |
| `deprecation` header | Returned              | Not returned          |
| `sunset` header      | Returned              | Not returned          |
| `link` header        | Returned              | Not returned          |
| Response body        | Includes `legacyName` | Includes `legacyName` |

For example, a request acknowledging `2026-08` receives a response similar to:

```http
HTTP/1.1 200 OK
qlik-api-version: 2026-08
deprecation: @1793491200
sunset: Mon, 01 Nov 2027 00:00:00 GMT
link: <DEPRECATION_URL>; rel="deprecation"; type="text/html"
content-type: application/json

{
  "id": "123",
  "legacyName": "Example",
  "displayName": "Example"
}
```

A request acknowledging `2026-11` receives the same response body, but without deprecation headers for `legacyName`,
because the integration is considered aware of the deprecation.

After the sunset date, Qlik may remove `legacyName` for all consumers, regardless of the version they specify.

*This example is illustrative. The property names and deprecation are not actual Qlik API changes.*

## Update your REST API version

Before updating the version acknowledged by your integration using the `qlik-api-version` header:

1. Review the [API changelog](https://qlik.dev/changelog/) and relevant deprecation notices.
2. Check whether your integration uses deprecated functionality.
3. Update your integration if necessary and test it against the current API behavior.
4. Change the version header to the newer release.
5. Continue monitoring deprecation and sunset headers.

Changing the version header does not switch to a different API implementation or restore removed functionality.
It updates which release your integration acknowledges and therefore which version-dependent deprecation warnings it
receives.

Update the version before its support period ends to avoid an automatic fallback to the oldest supported release.

## System events

Qlik Cloud system events follow the same quarterly release schedule and deprecation policy as REST APIs, but do not use
the `qlik-api-version` header.

Deprecated events and event payload properties are documented in the AsyncAPI specs, including the release in
which they were deprecated and their sunset date.

For more information, see [Qlik Cloud system events](https://qlik.dev/apis/event/).
