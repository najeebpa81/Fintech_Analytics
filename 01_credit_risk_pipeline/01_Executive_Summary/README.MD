# Executive Summary: Credit Risk Decision Engine

**Date:** January 01, 2026  
**Project Lead:** [Your Name/ID]  
**Status:** Production-Ready  

## 🎯 Project Objective
The goal of this initiative was to modernize a legacy credit approval process by implementing a dual-gate machine learning pipeline. This system replicates existing policies while adding a predictive layer to identify high-risk applicants before a loan is funded.

---

## 📈 Key Performance Results

The pipeline was evaluated on a hold-out test set (~20,183 rows) that the model had never seen during training.

| Metric | Stage 1 (Approval Filter) | Stage 2 (Risk Engine) |
| :--- | :--- | :--- |
| **Primary Goal** | Policy Replication | Default Prevention |
| **Model Type** | XGBoost Classifier | XGBoost Classifier |
| **AUC-ROC** | ~0.96 | 0.7042 |
| **Precision** | High | 0.369 (Avg. Precision) |
| **Result** | Replicates historical logic | Captures ~69% of Defaults |



---

## 💰 Business Impact & Recommendations

Based on the performance analysis in Step 14, I recommend deploying the model with a **probability threshold of 0.45**.

### **Estimated Impact at 0.45 Threshold:**
* **Portfolio Health:** Reduces the expected default rate among approved loans to **11.4%**, down from a natural baseline of ~20%.
* **Operational Efficiency:** Automatically flags **69% of future defaults** for immediate rejection or manual review.
* **Volume Maintenance:** Maintains a healthy **55% approval rate**, ensuring the bank continues to grow its loan book while filtering the highest-risk profiles.



---

## 🔍 Interpretability & Compliance
To meet financial regulatory standards, the model is not a "black box". Using **SHAP explainability**, we have identified the primary drivers of risk:
1. **Loan Grade & Interest Rate:** Highest predictors of repayment difficulty.
2. **Debt-to-Income (DTI):** High values indicate over-leveraged borrowers.
3. **FICO Scores:** Critical for baseline creditworthiness.

Every individual decision can be justified with a **Local Force Plot**, showing exactly which factors led to an approval or denial.



---

## 🚀 Final Delivery Status
The models are refined and ready for deployment. 
**Recommendation:** Quarterly retraining is advised to monitor for data drift and ensure the model adapts to changing economic conditions.
