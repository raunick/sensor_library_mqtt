import time
from PySensorMQTT.sensors.temperature import TemperatureSensor
from PySensorMQTT.sensors.humidity_air import HumidityAirSensor
from PySensorMQTT.sensors.humidity_soil import HumiditySoilSensor
from PySensorMQTT.sensors.light import LightSensor
from PySensorMQTT.sensors.motion import MotionSensor
from PySensorMQTT.sensors.modulo_rele import ModuloRele

class SensorManager:
    def __init__(self) -> None:
        self.sensors = []

    def add_sensor(self, parameters) -> None:
        sensor_classes = {
            'temperature': TemperatureSensor,
            'humidity_air': HumidityAirSensor,
            'humidity_soil': HumiditySoilSensor,
            'light': LightSensor,
            'motion': MotionSensor,
            'modulo_rele': ModuloRele,
            # Adicionar outros sensores
        }

        sensor_type = parameters['sensor_type']
        if sensor_type not in sensor_classes:
            raise ValueError(f"Tipo de sensor inválido: {sensor_type}")

        sensor = sensor_classes[sensor_type](parameters)
        self.sensors.append(sensor)

    def start(self) -> None:
        while True:
            for sensor in self.sensors:
                sensor.publish()
            time.sleep(min(sensor.parameters['update_interval'] for sensor in self.sensors))
