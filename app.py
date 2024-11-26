from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd

# Define the FastAPI app
app = FastAPI()

# Load the trained model
with open("models/trained_model.pkl", "rb") as f:
    model = pickle.load(f)

# Preprocessing logic (same as during training)
numerical_cols = ["age", "trestbps", "chol", "thalach", "oldpeak"]
categorical_cols = ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal"]


# Input schema for requests
class PredictionRequest(BaseModel):
    features: dict  # Expecting a dictionary of column_name: value

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Heart Risk Prediction API. Visit /docs for API documentation."}

@app.post("/predict/")
async def predict(request: PredictionRequest):

    # Convert input dictionary to DataFrame
    input_data = pd.DataFrame([request.features])
    print("Received input:", input_data)

    # Drop the target column if it exists in the payload
    if "num" in input_data.columns:
        print("Dropping target column 'num' from input data.")
        input_data.drop(columns="num", inplace=True)

    # Ensure categorical columns have the correct dtype
    for col in categorical_cols:
        if col in input_data.columns:
            input_data[col] = input_data[col].astype("category")

    print("Preprocessed data:", input_data)

    print("Preprocessed input data:", input_data)

    # Make prediction
    try:
        prediction = model.predict(input_data)
        print("Model prediction:", prediction)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        print("Error during prediction:", str(e))
        raise HTTPException(
            status_code=500, detail="An error occurred during prediction."
        )


# To test the api endpoint run in the terminal:
# uvicorn app:app --host 0.0.0.0 --port 8000
# open http://127.0.0.1:8000/docs
# test the 'predict/' endpoint
# Click the "Try it out" button and paste the content of request.json

# Alternatively use the terminal
# curl -X POST "http://127.0.0.1:8000/predict/" \
# -H "Content-Type: application/json" \
# -d '{
#     "features": {
#         "age": 63,
#         "sex": 1,
#         "cp": 3,
#         "trestbps": 145,
#         "chol": 233,
#         "fbs": 1,
#         "restecg": 0,
#         "thalach": 150,
#         "exang": 0,
#         "oldpeak": 2.3,
#         "slope": 0,
#         "ca": 0,
#         "thal": 1
#     }
# }'
