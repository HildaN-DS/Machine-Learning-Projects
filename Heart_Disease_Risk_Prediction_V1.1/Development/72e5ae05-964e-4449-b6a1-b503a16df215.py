import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Identify numerical columns
numerical_features = heart_df.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Create subplots for boxplots
_fig, _axes = plt.subplots(3, 3, figsize=(15, 12))
_axes = _axes.flatten()

for _idx, _feature in enumerate(numerical_features):
    sns.boxplot(data=heart_df, y=_feature, ax=_axes[_idx], color='lightcoral')
    _axes[_idx].set_title(f'{_feature} - Outlier Detection', fontsize=12, fontweight='bold')
    _axes[_idx].set_ylabel(_feature, fontsize=10)

plt.tight_layout()
plt.show()

print(f'Created boxplots for {len(numerical_features)} numerical features to detect outliers')