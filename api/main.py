from fastapi import FastAPI
from analysis.detect import detect_fraud

app = FastAPI()

@app.get("/check")

def check_bet(amount: float, time_between: float, odds: float):
    result = detect_fraud(amount, time_between, odds)
    
    if result == 1:
        return {"status": "Fraud detected"}
    else:
        return {"status": "Normal bet"}