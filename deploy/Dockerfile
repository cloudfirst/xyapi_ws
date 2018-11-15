FROM ubuntu:18.04
RUN apt-get update && apt-get -y apt-transport-https install supervisor
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY requirements.txt /tmp/
WORKDIR /tmp
RUN pip install -r requirements.txt
RUN useradd -m  sinobot && \
    mkdir -p /usr/local/xyapi_ws && mkdir -p /media/data && mkdir -p /var/log/sinyi \ 
    chown -R sinobot:sinobot /usr/local/xyapi_ws && chown -R sinobot:sinobot /var/log/sinyi
USER sinobot
