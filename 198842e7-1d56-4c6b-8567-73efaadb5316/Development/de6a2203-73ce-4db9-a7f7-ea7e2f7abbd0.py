from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import pandas as pd

# Calculate metrics for all three models
eval_results = []

# Logistic Regression
lr_metrics = {
    'Model': 'Logistic Regression',
    'Accuracy': accuracy_score(y_test, lr_test_pred),
    'Precision': precision_score(y_test, lr_test_pred),
    'Recall': recall_score(y_test, lr_test_pred),
    'F1-Score': f1_score(y_test, lr_test_pred),
    'ROC-AUC': roc_auc_score(y_test, lr_test_proba)
}
eval_results.append(lr_metrics)

# Random Forest
rf_metrics = {
    'Model': 'Random Forest',
    'Accuracy': accuracy_score(y_test, rf_test_pred),
    'Precision': precision_score(y_test, rf_test_pred),
    'Recall': recall_score(y_test, rf_test_pred),
    'F1-Score': f1_score(y_test, rf_test_pred),
    'ROC-AUC': roc_auc_score(y_test, rf_test_proba)
}
eval_results.append(rf_metrics)

# Gradient Boosting
gb_metrics = {
    'Model': 'Gradient Boosting',
    'Accuracy': accuracy_score(y_test, gb_test_pred),
    'Precision': precision_score(y_test, gb_test_pred),
    'Recall': recall_score(y_test, gb_test_pred),
    'F1-Score': f1_score(y_test, gb_test_pred),
    'ROC-AUC': roc_auc_score(y_test, gb_test_proba)
}
eval_results.append(gb_metrics)

# Create DataFrame
eval_metrics_df = pd.DataFrame(eval_results)

print('Model Evaluation Metrics:')
print('='*80)
print(eval_metrics_df.to_string(index=False))
print('='*80)