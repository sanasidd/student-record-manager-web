from flask import Flask, render_template, request, redirect, flash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'any-secret-key'

# MongoDB setup
client = MongoClient("mongodb+srv://studentadmin:student123@@cluster0.2t1m6sj.mongodb.net/?retryWrites=true&w=majority")

db = client["school"]
students = db["students"]


@app.route('/')
def index():
    all_students = list(students.find())
    return render_template("index.html", students=all_students)

@app.route('/add', methods=['POST'])
def add():
    student = {
        "roll_no": request.form['roll_no'],
        "name": request.form['name'],
        "class": request.form['class'],
        "age": int(request.form['age']),
        "gender": request.form['gender'],
        "address": request.form['address'],
        "phone": request.form['phone']
    }
    students.insert_one(student)
    flash("Student added successfully!")
    return redirect('/')

@app.route('/delete/<roll_no>')
def delete(roll_no):
    students.delete_one({"roll_no": roll_no})
    flash("Student deleted.")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
