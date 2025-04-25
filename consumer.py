from kafka import KafkaConsumer
import json

def create_consumer():
    return KafkaConsumer(
        'test_topic',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

if __name__ == "__main__":
    consumer = create_consumer()
    print("Starting consumer...")
    
    try:
        for message in consumer:
            print(f"Received message: {message.value}")
    except KeyboardInterrupt:
        print("Consumer stopped by user")
    finally:
        consumer.close() 