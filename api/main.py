from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
from fastapi import UploadFile, File
import boto3
import uuid

s3 = boto3.client("s3")

BUCKET_NAME = "nunebucketf"

app = FastAPI(title="Bet Fraud Detection API")


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "fraud_model.pkl")

model = joblib.load(model_path)
class Bet(BaseModel):
    bet_amount: float
    time_between_bets: float
    odds: float


@app.get("/")
def root():
    return {"message": "Bet Fraud Detection API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(bet: Bet):
    data = np.array([[
        bet.bet_amount,
        bet.time_between_bets,
        bet.odds
    ]])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return {
        "fraud": int(prediction),
        "fraud_probability": float(probability)
    }
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_key = f"uploads/{uuid.uuid4()}_{file.filename}"

    s3.upload_fileobj(
        file.file,
        BUCKET_NAME,
        file_key
    )

    return {
        "message": "uploaded successfully",
        "file_key": file_key
    }
