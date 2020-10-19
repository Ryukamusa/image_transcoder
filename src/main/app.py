from flask import Flask, jsonify, request
import os
from s3_access import *
from pathlib import Path
from dotenv import load_dotenv
import os
from transcoder import transcode_image

def load_env_vars():
    staging_env = os.environ['STAGE_ENV']
    env_path = Path(f'env/{staging_env}.env')
    load_dotenv(dotenv_path=env_path)
    
app = Flask(__name__)

API_PATH = '/api/v1/'

def process_files(source_bucket, destination_bucket, files_name):
    for file_name in files_name:
        get_s3_file(source_bucket, file_name)
        transcode_image(file_name)
        upload_transcoded_image(file_name, destination_bucket)

def get_env(value):
    return os.environ.get(value)

## ROUTES
@app.route(f'{API_PATH}/health', methods = ['GET'])
def health():
    return 'OK', 200

@app.route(f'{API_PATH}/s3', methods = ['POST'])
def s3_update():
    filesList = request.json
    file_names = filesList.get('files')
    process_files(get_env('S3_SOURCE_DATA'), get_env('S3_DESTINATION_DATA'), file_names)
    return jsonify(file_names)

@app.route(f'{API_PATH}/transcoder', methods = ['POST'])
def transcode_file():
    filesList = request.json
    return jsonify(filesList)


if __name__ == '__main__':
    load_env_vars()
    app.run('0.0.0.0', port = 8080, debug = True)