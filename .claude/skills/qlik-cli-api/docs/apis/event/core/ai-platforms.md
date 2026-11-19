---
source: https://qlik.dev/apis/event/core/ai-platforms/
last_updated: 2026-09-30T18:04:09+02:00
---

# Ai platforms

## Table of Contents

### system-events.ai-platform

- [com.qlik.core.ai-platform.conversations-job.finished](#comqlikcoreai-platformconversations-jobfinished)

## Events published on the `system-events.ai-platform` channel

### com.qlik.core.ai-platform.conversations-job.finished

**Title:** Conversations finished

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

This event will be published when conversations have been received from the LLM provider.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.core.ai-platform.conversations-job.finished". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `host` | `string` | No | Unique identifier for the host related to the event. |
| `reason` | `string` | No | Reason associated with the occurrence, when applicable. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `ownerid` | `string` | No | Unique identifier for the owner related to the event. |
| `spaceid` | `string` | No | Unique identifier for the space related to the event. |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | Unique identifier for the client related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing the impersonating entity (the JWT "act" claim), if any. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `toplevelresourceid` | `string` | No | If the event originated from a sub resource the toplevelresourceid MUST contain the id of the top level resource associated with the sub resource. If the event originated from a top level resource it MUST NOT be defined. |
| `data` | `conversationFinishedData` | No | Conversations finished event specific data. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | A unique identifier for the completion. |
| `cost` | `cost` | No | Estimated token cost in USD. When per-token pricing is configured for the model, the object contains input, output, and total cost values. When pricing is not configured for the model, this property is omitted entirely. Prompt-cache token pricing is not included. |
| `_meta` | `metaClaims` | No | Internal metadata associated with the request. |
| `jobId` | `string` | No | Optional RFS job ID forwarded from the X-Qlik-RFS-JobID request header to correlate triggered and finished events. |
| `model` | `string` | No | The model used for conversation. |
| `usage` | `usage` | No | Token usage for a conversations response, including optional prompt-cache token counts. |
| `callId` | `string` | No | The call ID associated with this request. |
| `object` | `string` | Yes | The object type. Always set to conversation. |
| `choices` | `object[]` | Yes | A list of conversation choices. |
| `traceId` | `string` | No | The trace ID associated with this request. |
| `createdAt` | `integer` | Yes | Unix timestamp of when the response was generated. |
| `systemFingerprint` | `string \| null` | No | This fingerprint represents the backend configuration that the model runs with. |
| `performanceMetrics` | `performanceMetrics` | No | Only present on streaming requests. |

<details>
<summary>Properties of `cost`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `inputCost` | `string` | No | Cost of prompt/input tokens in USD. |
| `totalCost` | `string` | No | Sum of inputCost and outputCost. |
| `outputCost` | `string` | No | Cost of completion/output tokens in USD. |

</details>

<details>
<summary>Properties of `_meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `act` | `authclaims` | No | Details of the impersonating entity. |
| `aud` | `string[]` | No | Audience(s) the JWT was issued for. |
| `iss` | `string` | No | Issuer of the principal's identity. |
| `sid` | `string` | No | ID of the session associated with this JWT, if any. |
| `sub` | `string` | No | Subject of the principal's identity. |
| `level` | `string` | No | Access level of the principal. |
| `userId` | `string` | No | Internal ID of the user making the request. Present when subType is "user". |
| `subType` | `string` | No | Type of the principal's subject. |
| `clientId` | `string` | No | ID of the client making the request. |
| `tenantId` | `string` | No | Internal ID of the tenant to restrict access to. |
| `licenseId` | `string` | No | License ID associated with the principal. |
| `parentLicenseId` | `string` | No | Parent license ID associated with the principal. |

<details>
<summary>Properties of `act`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `usage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalTokens` | `integer` | Yes | Addition of the completion and prompt tokens. |
| `promptTokens` | `integer` | Yes | Tokens explicitly provided as input to the model. |
| `completionTokens` | `integer` | Yes | Tokens generated by the model in response to the input. |
| `cacheReadInputTokens` | `integer` | No | Tokens read from the prompt cache. |
| `cacheWriteInputTokens` | `integer` | No | Tokens written to the prompt cache. |

</details>

<details>
<summary>Properties of `choices`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `index` | `integer` | Yes | Position of a specific token within the generated output. Each token in the model's response has an associated index, starting from 0. |
| `message` | `conversationMessage` | No | Individual communication within a conversation. This field (along with toolCalls/functionCall and any other generated content) is redacted and is never present on the published event; it is documented here only for historical/reference purposes. |
| `finishReason` | `string` | Yes | Reason why a model's response generation process ended. |

<details>
<summary>Properties of `message`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `performanceMetrics`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ttft` | `string \| null` | Yes | Time to first token (TTFT) in seconds. Null when timing data is unavailable. |
| `endTime` | `string` | Yes | Finishing time of the task. |
| `startTime` | `string` | Yes | Starting time of the task. |
| `totalTime` | `string \| null` | Yes | Total time of the task in seconds. Null when timing data is unavailable. |
| `inferenceSpeed` | `string \| null` | Yes | Tokens per second generated by the model in response to the input. Null when timing data is unavailable. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2023-01-01T12:00:00Z",
  "type": "com.qlik.core.ai-platform.conversations-job.finished",
  "source": "com.qlik/ai-platform",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "host": "ai-platform-llm-gateway-844db7d4c7-4glrb",
  "reason": "string",
  "userid": "00000000-0000-0000-0000-000000000000",
  "ownerid": "00000000-0000-0000-0000-000000000000",
  "spaceid": "00000000-0000-0000-0000-000000000000",
  "authtype": "user",
  "clientid": "00000000-0000-0000-0000-000000000000",
  "tenantid": "00000000-0000-0000-0000-000000000000",
  "sessionid": "00000000-0000-0000-0000-000000000000",
  "authclaims": "{\"sub\":\"1234567890\",\"subType\":\"user\",\"iss\":\"qlik.api.internal\"}",
  "tracestate": "congo=t61rcWkgMzE",
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "toplevelresourceid": "id123",
  "data": {
    "id": "converse-393592ed-ca78-4740-aa87-0ca97480706f",
    "cost": {
      "inputCost": "0.000300",
      "totalCost": "0.003300",
      "outputCost": "0.003000"
    },
    "model": "anthropic.claude-3-sonnet-20240229-v1:0",
    "usage": {
      "totalTokens": 238,
      "promptTokens": 16,
      "completionTokens": 222
    },
    "object": "conversation",
    "createdAt": 1728909071,
    "systemFingerprint": null,
    "performanceMetrics": {
      "ttft": "0.57",
      "endTime": "2024-07-10T15:48:30.416262",
      "startTime": "2024-07-10T15:48:21.598495",
      "totalTime": "8.82",
      "inferenceSpeed": "34.5"
    }
  }
}
```


## Schemas

### authclaims

Details of the impersonating entity (the JWT "act" claim), present when the request was made on behalf of another principal.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `iss` | `string` | No | Issuer of the impersonating entity's identity. |
| `sub` | `string` | No | Subject of the impersonating entity. |
| `subType` | `string` | No | Type of the impersonating entity's subject. |



### cloudEventsContextAttributes

CloudEvents Specification JSON Schema

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `host` | `string` | No | Unique identifier for the host related to the event. |
| `reason` | `string` | No | Reason associated with the occurrence, when applicable. |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `ownerid` | `string` | No | Unique identifier for the owner related to the event. |
| `spaceid` | `string` | No | Unique identifier for the space related to the event. |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `clientid` | `string` | No | Unique identifier for the client related to the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `authclaims` | `string` | No | A JSON string representing the impersonating entity (the JWT "act" claim), if any. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `toplevelresourceid` | `string` | No | If the event originated from a sub resource the toplevelresourceid MUST contain the id of the top level resource associated with the sub resource. If the event originated from a top level resource it MUST NOT be defined. |



### conversationChoices

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `index` | `integer` | Yes | Position of a specific token within the generated output. Each token in the model's response has an associated index, starting from 0. |
| `message` | `conversationMessage` | No | Individual communication within a conversation. This field (along with toolCalls/functionCall and any other generated content) is redacted and is never present on the published event; it is documented here only for historical/reference purposes. |
| `finishReason` | `string` | Yes | Reason why a model's response generation process ended. |

<details>
<summary>Properties of `message`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `role` | `string` | Yes | The role of the message sender, either "user" or "assistant". Allowed values: user \| assistant. |

</details>



### conversationFinishedData

Conversations finished operation specific data.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | A unique identifier for the completion. |
| `cost` | `cost` | No | Estimated token cost in USD. When per-token pricing is configured for the model, the object contains input, output, and total cost values. When pricing is not configured for the model, this property is omitted entirely. Prompt-cache token pricing is not included. |
| `_meta` | `metaClaims` | No | Internal metadata associated with the request. |
| `jobId` | `string` | No | Optional RFS job ID forwarded from the X-Qlik-RFS-JobID request header to correlate triggered and finished events. |
| `model` | `string` | No | The model used for conversation. |
| `usage` | `usage` | No | Token usage for a conversations response, including optional prompt-cache token counts. |
| `callId` | `string` | No | The call ID associated with this request. |
| `object` | `string` | Yes | The object type. Always set to conversation. |
| `choices` | `object[]` | Yes | A list of conversation choices. |
| `traceId` | `string` | No | The trace ID associated with this request. |
| `createdAt` | `integer` | Yes | Unix timestamp of when the response was generated. |
| `systemFingerprint` | `string \| null` | No | This fingerprint represents the backend configuration that the model runs with. |
| `performanceMetrics` | `performanceMetrics` | No | Only present on streaming requests. |

<details>
<summary>Properties of `cost`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `inputCost` | `string` | No | Cost of prompt/input tokens in USD. |
| `totalCost` | `string` | No | Sum of inputCost and outputCost. |
| `outputCost` | `string` | No | Cost of completion/output tokens in USD. |

</details>

<details>
<summary>Properties of `_meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `act` | `authclaims` | No | Details of the impersonating entity. |
| `aud` | `string[]` | No | Audience(s) the JWT was issued for. |
| `iss` | `string` | No | Issuer of the principal's identity. |
| `sid` | `string` | No | ID of the session associated with this JWT, if any. |
| `sub` | `string` | No | Subject of the principal's identity. |
| `level` | `string` | No | Access level of the principal. |
| `userId` | `string` | No | Internal ID of the user making the request. Present when subType is "user". |
| `subType` | `string` | No | Type of the principal's subject. |
| `clientId` | `string` | No | ID of the client making the request. |
| `tenantId` | `string` | No | Internal ID of the tenant to restrict access to. |
| `licenseId` | `string` | No | License ID associated with the principal. |
| `parentLicenseId` | `string` | No | Parent license ID associated with the principal. |

