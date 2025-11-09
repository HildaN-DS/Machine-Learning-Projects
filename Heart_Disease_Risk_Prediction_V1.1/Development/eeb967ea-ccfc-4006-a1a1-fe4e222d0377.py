import pandas as pd

# Create a summary of all trained models
models_summary = {
    'Model': ['Logistic Regression', 'Random Forest', 'Gradient Boosting'],
    'Type': ['Linear', 'Ensemble (Bagging)', 'Ensemble (Boosting)'],
    'Trained': ['✓', '✓', '✓'],
    'Variables': ['lr_model, lr_train_pred, lr_test_pred', 
                  'rf_model, rf_train_pred, rf_test_pred',
                  'gb_model, gb_train_pred, gb_test_pred']
}

models_df = pd.DataFrame(models_summary)

print('='*60)
print('BASELINE MODELS TRAINING COMPLETE')
print('='*60)
print(models_df.to_string(index=False))
print('='*60)
print(f'\n✓ {len(models_df)} baseline models trained successfully')
print(f'✓ Training data: {X_train.shape[0]} samples, {X_train.shape[1]} features')
print(f'✓ Test data: {X_test.shape[0]} samples')
print('\nReady for model evaluation and comparison!')