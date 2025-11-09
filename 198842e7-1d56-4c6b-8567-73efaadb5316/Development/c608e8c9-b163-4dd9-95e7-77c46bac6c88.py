import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Identify numerical columns
numeric_features = heart_df.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Create subplots for violin plots
_fig, _axes = plt.subplots(3, 3, figsize=(15, 12))
_axes = _axes.flatten()

for _idx, _col_name in enumerate(numeric_features):
    sns.violinplot(data=heart_df, y=_col_name, ax=_axes[_idx], color='mediumpurple')
    _axes[_idx].set_title(f'{_col_name} - Violin Plot', fontsize=12, fontweight='bold')
    _axes[_idx].set_ylabel(_col_name, fontsize=10)

plt.tight_layout()
plt.show()

print(f'Created violin plots for {len(numeric_features)} numerical features')