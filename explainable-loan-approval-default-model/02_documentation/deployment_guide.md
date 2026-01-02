# Deployment Guide: Applying Models to New Client Data

## 1. Approval Model (Stage 1)
- Required input columns: loan_amnt, dti, emp_length_years
- Load saved model: approval_model.pkl
- Code example (Python):
```python
# Load model
import joblib
approval_model = joblib.load('approval_model.pkl')

# Predict on new dataframe df_new
df_new['approval_probability'] = approval_model.predict_proba(df_new[['loan_amnt', 'dti', 'emp_length_years']])[:, 1]
df_new['predicted_decision'] = (df_new['approval_probability'] >= 0.5).map({True: 'Approved', False: 'Rejected'})
