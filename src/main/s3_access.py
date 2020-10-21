import boto3

s3_client = boto3.client('s3')

def get_s3_resource(local_file_name):
    pass

def upload_transcoded_image(file_name, destination_bucket):
    with open(file_name, 'rb') as f:
        s3_client.upload_fileobj(f, destination_bucket, file_name) 
