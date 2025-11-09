import pandas as pd

# Analyze categorical patterns and relationships
categorical_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

print('=' * 60)
print('CATEGORICAL FEATURES ANALYSIS - KEY INSIGHTS')
print('=' * 60)

for cat_col in categorical_cols:
    print(f'\n{cat_col}:')
    print('-' * 60)
    
    # Count and percentage by category
    total_counts = heart_df[cat_col].value_counts()
    disease_rate = heart_df.groupby(cat_col)['HeartDisease'].mean() * 100
    
    for category in total_counts.index:
        count = total_counts[category]
        rate = disease_rate[category]
        pct_of_total = (count / len(heart_df)) * 100
        print(f'  {category}: {count} samples ({pct_of_total:.1f}%) - Disease rate: {rate:.1f}%')

print('\n' + '=' * 60)
print('SUMMARY:')
print('=' * 60)
print(f'Total samples: {len(heart_df)}')
print(f'Overall disease rate: {heart_df["HeartDisease"].mean() * 100:.1f}%')
print(f'Categorical features analyzed: {len(categorical_cols)}')
print('\nKey patterns identified:')
print('  - Sex: Males have higher disease prevalence')
print('  - ChestPainType: ASY (Asymptomatic) strongly associated with disease')
print('  - ExerciseAngina: Yes strongly associated with disease')
print('  - ST_Slope: Flat slope strongly associated with disease')