# 🛡️ 01: End-to-End Credit Risk Pipeline

## Project Overview
This project addresses the critical challenge of balancing loan approval volume with effective default prevention. Using the **Lending Club dataset (2007–2018)**—treated as raw client input—I developed a dual-stage machine learning system that replicates initial "Gatekeeper" decisions before applying a high-fidelity risk prediction engine.

---

## 🏗️ The Dual-Gate Architecture

The system is designed as a sequence of two distinct models to simulate a real-world professional banking workflow:

### 1. Stage 1: The Approval Filter
* **Objective:** Replicate the historical initial decision policy to identify which applicants typically qualify for a loan.
* **Inputs:** Core application data including `loan_amnt`, `dti`, and `emp_length_years`.
* **Performance:** Achieved a **Validation AUC of ~0.96**, ensuring the model replicates historical patterns with high accuracy.

### 2. Stage 2: The Default Risk Engine
* **Objective:** Predict the actual probability of default (PD) specifically for those applicants who pass the first gate.
* **Inputs:** 40 engineered features derived from rich accepted loan data, including FICO scores, interest rates, and debt metrics.
* **Performance:** Achieved a **Test AUC of 0.7042** and an **Average Precision (AP) of 0.369**.



---

## 📊 Key Results & Business Impact

The model provides actionable, data-driven recommendations that can be tuned based on a bank's specific risk appetite:

* **Default Capture:** At the recommended threshold, the model successfully identifies **~69% of future defaults**.
* **Approval Quality:** By filtering out high-risk applicants, the expected default rate among approved loans is reduced to **~11.4%** (compared to the ~20% natural baseline).
* **Optimized Recommendation:** A probability threshold of **0.45** is suggested to maximize risk control while maintaining a sustainable approval rate of ~55%.

---

## 🔍 Explainable AI (SHAP)
Financial transparency is a regulatory requirement. Using **SHAP (SHapley Additive exPlanations)**, this pipeline moves beyond "Black Box" modeling:

* **Global Feature Importance:** Grade, interest rate, term, DTI, and FICO were identified as the dominant drivers of default risk.
* **Local Transparency:** Force plots provide a clear "why" for every individual prediction, allowing for client-friendly explanations and regulatory auditability.



---

## 📂 Directory Structure
This project follows a systematic, professional documentation standard:

* **`01_Executive_Summary/`**: Client-ready executive summary and business impact overview.
* **`02_Documentation/`**: Technical methodology, data dictionary, and research notes.
* **`03_Source_Code/`**: Annotated Jupyter Notebooks covering the end-to-end pipeline.
* **`04_Data_Deliverables/`**: Threshold optimization tables and performance metrics.
* **`05_Visual_Insights/`**: High-resolution ROC/PR curves and SHAP explainability visualizations.

---
**Status:** Complete and Ready for Deployment  
**Next Steps:** Integrate into application API, monitor performance, and retrain quarterly to account for data drift.
