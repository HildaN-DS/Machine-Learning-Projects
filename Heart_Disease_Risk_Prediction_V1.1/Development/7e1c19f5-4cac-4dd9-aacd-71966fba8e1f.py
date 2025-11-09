import pandas as pd
import matplotlib.pyplot as plt

# Get categorical features
cat_features = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

# Create bar charts for each categorical feature
_fig, _axes = plt.subplots(2, 3, figsize=(15, 8))
_axes = _axes.flatten()

for _i, _cat_feat in enumerate(cat_features):
    value_counts = heart_df[_cat_feat].value_counts()
    _axes[_i].bar(range(len(value_counts)), value_counts.values, color='steelblue')
    _axes[_i].set_xticks(range(len(value_counts)))
    _axes[_i].set_xticklabels(value_counts.index, rotation=45, ha='right')
    _axes[_i].set_title(f'{_cat_feat} Distribution')
    _axes[_i].set_ylabel('Count')
    _axes[_i].grid(axis='y', alpha=0.3)

# Hide unused subplot
_axes[-1].axis('off')

plt.tight_layout()
plt.show()

print(f'Created distribution plots for {len(cat_features)} categorical features')