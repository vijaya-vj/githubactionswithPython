#FROM alpine:3.13
FROM python:3
sudo docker build -t samplePythonImage .

ADD TestPython.py ./src/TestPython.py
RUN python3 ./TestPython.py
ENTRYPOINT ["./TestPython.py"]