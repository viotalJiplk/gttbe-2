FROM python:alpine

RUN apk add --update --no-cache bash
COPY buildConfig/prod/requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /build
WORKDIR /build
COPY src /build
RUN mv config-template.json config.json



CMD ["gunicorn", "-b :80", "app:app"]
