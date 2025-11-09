import pandas as pd
import matplotlib.pyplot as plt

# Get categorical features
cat_vars = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

# Create percentage bar charts showing disease rate by category
_fig, _axes = plt.subplots(2, 3, figsize=(16, 9))
_axes = _axes.flatten()

for _j, _cat_var in enumerate(cat_vars):
    # Calculate proportion of heart disease for each category
    prop_table = pd.crosstab(heart_df[_cat_var], heart_df['HeartDisease'], normalize='index') * 100
    
    # Create grouped bar chart
    prop_table.plot(kind='bar', ax=_axes[_j], color=['#2ecc71', '#e74c3c'], 
                    width=0.8, legend=False)
    _axes[_j].set_title(f'Heart Disease Rate by {_cat_var}')
    _axes[_j].set_xlabel(_cat_var)
    _axes[_j].set_ylabel('Percentage (%)')
    _axes[_j].tick_params(axis='x', rotation=45)
    _axes[_j].grid(axis='y', alpha=0.3)
    _axes[_j].set_ylim(0, 100)

# Add legend
_axes[4].legend(['No Disease', 'Has Disease'], title='Heart Disease', loc='upper right')

# Hide unused subplot
_axes[-1].axis('off')

plt.tight_layout()
plt.show()

print(f'Created proportion charts for {len(cat_vars)} categorical features')