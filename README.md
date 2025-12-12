# 🔥 Furnace Temperature Monitoring Using Pyrometer

### *An IoT + FastAPI + SQL Server + Flutter Industrial Monitoring System*

![Status](https://img.shields.io/badge/Project-IoT%20Industrial-blueviolet)
![Language](https://img.shields.io/badge/ESP32-C++-orange)
![Backend](https://img.shields.io/badge/Backend-FastAPI-green)
![Frontend](https://img.shields.io/badge/Frontend-Flutter-blue)
![Database](https://img.shields.io/badge/Database-SQL%20Server-red)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Cross--Platform-lightgrey)

---

## 📌 Overview

This project provides a **real-time, non-contact furnace temperature monitoring system** using an **Industrial Infrared Pyrometer**, **ESP32**, **FastAPI backend**, **SQL Server database**, and a **Flutter-based desktop dashboard**.

It is developed for industries where manual temperature monitoring is:

❌ Unsafe
❌ Inaccurate
❌ Slow
❌ Prone to human error

This IoT system solves that by offering:

✔ Continuous monitoring
✔ Wireless data transmission
✔ Instant alerts
✔ Data logging
✔ Trend analysis
✔ Desktop visualization

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/769590f3-ec0a-41b7-b606-e61e8c85210f" />


---

## 🚀 Features

### 🔭 **Non-Contact Pyrometer Sensing**

* Measures high temperatures safely.
* Works in hazardous furnace environments.

### 🧠 **ESP32 Edge Processing**

* Reads & filters sensor data
* Checks safety thresholds
* Sends readings through Wi-Fi
* Activates buzzer when unsafe

### ⚡ **FastAPI Backend**

* High-speed ingestion endpoint
* Validates and stores data
* Handles alert classification

### 🗄 **SQL Server Time-Series Database**

Stores:

* Temperature
* Timestamp
* Status (Normal / Alert)
* Sensor ID

### 💻 **Flutter Desktop Dashboard**

* Live temperature display
* Smooth real-time graph
* Alert notifications
* Threshold customization
* Historical data view

### 🔔 **On-Site Safety Alarm**

Buzzer automatically rings when furnace temperature crosses limit.

---

## 🏗 System Architecture

```
Pyrometer → ESP32 → FastAPI → SQL Server → Flutter Dashboard
```

* Pyrometer senses high temperature
* ESP32 processes and sends reading to backend
* FastAPI stores into SQL Server
* Dashboard fetches & visualizes in real-time
* Alerts are shown both on hardware & software

---

## 📁 Repository Structure

```
/esp32-code/                 → Firmware for ESP32 (C++)
/backend-fastapi/            → FastAPI ingestion API
/database/                   → SQL scripts and schema
/flutter-desktop-app/        → Flutter UI project
/docs/                       → UML, report, screenshots
```

---

## 🔧 Hardware Requirements

| Component        | Specification         | Purpose                 |
| ---------------- | --------------------- | ----------------------- |
| **ESP32 DevKit** | Wi-Fi enabled         | Edge IoT node           |
| **Pyrometer**    | IR-based, non-contact | Temperature measurement |
| **Buzzer**       | 5V/3.3V compatible    | Overheat alarm          |
| **Power Supply** | Stable 5V DC          | ESP32 + Sensor          |
| **Host PC**      | i5 / 8GB RAM          | Backend + Database      |

---

## 💻 Software Requirements

| Software             | Purpose                 |
| -------------------- | ----------------------- |
| **Arduino IDE**      | ESP32 programming       |
| **Python 3.x**       | FastAPI backend         |
| **Flask**            | Query API for dashboard |
| **SQL Server 2019**  | Time-series database    |
| **Flutter SDK**      | Desktop UI              |
| **SQLAlchemy**       | DB ORM                  |
| **Requests Library** | API communication       |

---

## ⚙ Installation & Setup

### **1️⃣ Flash ESP32**

* Open Arduino IDE
* Install ESP32 board manager
* Upload the firmware from `/esp32-code/`
* Configure:

  * WiFi SSID
  * Password
  * API URL
  * Temperature threshold

---

### **2️⃣ Setup FastAPI Backend**

```
cd backend-fastapi
pip install -r requirements.txt
uvicorn main:app --reload
```

API will start on:

```
http://localhost:8000/ingest
```

---

### **3️⃣ Configure SQL Server**

* Create database
* Run schema file: `/database/schema.sql`

---

### **4️⃣ Run Flutter Dashboard**

```
cd flutter-desktop-app
flutter pub get
flutter run
```

---

## 🔌 API Endpoints

### **POST /ingest**

ESP32 → Server
Sends a temperature reading.

#### Payload:

```json
{
  "sensor_id": "FURNACE_01",
  "temperature": 764.22,
  "status": "NORMAL"
}
```

---

### **GET /history**

Dashboard → Server
Fetches all readings for graph display.

---

## 📊 Dashboard Screens

### ✔ Real-Time Monitoring

Live temperature, color indicators, alert popup.

### ✔ History Graph

Interactive chart showing the last 24 hours or full history.

### ✔ Alerts Section

Shows all limit-crossing events.

### ✔ Settings Page

Modify temperature threshold.

---

## ⭐ Testing & Validation

Successfully Data Transmission Through Esp32

![WhatsApp Image 2025-12-06 at 15 38 59_553c5d50](https://github.com/user-attachments/assets/3c06e1fa-3af9-4c2b-a8de-84f459b8826d)

Successfully Data Logging in Database

![WhatsApp Image 2025-12-06 at 16 41 11_ad9af2ad](https://github.com/user-attachments/assets/c775e6ab-245b-40e5-b4f4-7bfd8459ae7c)

---

## 🔮 Future Enhancements

* AI-based predictive maintenance
* Cloud dashboard (AWS/GCP/IoT Core)
* Multi-sensor deployment
* SMS/Email alert integration
* Full automation for furnace control

---

## 👨‍💻 Author

**Mr. Vishwajit Mahesh Bavadhankar**,
B.Tech CSE (IoT, Cybersecurity, Blockchain),
Annasaheb Dange College of Engineering & Technology, Ashta

**Ms. Gayatri Balaso Patil**,
B.Tech CSE,
Annasaheb Dange College of Engineering & Technology, Ashta

**Ms. Shivani Krishnath Patil**,
B.Tech CSE,
Annasaheb Dange College of Engineering & Technology, Ashta

---

## ⭐ Implementation

![WhatsApp Image 2025-12-06 at 16 40 35_bdc984a5](https://github.com/user-attachments/assets/0999b6e1-eab8-4157-80c9-60ed72938947)
