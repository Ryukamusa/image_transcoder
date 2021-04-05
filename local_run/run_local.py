#!/usr/bin/python3
import requests as req
import subprocess
import time

subprocess.call('./run-local-py', shell=True)

health_url = 'http://localhost:80/api/v1/health'

try:
    resp = req.get(health_url)
except:
    time.sleep(10)
    resp = req.get(health_url)
while resp.status_code != 200:
    resp = req.get(health_url)
    time.sleep(1)

print('Deploy feito!')
