
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

print("Loading California Housing dataset...")

data = fetch_california_housing()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training model...")

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")

print("Model saved successfully!")
print("Model R2 score:", model.score(X_test, y_test))
