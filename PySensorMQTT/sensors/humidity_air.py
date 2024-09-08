from PySensorMQTT.sensors.base import SensorBase
import random

class HumidityAirSensor(SensorBase):
    def generate_humidity_air(self) -> float:
        return round(random.uniform(60.0, 80.0), 2)

    # Publica os dados simulados de umidade do ar
    def publish(self) -> None:
        humidity = self.generate_humidity_air()
        if humidity is not None and isinstance(humidity, float):
            payload = f"Humidity Air: {humidity}"
            self.mqtt_client.publish(self.parameters['topic'], payload)
            print(f"Publicado: {payload}")
        else:
            print("Falha na geração de umidade do ar.")
