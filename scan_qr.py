import cv2
from datetime import date
from database import connect_db

db = connect_db()
cursor = db.cursor()

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    _, frame = cap.read()
    data, _, _ = detector.detectAndDecode(frame)

    if data:
        today = date.today()
        cursor.execute("SELECT * FROM students WHERE student_id=%s", (data,))
        student = cursor.fetchone()

        if student:
            cursor.execute("INSERT INTO attendance (student_id,date,status) VALUES (%s,%s,%s)",
                           (data,today,"Present"))
            db.commit()

            print("Attendance Marked ✅")
            print("Student Details:")
            print(student)

        break

    cv2.imshow("Scan QR", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
