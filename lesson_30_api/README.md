# Image Classification API

This project is a simple REST API for image classification using the Hugging Face model **google/vit-base-patch16-224**.  
The service is implemented with **FastAPI** and deployed locally using **Uvicorn**.

## Overview
- **Task**: Deploy a simple computer vision model as a REST API using FastAPI.
- **Model**: [`google/vit-base-patch16-224`](https://huggingface.co/google/vit-base-patch16-224)
- **Frameworks**: HuggingFace Transformers, FastAPI, Uvicorn, PyTorch

## Deployment Info
Start the API server with:

uvicorn api:app --reload --port 8030

	•	api:app -> points to app = FastAPI() inside api.py
	•	--reload -> auto-reload on code changes
	•	--port 8030 -> runs the service on http://127.0.0.1:8030

Once launched, you can open:
	•	Swagger UI: http://127.0.0.1:8030/docs

## Create and activate environment
conda create -n tf-m1 python=3.9 -y
conda activate tf-m1

# Install requirements
pip install -r requirements.txt

Dependencies in requirements.txt:

- fastapi
- uvicorn
- transformers
- torch
- torchvision
- pillow
- python-multipart

## API Endpoints:

### 1. Health Check  
**GET** `/health`  
- **Description**: Verifies that the service is running.  
- **Response**: 
```bash
{"status": "ok"}
```

### 2.  Model Info 
**GET** `/info`  
- **Description**: Returns metadata about the model.  
- **Response**: 
```bash
{
  "model": "google/vit-base-patch16-224",
  "task": "image classification",
  "framework": "HuggingFace Transformers + FastAPI"
}
```

### 3. Prediction

- **POST /predict**
- **Description:** Accepts an uploaded image and returns predicted classes with confidence scores.
- **Request:**
	- Content type: multipart/form-data
	- Parameter: file → image file (.jpg, .png, etc.)

- Response example:
```bash
{
  "predictions": [
    {"label": "airliner", "score": 0.8013},
    {"label": "wing", "score": 0.1693},
    {"label": "warplane, military plane", "score": 0.0201}
  ]
}
```

## Examples

### 1. Installing dependencies
Shows how to install all required dependencies from `requirements.txt`.  

![Install requirements](assets/install%20requirements.png)

### 2. Starting FastAPI server
The server is launched on `http://127.0.0.1:8030` using:  
`uvicorn api:app --reload --port 8030`  

![Starting FastAPI server](assets/Starting%20the%20FastAPI%20server.png)

### 3. Health check
A request to `GET /health` confirms that the service is running.  
Response: `{"status": "ok"}`  

![Health check](assets/Health%20check.png)

### 4. Model info
A request to `GET /info` returns metadata about the model.  

![Model info](assets/Model%20info.png)

### 5. Swagger UI
Auto-generated API documentation available at `/docs`. 

![Swagger UI](assets/Swagger%20UI.png)

### 6. Predictions
Examples of classification results for different images:

- **Airliner**  
  The model correctly classifies the airplane as airliner.  
  ![Airliner](assets/Airliner.png)  

- **Cat**  
  The image shows a cat, and the model returns the correct class. 
  ![Cat](assets/Cat.png)  

- **Food**  
  A sample with food, showing multi-class classification results.  
  ![Food](assets/Food.png)  

- **Gazelle**  
  A gazelle photo
  ![Gazelle](assets/Gazelle.png)  

- **Mountains with gazelle**  
  Natural landscape with a gazelle 
  ![Mountains with gazelle](assets/Mountains%20with%20gazelle.png)  
