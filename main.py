from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd


app = FastAPI()


class PatientsFeature(BaseModel):
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance: object
    

@app.get('/')
def home_page():
    return {'correct?': 'Right'}


forest_pipeline = joblib.load('models\Random Forest_pipeline.joblib')
encoder = joblib.load('models\encoder.joblib')

@app.post('/predict_random_forest')
def random_forest_predict(data: PatientsFeature):
    df = pd.DataFrame([data.model_dump()])
    print(df.shape)
    df_encoded = encoder.transform(df)
    flattened_data = df_encoded.values.flatten()
    prediction = forest_pipeline.predict(flattened_data)
    
    prediction = int(prediction[0])
    return {'prediction':prediction}




KNN_pipeline = joblib.load('models\K Nearest Neighbors_pipeline.joblib')
@app.post('/predict_K_Nearest Neighbor')
def KNN_predict(data: PatientsFeature):
    df = pd.DataFrame([data.model_dump()])
    df_encoded = encoder.transform(df)
    flattened_data = df_encoded.values.flatten()
    prediction = KNN_pipeline.predict(flattened_data)
    prediction = int(prediction[0])
    return prediction



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug = True)