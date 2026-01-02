# Explainable Credit Risk Pipeline: Approval + Default Prediction

**End-to-End Dual-Stage Lending Decision System**  
Built on Lending Club data (2007–2018) — treated as raw client input.

This project delivers a **production-ready, transparent credit risk pipeline** that balances loan volume with default prevention — designed to integrate directly into banking workflows.

## 🏗️ Dual-Gate Architecture

A realistic two-stage system mirroring professional lending processes:

### 1. Stage 1: Approval Filter (Gatekeeper)
- **Objective**: Replicate historical approval/rejection policy
- **Inputs**: 3 core features (`loan_amnt`, `dti`, `emp_length_years`)
- **Performance**: **Validation AUC ~0.96** — near-perfect replication of past decisions

### 2. Stage 2: Default Risk Engine
- **Objective**: Predict probability of default **only for approved applicants**
- **Inputs**: 40 engineered features (grade, interest rate, FICO, income, DTI, etc.)
- **Performance**: 
  - Test **AUC 0.7042**
  - Average Precision **0.369**
  - Catches **~69% of defaults** at optimal threshold

## 📊 Key Business Impact

Tunable risk thresholds enable direct control over portfolio quality:

| Metric                          | Value                  | Insight                                      |
|---------------------------------|-----------------------|----------------------------------------------|
| Default Capture (Recall)        | ~69%                  | Identifies majority of future defaulters     |
| Approval Rate (at optimal)      | ~55%                  | Sustainable volume                           |
| Default Rate Among Approved     | ~11.4%                | Halves natural baseline (~20%)               |
| Recommended Threshold           | 0.45                  | Best risk/volume balance (highest F1)        |

## 🔍 Full Explainability with SHAP

Regulatory-compliant transparency built in:

- **Global insights**: Grade, interest rate, term length, DTI, and FICO dominate default risk
- **Local explanations**: Force plots show exactly **why** each applicant was scored high/low risk
- Enables fair lending compliance, customer communication, and audit trails

## 📂 Repository Structure

Professional, client-ready organization:

- **01_Executive_Summary/** → Presentation-ready overview and business case
- **02_Documentation/** → Methodology, data dictionary, deployment guide
- **03_Source_Code/** → Fully annotated Jupyter notebook + saved models
- **04_Data_Deliverables/** → Sample scored outputs and threshold analysis
- **05_Visual_Insights/** → ROC/PR curves, SHAP beeswarm & force plots

## 🚀 Status & Next Steps

**Project Status**: Complete · Production-Ready  
**Recommended Actions**:
- Integrate into loan origination system
- Monitor model drift quarterly
- Retrain with fresh client data

**Tech Stack**: Python · Pandas · XGBoost · SHAP · Matplotlib/Seaborn

---

*Ideal for fintech lenders seeking automated, transparent, and tunable credit decisioning.*

Contact: Mohamed Najeeb P.A/najeebpa81@gmail.com for customization or deployment support.
