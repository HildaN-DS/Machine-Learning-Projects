from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# Calculate ROC curves for all models
_lr_fpr, _lr_tpr, _ = roc_curve(y_test, lr_test_proba)
_rf_fpr, _rf_tpr, _ = roc_curve(y_test, rf_test_proba)
_gb_fpr, _gb_tpr, _ = roc_curve(y_test, gb_test_proba)

_lr_auc = auc(_lr_fpr, _lr_tpr)
_rf_auc = auc(_rf_fpr, _rf_tpr)
_gb_auc = auc(_gb_fpr, _gb_tpr)

# Create ROC curve plot
_fig, _ax = plt.subplots(figsize=(10, 8))

_ax.plot(_lr_fpr, _lr_tpr, color='#2E86AB', lw=2, 
         label=f'Logistic Regression (AUC = {_lr_auc:.3f})')
_ax.plot(_rf_fpr, _rf_tpr, color='#A23B72', lw=2, 
         label=f'Random Forest (AUC = {_rf_auc:.3f})')
_ax.plot(_gb_fpr, _gb_tpr, color='#F18F01', lw=2, 
         label=f'Gradient Boosting (AUC = {_gb_auc:.3f})')
_ax.plot([0, 1], [0, 1], color='gray', lw=1, linestyle='--', label='Random Classifier')

_ax.set_xlim([0.0, 1.0])
_ax.set_ylim([0.0, 1.05])
_ax.set_xlabel('False Positive Rate', fontsize=12, fontweight='bold')
_ax.set_ylabel('True Positive Rate', fontsize=12, fontweight='bold')
_ax.set_title('ROC Curves - Model Comparison', fontsize=14, fontweight='bold')
_ax.legend(loc='lower right')
_ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()

print('ROC curves comparison created')