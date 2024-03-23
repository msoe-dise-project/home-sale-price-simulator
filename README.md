# home-sale-price-simulator
Simulates home sale data

## Build

```bash
$ docker build -t home-sale-price-simulator .
$ docker tag home-sale-price-simulator dh-arm.hpc.msoe.edu:5000/home-sale-price-simulator
$ docker push dh-arm.hpc.msoe.edu:5000/home-sale-price-simulator
```

## Run
The simulator needs several parameters to be provided.

```
NDAYS="1.0"
KAFKA_HOST="kafka-broker:9092" 
KAFKA_TOPIC="labeled-home-sale-events"
```

```bash
$ docker run --name "home-sale-price-simulator" \
			 --network home-sale-event-system \
			 -d \
			 -e NDAYS="1.0" \
			 -e KAFKA_HOST="kafka-broker:9092" \
			 -e KAFKA_TOPIC="labeled-home-sale-events" \
			 dh-arm.hpc.msoe.edu:5000/home-sale-price-simulator
```

TODO: add interest rates
