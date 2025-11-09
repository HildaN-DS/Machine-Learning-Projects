import pandas as pd

# Analyze target variable distribution
target_counts = heart_df['HeartDisease'].value_counts()
target_pct = (target_counts / len(heart_df) * 100).round(2)

print('Target Variable (HeartDisease) Distribution:')
print(f'  No Heart Disease (0): {target_counts[0]} ({target_pct[0]}%)')
print(f'  Heart Disease (1): {target_counts[1]} ({target_pct[1]}%)')
print(f'\nClass balance ratio: {(target_counts[1] / target_counts[0]):.2f}')