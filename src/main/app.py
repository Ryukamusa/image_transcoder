from flask import Flask, jsonify, request
import os
from s3_access import *
from pathlib import Path
from dotenv import load_dotenv
import os
from transcoder import transcode_image
import uuid

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
        image_id = uuid.uuid4()
        file_name = uuid.uuid4()
        with(file_name, 'wb') as f:
            f.write(request.get_data())
        local_name = transcode_file(file_name, size)
        get_s3_resource(local_name)
        return f'allowed {local_name}'
    return 'Content-Type not allowed', 400


if __name__ == '__main__':
    app.run('0.0.0.0', port = 8081, debug = True)

if __name__ == '__main__':
    load_env_vars()
    allowed_types = [image_type for image_type in get_env('IMAGE_TYPES').split(',')]
    app.run('0.0.0.0', port = 80, debug = True)