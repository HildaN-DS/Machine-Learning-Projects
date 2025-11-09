import matplotlib.pyplot as plt

# Scatter plot: Age vs Oldpeak colored by HeartDisease
age_oldpeak_fig, _ax = plt.subplots(figsize=(8, 6))

# Separate by target class
_no_disease_df = heart_df[heart_df['HeartDisease'] == 0]
_disease_df = heart_df[heart_df['HeartDisease'] == 1]

_ax.scatter(_no_disease_df['Age'], _no_disease_df['Oldpeak'], alpha=0.6, c='#2ecc71', label='No Disease', s=40)
_ax.scatter(_disease_df['Age'], _disease_df['Oldpeak'], alpha=0.6, c='#e74c3c', label='Heart Disease', s=40)

_ax.set_xlabel('Age (years)', fontsize=11)
_ax.set_ylabel('ST Depression (Oldpeak)', fontsize=11)
_ax.set_title('Age vs Oldpeak by Heart Disease Status', fontsize=12, fontweight='bold')
_ax.legend()
_ax.grid(True, alpha=0.3)

plt.tight_layout()
print('Age vs Oldpeak: Older patients with higher Oldpeak more likely to have disease')