<details>
<summary>Properties of `act`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `iss` | `string` | No | Issuer of the impersonating entity's identity. |
| `sub` | `string` | No | Subject of the impersonating entity. |
| `subType` | `string` | No | Type of the impersonating entity's subject. |

</details>

</details>

<details>
<summary>Properties of `usage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalTokens` | `integer` | Yes | Addition of the completion and prompt tokens. |
| `promptTokens` | `integer` | Yes | Tokens explicitly provided as input to the model. |
| `completionTokens` | `integer` | Yes | Tokens generated by the model in response to the input. |
| `cacheReadInputTokens` | `integer` | No | Tokens read from the prompt cache. |
| `cacheWriteInputTokens` | `integer` | No | Tokens written to the prompt cache. |

</details>

<details>
<summary>Properties of `choices`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `index` | `integer` | Yes | Position of a specific token within the generated output. Each token in the model's response has an associated index, starting from 0. |
| `message` | `conversationMessage` | No | Individual communication within a conversation. This field (along with toolCalls/functionCall and any other generated content) is redacted and is never present on the published event; it is documented here only for historical/reference purposes. |
| `finishReason` | `string` | Yes | Reason why a model's response generation process ended. |

<details>
<summary>Properties of `message`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `role` | `string` | Yes | The role of the message sender, either "user" or "assistant". Allowed values: user \| assistant. |

