import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Identify numerical columns
num_cols = heart_df.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Create subplots for histograms with KDE curves
_fig, _axes = plt.subplots(3, 3, figsize=(15, 12))
_axes = _axes.flatten()

for _idx, _col in enumerate(num_cols):
    sns.histplot(data=heart_df, x=_col, kde=True, ax=_axes[_idx], color='skyblue', edgecolor='black')
    _axes[_idx].set_title(f'{_col} Distribution', fontsize=12, fontweight='bold')
    _axes[_idx].set_xlabel(_col, fontsize=10)
    _axes[_idx].set_ylabel('Frequency', fontsize=10)

plt.tight_layout()
plt.show()

print(f'Created histograms with KDE for {len(num_cols)} numerical features')