from confluent_kafka import Producer
import time
# flow: realtime data prod -> realtime data consumer & join/aggregate (& calc blackboxed odds) -> relayed to connected clients via ws

class RealtimeProducer:
    def __init__(self, config, topic):
        self.producer = Producer(config)
        self.topic = topic

    def on_delivery(self, err, msg):
        if err:
            print(err)
        else:
            print(f"msg delivered by RealtimeProducer, {msg.topic()}, {msg.partition()}\n")    

    def produce_msg(self):
        """
        Produces the messages, published to broker by the Producer
        Requires topic
        Dummy data sent out as of now
        """

        for i in range(5):
            key = f"key-{i}"
            value = f"value-{i}"
            print(f"sending {key} : {value}\n")
            self.producer.produce(
                topic=self.topic,
                key=key,
                value=value,
                callback=self.on_delivery
            )
            time.sleep(1)

