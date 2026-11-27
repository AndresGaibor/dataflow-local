---
title: "Example - What-if analysis with the Qlik Predict analytics connector"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/example-what-if-analysis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik Predict analytics source"]
---

# Example - What-if analysis with the Qlik Predict analytics connector

Expand/Collapse all

# Example - What-if analysis with the Qlik Predict analytics connector

In this example, you will configure a what-if analysis to simulate how predicted values change when different variables are adjusted. The example involves training and deploying a binary classification model in Qlik Predict, and using it to create predictions with the Qlik Predict analytics connector.

What-if analysis application

![What-if analysis result](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/what-if-analysis.png "Click to view full size")

## Before you start

### Download example materials

Download the example resources here:

[WhatIfAnalysisExample.zip](/en-US/cloud-services/tutorials/WhatIfAnalysisExample.zip)

The materials consist of:

- A training dataset—data-turnover-employees.xlsx. This dataset is used for both the training and predictions for the example.
- An application—What-If Analysis.qvf. The application cannot be used to generate predictions without first training and deploying a model.

### Prerequisites

Before you start, ensure:

- Your Qlik Cloud subscription can run real-time predictions. Refer to the following, or contact the tenant service account owner.

  - [Qlik Pricing](https://www.qlik.com/us/pricing)
  - [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms)
- Your tenant administrator has enabled machine learning endpoints.

  [*Enabling ML endpoints in Qlik Cloud*](../LoadData/ac-qlik-automl-connector-overview.htm#EnableMLEndpoints)
- You have the required permissions assigned to you by a tenant administrator:

  - The Data connections permission set to Allowed.

    [*Assigning permissions for users to work with data connections*](../Admin/mc-administer-data-connections.htm#Permissions)
  - Permissions for working with experiments.

    [*User access to ML experiments*](who-can-work-with-automl.htm#AccessExperiment)
  - Permissions for working with deployments and working with the Qlik Predict analytics connector.

    [*User access to ML deployments and predictions*](who-can-work-with-automl.htm#AccessDeployment)

## Part 1: Upload the dataset

Do the following:

1. Go to the Create page of the Analytics [activity center](#glossary-0 "Glossary term") and select Dataset.
2. Click Upload data file.
3. Drag and drop the data-turnover-employees.xlsx data file into the Add file dialog.
4. Select a destination space for the file. It can be your personal space or a shared space. Use the same space for all tutorial assets.
5. Click Upload.

## Part 2: Train the experiment

Create, configure, and run an experiment to train a binary classification model. All available features will be included by default.

Do the following:

1. Go to the Create page of the Analytics [activity center](#glossary-1 "Glossary term") and select ML experiment.
2. Enter a name for your experiment, for example, Employee turnover analysis.
3. Choose a space for the experiment (use the same space you used in [*Part 1: Upload the dataset*](#Upload)).
4. Click Create.
5. Select the training dataset file data-turnover-employees.xlsx.
6. Select the left column as the target. This is a column indicating whether or not an employee left the company.
7. Click Run experiment.

## Part 3: Deploy and activate the top-performing model

### Deployment

After experiment training completed, you land on the Models tab. Deploy the top-performing model as an ML deployment.

Do the following:

1. Click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the model that has a ![Trophy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_trophy.svg) icon next to it.
2. Click ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton.svg) Deploy.
3. Select the option to deploy the model to A new deployment.
4. Type a name for your deployment, such as Employee Turnover Predictions.
5. If needed, adjust the space, description, and tags.
6. Turn on Enable real-time API access. This is required for running predictions with the Qlik Predict analytics connector.
7. Click Create.

### Activation

Open the newly created deployment.

At the top of the ML deployment interface, a banner indicates that a model approver needs to activate the default model for making predictions.

Do the following:

1. In the banner at the top of the ML deployment, click Activate model.
2. In the dialog that opens, click Activate model to confirm.

## Part 4: Create a connection to the Qlik Predict analytics connector

Next, create a connection to the Qlik Predict analytics connector. This will allow you to generate predictions on the fly within the analytics application.

Do the following:

1. Go to the Create page of the Analytics activity center and select Data connection.
2. Under Space, select the same space you used in [*Part 1: Upload the dataset*](#Upload).
3. Select the Qlik Predict connector.
4. Select the ML deployment that you created in [*Part 3: Deploy and activate the top-performing model*](#Deploy).
5. Enter the following Name: MLModel.
6. Click Create.

## Part 5: Upload the analytics application

Upload the analytics application you downloaded in [*Download example materials*](#Download).

Do the following:

1. Go to the Create page of the Analytics activity center.
2. Under Data and upload, select Upload.
3. Drop the What-If Analysis.qvf application into the dialog.
4. Under Space, select the same space you used in [*Part 1: Upload the dataset*](#Upload) and [*Part 4: Create a connection to the Qlik Predict analytics connector*](#Connection).
5. Click Upload.

After uploading the application, open it, and then open the What-If Analysis [sheet](#glossary-2 "Glossary term").

Information noteThe application is pre-configured so you do not need to add sheets and expressions. However, each step is detailed in [*Understanding the application*](#Understanding).

## Explore the results

You now have the What-If Analysis sheet opened in the application.

Do the following:

1. Select a single employee value in the employee\_number field. A value appears in the Risk of Turnover KPI.
2. Adjust the sliders below the KPI. With each adjustment, a simulation is performed to predict the risk of employee churn.

What-if analysis with a single employee selected, and variables adjusted.

![What-if analysis result](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/what-if-analysis.png "Click to view full size")

## Understanding the application

### Loaded data

The training dataset used in [*Part 2: Train the experiment*](#Train) is used as the application data. In real-world scenarios, this might not always be the case.

### Sheet variables

The following variables were created, each with a blank default definition. The definition is left blank because the variable values are updated on the fly during analysis instead.

Variables for what-if analysis

| Variable name | Model feature it represents | Variable default definition |
| --- | --- | --- |
| vSatisfactionLevel | satisfaction\_level | - |
| vTimeSpent | time\_spend\_company | - |
| vNumberOfProjects | number\_project | - |
| vAvgMonthlyHoursWorked | average\_monthly\_hours | - |

### KPI and expression

A KPI was added to the sheet. The following chart expression is used:

```
endpoints.ScriptEvalStr('{"RequestType":"endpoint", "endpoint":{"connectionname":":MLModel","column":"left_yes"}}',
	vSatisfactionLevel as satisfaction_level,
	vTimeSpent as time_spend_company,
	last_evaluation,
	vNumberOfProjects as number_project,
	vAvgMonthlyHoursWorked as average_monthly_hours)
```

The calculation represents the risk of turnover for the selected employee.

The sections below outline how this expression uses server-side extensions syntax to call the Machine Learning API for real-time predictions.

#### Breaking down the expression

The expression uses server-side extensions (SSE) syntax to generate predictions on the fly.

endpoints.ScriptEvalStr

The endpoints.ScriptEvalStr prefix indicates that server-side extensions are being used. In particular, the ScriptEvalStr function is used. This function allows you to specify the connection name, target, and features without declaring types explicitly. In other words, the API infers feature types automatically when this function is used.

[*Server side extensions syntax*](../LoadData/sse-syntax.htm)

('{"RequestType":"endpoint",

This segment further invokes server-side extensions by specifying that the request is to access a specific endpoint.

[*Server side extensions syntax*](../LoadData/sse-syntax.htm)

Specifying the connection name

The segment "endpoint":{"connectionname":":MLModel" indicates the name of the connection to use. This needs to match the connection name specified in [*Part 4: Create a connection to the Qlik Predict analytics connector*](#Connection). The connection also contains a : prefix to indicate that the connection to use is in the same space as the application.

Specifying the target and requesting probability

The column":"left\_yes" segment indicates that we want to use the left column as the target. The \_yes suffix indicates that we are looking for a probability of the yes outcome. In other words, we are not requesting a predicted value specifically, but instead, the probability of a positive value being predicted.

Specifying the features and variables

After specifying the target column, we need to specify the features in the model. The model features can be obtained by opening the ML deployment (created in [*Part 3: Deploy and activate the top-performing model*](#Deploy)), and then opening Deployment overview. This opens the model schema: the list of features and their feature types.

Deployment overview in an ML deployment, showing the Model schema

![Model schema in Deployment overview for an ML deployment.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/what-if-analysis-model-schema.png "Click to view full size")

From here, the list of features can be constructed as a comma-separated list. Variable substitutions—using the "as" keyword—indicate that current values of variables are to be used as feature data, rather than the application data itself. These variable substitutions allow the interactive, "what-if" simulation that is demonstrated in this example.

```
vSatisfactionLevel as satisfaction_level,
vTimeSpent as time_spend_company,
last_evaluation,
vNumberOfProjects as number_project,
vAvgMonthlyHoursWorked as average_monthly_hours)
```

Information noteThe feature list in the expression needs to include all features in the model schema. Otherwise, predictions fail. Also, if there are features listed in the expression that do not appear in the model schema, the predictions will likewise fail. If you trained a model that does not have the identical set of features as the ones listed in the expressions above, you will need to edit your expression to include or remove features as applicable.

### Variable input objects

Four variable input controls were added to the sheet—one for each variable. The following configurations have been done:

- The variable to use was selected.
- The type of input was selected as Slider.
- Minimum and maximum ranges for each variable were configured, based on values that could reasonably occur as per the original data.

For more information about variable input objects, see [*Creating variable input controls*](../Visualizations/DashboardBundle/creating-variable-input.htm).

### Filter pane

A filter pane was added to allow easy selection of the employee on which to focus.

### Table with the original data

A straight table was also added at the bottom of the sheet, to make it easy to see the original data—before it was altered during the what-if analysis.

## Learn more

- [*Server side extensions syntax*](../LoadData/sse-syntax.htm)
- [*Using Qlik Predict connections in visualization expressions*](../LoadData/ac-qlik-automl-connector-use.htm)
