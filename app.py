# Flask app

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import boto3
import os
from werkzeug.utils import secure_filename
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# AWS S3 Setup
s3 = boto3.client("s3", region_name=Config.S3_REGION)

# Database Model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.String(200), nullable=True)

# Create DB
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    employees = Employee.query.all()
    return render_template("index.html", employees=employees)

@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        photo = request.files["photo"]

        if photo:
            filename = secure_filename(photo.filename)
            s3.upload_fileobj(photo, Config.S3_BUCKET, filename)
            photo_url = f"https://{Config.S3_BUCKET}.s3.{Config.S3_REGION}.amazonaws.com/{filename}"
        else:
            photo_url = None

        new_employee = Employee(name=name, email=email, department=department, photo_url=photo_url)
        db.session.add(new_employee)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("add_employee.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
