from confluent_kafka import Producer
# from kafka_config import KAFKA_CONFIG
import time

KAFKA_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
}

producer = Producer(KAFKA_CONFIG)

def callback(err, msg):
    if err:
        print(err)
    else:
        print(f"message published to {msg.topic()} [partition {msg.partition()}]")    

topic = 'rtt'

for i in range(5):
    key = f'key-{i}'
    value = f'value-{i}'
    producer.produce(topic, key=key, value=value, callback=callback)
    # producer.flush()
    time.sleep(1)