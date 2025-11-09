import matplotlib.pyplot as plt
import pandas as pd

# Create pie chart for target variable distribution
_fig, _ax = plt.subplots(figsize=(8, 6))

target_pie_counts = heart_df['HeartDisease'].value_counts().sort_index()
_labels = ['No Heart Disease (0)', 'Heart Disease (1)']
_colors = ['#2ecc71', '#e74c3c']
_explode = (0.05, 0.05)

_wedges, _texts, _autotexts = _ax.pie(target_pie_counts.values, 
                                       labels=_labels,
                                       colors=_colors, 
                                       autopct='%1.1f%%',
                                       startangle=90,
                                       explode=_explode,
                                       textprops={'fontsize': 11, 'weight': 'bold'})

# Make percentage text more visible
for _autotext in _autotexts:
    _autotext.set_color('white')
    _autotext.set_fontsize(12)

_ax.set_title('Target Variable Class Distribution - Pie Chart', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()

print(f'Pie chart visualization complete')