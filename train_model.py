from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1) Дані
X, y = load_iris(return_X_y=True)

# 2) Трейн/тест
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)

# 3) Модель
clf = RandomForestClassifier(n_estimators=150, random_state=42)
clf.fit(Xtr, ytr)

# 4) Перевірка
acc = accuracy_score(yte, clf.predict(Xte))
print(f"Test accuracy: {acc:.3f}")

# 5) Збереження
joblib.dump(clf, "iris_model.pkl")
print("Saved iris_model.pkl")
