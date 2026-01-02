# Source Code: End-to-End Credit Risk Pipeline

This directory contains the complete, reproducible codebase for the dual-stage lending decision system.

## 🛠️ Main Notebook
**`Predictive_Model_Loan_Approval.ipynb`**

A fully annotated Jupyter notebook implementing the entire pipeline in a logical, step-by-step flow:

1. **Data Ingestion & Cleaning** — Loading and preparing Lending Club data as raw client input
2. **Stage 1: Approval Filter** — XGBoost model replicating historical approval policy (AUC ~0.96)
3. **Feature Engineering** — Creating 40+ predictive features for risk scoring
4. **Stage 2: Default Risk Engine** — XGBoost with class weighting for imbalanced defaults (Test AUC 0.7042)
5. **Explainability** — Comprehensive SHAP analysis (global importance + local force plots)
6. **Evaluation & Threshold Optimization** — Test performance and business impact simulation
7. **Production Simulation** — Applying models to generate predictions on new data

The notebook is designed for both **understanding** and **deployment adaptation**.

## 📦 Saved Models
- `approval_model.pkl` — Trained approval filter
- `default_model.pkl` — Trained default risk engine

Load with:
```python
import joblib
approval_model = joblib.load('approval_model.pkl')
default_model = joblib.load('default_model.pkl')
