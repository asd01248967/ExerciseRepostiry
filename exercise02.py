import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('name')
# for bucket in s3.bucket.all():
#     print(bucket.name)


# s3 = boto3.client('s3')
# s3.create_bucket(Bucket='my-bucket')
 