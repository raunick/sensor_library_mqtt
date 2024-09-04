from sensor_library.sensors.base import SensorBase
import random

# Sensor de movimento
class MotionSensor(SensorBase):
    def generate_motion(self) -> float:
        return round(random.uniform(40.0, 60.0), 2)

    def publish(self) -> None:
        motion = self.generate_motion()
        payload = f"Motion: {motion}"
        self.client.publish(self.parameters['topic'], payload)
        print(f"Publicado: {payload}")