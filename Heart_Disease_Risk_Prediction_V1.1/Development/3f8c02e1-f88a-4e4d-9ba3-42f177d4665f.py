import matplotlib.pyplot as plt
import pandas as pd

# Create count plot for target variable
_fig, _ax = plt.subplots(figsize=(8, 6))

target_counts_viz = heart_df['HeartDisease'].value_counts().sort_index()
_bars = _ax.bar(['No Heart Disease', 'Heart Disease'], target_counts_viz.values, 
                color=['#2ecc71', '#e74c3c'], edgecolor='black', linewidth=1.5)

# Add value labels on bars
for _bar in _bars:
    _height = _bar.get_height()
    _ax.text(_bar.get_x() + _bar.get_width()/2., _height,
            f'{int(_height)}',
            ha='center', va='bottom', fontsize=12, fontweight='bold')

_ax.set_ylabel('Count', fontsize=12)
_ax.set_title('Target Variable Distribution - Count Plot', fontsize=14, fontweight='bold')
_ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

print(f'Count visualization complete')