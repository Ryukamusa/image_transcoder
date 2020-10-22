from PIL import Image
import boto3
import os
import json
from time import time

Image.MAX_IMAGE_PIXELS = 933120000

s3_client = boto3.client('s3')
writable_dir = '/tmp/'

def get_s3_file(source_bucket, file_name):
    st = time()
    with open(writable_dir + file_name, 'wb') as f:
        s3_client.download_fileobj(source_bucket, file_name, f)
    fn = time()
    took = fn-st
    # print(f'Downloaded file - {took}')

def upload_transcoded_image(file_name, destination_bucket):
    st = time()
    with open(file_name, 'rb') as f:
        s3_client.upload_fileobj(f, destination_bucket, file_name.split(writable_dir)[1]) 
    fn = time()
    took = fn-st
    # print(f'Uploaded file - {took}')

def transcode_image(file_name, size, new_name):
    st = time()
    im = Image.open(file_name)
    im.thumbnail((size, size))
    im.save(new_name)
    fn = time()
    took = fn-st
    # print(f'Converted {size} file - {took}')

def create_and_push_image(original_name, destination_bucket, sizes):
    for size in sizes:
        original_image_path = writable_dir + original_name
        original_image_path_splited = original_image_path.split('.')
        name_without_ext = '.'.join(original_image_path_splited[0:-1])
        new_name = f'{name_without_ext}_{size}.{original_image_path_splited[-1]}'
        transcode_image(original_image_path, size, new_name)
        upload_transcoded_image(new_name, destination_bucket)

def process_files(source_bucket, destination_bucket, files_name, sizes):
    for file_name in files_name:
        get_s3_file(source_bucket, file_name)
        create_and_push_image(file_name, destination_bucket, sizes)

        
def get_files_from_event(event):
    return [record['s3']['object']['key'] for record in event['Records']]

def lambda_handler(event, context):
    try:
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        destination_bucket = os.environ['S3_DESTINATION_BUCKET']
        sizes = [int(size) for size in os.environ['TRANSCODE_SIZES'].split(',')]
        files_name = get_files_from_event(event)
        process_files(source_bucket, destination_bucket, files_name, sizes)
        return {'statusCode': 200}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps(e.args)}
