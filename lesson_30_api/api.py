from fastapi import FastAPI, UploadFile, File
from model import predict, model_name
from PIL import Image
import io

app = FastAPI(title="Image Classification API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/info")
def model_info():
    return {
        "model": model_name,
        "task": "image classification",
        "framework": "HuggingFace Transformers + FastAPI"
    }

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    results = predict(image)
    return {"predictions": results}