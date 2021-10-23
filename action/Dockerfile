#FROM alpine:3.13
FROM python:3

RUN apt-get update &&  apt-get -y install sudo
sudo docker build -t samplePythonImage .

ADD TestPython.py ./src/TestPython.py
RUN python3 ./TestPython.py
ENTRYPOINT ["./TestPython.py"]