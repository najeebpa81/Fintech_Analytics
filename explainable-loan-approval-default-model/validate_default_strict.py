from pathlib import Path
import json, numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import roc_auc_score,average_precision_score,precision_recall_curve,precision_score,recall_score,f1_score,confusion_matrix
from xgboost import XGBClassifier
root=Path(__file__).resolve().parent
import argparse
parser=argparse.ArgumentParser(description='Reproduce the strict default-model validation using local, untracked datasets')
parser.add_argument('--accepted-csv',required=True,help='Path to accepted_sample.csv')
args=parser.parse_args()
cols=['loan_status','loan_amnt','term','int_rate','installment','grade','sub_grade','emp_length','home_ownership','annual_inc','verification_status','purpose','dti','delinq_2yrs','fico_range_low','fico_range_high','inq_last_6mths','open_acc','pub_rec','revol_bal','revol_util','total_acc','initial_list_status','application_type','mort_acc','pub_rec_bankruptcies']
df=pd.read_csv(args.accepted_csv,usecols=cols,low_memory=False)
statuses=['Fully Paid','Charged Off','Default','Does not meet the credit policy. Status:Fully Paid','Does not meet the credit policy. Status:Charged Off']
df=df[df.loan_status.isin(statuses)].copy()
y=df.loan_status.isin(['Charged Off','Default','Does not meet the credit policy. Status:Charged Off']).astype(int)
X=df.drop(columns=['loan_status']).copy()
# Keep grade and loan terms as in the historical exploratory experiment, but explicitly note their availability limitations.
num=X.select_dtypes(include='number').columns.tolist(); cat=[c for c in X.columns if c not in num]
Xdev,Xtest,ydev,ytest=train_test_split(X,y,test_size=.15,stratify=y,random_state=42)
Xtrain,Xval,ytrain,yval=train_test_split(Xdev,ydev,test_size=.1765,stratify=ydev,random_state=42)
prep=ColumnTransformer([('num',SimpleImputer(strategy='median'),num),('cat',Pipeline([('impute',SimpleImputer(strategy='most_frequent')),('onehot',OneHotEncoder(handle_unknown='ignore',sparse_output=True))]),cat)],sparse_threshold=.3)
w=float((ytrain==0).sum()/(ytrain==1).sum())
model=XGBClassifier(n_estimators=300,max_depth=7,learning_rate=.05,subsample=.8,colsample_bytree=.8,random_state=42,scale_pos_weight=w,eval_metric='auc',n_jobs=4,tree_method='hist')
pipe=Pipeline([('preprocessing',prep),('classifier',model)])
pipe.fit(Xtrain,ytrain)
val=pipe.predict_proba(Xval)[:,1]; test=pipe.predict_proba(Xtest)[:,1]
pr,rc,thr=precision_recall_curve(yval,val); f1=2*pr[:-1]*rc[:-1]/np.maximum(pr[:-1]+rc[:-1],1e-12); idx=int(np.argmax(f1)); threshold=float(thr[idx])
metrics={'dataset_rows_resolved':len(df),'train_rows':len(Xtrain),'validation_rows':len(Xval),'test_rows':len(Xtest),'default_rate':float(y.mean()),'validation_roc_auc':float(roc_auc_score(yval,val)),'test_roc_auc':float(roc_auc_score(ytest,test)),'test_average_precision':float(average_precision_score(ytest,test)),'threshold_selected_on_validation':threshold,'test_precision_at_selected_threshold':float(precision_score(ytest,test>=threshold,zero_division=0)),'test_recall_at_selected_threshold':float(recall_score(ytest,test>=threshold,zero_division=0)),'test_f1_at_selected_threshold':float(f1_score(ytest,test>=threshold,zero_division=0)),'test_confusion_matrix':confusion_matrix(ytest,test>=threshold).tolist()}
(root/'strict_validation_metrics.json').write_text(json.dumps(metrics,indent=2))
print(json.dumps(metrics,indent=2),flush=True)
# New SHAP summary, computed on a reproducible 150-record held-out subset.
try:
 import shap, matplotlib
 matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 sample=Xtest.sample(n=min(150,len(Xtest)),random_state=42)
 transformed=prep.transform(sample)
 if hasattr(transformed,'toarray'):transformed=transformed.toarray()
 names=prep.get_feature_names_out()
 explainer=shap.TreeExplainer(model)
 sv=explainer.shap_values(transformed)
 shap.summary_plot(sv,transformed,feature_names=names,show=False,max_display=15)
 plt.tight_layout();plt.savefig(root/'05_visual_insights'/'shap_summary_strict_validation.png',dpi=140,bbox_inches='tight');plt.close()
 metrics['shap_regenerated']=True
except Exception as e:
 metrics['shap_regenerated']=False;metrics['shap_error']=str(e)
 (root/'strict_validation_metrics.json').write_text(json.dumps(metrics,indent=2))
 print('SHAP:',str(e),flush=True)

(root/'strict_validation_metrics.json').write_text(json.dumps(metrics,indent=2))
