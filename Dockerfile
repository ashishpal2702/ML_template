FROM python:3.10.5-slim-buster

EXPOSE 9001

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install supervisor

COPY requirements.txt /mnt/src/requirements.txt

RUN  pip install -r /mnt/src/requirements.txt

COPY . /mnt/src/

WORKDIR /mnt/src/

RUN pip install -e .

# Initializing from supervisord
CMD ["supervisord","-c","/mnt/src/config/service_script.conf"]