import pandas as pd
import matplotlib.pyplot as plt

# Get categorical features
categorical_features = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

# Create stacked bar charts showing relationship with target
_fig, _axes = plt.subplots(2, 3, figsize=(16, 9))
_axes = _axes.flatten()

for _idx, _cat_feature in enumerate(categorical_features):
    # Create crosstab for each categorical feature vs HeartDisease
    crosstab_data = pd.crosstab(heart_df[_cat_feature], heart_df['HeartDisease'])
    
    # Create stacked bar chart
    crosstab_data.plot(kind='bar', stacked=True, ax=_axes[_idx], 
                       color=['#2ecc71', '#e74c3c'], legend=False)
    _axes[_idx].set_title(f'{_cat_feature} vs Heart Disease')
    _axes[_idx].set_xlabel(_cat_feature)
    _axes[_idx].set_ylabel('Count')
    _axes[_idx].tick_params(axis='x', rotation=45)
    _axes[_idx].grid(axis='y', alpha=0.3)

# Add legend to last used subplot
_axes[4].legend(['No Disease', 'Has Disease'], title='Heart Disease', loc='upper right')

# Hide unused subplot
_axes[-1].axis('off')

plt.tight_layout()
plt.show()

print(f'Created stacked bar charts for {len(categorical_features)} features vs target')