# qr-attendance-system-Python-
QR Code Based Attendance Management System using Flask &amp; MySQL
PROJECT TITLE
-------------
QR Code Based Attendance Management System
(Web Version – A.N College Portal)


PROJECT DESCRIPTION
-------------------
This project is a web-based attendance management system developed using
Python, Flask, and MySQL.

Each student has a unique Student ID (linked to a QR code in the offline system).
Students and administrators can log in through a web browser to view attendance
and student information in a professional college-style portal.

The system is designed for colleges and educational institutions to manage
student data securely and efficiently.


FEATURES
--------
Admin Panel:
- Secure Admin Login
- View all students details
- Professional Admin Dashboard
- College branding (A.N College name & logo)

Student Panel:
- Student Login using Student ID
- View personal profile (ID, Name, Roll No, Class, Session, Email)
- Clean and professional Student Dashboard

General:
- Web-based system (runs on Chrome / any browser)
- Flask backend with MySQL database
- Responsive and clean UI design
- Ready for future upgrades (attendance %, reports, QR scan integration)


TECHNOLOGIES USED
-----------------
Frontend:
- HTML
- CSS

Backend:
- Python
- Flask

Database:
- MySQL

Tools & Libraries:
- mysql-connector-python
- Flask framework


PROJECT FOLDER STRUCTURE
------------------------
QR_Attendance_Web/
│
├── app.py                 # Main Flask application
├── database.py            # Database connection file
│
├── templates/             # HTML templates
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   └── student_dashboard.html
│
├── static/
│   └── img/
│       └── an_college_logo.png
│
└── README.md / README.txt


DATABASE STRUCTURE
------------------

Database Name:
attendance_system

Table: students
- id (INT, Primary Key)
- student_id (VARCHAR)
- name (VARCHAR)
- roll_no (VARCHAR)
- class (VARCHAR)
- session (VARCHAR)
- email (VARCHAR)


HOW TO RUN THE PROJECT
---------------------

1. Install Python (3.x)
2. Install MySQL Server
3. Create database:
   CREATE DATABASE attendance_system;

4. Create students table in MySQL
5. Install required libraries:
   pip install flask mysql-connector-python

6. Run the Flask app:
   python app.py

7. Open browser and visit:
   http://127.0.0.1:5000


LOGIN DETAILS (Demo)
-------------------
Admin Login:
- Username: admin
- Password: admin123

Student Login:
- Use registered Student ID


FUTURE ENHANCEMENTS
-------------------
- QR Code scanning via web camera
- Attendance percentage calculation
- Monthly attendance report
- Export attendance to Excel/PDF
- Role-based authentication
- Cloud deployment


DEVELOPER DETAILS
-----------------
Name: Keshav Kumar Sinha
Course: B.Sc. IT
Project Type: Academic & Resume Project


INTERVIEW DESCRIPTION (SHORT)
-----------------------------
This project demonstrates a Flask-based web portal for managing student
attendance and profiles with MySQL integration and a professional UI.
