import boto3
    
bucket_name = "react-app-yourname"  # Replace with your bucket name
s3 = boto3.client("s3")
    
# Get all objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)
for obj in response.get("Contents", []):
    key = obj["Key"]
    s3.put_object_acl(ACL="public-read", Bucket=bucket_name, Key=key)
    print(f"Public access granted for: {key}")