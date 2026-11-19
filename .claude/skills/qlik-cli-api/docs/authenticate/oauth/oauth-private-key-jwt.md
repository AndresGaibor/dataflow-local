---
source: https://qlik.dev/authenticate/oauth/oauth-private-key-jwt/
last_updated: 2026-09-23T12:07:01+02:00
---

# Authenticate with Private Key JWT

In this tutorial, you'll learn how to use Private Key JWT to authenticate your OAuth client application to Qlik Cloud
securely.

Instead of sharing a client secret, your application signs authentication requests with a private key, and Qlik Cloud
validates them using your registered public key.

This approach avoids using a shared client secret and is suitable for applications that can securely manage private
keys.

This tutorial uses a Web OAuth client with the `client_credentials` flow.

## What you'll learn

- How to generate a public/private key pair for OAuth authentication
- How to register your public key with an OAuth client in Qlik Cloud
- How to sign JWT assertions and request access tokens
- How to use tokens to authenticate API requests

## Prerequisites

- A Qlik Cloud tenant with Tenant Admin access
- OpenSSL installed on your development machine
- A programming language with the required libraries (JavaScript with `jose`, or Python with `PyJWT`,
  `cryptography`, and `requests`)

## How it works

Private Key JWT lets your application prove its identity using asymmetric cryptography instead of a shared secret:

1. You generate a public/private key pair and register the public key with your OAuth client in Qlik Cloud
2. Your application creates a JWT (JSON Web Token) signed with its private key
3. Your application sends the signed JWT to Qlik Cloud's token endpoint
4. Qlik Cloud validates the signature using your registered public key and returns an access token
5. Your application uses the access token for API requests

The private key remains with your application and is used to sign the JWT assertion. Qlik Cloud validates the
assertion using the registered public key.

## Step 1: Generate your key pair

Generate a public/private key pair that will be used to sign the JWT assertion
and register the public key with your OAuth client.

For this tutorial, use OpenSSL to generate a 2048-bit RSA key pair, the minimum key size for RS256:

```bash
openssl genrsa -out private_key.pem 2048
openssl rsa -in private_key.pem -pubout -out public_key.pem
```

For supported algorithms and production key-size guidance, see
[Private Key JWT reference](https://qlik.dev/authenticate/oauth/oauth-private-key-jwt-reference).

> **Warning:** Keep your private key (`private_key.pem` file) secure and never share it.
> It is used to sign JWT assertions.

Convert the public key from PEM to JSON Web Key (JWK) format using the `jose` package:

```js
import { exportJWK, importSPKI } from 'jose';
import { readFileSync } from 'node:fs';

const KEY_ID = 'my-key-1';

const pem = readFileSync('public_key.pem', 'utf8');
const key = await importSPKI(pem, 'RS256');
const jwk = await exportJWK(key);
jwk.alg = 'RS256';
jwk.use = 'sig';
jwk.kid = KEY_ID;
console.log(JSON.stringify(jwk, null, 2));
```

```python
import json

from cryptography.hazmat.primitives import serialization
from jwt.algorithms import RSAAlgorithm

KEY_ID = 'my-key-1'

with open('public_key.pem', 'rb') as f:
    public_key = serialization.load_pem_public_key(f.read())

jwk = RSAAlgorithm.to_jwk(public_key, as_dict=True)
jwk.update({
    'alg': 'RS256',
    'use': 'sig',
    'kid': KEY_ID,
})

print(json.dumps(jwk, indent=2))
```

Save the JWK output. You'll register it with your OAuth client in the next step.

> **Tip:** For other algorithms (RS512, ES384), see [Supported algorithms](https://qlik.dev/authenticate/oauth/oauth-private-key-jwt-reference#supported-algorithms) in the reference.

## Step 2: Create and configure your Web OAuth client

Now that you have your public key in JWK format, create a new Web OAuth client and register it.

1. In the Administration activity center, go to **OAuth**.

2. Select **Create new**, then **Web** as the client type.

3. Enter a name.

4. Select the `user_default` scope.

5. Under **Authentication method**, select **Private Key JWT**.

6. Paste your JWK (from Step 1) into the **Public key** field.

   > **Warning:** Paste only the public key in JWK format. Never upload or share your private key.

7. For the `client_credentials` flow used in this tutorial, select the **Machine-to-machine** checkbox.

8. Select **Create**.

9. Copy your **Client ID** for use in the next step.

10. Set the consent method to **Trusted** (select the action menu and select **Change consent method**).

Your OAuth client is now configured for Private Key JWT authentication.

Qlik Cloud will validate JWT signatures against this public key during token requests.

## Step 3: Request an access token

To request an access token, first generate a signed JWT assertion, then send the assertion to the token endpoint.

### Generate the JWT assertion

Use your private key to create a signed JWT assertion:

```js
import { SignJWT, importPKCS8 } from 'jose';
import { randomUUID } from 'node:crypto';
import { readFileSync } from 'node:fs';

const TENANT = '<TENANT>';
const CLIENT_ID = '<CLIENT_ID>';
const KEY_ID = 'my-key-1';
const PRIVATE_KEY_PEM = readFileSync('private_key.pem', 'utf8');

try {
  const privateKey = await importPKCS8(PRIVATE_KEY_PEM, 'RS256');
  const now = Math.floor(Date.now() / 1000);

  const assertion = await new SignJWT({})
    .setProtectedHeader({ alg: 'RS256', kid: KEY_ID })
    .setIssuer(CLIENT_ID)
    .setSubject(CLIENT_ID)
    .setAudience(`https://${TENANT}.qlikcloud.com/oauth/token`)
    .setJti(randomUUID())
    .setIssuedAt(now)
    .setExpirationTime(now + 300)
    .sign(privateKey);

  console.log(assertion);
} catch (error) {
  console.error('Failed to generate JWT:', error.message);
}
```

```python
import time
import uuid
import jwt

TENANT = '<TENANT>'
CLIENT_ID = '<CLIENT_ID>'
KEY_ID = 'my-key-1'

try:
    with open('private_key.pem', 'rb') as f:
        private_key = f.read()

    now = int(time.time())
    payload = {
        'iss': CLIENT_ID,
        'sub': CLIENT_ID,
        'aud': f'https://{TENANT}.qlikcloud.com/oauth/token',
        'jti': str(uuid.uuid4()),
        'iat': now,
        'exp': now + 300,
    }
    assertion = jwt.encode(
        payload,
        private_key,
        algorithm='RS256',
        headers={'kid': KEY_ID},
    )

    print(assertion)
except Exception as error:
    print(f'Failed to generate JWT: {error}')
```

Copy the output (your signed JWT assertion). You'll use it to request an access token in the next section.

### Exchange the assertion for a token

Send your JWT assertion to the Qlik Cloud token endpoint. Use one of the methods below:

```js
const TENANT = '<TENANT>';
const CLIENT_ID = '<CLIENT_ID>';
const assertion = '<SIGNED_JWT_ASSERTION>';  // From previous step

try {
  const response = await fetch(
    `https://${TENANT}.qlikcloud.com/oauth/token`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        grant_type: 'client_credentials',
        client_id: CLIENT_ID,
        client_assertion_type:
          'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
        client_assertion: assertion,
        scope: 'user_default',
      }),
    }
  });

  if (!response.ok) {
    throw new Error(`Token request failed: ${response.status} ${response.statusText}`);
  }

  const data = await response.json();
  console.log(data.access_token);
} catch (error) {
  console.error('Authentication failed:', error.message);
}
```

```python
import requests

