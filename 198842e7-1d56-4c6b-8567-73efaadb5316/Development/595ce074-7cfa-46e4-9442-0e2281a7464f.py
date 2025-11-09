import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Encode categorical variables
encoded_df = preprocessed_df.copy()

# Identify categorical columns (excluding target)
cat_features = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

# Use Label Encoding for binary categorical and one-hot encoding for multi-class
# Sex and ExerciseAngina are binary - use label encoding
le_sex = LabelEncoder()
encoded_df['Sex'] = le_sex.fit_transform(encoded_df['Sex'])

le_angina = LabelEncoder()
encoded_df['ExerciseAngina'] = le_angina.fit_transform(encoded_df['ExerciseAngina'])

# For multi-class categorical variables, use one-hot encoding
# ChestPainType, RestingECG, ST_Slope
encoded_df = pd.get_dummies(encoded_df, columns=['ChestPainType', 'RestingECG', 'ST_Slope'], drop_first=True)

print(f'Data shape after encoding: {encoded_df.shape}')
print(f'Encoded columns: {list(encoded_df.columns)}')