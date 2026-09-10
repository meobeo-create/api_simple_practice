from fastapi import FastAPI
from typing import Optional
app = FastAPI()
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="frontend"), name='static')


@app.get('/predict')
def predict_price (area:float, bedrooms:int, location: Optional[str] = ""):
    location=(location or "").lower
    total = 500 + 15*area + 50*bedrooms
    if location=='hanoi':
        total=total*1.3
    elif location=='hcmc':
        total = total*1.25
    else:
        total = total *1
    return f'Prediction price: {total:.2f}'

