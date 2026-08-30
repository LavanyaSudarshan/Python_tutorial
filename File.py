import boto3

client = boto3.client('s3')

#response = client.create_bucket(
    #Bucket='lavanya-demo-boto3-yt-123', 
#)

response = client.get_bucket_acl(
    Bucket='lavanya-demo-boto3-yt-123'
)

print(response)