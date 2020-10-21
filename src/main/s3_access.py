import boto3

s3_client = boto3.client('s3')

def get_s3_resource(file_name, resized_image_data, destination_bucket):
    upload_transcoded_image(file_name, resized_image_data, destination_bucket)

def upload_transcoded_image(file_name, resized_image_data, destination_bucket):
    s3_client.upload_fileobj(resized_image_data, destination_bucket, file_name)
