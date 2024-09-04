from sensor_library.sensors.manager import SensorManager

manager = SensorManager()
params = {
    'sensor_name': 'sensor_1',
    'broker': 'localhost',
    'port': 1883,
    'topic': 'sensor/temperature',
    'update_interval': 5,
    'sensor_type': 'temperature'
}

manager.add_sensor(params)
manager.start()
