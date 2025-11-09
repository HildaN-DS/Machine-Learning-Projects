import pandas as pd
import matplotlib.pyplot as plt

# Extract correlations with the target variable (HeartDisease)
hd_correlations = corr_matrix['HeartDisease'].copy()

# Map indices to feature names for better readability
feature_names_mapping = dict(enumerate(corr_matrix.columns))
hd_correlations.index = hd_correlations.index.map(feature_names_mapping)

# Remove self-correlation (HeartDisease with itself = 1.0)
hd_correlations = hd_correlations[hd_correlations.index != 'HeartDisease']

# Sort by correlation values
target_corr_sorted = hd_correlations.sort_values(ascending=False)

# Create bar chart
plt.figure(figsize=(10, 6))
colors = ['#d62728' if x > 0 else '#1f77b4' for x in target_corr_sorted.values]
bars = plt.barh(range(len(target_corr_sorted)), target_corr_sorted.values, color=colors)
plt.yticks(range(len(target_corr_sorted)), target_corr_sorted.index)
plt.xlabel('Correlation with Heart Disease', fontsize=12)
plt.ylabel('Features', fontsize=12)
plt.title('Feature Correlation with Heart Disease Target', fontsize=14, pad=20)
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.grid(axis='x', alpha=0.3)

# Add value labels on bars
for i, (_bar, val) in enumerate(zip(bars, target_corr_sorted.values)):
    plt.text(val + 0.01 if val > 0 else val - 0.01, i, f'{val:.3f}', 
             va='center', ha='left' if val > 0 else 'right', fontsize=10)

plt.tight_layout()
plt.show()

print('Top 3 positively correlated features:')
for feat, corr_val in target_corr_sorted.head(3).items():
    print(f'  {feat}: {corr_val:.3f}')
    
print('\nTop 3 negatively correlated features:')
for feat, corr_val in target_corr_sorted.tail(3).items():
    print(f'  {feat}: {corr_val:.3f}')