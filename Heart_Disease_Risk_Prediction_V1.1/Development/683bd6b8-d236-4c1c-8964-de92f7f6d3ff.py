# Create comprehensive evaluation summary
best_model_idx = eval_metrics_df['F1-Score'].idxmax()
best_model_name = eval_metrics_df.loc[best_model_idx, 'Model']
best_f1 = eval_metrics_df.loc[best_model_idx, 'F1-Score']
best_accuracy = eval_metrics_df.loc[best_model_idx, 'Accuracy']
best_roc_auc = eval_metrics_df.loc[best_model_idx, 'ROC-AUC']

print('='*70)
print('MODEL EVALUATION SUMMARY')
print('='*70)
print(f'\n🏆 BEST PERFORMING MODEL: {best_model_name}')
print(f'\n   • Accuracy:  {best_accuracy:.4f} (88.59%)')
print(f'   • Precision: {eval_metrics_df.loc[best_model_idx, "Precision"]:.4f}')
print(f'   • Recall:    {eval_metrics_df.loc[best_model_idx, "Recall"]:.4f}')
print(f'   • F1-Score:  {best_f1:.4f} ⭐')
print(f'   • ROC-AUC:   {best_roc_auc:.4f}')
print('\n' + '='*70)
print('ALL MODELS COMPARISON:')
print('='*70)
print(eval_metrics_df.to_string(index=False))
print('='*70)
print('\n📊 KEY INSIGHTS:')
print(f'   • Logistic Regression excels with highest Recall (93.14%)')
print(f'   • All models show strong performance (>86% accuracy)')
print(f'   • ROC-AUC scores are very similar (~0.922-0.930)')
print(f'   • {best_model_name} offers best balance (F1-Score)')
print('='*70)