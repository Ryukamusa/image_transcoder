from flask import Flask, jsonify, request
import os
from s3_access import *
from pathlib import Path
from dotenv import load_dotenv
import os
from transcoder import transcode_image
import uuid
import io


app = Flask(__name__)

API_PATH = '/api/v1/'

def load_env_vars():
    staging_env = os.environ['STAGE_ENV']
    env_path = Path(f'env/{staging_env}.env')
    load_dotenv(dotenv_path=env_path)
    

def get_env(value):
    return os.environ.get(value)

## ROUTES
@app.route(f'{API_PATH}/health', methods = ['GET'])
def health_api():
    return 'OK', 200

@app.route(f'{API_PATH}/transcoder', methods = ['POST'])
def transcode_file_api():
    content_type = request.content_type
    extension = content_type.split('/')[1]
    if content_type in allowed_types:
        file_name = str(uuid.uuid4())
        file_name = str(uuid.uuid4())
        data = request.get_data()
        resized_image_data = transcode_file(data, file_name, size)
        local_name = transcode_file(file_name, size)
        get_s3_resource(file_name, resized_image_data)
        return 'Foi'
    return 'Content-Type not allowed', 400

if __name__ == '__main__':
    load_env_vars()
    allowed_types = [image_type for image_type in get_env('IMAGE_TYPES').split(',')]
    app.run('0.0.0.0', port = 80, debug = True)