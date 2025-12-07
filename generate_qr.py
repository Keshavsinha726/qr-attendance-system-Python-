import qrcode
from database import connect_db

db = connect_db()
cursor = db.cursor()

student_id = input("Enter Student ID: ")
name = input("Enter Name: ")
roll = input("Enter Roll No: ")
class_name = input("Enter Class: ")
session = input("Enter Session: ")
email = input("Enter Email: ")

sql = """
INSERT INTO students
(student_id, name, roll_no, class, session, email)
VALUES (%s, %s, %s, %s, %s, %s)
"""

values = (student_id, name, roll, class_name, session, email)

cursor.execute(sql, values)
db.commit()

qr = qrcode.make(student_id)
qr.save(f"qrcodes/{student_id}.png")

print("✅ QR Code Generated Successfully")