</details>

</details>

<details>
<summary>Properties of `performanceMetrics`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ttft` | `string \| null` | Yes | Time to first token (TTFT) in seconds. Null when timing data is unavailable. |
| `endTime` | `string` | Yes | Finishing time of the task. |
| `startTime` | `string` | Yes | Starting time of the task. |
| `totalTime` | `string \| null` | Yes | Total time of the task in seconds. Null when timing data is unavailable. |
| `inferenceSpeed` | `string \| null` | Yes | Tokens per second generated by the model in response to the input. Null when timing data is unavailable. |

</details>



### conversationMessage

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `role` | `string` | Yes | The role of the message sender, either "user" or "assistant". Allowed values: user \| assistant. |



### conversationUsage

Token usage for a conversations response, including optional prompt-cache token counts.

**Type:** `usage`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalTokens` | `integer` | Yes | Addition of the completion and prompt tokens. |
| `promptTokens` | `integer` | Yes | Tokens explicitly provided as input to the model. |
| `completionTokens` | `integer` | Yes | Tokens generated by the model in response to the input. |
| `cacheReadInputTokens` | `integer` | No | Tokens read from the prompt cache. |
| `cacheWriteInputTokens` | `integer` | No | Tokens written to the prompt cache. |



### cost

Estimated token cost in USD. When per-token pricing is configured for the model, the object contains input, output, and total cost values. When pricing is not configured for the model, this property is omitted entirely. Prompt-cache token pricing is not included.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `inputCost` | `string` | No | Cost of prompt/input tokens in USD. |
| `totalCost` | `string` | No | Sum of inputCost and outputCost. |
| `outputCost` | `string` | No | Cost of completion/output tokens in USD. |



