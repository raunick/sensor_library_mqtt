# sensors/temperature.py

from sensor_library.sensors.base import SensorBase
import random

class TemperatureSensor(SensorBase):
    def generate_temperature(self) -> float:
        return round(random.uniform(15.0, 30.0), 2)

    def publish(self) -> None:
        temperature = self.generate_temperature()
        payload = f"Temperature: {temperature}"
        self.mqtt_client.publish(self.parameters['topic'], payload)
        print(f"Publicado: {payload}")
