from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Iris API", version="1.0")

# Дозволяємо звертання з іншого порту (Gradio)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Завантажуємо модель
model = joblib.load("iris_model.pkl")
LABELS = ["setosa", "versicolor", "virginica"]

class IrisIn(BaseModel):
    sl: float  # sepal length
    sw: float  # sepal width
    pl: float  # petal length
    pw: float  # petal width

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/predict/")
def predict(x: IrisIn):
    feats = np.array([[x.sl, x.sw, x.pl, x.pw]])
    proba = model.predict_proba(feats)[0]          # ймовірності
    idx = int(np.argmax(proba))                    # індекс класу
    return {
        "prediction": LABELS[idx],
        "proba": {LABELS[i]: float(p) for i, p in enumerate(proba)}
    }
