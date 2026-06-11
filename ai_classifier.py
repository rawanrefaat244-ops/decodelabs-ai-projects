# 1. Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report


# 2. Load  the Iris dataset
iris = load_iris()
X = iris.data       # Features: Sepal & Petal measurements
y = iris.target     # Labels: Setosa, Versicolor, Virginica
feature_names = iris.feature_names
target_names = iris.target_names

# 3. Explore dataset (optional)
print("Features:", feature_names)
print("Target names:", target_names)
print("First 5 samples:\n", X[:5])
print("first 5 labels:", y[:5])

# 4. Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. Split into training and test sets (80% / 20%)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, shuffle=True
)

# 6. Train the KNN classifier
k = 5  
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)

# 7. Make predictions on the test set
y_pred = model.predict(X_test)

# 8. Evaluate the model
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))