### metaClaims

PII-safe subset of the JWT claims of the principal that triggered the event, propagated internally as request metadata.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `act` | `authclaims` | No | Details of the impersonating entity. |
| `aud` | `string[]` | No | Audience(s) the JWT was issued for. |
| `iss` | `string` | No | Issuer of the principal's identity. |
| `sid` | `string` | No | ID of the session associated with this JWT, if any. |
| `sub` | `string` | No | Subject of the principal's identity. |
| `level` | `string` | No | Access level of the principal. |
| `userId` | `string` | No | Internal ID of the user making the request. Present when subType is "user". |
| `subType` | `string` | No | Type of the principal's subject. |
| `clientId` | `string` | No | ID of the client making the request. |
| `tenantId` | `string` | No | Internal ID of the tenant to restrict access to. |
| `licenseId` | `string` | No | License ID associated with the principal. |
| `parentLicenseId` | `string` | No | Parent license ID associated with the principal. |

<details>
<summary>Properties of `act`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `iss` | `string` | No | Issuer of the impersonating entity's identity. |
| `sub` | `string` | No | Subject of the impersonating entity. |
| `subType` | `string` | No | Type of the impersonating entity's subject. |

</details>



### performanceMetrics

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ttft` | `string \| null` | Yes | Time to first token (TTFT) in seconds. Null when timing data is unavailable. |
| `endTime` | `string` | Yes | Finishing time of the task. |
| `startTime` | `string` | Yes | Starting time of the task. |
| `totalTime` | `string \| null` | Yes | Total time of the task in seconds. Null when timing data is unavailable. |
| `inferenceSpeed` | `string \| null` | Yes | Tokens per second generated by the model in response to the input. Null when timing data is unavailable. |



### rfsJobId

Optional RFS job ID forwarded from the X-Qlik-RFS-JobID request header to correlate triggered and finished events.

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfsJobId` | `string` | No | Optional RFS job ID forwarded from the X-Qlik-RFS-JobID request header to correlate triggered and finished events. |



### usage

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalTokens` | `integer` | Yes | Addition of the completion and prompt tokens. |
| `promptTokens` | `integer` | Yes | Tokens explicitly provided as input to the model. |
| `completionTokens` | `integer` | Yes | Tokens generated by the model in response to the input. |


