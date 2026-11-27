---
title: "Getting started with analytic connections"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/load-data-from-advanced-analytic-connections.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics"]
---

# Getting started with analytic connections

Create an analytic [connection](#glossary-0 "Glossary term") to load and generate data from models deployed from Qlik Cloud or from various third-party machine learning tools. These models typically expose REST-based API endpoints. Before creating and using the connection, you need to create and deploy, or obtain access to, your desired machine learning models.

In addition to Qlik Predict, there are several third-party platforms where machine learning models can be created, trained, and deployed, such as:

- Azure ML
- Amazon SageMaker

[Train a classification model with no-code AutoML in the Azure Machine Learning studio](https://docs.microsoft.com/en-gb/azure/machine-learning/tutorial-first-experiment-automated-ml)

[Get Started with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html)

## Enabling analytic connections for machine learning endpoints

Machine learning endpoints are disabled by default.

Tenant administrators can enable machine learning endpoints in Administration, under Feature control in the Settings window.

## Using analytic connections and server-side extensions syntax

Analytic connections can send data to Qlik Predict or externally exposed machine learning endpoints for calculations. Data returned from these connections can be loaded into a Qlik Sense application.

Data load scripts and chart expressions are two ways in which analytic connections can be added to a Qlik Sense application. Both server-side extension (SSE) functions and parameters are processed within Qlik Sense, then converted into REST requests which are sent to machine learning models. SSE load scripts and chart expressions must honor SSE syntax. See [*Server side extensions syntax*](sse-syntax.htm).

### Data load script

- You can return a table from the SSE call and load data from analytic connections using the LOAD ... EXTENSION statement in the Qlik Sense data [load script](#glossary-2 "Glossary term"). You can send a single table to the model, and a single data table is returned.
- When you use an SSE function in the Qlik Sense data load script (the LOAD ... EXTENSION statement excluded), the [cardinality](#glossary-3 "Glossary term") is preserved, and a single column is returned.
- SSE function calls from within any other load statements, for example Load ... From ..., only support scalar and [aggregation](#glossary-4 "Glossary term") function types. This implies that data containing n rows, will result in n calls to the model unless you are aggregating the data resulting in a single call.
- Data types are automatically detected in analytic connections. If the data has no numeric values and at least one non-NULL text string, the [field](#glossary-5 "Glossary term") is considered as text. In any other case it is considered as numeric. You can force the data type by wrapping a field name with String() or Mixed(). String() forces the field to be text. If the field is numeric, the text part of the dual value is extracted, there is no conversion performed. Mixed() forces the field to be dual.

### Chart expressions

- Chart expressions cannot consume a table returned from the SSE function call. When you use an SSE function in a chart expression, the cardinality is preserved and only the first column returned will be used by Qlik Sense.

### Referencing the data connection's space

If you are publishing the application or script to a [managed space](#glossary-6 "Glossary term"), or if you want your SSE requests to refer to a connection in the current space, use relative syntax. Alternatively, configure the request with a reference to a specific space name. These concepts are important in both the load script and chart expressions.

For more information about using space-aware syntax, see:

- [*Connect to data sources in load scripts*](connect-data-sources-data-load-editor.htm)
- [*Data sources for applications in managed spaces*](../Spaces/app-data-managed-spaces.htm)

#### Example 1: Relative space syntax in load script

The following example is a sample from a connection to an analytic connection within a load script. The code has been modified to point to a connection in the current space of the app or script. This is done by adding a colon at the beginning of the connection name (in this case, ":Amazon\_Titan\_(Amazon\_Bedrock)"). Without this colon, the reference would point to a connection in the [personal space](#glossary-7 "Glossary term") of the user running the reload (or the reload schedule owner).

```
EXTENSION endpoints.ScriptEval('{"RequestType":"endpoint", "endpoint":{"connectionname":":Amazon_Titan_(Amazon_Bedrock)"}}', QuestionsTable{Question_ID,Question});
```

This space-aware syntax could be used before publishing the application or script to a managed space that also contains the analytic connection.

#### Example 2: Relative space syntax in chart expression

The following example is a chart expression containing a reference to a connection in the current space. This is done by adding a colon at the beginning of the connection name (in this case, ":Amazon\_Titan\_(Amazon\_Bedrock)"). Without this colon, the reference would point to a connection in the personal space of the user running the reload (or the reload schedule owner).

```
if(vQuestion <> '', endpoints.scriptAggrStr('{"RequestType":"endpoint", "endpoint":{"connectionname":":Amazon_Titan_(Amazon_Bedrock)","column":"outputText"}}',vQuestion))
```

This space-aware syntax could be used before publishing the application or script to a managed space that has also contains the analytic connection.

#### Example 3: Hard-coded space syntax in load script

If you want the reference to the analytic connection to only work in a specific space, you can hard-code the expression to contain a direct reference to the space. If you do not include the space name (and also omit the colon that was added to examples 1 and 2), the syntax is hard-coded to refer to a connection in the [personal space](#glossary-8 "Glossary term") of the user running the reload (or the reload schedule owner).

If you use the Select data wizard to add the load statement, this will be the syntax used automatically.

```
EXTENSION endpoints.ScriptEval('{"RequestType":"endpoint", "endpoint":{"connectionname":"My_Shared_Space:Amazon_Titan_(Amazon_Bedrock)"}}', QuestionsTable{Question_ID,Question});
```

In this case, the reference is to a connection in a space named My\_Shared\_Space.

#### Example 4: Hard-coded space syntax in chart expression

This example is similar to example 3. If you do not include the space name (and also omit the colon that was added to examples 1 and 2), the syntax is hard-coded to refer to a connection in the [personal space](#glossary-9 "Glossary term") of the user running the reload (or the reload schedule owner).

```
if(vQuestion <> '', endpoints.scriptAggrStr('{"RequestType":"endpoint", "endpoint":{"connectionname":"My_Shared_Space:Amazon_Titan_(Amazon_Bedrock)","column":"outputText"}}',vQuestion))
```

In this case, the reference is to a connection in a space named My\_Shared\_Space.
