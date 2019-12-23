FROM python:3.7-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

# -- Install dependencies:
RUN pip3 install --upgrade pip \
    && pip3 install -r /usr/src/app/requirements.txt

ENTRYPOINT ["python","run.py"]
