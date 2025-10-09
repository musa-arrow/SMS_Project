import numpy as np
from fastapi import FastAPI,Request,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pickle
from starlette.staticfiles import StaticFiles
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = FastAPI()

app.mount("/static", StaticFiles(directory="."),name="static")

templates = Jinja2Templates(directory="templates")

model = load_model("sms.h5")

with open ("tokenizer.pkl","rb") as f:
    tokenizer = pickle.load(f)

class SMS(BaseModel):
    Message: str

class Prediction(BaseModel):
    label: int

@app.get("/",response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/predict")
async def predict(features: SMS):
    text = features.Message

    seq = tokenizer.texts_to_sequences([text])

    pad = pad_sequences(seq, maxlen=20)

    prediction = model.predict(pad)

    if prediction[0] > 0.5:
        prediction = 1
    else:
        prediction = 0

    return {"predicted": int(prediction)}

















