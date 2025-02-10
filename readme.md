Employee Directory Application

<img width="802" alt="Screenshot 2025-02-09 at 8 13 06 PM" src="https://github.com/user-attachments/assets/b54346ab-77ee-4cee-940b-3d86b5223f3c" />


Steps To Host

STEP 1
Python 3.x installed

STEP 2
Install required dependencies:
pip install flask boto3 flask-sqlalchemy flask-wtf

STEP 3
AWS Credentials configured using aws configure

STEP 4
Create an S3 Bucket for storing photos

Commands

1. git clone https://github.com/ninjaadevops/employee_app.git
2. sudo apt-get update && sudo apt-get install -y git python3 
3. ls
4. cd employee_app
5. sudo apt install python3-pip
6. sudo apt install python3-flask
7. pip install Flask-SQLAlchemy --break-system-packages
8. pip list
9. export SECRET_KEY="YOUR-SECRET-KEY"
10. export S3_BUCKET='YOUR-S3-BUCKET'
11. export S3_REGION='YOUR-REGION'
12. source ~/.bashrc
13. python3 app.py

S3 Bucket Policy

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadAccess",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::Your-bucket-name/*"
        }
    ]
}

Watch My Youtube Video for Detailed Explaination. And Subscribe For More!!
