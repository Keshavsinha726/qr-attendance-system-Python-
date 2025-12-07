from database import connect_db

db = connect_db()
cursor = db.cursor()

student_id = input("Enter Student ID: ")

cursor.execute("SELECT COUNT(*) FROM attendance WHERE student_id=%s", (student_id,))
present_days = cursor.fetchone()[0]

total_days = 30   # assume

percentage = (present_days / total_days) * 100
print("Attendance Percentage:", round(percentage,2), "%")
