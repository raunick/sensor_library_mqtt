# test_sensors.py
import unittest
from unittest.mock import patch
from PySensorMQTT.sensors.temperature import TemperatureSensor
from PySensorMQTT.sensors.base import MqttParameters

class TestTemperatureSensor(unittest.TestCase):
    def setUp(self):
        # Configurando os parâmetros do sensor antes de cada teste
        """
        Configura os parâmetros do sensor antes de cada teste.

        Os parâmetros utilizados s o:
        - broker: localhost
        - port: 1883
        - topic: sensor/temperature
        - update_interval: 5
        - sensor_type: temperature
        - device_id: STEMP01

        Depois disso, instancia o sensor com esses parâmetros.
        """
        self.parameters = MqttParameters(
            broker='localhost',
            port=1883,
            topic='sensor/temperature',
            update_interval=5,
            sensor_type='temperature',
            device_id='STEMP01'
        )
        self.sensor = TemperatureSensor(self.parameters)

    def test_generate_temperature(self):
        # Teste para verificar se a temperatura gerada é um número float
        """
        Verifica se o valor de temperatura gerado pelo sensor de temperatura
        é um número float e se está no intervalo correto (entre 15.0 e 30.0).
        """
        temperature = self.sensor.generate_temperature()
        self.assertIsInstance(temperature, float)
        self.assertGreaterEqual(temperature, 15.0)  # Verifica se a temperatura está no intervalo correto
        self.assertLessEqual(temperature, 30.0)

    def test_get_battery_level(self):
        # Teste para verificar se o nível de bateria está entre 50% e 100%
        """
        Verifica se o valor de nível de bateria gerado pelo sensor de
        temperatura está entre 50% e 100%.
        """
        
        battery_level = self.sensor.get_battery_level()
        self.assertIsInstance(battery_level, int)
        self.assertGreaterEqual(battery_level, 50)
        self.assertLessEqual(battery_level, 100)

    @patch('PySensorMQTT.mqtt_sensor.MqttClient.publish')
    def test_publish_active(self, mock_publish):
        # Teste para verificar se o payload é publicado corretamente quando o sensor está ativo
        """
        Verifica se o payload é publicado corretamente quando o sensor está ativo.

        Verifica se o método publish é chamado corretamente e se o payload contém
        o device_id e a temperatura gerada pelo sensor.
        """
        self.sensor.status = "ativo"
        self.sensor.publish()  # Simula a publicação

        # Verifique se o método publish foi chamado corretamente
        mock_publish.assert_called_once()

        # Obtenha o argumento passado para a publicação
        topic, payload = mock_publish.call_args[0]
        self.assertIn("data", payload)  # Atualizando para "data" ao invés de "temperature"
        self.assertIn("device_id", payload)
        self.assertEqual(self.sensor.parameters.device_id, "STEMP01")

    @patch('PySensorMQTT.mqtt_sensor.MqttClient.publish')
    def test_publish_inactive(self, mock_publish):
        # Teste para verificar se o payload é publicado corretamente quando o sensor está desativado
        """
        Verifica se o payload é publicado corretamente quando o sensor está desativado.

        Verifica se o método publish foi chamado corretamente e se o payload contém
        o device_id e o valor "-" para a temperatura.
        """
        self.sensor.status = "desativado"
        self.sensor.publish()  # Simula a publicação

        # Verifique se o método publish foi chamado corretamente
        mock_publish.assert_called_once()

        # Obtenha o argumento passado para a publicação
        topic, payload = mock_publish.call_args[0]
        self.assertIn("data", payload)  # Atualizando para "data" ao invés de "temperature"
        self.assertEqual(payload["data"], "-")  # Verifica se o valor "data" é "-" para o sensor desativado

    def test_on_action_message_activate(self):
        # Teste para ativar o sensor via o tópico de ação
        """
        Verifica se o método on_action_message ativa o sensor corretamente
        quando recebe uma mensagem de ação com o valor "activate".
        """
        
        message_payload = '{"device_id": "STEMP01", "action": "activate"}'
        message = type('Message', (object,), {'payload': message_payload.encode()})
        self.sensor.on_action_message(None, None, message)
        self.assertEqual(self.sensor.status, "ativo")

    def test_on_action_message_deactivate(self):
        # Teste para desativar o sensor via o tópico de ação
        """
        Verifica se o método on_action_message desativa o sensor corretamente
        quando recebe uma mensagem de ação com o valor "deactivate".
        """
        message_payload = '{"device_id": "STEMP01", "action": "deactivate"}'
        message = type('Message', (object,), {'payload': message_payload.encode()})
        self.sensor.on_action_message(None, None, message)
        self.assertEqual(self.sensor.status, "desativado")

    @patch('paho.mqtt.client.Client.disconnect')
    def test_disconnect(self, mock_disconnect):
        # Teste para verificar se o método disconnect é chamado corretamente
        """
        Verifica se o método disconnect é chamado corretamente
        quando o sensor é desativado.
        """

        self.sensor.disconnect()
        mock_disconnect.assert_called_once()


if __name__ == '__main__':
    unittest.main()
