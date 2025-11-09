import pandas as pd

# Load the csv file
heart_df = pd.read_csv('heart_disease_prediction.csv')

print(f'Dataset loaded: {len(heart_df)} rows, {len(heart_df.columns)} columns')