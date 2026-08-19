import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

X = np.array([
    [25, 40000],
    [35, 60000],
    [45, 80000],
    [20, 20000],
    [55, 120000],
    [60, 140000]
])

y = np.array([0, 0, 1, 0, 1, 1])

# Stratified split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# Scale features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# Prediction
y_pred = knn.predict(X_test)

print("Actual labels:   ", y_test)
print("Predicted labels: ", y_pred)

print(f"\nAccuracy Score: {accuracy_score(y_test, y_pred):.2f}")

print(
    "\nClassification Report:\n",
    classification_report(y_test, y_pred, zero_division=0)
)

