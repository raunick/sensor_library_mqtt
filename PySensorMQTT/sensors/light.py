from PySensorMQTT.sensors.base import SensorBase
import random

# Sensor de luminosidade
class LightSensor(SensorBase):
    def generate_light(self) -> float:
        return round(random.uniform(40.0, 60.0), 2)

    def publish(self) -> None:
        light = self.generate_light()
        payload = f"Light PPD: {light}"
        self.mqtt_client.publish(self.parameters['topic'], payload)
        print(f"Publicado: {payload}")