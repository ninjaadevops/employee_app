# Run script

# Set up AWS Credentials:
export SECRET_KEY="your-secure-random-key"
export DATABASE_URL="postgresql://username:password@hostname:port/dbname"
export S3_BUCKET="your-s3-bucket-name"
export S3_REGION="us-east-1"

# Run the Flask App:
python app.py