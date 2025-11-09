import pandas as pd
from sklearn.preprocessing import StandardScaler

# Separate features and target
X_unscaled = encoded_df.drop('HeartDisease', axis=1)
y_target = encoded_df['HeartDisease']

# Apply standard scaling to all features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_unscaled)

# Convert back to DataFrame to maintain column names
X_scaled_df = pd.DataFrame(X_scaled, columns=X_unscaled.columns)

print(f'Feature matrix shape: {X_scaled_df.shape}')
print(f'Target variable shape: {y_target.shape}')
print(f'Target distribution: {y_target.value_counts().to_dict()}')