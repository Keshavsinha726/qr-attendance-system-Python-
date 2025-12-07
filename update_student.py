from database import connect_db

db = connect_db()
cursor = db.cursor()

student_id = input("Enter Student ID to update: ")

print("\nWhat do you want to update?")
print("1. Name")
print("2. Roll No")
print("3. Class")
print("4. Session")
print("5. Mobile")
print("6. Email")

choice = input("Enter choice (1-6): ")
new_value = input("Enter new value: ")

fields = {
    "1": "name",
    "2": "roll_no",
    "3": "class",
    "4": "session",
    "5": "mobile",
    "6": "email"
}

if choice in fields:
    query = f"UPDATE students SET {fields[choice]}=%s WHERE student_id=%s"
    cursor.execute(query, (new_value, student_id))
    db.commit()
    print("✅ Data updated successfully")
else:
    print("❌ Invalid choice")
