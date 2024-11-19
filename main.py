from kafkaS.producers import realtime_data_prod as rp
from kafkaS.consumers import realtime_data_consumer as rc

def callback():
    print("sending odds to ws")

producer_config = {
    'bootstrap.servers': 'localhost:9092',
}

consumer_config = {
    'group.id': 'default',
    'auto.offset.reset': 'earliest',
    'bootstrap.servers': 'localhost:9092',
}

topic = 'rtt'

producer = rp.RealtimeProducer(producer_config, topic)
producer.produce_msg()

consumer = rc.RealtimeConsumer(consumer_config, topic)
consumer.consume(callback)
