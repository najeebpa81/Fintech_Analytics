# Project Documentation: Explainable Credit Risk Pipeline

## 1. Overview
Brief recap of the dual-stage architecture (Approval Filter + Default Risk Engine).

## 2. Data Sources
- Lending Club public dataset (2007–2018)
- How it was treated as "raw client input"
- Separate accepted/rejected files → combined into master

## 3. Preprocessing & Cleaning
- Handling missing values (e.g., emp_length dropped or filled)
- Data type conversions
- Outlier treatment (if any)

## 4. Feature Engineering
- Approval model: 3 core features
- Default model: Full list of 40 features + derivations (term_months, grade_num, fico_avg, etc.)
- Rationale for each

## 5. Modeling Methodology
- Train/val/test split strategy (stratified)
- XGBoost configuration (parameters, scale_pos_weight for imbalance)
- Threshold selection process

## 6. Evaluation Metrics
- AUC-ROC, Average Precision, Recall at different thresholds
- Business-focused interpretation

## 7. Limitations & Future Improvements
- Sample size, historical bias
- Potential for more features (e.g., behavioral data)
- Monitoring for drift

## 8. Reproducibility Notes
- Python version, random_state=42
- requirements.txt location
