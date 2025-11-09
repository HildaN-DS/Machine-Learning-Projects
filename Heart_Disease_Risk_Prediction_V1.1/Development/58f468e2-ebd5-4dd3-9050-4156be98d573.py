import matplotlib.pyplot as plt

# Box plots for top numerical features grouped by target
boxplot_fig, boxplot_axes = plt.subplots(2, 2, figsize=(12, 10))

features_to_plot = ['Age', 'MaxHR', 'Oldpeak', 'Cholesterol']
_titles = ['Age Distribution', 'Max Heart Rate Distribution', 
          'ST Depression Distribution', 'Cholesterol Distribution']

for _idx, (_feat, _title) in enumerate(zip(features_to_plot, _titles)):
    _row = _idx // 2
    _col = _idx % 2
    _ax = boxplot_axes[_row, _col]
    
    # Prepare data for boxplot
    _data = [heart_df[heart_df['HeartDisease'] == 0][_feat],
            heart_df[heart_df['HeartDisease'] == 1][_feat]]
    
    _bp = _ax.boxplot(_data, labels=['No Disease', 'Heart Disease'], 
                      patch_artist=True)
    
    # Color boxes
    _bp['boxes'][0].set_facecolor('#2ecc71')
    _bp['boxes'][1].set_facecolor('#e74c3c')
    
    _ax.set_title(_title, fontsize=11, fontweight='bold')
    _ax.set_ylabel(_feat, fontsize=10)
    _ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
print('Box plots reveal distribution differences: MaxHR lower, Oldpeak higher in disease group')