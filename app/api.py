from fastapi import FastAPI
from src.utils import load_config
from src.prediction import Prediction
import pandas as pd

app = FastAPI()

@app.post("/predict/")
async def predict(data: dict):
    config = load_config()
    p = Prediction()
    model_weight_path = config['model_weight_path']
    feature_path = config['feature_path']
    
    # Convert input data to DataFrame
    features_df = pd.DataFrame.from_dict([data])
    
    # Preprocess inputs
    prediction = p.live_predict(features_df, model_weight_path, feature_path)
    
    if prediction == 1:
        return {"prediction": "Yes, the customer will Take Personal Loan."}
    else:
        return {"prediction": "No, the customer will not Take Personal Loan."}
