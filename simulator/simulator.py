#!/usr/bin/env python

import datetime as dt
import json
import os
import pprint
import sys
import time

import pandas as pd

from kafka import KafkaProducer

TOPIC_KEY = "KAFKA_TOPIC"
HOST_KEY = "KAFKA_HOST"

DATA_FILE_KEY = "DATA_FILE"
NDAYS_KEY = "NDAYS"

DAYS_TO_SEC = 24.0 * 60.0 * 60.0

def send_events(host, topic, flname, ndays):
    print("Creating producer")
    producer = KafkaProducer(bootstrap_servers=host,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    while True:
        for price_multiplier in [1.0, 1.33, 1.66, 2.0]:
            df = pd.read_csv(flname)
            df["price"] *= price_multiplier

            sales_events = df.to_dict("records")

            delay = ndays * DAYS_TO_SEC / len(sales_events)

            for record in sales_events:
                idx = record["id"]
                producer.send(topic, key=bytes(str(idx), "utf-8"), value=record)

            time.sleep(delay)

if __name__ == "__main__":
    for key in [DATA_FILE_KEY, TOPIC_KEY, HOST_KEY, NDAYS_KEY]:
        if key not in os.environ:
            msg = "Must specify environmental variable {}".format(key)
            print(msg)
            sys.exit(1)

    send_events(os.environ[HOST_KEY],
                os.environ[TOPIC_KEY],
                "kc_house_data.csv",
                float(os.environ[NDAYS_KEY]))
