import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self, broker: str, port: int):
        self.client = mqtt.Client()
        self.broker = broker
        self.port = port

    def connect(self) -> None:
        try:
            self.client.connect(self.broker, self.port)
            self.client.loop_start()
        except Exception as e:
            print(f"Erro ao conectar ao broker: {e}")
            raise

    def publish(self, topic: str, payload: str) -> None:
        self.client.publish(topic, payload)
