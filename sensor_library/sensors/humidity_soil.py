from sensor_library.sensors.base import SensorBase
import random

# Sensor de umidade do solo
class HumiditySoilSensor(SensorBase):
    def generate_humidity_soil(self) -> float:
        return round(random.uniform(40.0, 60.0), 2)

    def publish(self) -> None:
        humidity = self.generate_humidity_soil()
        payload = f"Humidity Soil: {humidity}"
        self.client.publish(self.parameters['topic'], payload)
        print(f"Publicado: {payload}")