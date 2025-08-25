import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  # fix for macOS

from transformers import pipeline
from PIL import Image

model_name = "google/vit-base-patch16-224"

pipe = pipeline("image-classification", model=model_name, framework="pt")

def predict(image: Image.Image):
    return pipe(image)