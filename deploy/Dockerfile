FROM python:3.6-alpine
RUN apt-get update && apt-get -y apt-transport-https install supervisor
COPY requirements.txt /tmp/
WORKDIR /tmp
RUN pip install -r requirements.txt
RUN useradd -m  sinobot && \
    mkdir /usr/local/xyapi_ws && \
    chown -R sinobot:sinobot /usr/local/xyapi_ws 
USER sinobot
