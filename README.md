# Smart Campus Security System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Nano-green?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge&logo=opencv)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

AI-powered Smart Campus Security System using YOLOv8, OpenCV, and SQLite for real-time surveillance, intrusion detection, evidence capture, and event logging.

---

## Overview

The Smart Campus Security System is an intelligent surveillance solution designed for educational institutions and restricted environments. The system leverages computer vision and artificial intelligence to monitor live camera feeds, detect human presence, identify unauthorized access, and maintain security records.

Built using YOLOv8 Nano, OpenCV, and SQLite, the project provides an efficient and lightweight security platform capable of running on standard consumer hardware without requiring dedicated GPUs.

---

## Features

### Implemented Features

- Real-time video surveillance
- YOLOv8 Nano object detection
- Human detection and monitoring
- Restricted Room Mode
- Surveillance Mode
- Intrusion detection
- Automatic evidence capture
- SQLite-based event logging
- Alert triggering system
- USB webcam support
- Integrated webcam support
- Lightweight CPU-friendly deployment

---

## System Workflow

```text
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
```

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python |
| AI Framework | YOLOv8 Nano |
| Computer Vision | OpenCV |
| Database | SQLite |
| Version Control | Git |
| Repository Hosting | GitHub |

---

## Project Structure

```text
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
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/buildJOI/smart-campus-security.git
cd smart-campus-security
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install ultralytics opencv-python
```

---

## Running the Application

```bash
python app.py
```

---

## Controls

| Key | Function |
|------|----------|
| R | Toggle Restricted Mode |
| ESC | Exit Application |

---

## Evidence Capture

When an intrusion is detected while Restricted Mode is active, the system automatically:

1. Captures a screenshot
2. Stores the image in the evidence directory
3. Logs the event in the SQLite database
4. Triggers an alert notification

### Example

```text
evidence/
├── 20260625_113015.jpg
├── 20260625_113105.jpg
└── 20260625_113214.jpg
```

---

## Database Logging

Each security event stores:

```text
Timestamp
Object Type
Camera ID
Event Type
```

### Example Record

| Timestamp | Object | Camera |
|------------|------------|------------|
| 2026-06-25 11:30:15 | Person | CAM_1 |

---

## Potential Applications

- Educational Institutions
- Smart Campuses
- Research Laboratories
- Libraries
- Server Rooms
- Administrative Offices
- Restricted Access Areas
- Industrial Monitoring Environments

---

## Future Integrations

### Phase 2 – Analytics and Monitoring

- Real-time people counting
- Occupancy analytics
- Attendance monitoring
- Security dashboard
- Web-based monitoring portal

### Phase 3 – Advanced Recognition

- Face recognition
- Authorized personnel identification
- Visitor tracking
- Suspicious activity detection

### Phase 4 – Mobile Platform

- Mobile application
- Push notifications
- Remote monitoring

### Phase 5 – Cloud Infrastructure

- Cloud deployment
- Multi-camera management
- Centralized monitoring system
- AWS integration
- Microsoft Azure integration

### Phase 6 – Smart Notifications

- Voice alerts
- SMS notifications
- Email alerts
- WhatsApp notifications
- Emergency response integration

---

## Development Roadmap

- [x] YOLOv8 Integration
- [x] Live Camera Feed
- [x] Human Detection
- [x] Intrusion Detection
- [x] Evidence Capture
- [x] SQLite Logging
- [x] Restricted Mode
- [ ] Face Recognition
- [ ] Multi-Camera Support
- [ ] Web Dashboard
- [ ] Mobile Application
- [ ] Cloud Deployment

---

## Contributors

- Jithin Jeevan
- Godphine A C
- Karthika Mahesh

---

## License

This project is licensed under the MIT License.

---

## Repository Topics

```text
computer-vision
yolov8
opencv
python
security-system
surveillance
intrusion-detection
smart-campus
artificial-intelligence
sqlite
machine-learning
```

If you found this project useful, consider starring the repository.
