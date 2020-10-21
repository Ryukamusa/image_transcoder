import boto3

s3_client = boto3.client('s3')

def get_s3_resource(file_name, destination_bucket):
    upload_transcoded_image(file_name, destination_bucket)
    return get_presigned_url(file_name, destination_bucket)

def upload_transcoded_image(file_name, destination_bucket):
    with open(file_name, 'rb') as f:
        s3_client.upload_fileobj(f, destination_bucket, file_name)

def get_presigned_url(object_name, bucket_name, expiration=60):
    response = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket_name,
        'Key': object_name},  ExpiresIn=expiration)