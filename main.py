from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import requests
from database import SessionLocal, EnergyData


app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Fetch energy data and store it in PostgreSQL
@app.get("/fetch-energy")
def fetch_energy(db: Session = Depends(get_db)):
    API_URL = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 51.5074,
        "longitude": -0.1278,
        "current": "temperature_2m,wind_speed_10m"
    }

@app.get("/energy-data")
def get_energy_data(db: Session = Depends(get_db)):
    data = db.query(EnergyData).all()
    return {"stored_energy_data": data}


    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()["current"]
        new_entry = EnergyData(
            location="London",
            latitude=51.5074,
            longitude=-0.1278,
            temperature=data["temperature_2m"],
            wind_speed=data["wind_speed_10m"]
        )
        
        db.add(new_entry)
        db.commit()
        
        return {"message": "Energy data saved", "data": data}
    
    return {"error": "Failed to fetch energy data"}

