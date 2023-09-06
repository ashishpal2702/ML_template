import numpy as np
import pandas as pd
import os 
import joblib

from utils import load_config

class Prediction:
    
    def load_data(self,data_path):
        
        df = pd.read_csv(data_path)
        print("loaded test data sucessfully")
        print("Number of test records", df.shape)
        return df
    
    def load_model(self,model_weight_path):
        
        model = joblib.load(model_weight_path)
        
        return model
        
    def load_features(self, feature_path):
        
        feature_columns = joblib.load(feature_path)
        
        return feature_columns
        
    def predict(self,data_path,model_weight_path,feature_path):
        
        data = self.load_data(data_path)
        
        model = self.load_model(model_weight_path)
        feature_columns= self.load_features(feature_path)
        test_data = data[feature_columns]
        y_prediction = model.predict(test_data)
        
        print(y_prediction)
        
    def live_predict(self,data,model_weight_path,feature_path):
        
        model = self.load_model(model_weight_path)
        feature_columns= self.load_features(feature_path)
        test_data = data[feature_columns]
        y_prediction = model.predict(test_data)
        
        print(y_prediction)
        
if __name__ == "__main__":
    print("Start Model Prediction on Test data")
    config = load_config()
    data_path = config['test_data_path']
    model_weight_path = config['model_weight_path']
    feature_path = config['feature_path']
    train_obj = Prediction()
    train_obj.predict(data_path,model_weight_path,feature_path)
    
    