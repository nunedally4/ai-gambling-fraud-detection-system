import joblib
import numpy as np

model = joblib.load("fraud_model.pkl")

def detect_fraud(amount, time_between, odds):
    data = np.array([[amount, time_between, odds]])
    prediction = model.predict(data)
    
    return prediction[0]