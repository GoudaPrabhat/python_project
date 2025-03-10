import boto3

# Define AWS region
region = "us-east-2"
client = boto3.client('s3')

# response = client.create_bucket(
#     Bucket='boto3-python-prabhat',
#     CreateBucketConfiguration={
#         'LocationConstraint': region,
#     },
#     )

response = client.get_bucket_acl(
    Bucket='boto3-python-prabhat',
)

print(response)