from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import joblib
import os

from agents import (
    leakage_detector,
    optimizer_agent,
    finance_agent
)

app = FastAPI(
    title="FulfillSense AI",
    description="Margin Leakage Detection API",
    version="1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates")
)

# Load trained model
model = joblib.load("cts_model.pkl")


@app.get("/")
def home():
    return {
        "message": "FulfillSense AI Running"
    }

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )

@app.post("/analyze")
def analyze(order: dict):

    df = pd.DataFrame([order])

    predicted_cts = model.predict(df)[0]

    order["cost_to_serve"] = float(predicted_cts)

    risk = leakage_detector(order)

    recommendation = optimizer_agent(order)

    finance = finance_agent(order)

    return {
        "predicted_cost_to_serve": round(
            float(predicted_cts), 2
        ),
        "risk": risk,
        "recommendation": recommendation,
        "finance": finance
    }