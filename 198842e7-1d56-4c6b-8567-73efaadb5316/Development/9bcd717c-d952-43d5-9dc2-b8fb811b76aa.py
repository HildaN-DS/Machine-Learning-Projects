import matplotlib.pyplot as plt
import numpy as np

# Create bar chart comparing metrics across models
_fig, _ax = plt.subplots(figsize=(12, 6))

_metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC']
_x = np.arange(len(_metrics))
_width = 0.25

# Plot bars for each model
_lr_vals = [eval_metrics_df.loc[0, m] for m in _metrics]
_rf_vals = [eval_metrics_df.loc[1, m] for m in _metrics]
_gb_vals = [eval_metrics_df.loc[2, m] for m in _metrics]

_ax.bar(_x - _width, _lr_vals, _width, label='Logistic Regression', color='#2E86AB')
_ax.bar(_x, _rf_vals, _width, label='Random Forest', color='#A23B72')
_ax.bar(_x + _width, _gb_vals, _width, label='Gradient Boosting', color='#F18F01')

_ax.set_xlabel('Metrics', fontsize=12, fontweight='bold')
_ax.set_ylabel('Score', fontsize=12, fontweight='bold')
_ax.set_title('Model Performance Comparison', fontsize=14, fontweight='bold')
_ax.set_xticks(_x)
_ax.set_xticklabels(_metrics)
_ax.legend()
_ax.set_ylim(0.8, 1.0)
_ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

print('Performance comparison chart created')