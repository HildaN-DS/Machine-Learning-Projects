import pandas as pd

# Analyze categorical features
categorical_cols = heart_df.select_dtypes(include=['object']).columns

print('Categorical Features:')
for _cat_col in categorical_cols:
    unique_vals = heart_df[_cat_col].value_counts()
    print(f'\n{_cat_col}:')
    for _val, _count in unique_vals.items():
        print(f'  {_val}: {_count}')