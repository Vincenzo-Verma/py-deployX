FROM ubuntu:focal

RUN sudo apt update
RUN sudo apt install -y curl git
RUN curl -sL https://deb.nodesource.com/setup_20.x | bash -
RUN sudo apt-get upgrade -y
RUN sudo api install -y nodejs 


WORKDIR /home/app
COPY main.sh main.sh
COPY main.py main.py

ENTRYPOINT [ main.sh ]


