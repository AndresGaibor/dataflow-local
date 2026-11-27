---
title: "Creating a Hugging Face connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-hugging-face-create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Hugging Face analytics source"]
---

# Creating a Hugging Face connection

To communicate with Hugging Face, create a connection to the Hugging Face analytics source. Create the [connection](#glossary-0 "Glossary term") in the Create page of the Analytics activity center, Data load editor, or Script.

Data received from these connections can be used in the load script and in chart expressions to enhance your Qlik Sense analytics applications.

## Configurations and configurable settings

Set up your Hugging Face analytics connection with one of the following configurations. Each connection can consist of a single configuration.

Each available configuration of the Hugging Face connector corresponds to a common task you want to perform with a model that is available through the Hugging Face platform. There are thousands of models available to help work with each task.

Not all Hugging Face models are available for use with the Qlik Hugging Face connector. The availability of a model for use in Qlik Sense depends, in part, on external factors. Additional model-specific limitations and requirements might apply, affecting how you configure the connector and exchange data with it. For full details on any specific model, refer to the official Hugging Face documentation.

[Tasks](https://huggingface.co/tasks)

[Models](https://huggingface.co/models)

### Feature Extraction

Use this configuration to work with models that perform feature extraction tasks. Generally, feature extraction is a technical machine learning process with many practical applications. With this task, input data is converted to numerical features.

See the following Hugging Face resources for more information:

- Overview of feature extraction tasks: [Feature Extraction](https://huggingface.co/tasks/feature-extraction)
- Detailed explanation of parameters: [Inference API - Detailed parameters](https://huggingface.co/docs/api-inference/detailed_parameters)

Configurable settings for Feature Extraction configuration

| Field | Description |
| --- | --- |
| Configuration | Select the connector configuration. For models used in feature extraction tasks, select Feature Extraction. |
| Hugging Face Inference API endpoint | Enter the endpoint URL through which Qlik Sense can access the model. This is generally done through Hugging Face Inference API. |
| Hugging Face API Token | Enter the Hugging Face API token that you generated after creating your account. This authenticates your account credentials so you can use the external services. See [*Generate an API token*](ac-hugging-face-overview.htm#Generate). |
| Use Cache | This is set to True by default. Select whether to utilize caching to reuse model responses if the same request is made twice. Depending on your model, you might want to turn this setting off. |
| Wait For Model | This is set to False by default. If this is turned on, you can reduce the number of requests made to the API by waiting for the model to be ready before making a request. |
| Association Field | Specify an association field, a field from the input data table containing a unique identifier. This is an optional parameter.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the response to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name is used if you do not enter a name. |

### Question Answering

Use this configuration to work with models that perform question answering tasks. With question answering, a model can be used to extract the answer to a question, given a separately provided context segment. In Qlik Sense, both the question and the context are provided in the application or script data.

See the following Hugging Face resources for more information:

- Overview of question answering tasks: [Question Answering](https://huggingface.co/tasks/question-answering)
- Detailed explanation of parameters: [Inference API - Detailed parameters](https://huggingface.co/docs/api-inference/detailed_parameters)

Configurable settings for Question Answering configuration

| Field | Description |
| --- | --- |
| Configuration | Select the connector configuration. For models used in question answering tasks, select Question Answering. |
| Hugging Face Inference API endpoint | Enter the endpoint URL through which Qlik Sense can access the model. This is generally done through Hugging Face Inference API. |
| Hugging Face API Token | Enter the Hugging Face API token that you generated after creating your account. This authenticates your account credentials so you can use the external services. See [*Generate an API token*](ac-hugging-face-overview.htm#Generate). |
| Use Cache | This is set to True by default. Select whether to utilize caching to reuse model responses if the same request is made twice. Depending on your model, you might want to turn this setting off. |
| Wait For Model | This is set to False by default. If this is turned on, you can reduce the number of requests made to the API by waiting for the model to be ready before making a request. |
| Association Field | Specify an association field, a field from the input data table containing a unique identifier. This is an optional parameter.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the response to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name is used if you do not enter a name. |

### Summarization

Use this configuration to work with models that perform summarization tasks. A model performs summarization by taking a particular input text and outputting a briefer summary of this text, retaining the essential details.

See the following Hugging Face resources for more information:

- Overview of summarization tasks: [Summarization](https://huggingface.co/tasks/summarization)
- Detailed explanation of parameters: [Inference API - Detailed parameters](https://huggingface.co/docs/api-inference/detailed_parameters)

Configurable settings for Summarization configuration

| Field | Description |
| --- | --- |
| Configuration | Select the connector configuration. For models used in summarization tasks, select Summarization. |
| Hugging Face Inference API endpoint | Enter the endpoint URL through which Qlik Sense can access the model. This is generally done through Hugging Face Inference API. |
| Hugging Face API Token | Enter the Hugging Face API token that you generated after creating your account. This authenticates your account credentials so you can use the external services. See [*Generate an API token*](ac-hugging-face-overview.htm#Generate). |
| Minimum Token Length | Set an integer value as the minimum number of tokens to be used in the model output. Optional parameter. If no value is specified, output will have no minimum length. |
| Maximum Token Length | Set an integer value as the maximum number of tokens to be used in the model output. Optional parameter. If no value is specified, output will have no maximum length. |
| Top K | Set an integer value as the number of most probable tokens to be used in the output. Optional parameter. If no value is specified, output will not have a top number of most probable token to use in the output. |
| Top P | Enter a numeric (specifically, a floating-point) number to control the randomness of the output, in terms of token probability. For full details, refer to the Hugging Face documentation.  Optional parameter. If no value is specified, output will not be controlled for randomness by your choices. |
| Temperature | Specify a floating-point value (between 0.00 and 100.0) to control the randomness of the output. A higher value generally results in more token randomness. The default value is 1.0. Optional parameter. |
| Repetition Penalty | Specify a floating-point value (between 0.00 and 100.0) to enforce a penalty on tokens that are repeated. The default value is 1.0. Optional parameter. |
| Maximum Query Time | Specify a floating-point value (between 0 and 120.0) for the maximum time in seconds for a query to take. This is a soft limit. Optional parameter. If no value is specified, no maximum query time will be set. |
| Use Cache | This is set to True by default. Select whether to utilize caching to reuse model responses if the same request is made twice. Depending on your model, you might want to turn this setting off. |
| Wait For Model | This is set to False by default. If this is turned on, you can reduce the number of requests made to the API by waiting for the model to be ready before making a request. |
| Association Field | Specify an association field, a field from the input data table containing a unique identifier. This is an optional parameter.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the response to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name is used if you do not enter a name. |

### Sentence Similarity

Use this configuration to work with models that perform sentence similarity analysis. In this task type, a model compares one or more distinct sentences against a source sentence, producing embeddings which store information about the similarity between them. These embeddings are numerical values. Utilizing embeddings is an advanced machine learning process.

In Qlik Sense, the source sentence is provided in the connector configuration, and the input sentences (which the model compares against the source sentence) are provided in the application or script data.

See the following Hugging Face resources for more information:

- Overview of sentence similarity tasks: [Sentence Similarity](https://huggingface.co/tasks/sentence-similarity)
- Detailed explanation of parameters: [Inference API - Detailed parameters](https://huggingface.co/docs/api-inference/detailed_parameters)

Configurable settings for Sentence Similarity configuration

| Field | Description |
| --- | --- |
| Configuration | Select the connector configuration. For models used in tasks related to sentence similarity analysis, select Sentence Similarity. |
| Hugging Face Inference API endpoint | Enter the endpoint URL through which Qlik Sense can access the model. This is generally done through Hugging Face Inference API. |
| Hugging Face API Token | Enter the Hugging Face API token that you generated after creating your account. This authenticates your account credentials so you can use the external services. See [*Generate an API token*](ac-hugging-face-overview.htm#Generate). |
| Source Sentence | The text string that the model compares against each of the input data items, assessing the similarity between the two strings. |
| Use Cache | This is set to True by default. Select whether to utilize caching to reuse model responses if the same request is made twice. Depending on your model, you might want to turn this setting off. |
| Wait For Model | This is set to False by default. If this is turned on, you can reduce the number of requests made to the API by waiting for the model to be ready before making a request. |
| Association Field | Specify an association field, a field from the input data table containing a unique identifier. This is an optional parameter.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the response to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name is used if you do not enter a name. |

### Text Classification

Use this configuration to work with models that perform text classification tasks. Text classification is a versatile task type, in which a model can perform sentiment analysis, grammar correctness checks, and other language processing actions.

See the following Hugging Face resources for more information:

- Overview of text classification tasks: [Text Classification](https://huggingface.co/tasks/text-classification)
- Detailed explanation of parameters: [Inference API - Detailed parameters](https://huggingface.co/docs/api-inference/detailed_parameters)

Configurable settings for Text Classification configuration

| Field | Description |
| --- | --- |
| Configuration | Select the connector configuration. For models used in text classification tasks, select Text Classification. |
| Hugging Face Inference API endpoint | Enter the endpoint URL through which Qlik Sense can access the model. This is generally done through Hugging Face Inference API. |
| Hugging Face API Token | Enter the Hugging Face API token that you generated after creating your account. This authenticates your account credentials so you can use the external services. See [*Generate an API token*](ac-hugging-face-overview.htm#Generate). |
| Use Cache | This is set to True by default. Select whether to utilize caching to reuse model responses if the same request is made twice. Depending on your model, you might want to turn this setting off. |
| Wait For Model | This is set to False by default. If this is turned on, you can reduce the number of requests made to the API by waiting for the model to be ready before making a request. |
| Association Field | Specify an association field, a field from the input data table containing a unique identifier. This is an optional parameter.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the response to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name is used if you do not enter a name. |

### Text Generation

Use this configuration to work with models that perform text generation tasks. Models using this task type can typically finish incomplete text segments, or perform paraphrasing of text.

See the following Hugging Face resources for more information:

- Overview of text generation tasks: [Text Generation](https://huggingface.co/tasks/text-generation)
- Detailed explanation of parameters: [Inference API - Detailed parameters](https://huggingface.co/docs/api-inference/detailed_parameters)

Configurable settings for Text Generation configuration

| Field | Description |
| --- | --- |
| Configuration | Select the connector configuration. For models used in text generation tasks, select Text Generation. |
| Hugging Face Inference API endpoint | Enter the endpoint URL through which Qlik Sense can access the model. This is generally done through Hugging Face Inference API. |
| Hugging Face API Token | Enter the Hugging Face API token that you generated after creating your account. This authenticates your account credentials so you can use the external services. See [*Generate an API token*](ac-hugging-face-overview.htm#Generate). |
| Maximum Token Length | Set an integer value as the maximum number of tokens to be used in the model output. Optional parameter. If no value is specified, output will have no maximum length. |
| Top K | Set an integer value as the number of most probable tokens to be used in the output. Optional parameter. If no value is specified, output will not have a top number of most probable token to use in the output. |
| Top P | Enter a numeric (specifically, a floating-point) number to control the randomness of the output, in terms of token probability. For full details, refer to the Hugging Face documentation.  Optional parameter. If no value is specified, output will not be controlled for randomness by your choices. |
| Temperature | Specify a floating-point value (between 0.00 and 100.0) to control the randomness of the output. A higher value generally results in more token randomness. The default value is 1.0. Optional parameter. |
| Repetition Penalty | Specify a floating-point value (between 0.00 and 100.0) to enforce a penalty on tokens that are repeated. The default value is 1.0. Optional parameter. |
| Maximum Query Time | Specify a floating-point value (between 0 and 120.0) for the maximum time in seconds for a query to take. This is a soft limit. Optional parameter. If no value is specified, no maximum query time will be set. |
| Use Cache | This is set to True by default. Select whether to utilize caching to reuse model responses if the same request is made twice. Depending on your model, you might want to turn this setting off. |
| Wait For Model | This is set to False by default. If this is turned on, you can reduce the number of requests made to the API by waiting for the model to be ready before making a request. |
| Association Field | Specify an association field, a field from the input data table containing a unique identifier. This is an optional parameter.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the response to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name is used if you do not enter a name. |

### Token Classification

Use this configuration to work with models that perform token classification tasks. With token classification, a model can identify text strings (tokens) as classifiable entities (for example, places, people, and parts of speech).

See the following Hugging Face resources for more information:

- Overview of token classification tasks: [Token Classification](https://huggingface.co/tasks/token-classification)
- Detailed explanation of parameters: [Inference API - Detailed parameters](https://huggingface.co/docs/api-inference/detailed_parameters)

Configurable settings for Token Classification configuration

| Field | Description |
| --- | --- |
| Configuration | Select the connector configuration. For models used in token classification tasks, select Token Classification. |
| Hugging Face Inference API endpoint | Enter the endpoint URL through which Qlik Sense can access the model. This is generally done through Hugging Face Inference API. |
| Hugging Face API Token | Enter the Hugging Face API token that you generated after creating your account. This authenticates your account credentials so you can use the external services. See [*Generate an API token*](ac-hugging-face-overview.htm#Generate). |
| Aggregation Strategy | The classification of the entities in your input can undergo aggregation processing. This parameter specifies the type of aggregation strategy applied when making classifications.  Choose from the following options:   - None: No further aggregation. - Simple: Uses the default schema. - First: A modified version of the Simple option, in which ambiguity is handled by using the tag of the first word. Different tags cannot be applied to words. - Average: A modified version of the Simple option, in which an averaging system is used and different tags cannot be applied to words. - Max: A modified version of the Simple option, in which a scoring system is used and different tags cannot be applied to words.   Simple is the default option. |
| Use Cache | This is set to True by default. Select whether to utilize caching to reuse model responses if the same request is made twice. Depending on your model, you might want to turn this setting off. |
| Wait For Model | This is set to False by default. If this is turned on, you can reduce the number of requests made to the API by waiting for the model to be ready before making a request. |
| Association Field | Specify an association field, a field from the input data table containing a unique identifier. This is an optional parameter.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the response to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name is used if you do not enter a name. |

### Translation

Use this configuration to work with models that perform translation tasks. Models can translate input text in a certain language into another language.

See the following Hugging Face resources for more information:

- Overview of translation tasks: [Translation](https://huggingface.co/tasks/translation)
- Detailed explanation of parameters: [Inference API - Detailed parameters](https://huggingface.co/docs/api-inference/detailed_parameters)

Configurable settings for Translation configuration

| Field | Description |
| --- | --- |
| Configuration | Select the connector configuration. For models used in translation tasks, select Translation. |
| Hugging Face Inference API endpoint | Enter the endpoint URL through which Qlik Sense can access the model. This is generally done through Hugging Face Inference API. |
| Hugging Face API Token | Enter the Hugging Face API token that you generated after creating your account. This authenticates your account credentials so you can use the external services. See [*Generate an API token*](ac-hugging-face-overview.htm#Generate). |
| Source Language | Enter the language of the input text you are requesting to be translated. Optional parameter.  Information noteThe language translation capabilities provided by each model can vary. For example, a model can be designed to only translate text between two specific languages. In this case, it makes sense to leave this parameter blank. |
| Target Language | Enter the language that you want your input text to be translated into. Optional parameter.  Information noteThe language translation capabilities provided by each model can vary. For example, a model can be designed to only translate text between two specific languages. In this case, it makes sense to leave this parameter blank. |
| Use Cache | This is set to True by default. Select whether to utilize caching to reuse model responses if the same request is made twice. Depending on your model, you might want to turn this setting off. |
| Wait For Model | This is set to False by default. If this is turned on, you can reduce the number of requests made to the API by waiting for the model to be ready before making a request. |
| Association Field | Specify an association field, a field from the input data table containing a unique identifier. This is an optional parameter.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the response to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name is used if you do not enter a name. |

## Creating a new connection

You can create a connection to the analytic connector from the Analytics activity center, from Data load editor in an existing application, or from Script in an existing script.
Follow the steps below to create a connection.

Do the following:

1. Access the connector through [Data load editor](#glossary-1 "Glossary term") or Script.
2. Click Create new connection.
3. Under Space, select the space where the connection will be located.
4. Select Hugging Face from the list of data connectors.
5. Fill out the connection dialog fields.
6. Click Create.

The data connection is saved to the space where the application is created, so it can be reused in other Qlik Sense applications and scripts. It is also listed under Data connections in Data load editor or Script.

Once you have created the connection, you can use it to load data with the requests and the platform's responses to them. Additionally, you can use it in chart expressions. For more information, see [*Select and load data from a Hugging Face connection*](ac-hugging-face-load.htm) and [*Using Hugging Face connections in visualization expressions*](ac-hugging-face-use.htm).

## Learn more

- [Hugging Face](https://huggingface.co/)
