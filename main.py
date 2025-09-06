from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_predictions, make_batch_predictions
from typing import List
app = FastAPI()

@app.get('/')
def index():
    return {'message':'welcome to home page'}

@app.post('/predict', response_model=OutputSchema)
def predict(user_input : InputSchema):
    prediction = make_predictions(user_input.model_dump()) #model dump for json op
    return OutputSchema(predicted_price=round(prediction,2))

@app.post('/batch_prediction', response_model=List[OutputSchema])
def batch_predict(user_input: List[InputSchema]):
    predictions = make_batch_predictions([x.model_dump() for x in user_input])
    return[OutputSchema(predicted_price=round(predictions,2)) for prediction in predictions]
