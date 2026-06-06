from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
import json
import joblib
import numpy as np
import os

app = FastAPI()

# Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Model load (քո existing model)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "fraud_model.pkl")
model = joblib.load(model_path)

# Request schema
class Bet(BaseModel):
    bet_amount: float
    time_between_bets: float
    odds: float


# Web → Kafka
@app.post("/send")
def send(bet: Bet):

    data = {
        "bet_amount": bet.bet_amount,
        "time_between_bets": bet.time_between_bets,
        "odds": bet.odds
    }

    producer.send("transactions-topic", data)

    return {"status": "sent to kafka", "data": data}


# Direct prediction (optional test)
@app.post("/predict")
def predict(bet: Bet):

    data = np.array([[bet.bet_amount, bet.time_between_bets, bet.odds]])

    prediction = model.predict(data)[0]
    prob = model.predict_proba(data)[0][1]

    return {
        "fraud": int(prediction),
        "probability": float(prob)
    }