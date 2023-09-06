import numpy as np
import pandas as pd
import os 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

# Classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

#Ensemble method
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
import joblib

from utils import load_config

class Training:
    
    def load_data(self,data_path):
        
        df = pd.read_csv(data_path)
        print("loaded data sucessfully")
        print("Number of records", df.shape)
        df.rename(columns={'Personal Loan': 'Personal_Loan'}, inplace=True)
        return df
    
    def split_data(self,df):
        Y = df['Personal_Loan']
        X = df.drop(['ID', 'ZIP Code', 'Personal_Loan'], axis=1)

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=5)
        
        return X_train, X_test, Y_train, Y_test
    
    def save_model(self,model,output_path):
        
        joblib.dump(model, output_path)
        
    def save_features(self,final_columns, feature_path):
        joblib.dump(final_columns, feature_path)
        
        
    def train(self,data_path,model_weight_path,feature_path):
        
        data = self.load_data(data_path)
        
        X_train, X_test, Y_train, Y_test = self.split_data(data)
        
        rf_clf = RandomForestClassifier(criterion = 'gini', n_estimators=60)
        rf_clf = rf_clf.fit(X_train, Y_train)
        accuracy = rf_clf.score(X_test, Y_test)
        Y_predicted  = rf_clf.predict(X_test)
        print('\nRandom Forest Model accuracy = ', accuracy)
        print('\nTest labels, Predicted labels')
        
        self.save_model(rf_clf, model_weight_path)
        
        final_columns = np.array(X_train.columns) 
        self.save_features(final_columns, feature_path)

        
if __name__ == "__main__":
    print("Start Model training on input data")
    config = load_config()
    data_path = config['train_data_path']
    model_weight_path = config['model_weight_path']
    feature_path = config['feature_path']
    train_obj = Training()
    train_obj.train(data_path,model_weight_path,feature_path)
    
    