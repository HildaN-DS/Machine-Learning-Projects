import pandas as pd

# Check for missing values
missing_vals = heart_df.isnull().sum()
missing_pct = (missing_vals / len(heart_df) * 100).round(2)

print('Missing Values Analysis:')
for _col, _miss_count, _miss_pct in zip(heart_df.columns, missing_vals, missing_pct):
    if _miss_count > 0:
        print(f'{_col}: {_miss_count} ({_miss_pct}%)')

if missing_vals.sum() == 0:
    print('No missing values detected ✓')