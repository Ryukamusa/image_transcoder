import boto3

s3_client = boto3.client('s3')
writable_dir = '/tmp/'

def get_s3_file(source_bucket, file_name):
    with open(writable_dir + file_name, 'wb') as f:
        s3_client.download_fileobj(source_bucket, file_name, f)

def upload_transcoded_image(file_name, destination_bucket):
    with open(writable_dir + file_name, 'rb') as f:
        s3_client.upload_fileobj(f, destination_bucket, file_name) 
