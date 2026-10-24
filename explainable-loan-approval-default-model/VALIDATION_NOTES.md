# Validation notes

## Reproduction scope

The models were rerun on the supplied files using the same XGBoost configurations and stratified 70/15/15 split settings as the notebook. Stage 1 test ROC-AUC **0.9651**; Stage 2 test ROC-AUC **0.7021**, compared with **0.7042** previously documented. The notebook's original charts and SHAP images were **not** regenerated.

## Material limitations

1. **Unverified provenance:** The two CSVs were supplied by the project owner. The construction of `initial_decision` and original source/redistribution license are not established. The master file has exactly 100,000 Accepted and 100,000 Rejected rows.
2. **Two separate data populations:** The initial-decision data and accepted-loan sample are not demonstrated to form a connected end-to-end decision pipeline.
3. **Completed-loan selection:** The default target uses only resolved loan outcomes; active loans are excluded, potentially introducing selection and time-window bias.
4. **Preprocessing leakage:** In the original notebook, default-model median imputation and one-hot encoding are performed before train/test splitting. The reproduced script follows that approach for comparability; a stricter evaluation would fit preprocessing on training data only.
5. **Test-set threshold tuning:** The notebook chooses a threshold by maximizing F1 on the test set. That selection is exploratory and cannot be reported as unbiased out-of-sample threshold performance.
6. **Feature timing:** Grade, sub-grade, interest rate, and installment can be set during underwriting. The deployment prediction point and feature availability are not established.
7. **No deployment/fairness validation:** No prospective, temporal, calibration, drift, fairness, privacy, or regulatory compliance study has been completed.
8. **Model interpretations:** Existing SHAP images are historical notebook artifacts, not regenerated in the reproduction run.

## Follow-up before making stronger claims

Verify dataset provenance; build a train-only preprocessing pipeline; use a temporal split where possible; choose operating thresholds on validation data; evaluate untouched test data once; inspect subgroup performance and calibration.

## Subsequent stricter evaluation (24 October 2026)

A separate `validate_default_strict.py` run corrected the default model's pre-split imputation/encoding and moved threshold selection to the validation partition. It yielded **0.7019 test ROC-AUC**, **0.3675 average precision**, and, at the validation-selected **0.4972** threshold, **32.7% precision / 60.1% recall**. A new SHAP summary was generated from 150 held-out records as `shap_summary_strict_validation.png`. The original notebook and historical SHAP charts are retained for transparency, not claimed to reflect the stricter run. The initial-decision model was not methodologically revised in this step.

The stricter run is still exploratory because the dataset's provenance and target construction are unverified, the sample excludes unresolved loans, the split is random rather than temporal, and several features may only be known after loan terms are established.
