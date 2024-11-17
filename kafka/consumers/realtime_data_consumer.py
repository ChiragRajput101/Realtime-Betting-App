from confluent_kafka import Consumer
# from kafka_config import CONSUMER_CONFIG
CONSUMER_CONFIG = {
    'group.id': 'default-group',  # Override in consumers
    'auto.offset.reset': 'earliest',
    'bootstrap.servers': 'localhost:9092',
}

config = CONSUMER_CONFIG.copy()
config['group.id'] = 'realtime-data-consumer-group'

consumer = Consumer(config)
topic = 'rtt'
consumer.subscribe([topic])

print(f"Listening to {topic}...")

try:
    while True:
        msg = consumer.poll(1.0)  # Poll for messages
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        # Process the received message
        key = msg.key().decode('utf-8') if msg.key() else None
        value = msg.value().decode('utf-8')
        print(f"Received: key={key}, value={value}")

        # odds cal and publish to another topic
        
except KeyboardInterrupt:
    print("Consumer interrupted.")
finally:
    consumer.close()




