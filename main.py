from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd


app = FastAPI()


class PatientsFeature(BaseModel):
    ID: int
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance: int

@app.get('/')
def home_page():
    return {'correct?': 'Right'}


forest_pipeline = joblib.load('models\Random Forest_pipeline.joblib')
encoder = joblib.load('models\encoder.joblib')

@app.post('/predict_random_forest')
def random_forest_predict(data: PatientsFeature):
    df = pd.DataFrame([data.model_dump()])
    print(df.shape)
    prediction = forest_pipeline.predict(df)
    
    
    probability = forest_pipeline.predict_proba(df)
    
    probabilities = probability.tolist()
    
    prediction = int(prediction[0])
    return {'prediction':prediction, 'probability':probability}






KNN_pipeline = joblib.load('models\K Nearest Neighbors_pipeline.joblib')
@app.post('/predict_K_Nearest_Neighbors')
def KNN_predict(data: PatientsFeature):
    df = pd.DataFrame([data.model_dump()])
        
    prediction = KNN_pipeline.predict(df)
    probability = KNN_pipeline.predict_proba(df)
    
    probabilities = probability.tolist()
    prediction = int(prediction[0])
    return {'prediction':prediction, 'probability':probability}


Logistic_pipeline = joblib.load('models\Logistic Regression_pipeline.joblib')
@app.post('/predict_Logistic_Regression')
def Logistic_predict(data: PatientsFeature):
    df = pd.DataFrame([data.model_dump()])
    
    prediction = Logistic_pipeline.predict(df)
    prediction = Logistic_pipeline.predict(df)
    probability = Logistic_pipeline.predict_proba(df)
    prediction = int(prediction[0])
    return {'prediction':prediction, 'probability':probability}


@app.get('/documents')
def documentation():
    return{'description': 'All documentation'}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug = True)