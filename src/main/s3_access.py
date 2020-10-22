import boto3

s3_client = boto3.client('s3')

def get_s3_resource(file_name, destination_bucket):
    upload_transcoded_image(file_name, destination_bucket)
    return f'https://{destination_bucket}.s3.eu-central-1.amazonaws.com/{file_name}'
    
def upload_transcoded_image(file_name, destination_bucket):
    with open(file_name, 'rb') as f:
        s3_client.upload_fileobj(f, destination_bucket, file_name)