from sensor_library.sensors.base import SensorBase
import random

# Módulo relé
class ModuloRele(SensorBase):
    def generate_modulo_rele(self) -> bool:
        return random.choice([True, False])

    def publish(self) -> None:
        modulo_rele = self.generate_modulo_rele()
        payload = f"Modulo Rele: {modulo_rele}"
        self.client.publish(self.parameters['topic'], payload)
        print(f"Publicado: {payload}")