FROM python:3
COPY . /app
WORKDIR /app
RUN dir
RUN echo "WORKDIR" $WORKDIR
RUN echo "dir" dir
RUN chmod +x src/TestPython.py
RUN python3 ./src/TestPython.py