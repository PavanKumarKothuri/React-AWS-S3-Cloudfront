import boto3
import os

bucket_name = "react-app-yourname"  # Replace with your bucket name
build_folder = "./build"  # Path to the build folder

s3 = boto3.client("s3")

# Upload files
for root, dirs, files in os.walk(build_folder):
    for file in files:
        file_path = os.path.join(root, file)
        s3_key = os.path.relpath(file_path, build_folder)
        s3.upload_file(file_path, bucket_name, s3_key)
        s3.put_object_acl(ACL="public-read", Bucket=bucket_name, Key=s3_key)
        print(f"Uploaded and made public: {s3_key}")