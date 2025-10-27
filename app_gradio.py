import gradio as gr
import requests

FASTAPI_URL = "http://127.0.0.1:8000/predict/"  # важливо: саме /predict/

def infer(sl, sw, pl, pw):
    try:
        payload = {"sl": sl, "sw": sw, "pl": pl, "pw": pw}
        r = requests.post(FASTAPI_URL, json=payload, timeout=10)
        r.raise_for_status()
        data = r.json()
        pred = data.get("prediction", "n/a")
        proba = data.get("proba", {})
        pretty = ", ".join([f"{k}: {v:.2f}" for k, v in proba.items()])
        return f"Prediction: {pred}\nProbabilities: {pretty}"
    except Exception as e:
        return f"Error: {e}"

demo = gr.Interface(
    fn=infer,
    inputs=[
        gr.Slider(4.0, 8.0, value=5.1, label="sepal length (sl)"),
        gr.Slider(2.0, 4.5, value=3.5, label="sepal width (sw)"),
        gr.Slider(1.0, 7.0, value=1.4, label="petal length (pl)"),
        gr.Slider(0.1, 2.5, value=0.2, label="petal width (pw)"),
    ],
    outputs="text",
    title="Iris species predictor (calls FastAPI)",
)

if __name__ == "__main__":
    # локальний UI на 127.0.0.1:7860
    demo.launch(server_port=7860)
