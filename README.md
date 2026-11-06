# Fintech Analytics — Explainable Loan Classification

An educational two-stage machine-learning study using Python, XGBoost, and SHAP. The first model predicts a supplied historical `initial_decision` label; the second distinguishes charged-off/defaulted loans from fully paid loans among completed historical accepted loans. **Neither model is validated for operational credit decisions.**

## Why this project matters to an analytics client

This project demonstrates a repeatable **analytics workflow**: define a prediction target, prepare historical data, evaluate a classification model on held-out records, explain model behavior with SHAP, and document limitations. These skills can support scoped work such as data-quality reviews, retrospective model assessments, explainability reports, and stakeholder-friendly analytical summaries. Any client engagement would require a separate data-access, governance, and validation review.

**What this portfolio does not offer:** a ready-to-use loan approval engine, a production default-risk score, a fair-lending compliance assessment, or proof of prospective business impact.

## How to navigate the evidence

- Start with the [project README](explainable-loan-approval-default-model/README.md) for scope and setup.
- Read the [methodological limitations](explainable-loan-approval-default-model/VALIDATION_NOTES.md) before interpreting performance figures.
- Use the [strict validation results](explainable-loan-approval-default-model/strict_validation_metrics.json) for the separately improved retrospective default-model evaluation.
- Treat the [exploratory notebook](explainable-loan-approval-default-model/03_source_code/Predictive_Model_Loan_Approval.ipynb) and most historical charts as educational artifacts, not outputs from the strict validation run.

**Reproduction:** The original CSV inputs are not included. Dataset provenance and redistribution rights remain unverified, so a reader cannot reproduce the metrics from the public repository alone.

## Project

[Explainable Loan Approval & Default Modeling](explainable-loan-approval-default-model/README.md)

## Verified reproduction (original methodology)

| Model | Validation ROC-AUC | Held-out test ROC-AUC |
|---|---:|---:|
| Initial-decision classification | 0.9635 | 0.9651 |
| Completed-loan default classification | 0.7174 | 0.7021 |

These are results from a fresh run of the original model settings using the user-provided CSV files. They are not evidence of production performance. See [validation notes](explainable-loan-approval-default-model/VALIDATION_NOTES.md).

Raw and row-level datasets are excluded pending source/license verification.

## Improved retrospective evaluation

A separate stricter default-risk evaluation fits preprocessing on training data only and selects its classification threshold on validation data. Held-out test ROC-AUC **0.7019**, average precision **0.3675**, precision **32.7%**, and recall **60.1%** at the validation-selected threshold. See [strict validation metrics](explainable-loan-approval-default-model/strict_validation_metrics.json) and [limitations](explainable-loan-approval-default-model/VALIDATION_NOTES.md).

These are historical classification experiments, not lending recommendations or a deployed system.
