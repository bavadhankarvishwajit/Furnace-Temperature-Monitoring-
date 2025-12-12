from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import pyodbc
from passlib.context import CryptContext
from typing import Optional, List

app = FastAPI(title="ESP32 Sensor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_CONN = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=AdminDB;"
    "Trusted_Connection=yes;"
)

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# -------------------- Models --------------------
class SensorReading(BaseModel):
    temperature: str = Field(..., alias="temperature")

class LoginRequest(BaseModel):
    username: str
    password: str

# -------------------- Helpers --------------------
def verify_api_key(raw_key: str) -> bool:
    conn = pyodbc.connect(DB_CONN)
    try:
        cur = conn.cursor()
        cur.execute("SELECT KeyHash FROM ApiKeys WHERE IsEnabled=1")
        rows = cur.fetchall()
        hashes = [r[0] for r in rows]
    finally:
        cur.close()
        conn.close()

    for h in hashes:
        try:
            if pwd_context.verify(raw_key, h):
                return True
        except Exception:
            continue
    return False

# -------------------- POST endpoint --------------------
@app.post("/api/readings")
def create_reading(reading: SensorReading, x_api_key: str = Header(...)):
    if not verify_api_key(x_api_key):
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Convert temperature to float for optional status check
    try:
        temp_val = float(reading.temperature)
    except ValueError:
        raise HTTPException(status_code=400, detail="Temperature must be a number")

    # Insert into DB
    conn = pyodbc.connect(DB_CONN)
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO SensorReadings4 (Temperature) VALUES (?)",
            reading.temperature
        )
        conn.commit()
    finally:
        cur.close()
        conn.close()

    return {"message": "Reading recorded", "temperature": temp_val}

# -------------------- GET latest reading --------------------
@app.get("/api/readings/latest")
def get_latest_reading():
    conn = pyodbc.connect(DB_CONN)
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT TOP 1 Temperature, DateTime FROM SensorReadings4 ORDER BY DateTime DESC"
        )
        row = cur.fetchone()
    finally:
        cur.close()
        conn.close()

    if not row:
        return {"message": "No data"}

    return {
        "temperature": str(row[0]),
        "datetime": str(row[1])
    }

# -------------------- GET last N readings --------------------
@app.get("/api/readings")
def get_readings(limit: int = Query(20, ge=1, le=200)):
    conn = pyodbc.connect(DB_CONN)
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT Temperature, DateTime FROM SensorReadings4 ORDER BY DateTime DESC"
        )
        rows = cur.fetchall()
    finally:
        cur.close()
        conn.close()

    result = []
    for r in rows[:limit]:
        result.append({
            "temperature": str(r[0]),
            "datetime": str(r[1])
        })
    return result

# -------------------- Login --------------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

@app.post("/login")
def login(request: LoginRequest):
    if request.username == ADMIN_USERNAME and request.password == ADMIN_PASSWORD:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
