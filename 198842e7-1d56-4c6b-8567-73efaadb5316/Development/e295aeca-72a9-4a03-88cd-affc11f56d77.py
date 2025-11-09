import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Select only numerical features for correlation analysis
numerical_cols = heart_df.select_dtypes(include=['int64', 'float64']).columns
correlation_data = heart_df[numerical_cols]

# Calculate correlation matrix
corr_matrix = correlation_data.corr()

# Create heatmap with annotations
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, 
            annot=True, 
            fmt='.2f', 
            cmap='coolwarm', 
            center=0,
            square=True,
            linewidths=0.5,
            cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix Heatmap - Heart Disease Features', fontsize=14, pad=20)
plt.tight_layout()
plt.show()

print(f'Correlation matrix calculated for {len(numerical_cols)} numerical features')
print(f'Features analyzed: {", ".join(numerical_cols)}')