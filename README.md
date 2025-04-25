# Kafka KRaft POC

This is a simple Proof of Concept demonstrating Kafka in KRaft mode (without Zookeeper) with a producer and consumer.

## Prerequisites

- Docker and Docker Compose
- Python 3.x
- pip

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Start Kafka in KRaft mode:
```bash
docker-compose up -d
```

3. Wait for Kafka to start (about 30 seconds)

## Running the POC

1. In one terminal, start the consumer:
```bash
python consumer.py
```

2. In another terminal, start the producer:
```bash
python producer.py
```

The producer will send 10 messages to the 'test_topic' topic, and the consumer will receive and display them.

## Cleanup

To stop and remove the Kafka container:
```bash
docker-compose down
``` 