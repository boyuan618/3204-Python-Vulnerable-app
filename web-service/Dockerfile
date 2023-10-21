# syntax=docker/dockerfile:1

FROM python:3.12-bookworm

RUN apt-get update
RUN apt-get install -y syslog-ng
RUN /etc/init.d/syslog-ng start

WORKDIR /web-service

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py"]

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:root123' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
