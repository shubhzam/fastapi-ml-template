import joblib
import numpy as np
from typing import List

saved_model = joblib.load('model.joblib')
print("model loaded")

def make_predictions(data: dict)->float:
    features = np.array([
        [
            data['longitude'],
            data['latitude'],
            data['housing_median_age'],
            data['total_rooms'],
            data['total_bedrooms'],
            data['populations'],
            data['households'],
            data['median_income']
        ]
    ])
    return saved_model.predict(features)[0]

def make_batch_predictions(data: List[dict]) -> np.array:
    X = np.array([
        [
            x['longitude'],
            x['latitude'],
            x['housing_median_age'],
            x['total_rooms'],
            x['total_bedrooms'],
            x['populations'],
            x['households'],
            x['median_income']
        ]
        for x in data
    ])
    return saved_model.predict(X)