TENANT = '<TENANT>'
CLIENT_ID = '<CLIENT_ID>'
assertion = '<SIGNED_JWT_ASSERTION>'  # From previous step

try:
    response = requests.post(
        f'https://{TENANT}.qlikcloud.com/oauth/token',
        data={
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_assertion_type': 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
            'client_assertion': assertion,
            'scope': 'user_default',
        },
    )

    if response.status_code != 200:
        raise Exception(f'Token request failed: {response.status_code} {response.reason}')

    print(response.json()['access_token'])
except Exception as error:
    print(f'Authentication failed: {error}')
```

```bash
curl -X POST "https://<TENANT>.qlikcloud.com/oauth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=<CLIENT_ID>" \
  -d "client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer" \
  -d "client_assertion=<SIGNED_JWT_ASSERTION>" \
  -d "scope=user_default"
```

A successful response returns your access token:

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_at": "2026-01-15T18:24:31.000Z",
  "expires_in": 21600,
  "scope": "user_default"
}
```

## Use the token in API requests

Add your access token to the `Authorization` header:

```js
const response = await fetch(`https://${TENANT}.qlikcloud.com/api/v1/users/me`, {
  headers: {
    'Authorization': `Bearer ${access_token}`,
  },
});
const user = await response.json();
console.log(user);
```

```python
response = requests.get(
    f'https://{TENANT}.qlikcloud.com/api/v1/users/me',
    headers={'Authorization': f'Bearer {access_token}'}
)
print(response.json())
```

```bash
curl -L https://<TENANT>.qlikcloud.com/api/v1/users/me \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

## Troubleshooting

Private Key JWT authentication failures return `401 Unauthorized` with a detail field describing the failure
and an error code.

| Error detail                                                                    | Error code | Cause                                                                                      | Solution                                                                                  |
| ------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| **No matching public key found**                                                | `OAUTH-16` | The `kid` header is missing, or no registered JWK matches that `kid` and `alg`.            | Set `kid` to the `kid` of the registered JWK and make sure `alg` matches.                 |
| **JWT Verification failed: Assertion failure on claim 'aud'**                   | `OAUTH-16` | `aud` does not match your tenant token endpoint.                                           | Set `aud` to `https://<TENANT>.qlikcloud.com/oauth/token`.                                |
| **JWT Verification failed: Unexpected issuer**                                  | `OAUTH-16` | `iss` does not match your client ID.                                                       | Set `iss` to your OAuth client ID.                                                        |
| **JWT Verification failed: Assertion failure on claim 'sub'**                   | `OAUTH-16` | `sub` does not match your client ID.                                                       | Set `sub` to your OAuth client ID.                                                        |
| **JWT Verification failed: Assertion lifetime exceeds maximum of 3600 seconds** | `OAUTH-16` | `exp - iat` is greater than 3600 seconds.                                                  | Shorten the assertion lifetime to 3600 seconds or less.                                   |
| **Invalid authentication method used for client**                               | `OAUTH-47` | `client_assertion_type` is incorrect, or the client is not configured for Private Key JWT. | Use the documented `client_assertion_type` and select **Private Key JWT** for the client. |

For supported signing algorithms, JWT requirements, and JWK specifications, see
[Private Key JWT reference](https://qlik.dev/authenticate/oauth/oauth-private-key-jwt-reference).

## Next steps

- [Private Key JWT reference](https://qlik.dev/authenticate/oauth/oauth-private-key-jwt-reference): Algorithms and JWK specifications
- [OAuth API](https://qlik.dev/apis/rest/oauth/): Reference for the `/oauth/token` endpoint, request parameters, and responses
- [Create an OAuth2 client](https://qlik.dev/authenticate/oauth/create/create-oauth-client/): Set up a new OAuth client
- [OAuth scopes](https://qlik.dev/authenticate/oauth/scopes): Understand permissions and scope requirements
