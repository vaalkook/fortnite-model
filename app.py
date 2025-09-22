from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib

app = FastAPI(title="Fortnite Playstyle Classification")

model = load(pathlib.Path("model/fortnite-style.joblib"))

class InputData(BaseModel):
    materials_gathered: int
    materials_used: int
    damage_to_structures: int
    damage_to_players: int

class OutputData(BaseModel):
    playstyle: str

@app.post("/predict", response_model=OutputData)
def predict(data: InputData):
    model_input = np.array([[
        data.materials_gathered,
        data.materials_used,
        data.damage_to_structures,
        data.damage_to_players
    ]])
    result = model.predict(model_input)[0]
    return {"playstyle": result}
