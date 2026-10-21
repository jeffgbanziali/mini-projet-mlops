import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("regression.joblib")

class HouseFeatures(BaseModel):
    size: float
    nb_rooms: int
    garden: int

@app.get("/predict")
def predict_default():
    return {"y_pred": 2}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    data = pd.DataFrame([{
        "size": features.size,
        "nb_rooms": features.nb_rooms,
        "garden": features.garden
    }])
    raw_prediction = float(model.predict(data)[0])
    rounded_value = round(raw_prediction, 2)
    formatted_value = f"{rounded_value:,.2f} ".replace(",", " ").replace(".", ",")
    
    return {
        "prediction": formatted_value,
        
    }