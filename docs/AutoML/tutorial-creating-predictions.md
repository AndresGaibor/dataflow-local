---
title: "Creating prediction data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/tutorial-creating-predictions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Tutorial – Generating and visualizing prediction data"]
---

# Creating prediction data

After you have deployed and approved your model, you can create predictions on new data. In this tutorial, we create a prediction configuration within the ML deployment and use it to run a [batch prediction](#glossary-0 "Glossary term").

So far, we have used existing customer data to create a machine learning model. The goal with this process has been to recognize patterns through machine learning, with the goal of applying them to new data.

There is also a use case for only analyzing the SHAP values in the training data. This information is also highly valuable in its own right.

For more information about batch predictions in Qlik Predict, see [*Creating predictions on datasets*](creating-predictions.htm).

The first step in the process is to choose a dataset to which you will be applying your model to generate predictions. After this, you configure your desired properties for the output and generate the files.

Do the following:

1. In the catalog, open your new ML deployment.
2. In the bottom right corner, click Create prediction.
3. In the Prediction configuration pane on the right side, under Apply data, click Select apply dataset.
4. Select the [apply dataset](#glossary-1 "Glossary term") file. This will be either of the following, depending on whether you are working with CSV or QVD:

   - ML - Churn data - apply.csv
   - ML - Churn data - apply.qvf
5. Compare the schemas of the [training](#glossary-2 "Glossary term") and apply datasets. Because you deselected features during training, your apply dataset will have more fields than the training dataset. This is not any cause for concern. When generating predictions, Qlik Predict simply ignores fields from the apply dataset which do not exist in the training dataset.
6. In the Prediction configuration pane, click Name prediction dataset. Type the following name: ML - Prediction output. We will use the default Parquet format.
7. Select a space and click Confirm.
8. Under Prediction options, you configure the additional datasets you want to generate with this prediction. In this case, confirm that Coordinate SHAP is the only selected option. Allow AccountID to be used as the index column.

   ![Prediction configuration menu and dataset schemas when creating predictions.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-tutorial_batch-prediction.png "Click to view full size")

Click the ![Down arrow](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dropdown_arrow.svg) icon next to Save and close. Select Save and predict now.

The process can be monitored in Dataset predictions. You can review the output in the catalog by clicking Open in the popup that appears.

When the prediction has finished running, you can start building an application using the new datasets. Move to the next topic.
