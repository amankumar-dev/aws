import boto3
import json

# LocalStack ka S3 client connect karo
s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='mock_key',
    aws_secret_access_key='mock_secret',
    region_name='us-east-1'
)

# Ek dummy raw data jo hume pipeline me load karna hai
raw_data = {
    "role": "Data Engineer",
    "tools": ["Python", "Docker", "LocalStack", "PostgreSQL"],
    "status": "Learning Cloud Free Tier"
}

# Python dictionary ko string me badla
json_data = json.dumps(raw_data)

# Data ko local S3 bucket me upload kiya
s3_client.put_object(
    Bucket='my-first-bucket',
    Key='raw/profile.json',
    Body=json_data
)

print("🎉 Mubarak ho! Data local S3 bucket me load ho gaya hai.")

# Check karne ke liye wapas read karke dekhte hain
response = s3_client.get_object(Bucket='my-first-bucket', Key='raw/profile.json')
file_content = response['Body'].read().decode('utf-8')
print("S3 se wapas mila data:", file_content)