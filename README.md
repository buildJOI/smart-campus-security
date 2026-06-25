# Smart Campus Security System
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Nano-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?logo=opencv)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![GitHub last commit](https://img.shields.io/github/last-commit/buildJOI/smart-campus-security)
![GitHub repo size](https://img.shields.io/github/repo-size/buildJOI/smart-campus-security)

Overview
Smart Campus Security System is an AI-powered surveillance solution designed for educational institutions and restricted environments. The system utilizes YOLOv8 Nano and OpenCV to perform real-time object detection, monitor restricted areas, detect unauthorized access, capture evidence, and maintain security logs.

The project focuses on providing a lightweight and efficient security monitoring platform that can operate on standard consumer hardware without requiring dedicated GPUs.

Features
Implemented Features
Real-time video surveillance

YOLOv8 Nano object detection

Human detection and monitoring

Restricted Room Mode

Surveillance Mode

Intrusion detection

Automatic evidence capture

SQLite-based event logging

USB and integrated camera support

Alert triggering system

Lightweight CPU-friendly deployment

System Workflow
Camera Feed
     │
     ▼
YOLOv8 Detection
     │
     ▼
Person Detected
     │
     ▼
Restricted Mode Active?
     │
 ┌───┴───┐
 │       │
 No     Yes
 │       │
 ▼       ▼
Monitor  Generate Alert
             │
             ▼
      Capture Evidence
             │
             ▼
         Log Event
Technology Stack
Component	Technology
Programming Language	Python
AI Model	YOLOv8 Nano
Computer Vision	OpenCV
Database	SQLite
Version Control	Git
Repository Hosting	GitHub
Project Structure
smart-campus-security/
│
├── app.py
│
├── security/
│   ├── detector.py
│   ├── alerts.py
│   └── zones.py
│
├── database/
│   └── db.py
│
├── models/
│   └── yolov8n.pt
│
├── evidence/
│
├── campus.db
│
├── requirements.txt
│
└── README.md
Installation
Clone the Repository
git clone https://github.com/buildJOI/smart-campus-security.git
cd smart-campus-security
Create Virtual Environment
python -m venv .venv
Activate Environment
Windows

.venv\Scripts\activate
Linux / macOS

source .venv/bin/activate
Install Dependencies
pip install -r requirements.txt
or

pip install ultralytics opencv-python
Running the Application
python app.py
Controls
Key	Function
R	Toggle Restricted Mode
ESC	Exit Application
Evidence Capture
When an intrusion is detected while Restricted Mode is active, the system automatically:

Captures a screenshot

Stores the image in the evidence directory

Logs the event in SQLite

Triggers an alert

Example:

evidence/
├── 20260625_113015.jpg
├── 20260625_113105.jpg
└── 20260625_113214.jpg
Database Logging
Each event is stored with:

Timestamp
Object Type
Camera ID
Event Type
Example Record:

Timestamp	Object	Camera
2026-06-25 11:30:15	Person	CAM_1
Future Integrations
Phase 2
Real-time people counting

Occupancy analytics

Attendance monitoring

Security dashboard

Web-based monitoring portal

Phase 3
Face recognition

Authorized personnel identification

Visitor tracking

Suspicious activity detection

Phase 4
Mobile application

Push notifications

Remote monitoring

Phase 5
Cloud deployment

Multi-camera management

Centralized monitoring system

AWS integration

Microsoft Azure integration

Phase 6
Voice alerts

SMS notifications

Email alerts

WhatsApp notifications

Emergency response integration

Potential Applications
Educational institutions

Smart campuses

Research laboratories

Server rooms

Restricted access areas

Libraries

Administrative offices

Industrial monitoring environments

Development Roadmap
 YOLOv8 Integration

 Live Video Feed

 Human Detection

 Intrusion Detection

 SQLite Logging

 Evidence Capture

 Web Dashboard

 Face Recognition

 Multi-Camera Support

 Mobile Application

 Cloud Deployment

Contributors
Jithin Jeevan

Godphine A C

Karthika Mahesh

License
This project is licensed under the MIT License.
