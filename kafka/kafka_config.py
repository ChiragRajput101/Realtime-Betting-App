KAFKA_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
}

CONSUMER_CONFIG = {
    'group.id': 'default-group',  # Override in consumers
    'auto.offset.reset': 'earliest',
    'bootstrap.servers': 'localhost:9092',
}
