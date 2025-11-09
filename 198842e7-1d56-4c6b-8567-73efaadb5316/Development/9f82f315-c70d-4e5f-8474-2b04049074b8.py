import pandas as pd

# Create preprocessing summary
summary = {
    'Original Data Shape': '(918, 12)',
    'Missing Values': 'None (0 missing values)',
    'Categorical Encoding': 'Label encoding (Sex, ExerciseAngina) + One-hot (ChestPainType, RestingECG, ST_Slope)',
    'Feature Scaling': 'StandardScaler (mean=0, std=1)',
    'Final Feature Count': X_train.shape[1],
    'Training Samples': f'{X_train.shape[0]} (80%)',
    'Test Samples': f'{X_test.shape[0]} (20%)',
    'Target Variable': 'HeartDisease (0: No, 1: Yes)',
    'Class Balance (Train)': f"0: {y_train.value_counts()[0]}, 1: {y_train.value_counts()[1]}",
    'Class Balance (Test)': f"0: {y_test.value_counts()[0]}, 1: {y_test.value_counts()[1]}"
}

print('='*50)
print('DATA PREPROCESSING SUMMARY')
print('='*50)
for key, value in summary.items():
    print(f'{key}: {value}')
print('='*50)
print('\nPreprocessed datasets ready for modeling!')
print(f'Variables available: X_train, X_test, y_train, y_test')