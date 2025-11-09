from sklearn.ensemble import GradientBoostingClassifier

# Train Gradient Boosting model (sklearn alternative to XGBoost)
gb_model = GradientBoostingClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    random_state=42
)
gb_model.fit(X_train, y_train)

# Make predictions
gb_train_pred = gb_model.predict(X_train)
gb_test_pred = gb_model.predict(X_test)

# Get prediction probabilities
gb_train_proba = gb_model.predict_proba(X_train)[:, 1]
gb_test_proba = gb_model.predict_proba(X_test)[:, 1]

print('✓ Gradient Boosting model trained')
print(f'  n_estimators: {gb_model.n_estimators}')
print(f'  learning_rate: {gb_model.learning_rate}')
print(f'  max_depth: {gb_model.max_depth}')