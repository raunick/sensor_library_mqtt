# 🌐 Sensor Library - Simulação de Sensores com MQTT

Bem-vindo à **Sensor Library**! 🎉 Essa biblioteca Python foi projetada para facilitar a simulação e publicação de dados de sensores usando o protocolo MQTT. Ideal para projetos de IoT, automação e monitoramento em tempo real, essa biblioteca oferece uma interface simples para a criação de diferentes tipos de sensores e a publicação de dados via um broker MQTT. 🚀

# 📦 Instalação

Você pode instalar a biblioteca diretamente do PyPi com o comando abaixo:

```bash
pip install PySensor-Mqtt
```
# 🛠️ Funcionalidades

- 🌡️ Simulação de Sensores de Temperatura, Umidade do Ar, Umidade do Solo, Luminosidade, Movimento e Módulo Relé
- 🔄 Publicação de dados em tempo real via MQTT
- 🧑‍💻 Fácil integração com sistemas de monitoramento e automação
- 📊 Suporte para diferentes tipos de sensores personalizáveis
- 🛡️ Validação de integridade dos dados e robustez na conexão com o broker MQTT

# 🚀 Como Usar

Aqui está um exemplo de como configurar e iniciar a biblioteca:

**1. Crie um Gerenciador de Sensores**

```python
from PySensorMQTT import SensorManager

manager = SensorManager()
```

**2. Configure os Parâmetros do Sensor**

Cada sensor precisa de um conjunto de parâmetros para funcionar corretamente. Exemplo de configuração de um sensor de temperatura:

``` python
params = {
    'sensor_name': 'sensor_1',
    'broker': 'localhost',  # Endereço do broker MQTT
    'port': 1883,           # Porta do broker MQTT
    'topic': 'sensor/temperature',  # Tópico MQTT para publicação
    'update_interval': 5,    # Intervalo de atualização em segundos
    'sensor_type': 'temperature'  # Tipo do sensor
}
```

**3. Adicione o Sensor ao Gerenciador**

Agora, basta adicionar o sensor ao gerenciador e começar a publicação:

```python
manager.add_sensor(params)
manager.start()
```
✨ E pronto! Seus dados de sensor estão sendo simulados e publicados automaticamente no tópico MQTT especificado. 🚀

# 📚 Exemplos de Tipos de Sensores

Aqui estão os tipos de sensores que você pode adicionar à biblioteca:

- 🌡️ Temperature Sensor ('temperature')
- 💧 Humidity Air Sensor ('humidity_air')
- 🌱 Humidity Soil Sensor ('humidity_soil')
- 💡 Light Sensor ('light')
- 🕵️ Motion Sensor ('motion')
- 🔌 Módulo Relé ('modulo_rele')

## Exemplo de Adição de Múltiplos Sensores
```python
from PySensorMQTT import SensorManager

manager = SensorManager()
# Adiciona um sensor de temperatura
manager.add_sensor({
    'sensor_name': 'temp_sensor',
    'broker': 'broker.mqtt.cool',
    'port': 1883,
    'topic': 'sensor/temperature',
    'update_interval': 5,
    'sensor_type': 'temperature'
})

# Adiciona um sensor de umidade do ar
manager.add_sensor({
    'sensor_name': 'humidity_sensor',
    'broker': 'broker.mqtt.cool',
    'port': 1883,
    'topic': 'sensor/humidity_air',
    'update_interval': 10,
    'sensor_type': 'humidity_air'
})

manager.start()
```
# 🛡️ Segurança e Confiabilidade

Todos os dados gerados são validados para garantir sua integridade.
Conexão com o broker MQTT é automaticamente gerenciada, com retentativas em caso de falha.

# 🧪 Testes
Para garantir que sua implementação funcione corretamente, utilize os testes pré-configurados na biblioteca:

```bash
pytest tests/
```

# 🤝 Contribuições
Contribuições são bem-vindas! Se você tiver sugestões de melhorias, novas funcionalidades ou encontrar algum bug, sinta-se à vontade para abrir uma issue ou enviar um pull request.

# 📄 Licença

Esta biblioteca é licenciada sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

**Feita com 💙 por Raunick Vileforte - Raunickbhdesign@gmail.com ✨**
