from kafka import KafkaProducer
import time
import json

def create_producer():
    return KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )

def send_messages(producer, topic):
    for i in range(10):
        message = {
            'message_id': i,
            'content': f'This is message number {i}',
            'timestamp': time.time()
        }
        producer.send(topic, value=message)
        print(f"Sent message: {message}")
        time.sleep(1)

if __name__ == "__main__":
    topic = 'test_topic'
    producer = create_producer()
    print(f"Starting producer for topic: {topic}")
    send_messages(producer, topic)
    producer.flush()
    print("All messages sent successfully!") 