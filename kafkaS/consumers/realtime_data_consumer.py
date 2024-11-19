from confluent_kafka import Consumer

class RealtimeConsumer:
    def __init__(self, consumer_config, topic):
        self.topic = topic
        self.consumer = Consumer(consumer_config)
        self.consumer.subscribe([self.topic])

    def consume(self, callback):
        try:
            print(f"listening to {self.topic}\n")
            while True:
                msg = self.consumer.poll(1.0)  # Poll for messages
                if msg is None:
                    continue
                if msg.error():
                    print(f"Consumer error: {msg.error()}")
                    continue

                # Process the received message
                key = msg.key().decode('utf-8') if msg.key() else None
                value = msg.value().decode('utf-8')
                print(f"Received: key={key}, value={value}")

                # WS callback
                callback()

        except KeyboardInterrupt as ke:
            print("KeyboardInterrupt")        

        except Exception as e:
            print("Killed!")

        finally:
            self.consumer.close()    