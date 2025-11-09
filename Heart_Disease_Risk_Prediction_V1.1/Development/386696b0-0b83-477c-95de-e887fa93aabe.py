import pandas as pd
import numpy as np

# Calculate correlation matrix for numerical features
numeric_cols = heart_df.select_dtypes(include=['int64', 'float64']).columns
corr_matrix = heart_df[numeric_cols].corr()

# Get correlations with target variable
target_corrs = corr_matrix['HeartDisease'].abs().sort_values(ascending=False)
print('Top features correlated with HeartDisease:')
print(target_corrs.head(6))

# Get top feature pairs for pair plots (excluding target)
feature_cols = [col for col in numeric_cols if col != 'HeartDisease']
top_features = target_corrs.drop('HeartDisease').head(4).index.tolist()