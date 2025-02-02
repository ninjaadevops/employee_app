# Configuration (S3 details, DB)

import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")  
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///employees.db")  

    # AWS S3 Configuration
    S3_BUCKET = os.getenv("S3_BUCKET")
    S3_REGION = os.getenv("S3_REGION", "us-east-1")