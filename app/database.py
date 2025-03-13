from sqlalchemy import create_engine, Column, Integer, String, Float, TIMESTAMP
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# Database connection URL (Ensure password is URL-encoded if it contains special characters)
DATABASE_URL = "postgresql://postgres:Postgres%4020@localhost:5432/energy_db"

#  Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

#  Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  Base class for ORM models
Base = declarative_base()

#  Define EnergyData ORM Model
class EnergyData(Base):
    __tablename__ = "energy_data"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    location = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    temperature = Column(Float)
    wind_speed = Column(Float)

#  Create the database tables (Only runs if executed directly)
if __name__ == "__main__":
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully!")
    except Exception as e:
        print("Error creating tables:", e)
