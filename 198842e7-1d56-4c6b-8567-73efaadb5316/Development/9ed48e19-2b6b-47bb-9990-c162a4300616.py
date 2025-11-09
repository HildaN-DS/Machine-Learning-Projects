from sklearn.linear_model import LogisticRegression
import numpy as np

# Train Logistic Regression model
lr_model = LogisticRegression(random_state=42, max_iter=1000)
lr_model.fit(X_train, y_train)

# Make predictions
lr_train_pred = lr_model.predict(X_train)
lr_test_pred = lr_model.predict(X_test)

# Get prediction probabilities
lr_train_proba = lr_model.predict_proba(X_train)[:, 1]
lr_test_proba = lr_model.predict_proba(X_test)[:, 1]

print('✓ Logistic Regression model trained')
print(f'  Training samples: {X_train.shape[0]}')
print(f'  Test samples: {X_test.shape[0]}')
print(f'  Features: {X_train.shape[1]}')