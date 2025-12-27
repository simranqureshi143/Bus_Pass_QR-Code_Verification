# QR Code Based Bus Pass Verification System

## Overview
The **QR Code Based Bus Pass Verification System** is a web-based application designed to digitize traditional paper bus passes.  
It generates a **digital QR code bus pass** for passengers and allows conductors to **verify pass validity** through QR scanning using a browser.

This project demonstrates the practical use of **QR technology, web development, and backend validation** for public transportation systems.

---

## Problem Statement
Traditional paper-based bus pass systems suffer from:
- Manual verification delays
- Risk of pass duplication or misuse
- Wear and tear of physical passes
- Inefficient passenger verification

This project addresses these issues by introducing a **secure and fast digital verification mechanism**.

---

## Solution
The system generates a **unique QR code** for each bus pass and verifies it in real time using a backend service.

- Passengers display the QR code on their mobile device
- Conductors scan the QR code using a web-based scanner
- The system validates the pass and displays the result

---

## System Architecture
Passenger (Mobile Browser)
↓
QR Code Display
↓
Conductor (Browser Camera Scan)
↓
Flask Backend
↓
Validation Result (Valid / Invalid)

yaml
Copy code

---

## Features
- Digital QR-based bus pass
- Web-based implementation (no mobile app required)
- Works on local network (Laptop + Phone)
- Fast and contactless verification
- Simple and extensible architecture

---

## Technologies Used
- **Python 3**
- **Flask (Web Framework)**
- **qrcode library**
- **Pillow (Image Processing)**
- **HTML (Optional UI layer)**

---

## Project Structure
bus_pass/
│
├── app.py
├── qr/
│ └── pass.png
└── README.md

yaml
Copy code

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Install Dependencies
```bash
pip install flask qrcode pillow
Running the Application
bash
Copy code
python app.py
Expected output:

nginx
Copy code
Running on http://127.0.0.1:5000
Running on http://<LOCAL_IP>:5000
Usage
Passenger (QR Code Display)
Laptop:

arduino
Copy code
http://127.0.0.1:5000/pass
Mobile (same Wi-Fi network):

arduino
Copy code
http://<LOCAL_IP>:5000/pass
Conductor (Scanner)
Open scanner page (if enabled)

Allow camera permission

Scan passenger QR code

Use Cases
Public transportation systems

Smart city initiatives

Academic mini projects

Final year engineering projects

Learning Flask & QR integration

Future Enhancements
User authentication (Login / Registration)

Database integration (MySQL / SQLite)

Pass expiry and renewal system

Admin approval dashboard

Scan history and logs

Cloud deployment

Academic Relevance
This project demonstrates concepts from:

Web Technologies

Computer Networks

Software Engineering

Database Management Systems

Real-world system design

Viva / Interview Explanation
“This project implements a QR code–based digital bus pass system where passengers display a QR code on their mobile device, and conductors verify the pass using a web-based scanner connected to a backend validation system.”

Author
Simran Qureshi
