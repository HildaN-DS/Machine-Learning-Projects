import matplotlib.pyplot as plt

# Scatter plot: Oldpeak vs MaxHR colored by HeartDisease
oldpeak_maxhr_fig, _ax = plt.subplots(figsize=(8, 6))

# Separate by target class
_no_disease = heart_df[heart_df['HeartDisease'] == 0]
_disease = heart_df[heart_df['HeartDisease'] == 1]

_ax.scatter(_no_disease['Oldpeak'], _no_disease['MaxHR'], alpha=0.6, c='#2ecc71', label='No Disease', s=40)
_ax.scatter(_disease['Oldpeak'], _disease['MaxHR'], alpha=0.6, c='#e74c3c', label='Heart Disease', s=40)

_ax.set_xlabel('ST Depression (Oldpeak)', fontsize=11)
_ax.set_ylabel('Maximum Heart Rate (bpm)', fontsize=11)
_ax.set_title('Oldpeak vs Max Heart Rate by Heart Disease Status', fontsize=12, fontweight='bold')
_ax.legend()
_ax.grid(True, alpha=0.3)

plt.tight_layout()
print('Oldpeak vs MaxHR: Higher Oldpeak + Lower MaxHR associated with disease')