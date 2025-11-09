from sklearn.model_selection import train_test_split

# Split data into training and test sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled_df, 
    y_target, 
    test_size=0.2, 
    random_state=42,
    stratify=y_target
)

print(f'Training set size: {X_train.shape[0]} samples ({X_train.shape[0]/len(X_scaled_df)*100:.1f}%)')
print(f'Test set size: {X_test.shape[0]} samples ({X_test.shape[0]/len(X_scaled_df)*100:.1f}%)')
print(f'Training features shape: {X_train.shape}')
print(f'Test features shape: {X_test.shape}')
print(f'Training target distribution: {y_train.value_counts().to_dict()}')
print(f'Test target distribution: {y_test.value_counts().to_dict()}')