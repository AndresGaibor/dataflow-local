---
source: https://qlik.dev/embed/gen-ai/get-started-chatbot-v2/
last_updated: 2026-04-20T13:34:03+01:00
---

# Get started with chatbot integration

The Qlik Natural Language API makes it easy to embed augmented
analytics capabilities into multi-experience applications like chatbots.
The interface provides building blocks for requesting and accepting a
response from the analytics engine.

This tutorial is going to teach you how to use the Natural Language API to create
queries for chat-based communication with Qlik Sense applications. It shows how to converse
with the API through a series of requests using Postman.

## Prerequisites

1. Download and install [Postman](https://getpostman.com).

2. An access token or API key. For more information, see [Authentication](https://qlik.dev/authenticate).

3. The **Insight Advisor** > **Data analysis** permission must be set to "Allowed" for your user.
   For more information, see [Permissions in User Default and custom roles](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-scopes-capacity-model.htm)
   on Qlik Help.

4. "Demo App - Beginner's tutorial" Qlik Sense application. To open the
   app, click `Explore the Demo` in the hub. To make the app available
   for chat, see [Making apps available in Insight Advisor Chat](https://help.qlik.com/en-US/sense/Subsystems/Hub/Content/Sense_Hub/Insights/insight-advisor-available-chat.htm)
   on Qlik Help.

## Natural Language API endpoint

Connections to the Natural Language (NL) API endpoint is made using
HTTPS by default. When communicating with the NL API, the URL has
the following form:
`{URL}/api/v1/questions/actions/ask`
where `{URL}` is your tenant URL.

## API usage examples

### Set up Postman

1. Start Postman.

2. Set the HTTP method to POST.

3. Enter the following path in the URL area:
   `{url}/api/v1/questions/actions/ask`
   The full URL should look like: `https://your-tenant.us.qlikcloud.com/api/v1/questions/actions/ask`

4. Select `Headers` and add `Content-Type` as the key with `application/json`
   as the value. The following examples show how to access the Natural Language API
   using Postman. Before making API requests, add your access token as a Bearer Token to
   Postman. See [Authentication](https://qlik.dev/authenticate).

### Get sales by manager for a product line

This example shows how to engage the API with a series of requests to
get the sales by a manager for a product line for a particular year. Default
API settings are used.

1. In the body of the request, set the initial text for the conversation:

   ```json
   {
     "text": "show sales by product"
   }
   ```

2. Click `Send`. The JSON response from the API should look like this:

   ```json
   {
     "apps": [
       {
         "id": "f09ab541-cee5-4300-a563-e433b2428b4f"
       }
     ],
     "conversationalResponse": {
       "responses": [
         {
           "type": "chart",
           "sentence": {
             "text": "show sales by product"
           },
           "imageUrl": "/api/v1/temp-contents/60ae7a9d1bc69100013a2efb?inline=1"
         },
         {
           "type": "narrative",
           "sentence": {
             "text": "show sales by product"
           },
           "narrative": {
             "text": "* Sales is 105.1M."
           }
         }
       ],
       "apps": [
         {
           "id": "f09ab541-cee5-4300-a563-e433b2428b4f"
         }
       ],
       "sentenceWithMatches": "show **sales** by **product**",
       "drillDownURI": "/sense/app/f09ab541-cee5-4300-a563-e433b2428b4f/insightadvisor?query=show%20sales%20by%20product"
     },
     "nluInfo": {
       "elements": [
         {
           "text": "show "
         },
         {
           "text": "sales ",
           "entity": true,
           "type": "master_measure",
           "typeTranslated": "Master measure",
           "typeName": "Sales",
           "errorText": "",
           "isFilter": false,
           "filterText": "",
           "filterFieldName": "Sales"
         },
         {
           "text": "by "
         },
         {
           "text": "product",
           "entity": true,
           "type": "master_dimension",
           "typeTranslated": "Master dimension",
           "typeName": "Product Drilldown",
           "errorText": "",
           "isFilter": false,
           "filterText": "",
           "filterFieldName": "Product Drilldown"
         }
       ]
     }
   }
   ```

   The response shows that only the "Demo App - Beginner's tutorial"
   app has data that matches the request. The `narrative` object contains the
   answer to the request and it shows total sales is $105.1 million. What
   happens if other apps in your hub also respond to the request? Here is an
   example of the response when two apps have data that matches the request and no
   app was specified or present in the conversation context.

   ```json
   {
     "conversationalResponse": {
       "responses": [
         {
           "type": "info",
           "infoType": "apps",
           "sentence": {
             "text": "show product sales"
           },
           "infoValues": [
             {
               "space_id": null,
               "space_type": null,
               "space_name": null,
               "last_reload_date": "2021-05-25T16:57:23.348Z"
             },
             {
               "id": "f09ab541-cee5-4300-a563-e433b2428b4f",
               "name": "Demo App - Beginner's tutorial",
               "space_id": null,
               "space_type": null,
               "space_name": null,
               "last_reload_date": "2021-05-26T15:11:53.300Z"
             }
           ],
           "appsEnabled": true,
           "followupSentence": "show product sales"
         }
       ],
       "apps": [
         {
           "id": "f3c4bcf9-395c-4358-b098-e50a5adf0e54",
           "name": "Combo Chart Examples",
           "space_id": null,
           "space_type": null,
           "space_name": null,
           "last_reload_date": "2021-05-25T16:57:23.348Z"
         },
         {
           "id": "f09ab541-cee5-4300-a563-e433b2428b4f",
           "name": "Demo App - Beginner's tutorial",
           "space_id": null,
           "space_type": null,
           "space_name": null,
           "last_reload_date": "2021-05-26T15:11:53.300Z"
         }
       ]
     }
   }
   ```

   In this case, you need to copy the ID of the "Demo App - Beginner's tutorial"
   app and include it in your request so that you only get a response from
   that app. For example:

   ```json
   {
     "text": "show product sales",
     "app": {
       "id": "f09ab541-cee5-4300-a563-e433b2428b4f"
     }
   }
   ```

3. Now that the conversation context is set to product sales in the
   "Demo App - Beginner's tutorial" app, the next step is to request
   the sales amount for one of the product lines. In the body of the request,
   update the text for the conversation:

   ```json
   {
     "text": "same details for drink"
   }
   ```

4. Click `Send`. The JSON response from the API should look something like this:

   ```json
   {
     "apps": [
       {
         "id": "f09ab541-cee5-4300-a563-e433b2428b4f",
         "name": "Demo App - Beginner's tutorial",
         "space_id": null,
         "space_type": null,
         "space_name": null,
         "last_reload_date": null
       }
     ],
     "conversationalResponse": {
       "responses": [
         {
           "type": "chart",
           "sentence": {
             "text": "same details for drink"
           },
           "imageUrl": "/api/v1/temp-contents/60aea7c6f8fe440001837211?inline=1"
         },
         {
           "type": "narrative",
           "sentence": {
             "text": "same details for drink"
           },
           "narrative": {
             "text": "* Sales is 9.61M where Product Line is Drink."
           }
         }
       ],
       "apps": [
         {
           "id": "f09ab541-cee5-4300-a563-e433b2428b4f",
           "name": "Demo App - Beginner's tutorial",
           "space_id": null,
           "space_type": null,
           "space_name": null,
           "last_reload_date": null
         }
       ],
       "sentenceWithMatches": "same details for **drink**",
       "drillDownURI": "/sense/app/f09ab541-cee5-4300-a563-e433b2428b4f/insightadvisor",
       "contextInfo": "Sales, product(Product Drilldown)"
     },
     "nluInfo": {
       "elements": [
         {
           "text": "same details for "
         },
         {
           "text": "drink",
           "entity": true,
           "type": "filter",
           "typeTranslated": "Filter",
           "typeName": "Product Line",
           "errorText": "",
           "isFilter": true,
           "filterText": "Drink",
           "filterFieldName": "Product Line"
         }
       ]
     }
   }
   ```

   From the response, you can see that the total sales for drinks is $9.61 million.
   Just two more API requests are needed to reach the goal of getting the sales by
   a manager for a product line for a particular year.

5. Update the text in the conversation to specify a manager.

   ```json
   {
     "text": "same for manager Brenda Gibson"
   }
   ```

6. Click `Send`. The JSON response from the API should look something like this:

   ```json
   {
        "apps": [
            {
                "id": "f09ab541-cee5-4300-a563-e433b2428b4f",
                "name": "Demo App - Beginner's tutorial",
                "space_id": null,
                "space_type": null,
                "space_name": null,
                "last_reload_date": null
            }
        ],
        "conversationalResponse": {
            "responses": [
                {
                    "type": "narrative",
                    "sentence": {
                        "text": "and that for manager Brenda Gibson"
                    },
                    "narrative": {
                        "text": "Sales is 1.8M where Manager is Brenda Gibson, and Product Line is Drink."
                    }
                },
                Remainder of response not shown
   ```

   The response shows that the sales for drinks for manager Brenda Gibson
   is $1.8 million.

7. Update the text in the conversation to specify the year.

   ```json
   {
     "text": "in 2020"
   }
   ```

8. Click `Send`. The JSON response from the API should look something like this:

   ```json
   {
     "apps": [
       {
         "id": "f09ab541-cee5-4300-a563-e433b2428b4f",
         "name": "Demo App - Beginner's tutorial",
         "space_id": null,
         "space_type": null,
         "space_name": null,
         "last_reload_date": null
       }
     ],
     "conversationalResponse": {
       "responses": [
         {
           "type": "chart",
           "sentence": {
             "text": "in 2020"
           },
           "imageUrl": "/api/v1/temp-contents/60af85b2e889a500019922dc?inline=1"
         },
         {
           "type": "narrative",
           "sentence": {
             "text": "in 2020"
           },
           "narrative": {
             "text": "Sales is 95.58k where Manager is Brenda Gibson, Product Line is Drink, and Date between January 1st and December 31st, 2020."
           }
         },
         {
           "type": "info",
           "infoType": "recommendations",
           "followupSentence": "$value",
           "sentence": {
             "text": "in 2020"
           },
           "infoValues": [
             {
               "recId": "a93aa592-82a9-4328-ba72-307f928a6270",
               "name": "Sales"
             },
             {
               "recId": "e50605a2-934b-435f-a875-078e1c22682b",
               "name": "Control chart - Sales over Date against rolling mean"
             },
             {
               "recId": "935453ec-7b15-4c83-9d26-394584a7e868",
               "name": "Control chart - Sales over Date against mean"
             }
           ]
         }
       ],
       "apps": [
         {
           "id": "f09ab541-cee5-4300-a563-e433b2428b4f",
           "name": "Demo App - Beginner's tutorial",
           "space_id": null,
           "space_type": null,
           "space_name": null,
           "last_reload_date": null
         }
       ],
       "sentenceWithMatches": "in **2020**",
       "drillDownURI": "/sense/app/f09ab541-cee5-4300-a563-e433b2428b4f/insightadvisor",
       "contextInfo": "Brenda Gibson(Manager), drink(Product Line), Sales"
     },
     "nluInfo": {
       "elements": [
         {
           "text": "in "
         },
         {
           "text": "2020",
           "entity": true,
           "type": "filter",
           "typeTranslated": "Filter",
           "typeName": "Date",
           "errorText": "",
           "isFilter": true,
           "filterText": ">= 1/1/2020 <= 12/31/2020",
           "filterFieldName": "Date"
         }
       ]
     }
   }
   ```

   The response shows that the sales for drinks for manager "Brenda Gibson"
   in 2020 was $95.58k. Note that the context was considered throughout
   the series of requests. This creates a natural, conversational
   flow while interrogating the data.

### Get a list of apps

You can always start a conversation with simple requests to learn more about the
apps available or their dimensions and measures. This example shows how to get a
list of apps that are chat-enabled and accessible to the user.

1. In the body of the request, set the text for the conversation. For example:

   ```json
   {
     "text": "show apps"
   }
   ```

2. Click `Send`. The JSON response from the API should look something like this:

   ```json
   {
     "conversationalResponse": {
       "responses": [
         {
           "type": "info",
           "sentence": {
             "text": "show apps"
           },
           "infoType": "apps",
           "infoValues": [
             {
               "id": "50b40fd5-e9be-4cfc-9321-be58ec567eef",
               "name": "Executive Dashboard",
               "space_id": null,
               "space_type": null,
               "space_name": null,
               "last_reload_date": "2020-06-27T15:51:29.000Z"
             },
             {
               "id": "4a22ba23-7f8c-4ef0-9b84-955fa9247554",
               "name": "Helpdesk Management",
               "space_id": null,
               "space_type": null,
               "space_name": null,
               "last_reload_date": "2020-06-14T17:54:28.488Z"
             }
           ],
           "followupSentence": "show measures"
         }
       ],
       "apps": [
         {
           "id": "50b40fd5-e9be-4cfc-9321-be58ec567eef",
           "name": "Executive Dashboard",
           "space_id": null,
           "space_type": null,
           "space_name": null,
           "last_reload_date": "2020-06-27T15:51:29.000Z"
         },
         {
           "id": "4a22ba23-7f8c-4ef0-9b84-955fa9247554",
           "name": "Helpdesk Management",
           "space_id": null,
           "space_type": null,
           "space_name": null,
           "last_reload_date": "2020-06-14T17:54:28.488Z"
         }
       ]
     }
   }
   ```

### Render a chart from an API response

With the Natural Language API, there are two ways that a chart can be rendered from an API response: (1)
as a static image of the chart, or (2) from a nebula visualization object that can be used to render the
chart as a native web object.

#### Render a static image of the chart

1. In the body of the request, set the text for the conversation:

   ```json
   {
     "text": "show sales by product"
   }
   ```

2. Click `Send`.

3. In the API response, click the path assigned to the `imageUrl` property.

4. Click `Send`. A bar chart showing total sales by product is returned.

![Bar chart showing total sales by product.](https://qlik.dev/_astro/visualization-sample.BivpjUYD.png)

#### Render a nebula chart from a visualization object

For more information, see [Build a chatbot using the Qlik Sense Natural language API](https://qlik.dev/embed/gen-ai/create-chatbot-nl-api/).

### Turn off conversation context

Conversation context is on by default. When you turn off conversation
context, the app and entity contexts are not considered in the request
and follow-up recommendations are turned off. This can be handy when you
want to temporarily switch the context, for example, to request data from
a different app and then return to the original app and entity context later.

To turn off conversation context, in the body of the request, set
`disableConversationContext` to `true`. For example:

```json
{
    "text": " show product sales",
    "app": {
        "id": "50b40fd5-e9be-4cfc-9321-be58ec567eef"
    }
    "disableConversationContext": true
}
```

### Reset the entity context

The entity context is the context of the conversation. As you make requests,
the entity context is maintained. When you reset the entity context, it is
completely removed, which sets the stage for a new series of requests. Note
that app context is independent of the entity context so resetting the entity
context has no effect on the app context. If you want to reset both app context
and entity context, see [Reset the app and entity contexts](#reset-the-app-and-entity-contexts).

To reset the entity context, in the body of the request, set `clearEntityContext`
to `true`. For example:

```json
{
  "text": " show product sales",
  "clearEntityContext": true
}
```

### Reset the app and entity contexts

Reset the app and entity contexts when you want to restart a conversation. To
reset the app and entity contexts, in the body of the request, set the
conversation text to `clear`. For example:

```json
{
  "text": "clear"
}
```

Click Send. The response from the API should look like this:

```json
{
    "conversationalResponse": {
        "apps": [],
         responses": [
            {
                "type": "narrative",
                "sentence": {
                    "text": "clear"
                },
                "narrative": {
                    "text": "App context has been reset."
                }
            }
        ]
    }
}
```

### Use follow-up recommendations

Responses to some requests contain follow-up recommendations that you can use
to continue the conversation. Recommendations are identified by an ID (`recId`)
and a name. For example:

```json
 "infoValues": [
     {
         "recId": "e2c89c2a-d79e-4600-9504-9f96693a2169",
         "name": "Sales by Invoice Number"
     },
```

To follow a recommendation, copy the name of the recommendation from the
response and insert it as the conversation text in the body of the request.
Next, copy the recommendation ID from the response and also add it to the body
of the request. For example:

```json
{
  "text": "Sales by Invoice Number",
  "recId": "e2c89c2a-d79e-4600-9504-9f96693a2169"
}
```

### Turn off follow-up recommendations

To turn off the follow-up recommendations, in the body of the request, set
`disableFollowups` to `true`. For example:

```json
{
  "text": "same for manager Brenda Gibson",
  "disableFollowups": true
}
```

### Turn off narratives

Turn off narratives if you only want charts (if present) for your queries and
don't want any natural language responses or narratives. To turn off the
narratives, in the body of the request, set
`disableNarrative` to `true`. For example:

```json
{
  "text": "show product sales",
  "disableNarrative": true
}
```

## Next steps

Now that you know how to use the API with Postman, why not try building an
end-to-end chatbot? See [Build a chatbot using the Qlik Sense Natural language API](https://qlik.dev/tutorials/build-a-chatbot-using-the-qlik-sense-natural-language-api)
for step-by-step instructions.
