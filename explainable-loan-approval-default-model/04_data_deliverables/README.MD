# Data Deliverables: Scored Loan Applications

This folder contains sample output files that demonstrate the **real-world value** delivered to clients — enriched loan application data with model predictions and business decision tools.

## Files Overview

### 1. `master_lead_data_with_approval_predictions.csv`
- **Source**: Historical applications (combined accepted + rejected)
- **What we did**: Applied the **Approval Filter Model** to the full historical dataset
- **New columns added**:
  - `approval_probability`: Model confidence (0–1) that the application should be approved
  - `predicted_decision`: "Approved" or "Rejected" (threshold 0.5)
  - `approval_risk_tier`: Low/Medium/High Risk buckets
- **Purpose**: Shows how the model replicates (and potentially improves) past decisions
- **Sample size**: Full processed historical data (subset for repo)

### 2. `sample_new_applications_scored_client_friendly.csv`
- **Source**: Simulated **new/future** loan applications (random sample from accepted data, treated as incoming)
- **What we did**:
  - Applied **both models** in sequence:
    1. Approval Filter → decide Approve/Reject
    2. Default Risk Engine → score default probability **only for approved**
  - Simplified columns for easy reading (no internal one-hot dummies)
- **Key columns for clients**:
  - Original inputs (loan_amnt, int_rate, grade, dti, fico_avg, annual_inc, etc.)
  - `approval_probability` & `predicted_decision`
  - `default_probability` & `default_risk_tier` (Low/Medium/High)
- **Purpose**: Exact format of what clients receive for **new applications**

### 3. `threshold_analysis_summary.csv`
- **Source**: Test set evaluation of the Default Risk Model
- **What it shows**: Impact of different probability thresholds on key business metrics
- **Columns**:
  - `Threshold`: Cutoff for predicting "Default"
  - `Precision`, `Recall`, `F1_Score`
  - `Approved_%`: % of applications approved
  - `Default_Rate_Among_Approved_%`: Expected default rate in approved portfolio
  - `Note`: Highlights recommended threshold (highest F1)
- **Purpose**: Enables clients to **tune risk appetite** — balance volume vs default prevention
- **Recommendation**: Threshold **0.45** → ~55% approval rate, ~11.4% default rate among approved, captures ~69% of defaults

## Business Decisions Clients Can Make

| Use Case                          | How to Use the Files                             | Example Decision                              |
|-----------------------------------|--------------------------------------------------|-----------------------------------------------|
| **Automated Approval**            | Filter `predicted_decision == 'Approved'`        | Auto-approve low-risk tier                    |
| **Manual Review Queue**           | Filter `approval_risk_tier == 'Medium Risk'`     | Send for human review                         |
| **Risk-Based Pricing**            | Use `default_probability`                        | Higher interest for High Risk tier            |
| **Portfolio Monitoring**          | Track average `default_probability` over time    | Detect rising risk in new applications        |
| **Threshold Tuning**              | Refer to `threshold_analysis_summary.csv`        | Adjust cutoff for more/less conservative policy |
| **Customer Communication**        | Explain rejection using high-risk features       | "High DTI and interest rate increased risk"   |

## Notes
- Files are **samples only** (repo size limits). Full outputs available on request.
- Predictions generated using trained models (`approval_model.pkl`, `default_model.pkl`).
- Thresholds are fully tunable — contact for custom risk appetite adjustments.

These deliverables turn raw applications into **actionable, transparent lending decisions**.

