---
title: "Dynamic naming and storage for batch predictions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/automl-dynamic-naming-predictions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML predictions", "Creating predictions on datasets"]
---

# Dynamic naming and storage for batch predictions

You can use time-based variables when specifying output files and folders for your batch predictions. For example, this is helpful for scheduled predictions, when you need to differentiate many datasets automatically being generated from the same ML deployment.

Dynamic naming and storage is available for the following prediction output datasets:

- Prediction dataset
- Apply dataset
- SHAP dataset
- Coordinate SHAP dataset
- Errors dataset

Do the following:

1. Open an ML deployment, and create or edit a prediction configuration.
2. In the prediction configuration pane, select Prediction dataset (output) > Name prediction dataset.
3. Under Name, specify the path within the space where the datasets will be stored. The path includes folders and the file name.
   Separate folders with / characters. When using dynamic variables, enclose them in double sets of curly braces. File and folder names can both contain these dynamic naming variables. For a list of available variables, see [*Variables supported in output files and folders*](#Variables).

   Dialog for naming the prediction dataset. The Name input shows an example of using dynamic variables and folder storage.

   ![Dialog for naming the prediction dataset. The 'Name' input shows an example of using dynamic variables and folder storage.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-prediction-dataset-name.png "Click to view full size")
4. Select a Space and click Confirm.
5. Expand Prediction options. By default, all other datasets in the batch prediction will populate with the folder path you define above. You can change the dataset path for each of the available datasets. (apply, SHAP, coordinate SHAP, and errors).

Examples:

- A prediction dataset with the following Name: Sales predictions/Customer churn - {{MM-DD-YYYY}}. This could store a dataset Customer churn - 03-24-2025 to a folder Sales predictions within a space.
- A coordinate SHAP dataset with the following name: Predictions/Cancellations\_{{YYYY}}/Cancellations\_{{YYYY-w}}. This could store a dataset Cancellations\_2025-16 to a folder structure Predictions > Cancellations\_2025 within a space.
- A prediction dataset with the following Name: MonthlyProjections\_{{YYMM}}. This could store a dataset MonthlyProjections\_2506 to a space.

### Tips and considerations for dataset naming and storage

- You can use multiple instances of curly braces in a single file path.
- Multiple variables can be used in a single instance of curly braces.
- If any folders specified within the path do not yet exist, the folders are automatically created within the space when datasets are generated.
- Folders are not created if they contain non-compliant syntax. For more information, see [*Rules for valid space folder paths*](../Spaces/manage-data-files-spaces.htm#PathRules).
- The path you specify under Name will be nested within the space you select under Space. The full location for a dataset will include the space when, for example, referring to the dataset in load scripts. For more information, see [*Folder structures in spaces*](../Spaces/manage-data-files-spaces.htm#SpaceFolderStructure) and [*Referencing space folder structure in application and script development*](../Spaces/manage-data-files-spaces.htm#FolderStructureRefExamples).

## Variables supported in output files and folders

The following variables can be used to incorporate dynamic naming and storage for batch prediction output. These characters will only be interpreted as variables when you use a double set of curly braces around them.

- Day

  - DD: day characters
- Month

  - M: month one character
  - MM: month two characters
- Year

  - YY: numeric year (short)
  - YYYY: numeric year (long)
- Week day

  - W: day number of week
  - WW: day number of week (two characters)
- Week

  - w: week number
- Quarter (calendar year only)

  - Q: quarter character
- Time

  - hh: hour number
  - mm: minute number
  - ss: second number
  - ff: fraction of second
- Timestamp

  - X: unix timestamp
  - x: unix millisecond timestamp

    Information noteThe evaluated time always appears in GMT in the file or folder name.
