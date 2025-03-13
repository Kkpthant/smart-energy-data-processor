# 🌍 **Smart Energy Data Processor**

## **Overview**
The **Smart Energy Data Processor** is a FastAPI-powered application that fetches real-time energy-related data (such as temperature and wind speed) from the Open-Meteo API, processes it, and stores it in a PostgreSQL database. This project is designed to demonstrate **API integration, database management, and backend development** using Python frameworks.

---

## ✅ **Features**
- ✅ Fetches real-time energy data from Open-Meteo API  
- ✅ Stores energy data efficiently in a PostgreSQL database  
- ✅ Uses FastAPI to provide a robust REST API for data retrieval  
- ✅ Implements SQLAlchemy ORM for structured database interaction  
- ✅ Supports modular, scalable, and maintainable architecture  

---

## 🛠 **Technologies Used**
- **Python** (FastAPI, SQLAlchemy, Requests)  
- **PostgreSQL** (Data Storage)  
- **SQLAlchemy ORM** (Database Management)  
- **Uvicorn** (ASGI Server)  
- **Git & GitHub** (Version Control)  

---

## 🚀 **How to Run the Project**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/smart-energy-data-processor.git
cd smart-energy-data-processor

```
### **2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows

```
### **3️⃣ Install Dependencies
```bash
pip install -r requirements.txt

```
### **4️⃣ Set Up PostgreSQL Database
Ensure PostgreSQL is installed and running.
```bash
psql -U postgres -d energy_db
```
Then create the required table:
```sql
CREATE TABLE energy_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    location TEXT NOT NULL,
    latitude DECIMAL(9,6) NOT NULL,
    longitude DECIMAL(9,6) NOT NULL,
    temperature DECIMAL(5,2),
    wind_speed DECIMAL(5,2)
);

```
## **5️⃣ Run the Application
The FastAPI server will run at: http://127.0.0.1:8000
```bash
uvicorn main:app --reload

```
## **6️⃣ Test the API
http://127.0.0.1:8000/fetch-energy
✅ Expected Response:
```json
{
  "message": "Energy data saved",
  "data": {
    "temperature_2m": 15.2,
    "wind_speed_10m": 5.3
  }
}

```
🔜 Next Steps
This project is still in development, and the next steps will include:

- Deployment: Deploy the FastAPI application to AWS Elastic Beanstalk (or an alternative cloud provider).
- Frontend Dashboard: Build a frontend to visualize energy data trends.
- Authentication & Security: Implement user authentication and secure API endpoints.
- Docker & CI/CD: Dockerize the application and set up automated deployment pipelines.

⭐ Support & Collaboration
If you find this project interesting, feel free to star this repository ⭐ and reach out to me for collaboration!  



















