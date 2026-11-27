---
title: "Understanding model review concepts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/model-review-concepts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Reviewing models"]
---

# Understanding model review concepts

It can be helpful to have a basic understanding of model metrics before you start analyzing your training results.

The available model metrics can broadly be separated into two types: model scores and feature importance metrics. Both types of metrics should be analyzed when you review your models.

There are also differences between how each of the available algorithms trains your models.

## Model scores

Model scores indicate the accuracy of the model's predictions.

[*Interpreting model scores*](scoring-models.htm)

## Feature importance

Feature importance is not technically a model score, but it should be used in combination with model scores to assess model quality and diagnose potential issues. Feature importance also offers insight into the key drivers influencing trends in the data.

[*Understanding feature importance*](feature-importance.htm)

## Algorithms

Certain algorithms work best with specific problem types. Each algorithm has its strengths and weaknesses, which should be considered when reviewing models.

[*Understanding model algorithms*](algorithms.htm)
