from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
from fastapi import FastAPI, UploadFile, File
import base64
import json
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)



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

@app.post("/send")
def send(bet: Bet):
    data = {
        "bet_amount": bet.bet_amount,
        "time_between_bets": bet.time_between_bets,
        "odds": bet.odds
    }

    producer.send("transactions-topic", data)

    return {"status": "sent to kafka", "data": data}

@app.post("/send-to-stream")
def send_to_stream(bet: Bet):

    data = {
        "bet_amount": bet.bet_amount,
        "time_between_bets": bet.time_between_bets,
        "odds": bet.odds
    }

    producer.send("transactions-topic", data)

    return {"status": "sent to kafka"}


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

    content = await file.read()

    payload = {
        "filename": file.filename,
        "file": base64.b64encode(content).decode("utf-8")
    }

    response = lambda_client.invoke(
        FunctionName="upload-to-s3",
        InvocationType="RequestResponse",
        Payload=json.dumps(payload)
    )

    result = json.loads(
        response["Payload"].read()
    )

    return result
    
