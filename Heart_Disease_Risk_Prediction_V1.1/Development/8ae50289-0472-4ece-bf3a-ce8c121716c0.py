import pandas as pd

# Handle missing values (there are no missing values in this dataset)
preprocessed_df = heart_df.copy()

print(f'Data shape after handling missing values: {preprocessed_df.shape}')
print(f'Missing values check: {preprocessed_df.isnull().sum().sum()}')