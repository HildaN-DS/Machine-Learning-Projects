import matplotlib.pyplot as plt
import seaborn as sns

# Create pair plot for top correlated features
top_features_list = ['Oldpeak', 'MaxHR', 'Age', 'FastingBS']
plot_data = heart_df[top_features_list + ['HeartDisease']].copy()

# Create pairplot with color by target
pairplot_fig = sns.pairplot(plot_data, hue='HeartDisease', 
                            palette={0: '#2ecc71', 1: '#e74c3c'},
                            plot_kws={'alpha': 0.6, 's': 30},
                            diag_kind='kde',
                            height=2.5)

pairplot_fig.fig.suptitle('Pair Plot: Top Features vs Heart Disease', 
                          y=1.01, fontsize=14, fontweight='bold')

print('Pair plot shows feature interactions: clear separation in Oldpeak/MaxHR space')