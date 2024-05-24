FROM python:alpine

RUN apk add --update --no-cache bash
COPY buildConfig/prod/requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /build
WORKDIR /build
COPY src /build
RUN cd utils
RUN mv config-docker.py config.py



CMD ["gunicorn", "-b :80", "app:app"]