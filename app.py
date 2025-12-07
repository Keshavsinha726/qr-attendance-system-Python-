from flask import Flask, render_template, request
from database import connect_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("admin_login.html")

# STUDENT LOGIN
@app.route("/student_login", methods=["POST"])
def student_login():
    student_id = request.form["student_id"]

    db = connect_db()
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM students WHERE student_id=%s", (student_id,))
    student = cur.fetchone()

    return render_template("student_dashboard.html", student=student)

# ADMIN LOGIN
@app.route("/admin_login", methods=["POST"])
def admin_login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "admin123":
        db = connect_db()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM students")
        students = cur.fetchall()
        return render_template("admin_dashboard.html", students=students)
    else:
        return "Invalid Admin Login"

if __name__ == "__main__":
    app.run(debug=True)
