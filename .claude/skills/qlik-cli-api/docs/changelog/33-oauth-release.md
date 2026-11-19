---
source: https://qlik.dev/changelog/33-oauth-release/
last_updated: 2023-11-29T15:53:15+01:00
---

# OAuth has been released

## OAuth 2.0 Authorization

OAuth is a standard security protocol for authorization and delegation.
It allows third party applications to access API resources without disclosing
the end-user credentials.

Qlik Cloud supports OAuth 2.0 Authorization Code and Client Credentials flows.
The OAuth client can obtain an authorization code or send client credentials header
to exchange it with an access token that can be used to access Qlik Cloud APIs.

- Create OAuth in client
  [see tutorial here](https://qlik.dev/tutorials/create-an-oauth-client)

Alongside this delivery you will also get OAuth support for tools and libraries.

- OAuth in Qlik-Cli
  To quickly get started, you can use the qlik-cli command `qlik context init` for more
  details, read the [get started](https://qlik.dev/toolkits/qlik-cli/#get-started)
  section in the Qlik-Cli overview page or the
  [using OAuth clients with Qlik-Cli](https://qlik.dev/tutorials/get-started-with-oauth-machine-to-machine#using-oauth-clients-with-qlik-cli)
  section in
  [Get started with OAuth machine-to-machine](https://qlik.dev/tutorials/get-started-with-oauth-machine-to-machine#using-oauth-clients-with-qlik-cli)
  tutorial.

- Platform SDKs
  Back-end application, front-end application, Python or Javascript? no problem.
  You can find a simple example using `enigma.js` in the
  [Platform SDKs overview page](https://qlik.dev/libraries-and-tools/platform-sdk/#oauth2)
  or in the [Using OAuth clients with Qlik Platform SDKs](https://qlik.dev/tutorials/get-started-with-oauth-machine-to-machine/#using-oauth-clients-with-qlik-platform-sdks)
  section

Full tutorial OAuth single page applications with nebula.js can be found [here](https://qlik.dev/tutorials/build-a-simple-oauth-single-page-application)

- Capability APIs?
  Already have a `Client Id`? just switch the `webIntegrationId` config with the `clientId` instead,
  that's it. See example code in the
  [Build a simple mashup using capability APIs](https://qlik.dev/tutorials/build-a-simple-mashup-using-capability-apis#configure-your-qlik-sense-saas-tenant)
  tutorial.
