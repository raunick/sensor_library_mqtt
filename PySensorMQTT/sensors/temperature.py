import random
from PySensorMQTT.sensors.base import SensorBase

class TemperatureSensor(SensorBase):
    def generate_temperature(self) -> float:
        return round(random.uniform(15.0, 30.0), 2)

    def publish(self) -> None:
        temperature = self.generate_temperature()
        payload = f"Temperature: {temperature}"
        self.mqtt_client.publish(self.parameters['topic'], payload)
        print(f"Publicado: {payload}")
