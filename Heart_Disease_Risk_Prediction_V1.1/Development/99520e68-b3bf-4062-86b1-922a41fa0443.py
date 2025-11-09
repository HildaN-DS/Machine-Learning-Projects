import pandas as pd

# Calculate detailed percentage breakdown of target variable
target_breakdown_counts = heart_df['HeartDisease'].value_counts().sort_index()
target_breakdown_pct = (target_breakdown_counts / len(heart_df) * 100).round(2)

print('=' * 50)
print('TARGET VARIABLE PERCENTAGE BREAKDOWN')
print('=' * 50)
print(f'\nTotal Samples: {len(heart_df)}\n')
print(f'No Heart Disease (0):')
print(f'  • Count: {target_breakdown_counts[0]}')
print(f'  • Percentage: {target_breakdown_pct[0]}%')
print(f'\nHeart Disease (1):')
print(f'  • Count: {target_breakdown_counts[1]}')
print(f'  • Percentage: {target_breakdown_pct[1]}%')
print(f'\nClass Balance Ratio (Disease/No Disease): {(target_breakdown_counts[1] / target_breakdown_counts[0]):.2f}')
print('=' * 50)