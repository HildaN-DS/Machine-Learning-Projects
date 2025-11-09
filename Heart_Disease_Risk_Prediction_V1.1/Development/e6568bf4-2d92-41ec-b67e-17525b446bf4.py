import pandas as pd

# Get basic statistics for numeric features
numeric_cols = heart_df.select_dtypes(include=['int64', 'float64']).columns
numeric_stats = heart_df[numeric_cols].describe()

print('Numeric Features Summary Statistics:')
print(numeric_stats.round(2))