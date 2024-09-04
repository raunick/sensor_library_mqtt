from abc import ABC, abstractmethod
from sensor_library.mqtt_sensor import MqttClient
from typing import TypedDict

class MqttParameters(TypedDict):
    sensor_name: str
    broker: str
    port: int
    topic: str
    update_interval: int
    sensor_type: str

class SensorBase(ABC):
    def __init__(self, parameters: MqttParameters) -> None:
        self.parameters = parameters
        self.mqtt_client = MqttClient(parameters['broker'], parameters['port'])
        self.mqtt_client.connect()

    @abstractmethod
    def publish(self) -> None:
        raise NotImplementedError("Subclasses devem implementar este método.")
