FROM python:3.8-alpine3.11

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache build-base linux-headers
COPY requirements.txt reqs.dat
RUN cat reqs.dat
RUN pip3 install -r reqs.dat
RUN rm reqs.dat
COPY src/ /tmp/app/
WORKDIR /tmp/app/

ENTRYPOINT ["python3", "main/app.py"]