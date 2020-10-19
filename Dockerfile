FROM python:3.8-alpine3.11

COPY requirements.txt reqs.dat
RUN cat reqs.dat
RUN pip3 install -r reqs.dat
RUN pip install awscli --force-reinstall --upgrade
RUN rm reqs.dat
COPY src/ /tmp/app/
WORKDIR /tmp/app/

ENTRYPOINT ["python3", "main/app.py"]