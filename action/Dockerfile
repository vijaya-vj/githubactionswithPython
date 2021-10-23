#FROM alpine:3.13

#RUN apt-get update &&  apt-get -y install sudo
#docker build -t samplePythonImage .


FROM python:3
WORKDIR /app
ADD . /app
#RUN pip install --trusted-host pypi.python.org -r ./src/TestPython.py
#ADD TestPython.py ./src/TestPython.py
RUN python3 ./src/TestPython.py
ENTRYPOINT ["./src/TestPython.py"]