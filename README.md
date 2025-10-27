<div align="center">

# 🌸 Gradio + FastAPI — Machine Learning Mini Project  
**별도 서버 (Separate Servers) Implementation**  
🎓 *Kyungbok University — Big Data Department*  
📅 *Autumn 2025 • AI Model Operations (MLOps)*  

</div>

---

## 📘 Overview  

This project demonstrates how to deploy a **Machine Learning Model** using  
👉 **FastAPI** (backend server) and 👉 **Gradio** (frontend user interface).  

It predicts the species of an *Iris flower* from 4 features (lengths & widths).  

---

## 🧩 Folder Structure

iris-fastapi-gradio/
│
├── train_model.py # Trains ML model & saves iris_model.pkl
├── api.py # FastAPI backend server (model API)
├── app_gradio.py # Gradio frontend (UI calling FastAPI)
├── iris_model.pkl # Saved trained model
└── requirements.txt # Dependencies

yaml
Copy code

---

## ⚙️ Setup & Installation

### 🪄 1. Create Virtual Environment
```bash
python -m venv .venv
. .\.venv\Scripts\Activate.ps1     # (Windows)
# or
source .venv/bin/activate          # (Mac/Linux)
🧰 2. Install Dependencies
bash
Copy code
pip install fastapi uvicorn gradio scikit-learn joblib pydantic requests
🧠 Model Training
Run this script to train the model and save it as iris_model.pkl:

bash
Copy code
python train_model.py
After running, you’ll see:

yaml
Copy code
Test accuracy: 0.97
Saved iris_model.pkl
🚀 Run the Project
🖥️ Step 1 — Start FastAPI (Backend)
bash
Copy code
uvicorn api:app --reload --port 8000
✅ Open:

API docs → http://127.0.0.1:8000/docs

Health check → http://127.0.0.1:8000/healthz

🎨 Step 2 — Start Gradio (Frontend)
In a new terminal:

bash
Copy code
python app_gradio.py
✅ Open:

Gradio UI → http://127.0.0.1:7860

You’ll see sliders like this 👇
Adjust values and click Submit to get prediction results.

yaml
Copy code
Prediction: setosa
Probabilities: setosa: 0.981, versicolor: 0.019, virginica: 0.000
🔗 API Endpoint Example
POST /predict/
Request:

json
Copy code
{
  "sl": 5.1,
  "sw": 3.5,
  "pl": 1.4,
  "pw": 0.2
}
Response:

json
Copy code
{
  "prediction": "setosa",
  "proba": {
    "setosa": 0.981,
    "versicolor": 0.019,
    "virginica": 0.000
  }
}
🧩 Explanation
File	Description
train_model.py	Trains RandomForestClassifier and saves model
api.py	Loads model, serves prediction API using FastAPI
app_gradio.py	Provides UI to send data and display model results
requirements.txt	Lists all Python dependencies

📸 Screenshots
FastAPI Docs	Gradio Interface

✅ Final Check
Component	Status	URL
FastAPI Server	🟢 Running	http://127.0.0.1:8000/docs
Gradio UI	🟢 Running	http://127.0.0.1:7860
Model	🟢 Ready	iris_model.pkl

<div align="center">
👩‍💻 Author
Yelyzaveta Aslanova
빅데이터과 • 경복대학교
(Big Data Department, Kyungbok University)

📚 Autumn 2025 • MLOps Mini Project
💡 “From model training to API and UI integration.”

</div> ``
