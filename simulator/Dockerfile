FROM python:3.11-slim

WORKDIR /app
COPY simulator.py /app/
COPY kc_house_data.csv /app/

RUN pip3 install -U pip wheel
RUN pip3 install pandas kafka-python

ENV DATA_FILE="kc_house_data.csv"
CMD python3 simulator.py
