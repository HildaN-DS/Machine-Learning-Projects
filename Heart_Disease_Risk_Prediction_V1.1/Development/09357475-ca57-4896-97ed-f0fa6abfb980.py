import matplotlib.pyplot as plt

# Scatter plot: Age vs MaxHR colored by HeartDisease
age_maxhr_fig, _ax = plt.subplots(figsize=(8, 6))

# Separate by target class
no_disease = heart_df[heart_df['HeartDisease'] == 0]
disease = heart_df[heart_df['HeartDisease'] == 1]

_ax.scatter(no_disease['Age'], no_disease['MaxHR'], alpha=0.6, c='#2ecc71', label='No Disease', s=40)
_ax.scatter(disease['Age'], disease['MaxHR'], alpha=0.6, c='#e74c3c', label='Heart Disease', s=40)

_ax.set_xlabel('Age (years)', fontsize=11)
_ax.set_ylabel('Maximum Heart Rate (bpm)', fontsize=11)
_ax.set_title('Age vs Max Heart Rate by Heart Disease Status', fontsize=12, fontweight='bold')
_ax.legend()
_ax.grid(True, alpha=0.3)

plt.tight_layout()
print('Age vs MaxHR: Heart disease patients tend to have lower max HR across ages')