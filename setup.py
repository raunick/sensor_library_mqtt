from setuptools import setup, find_packages

setup(
    name='sensor_library',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'paho-mqtt',
    ],
    description='Biblioteca para simulação de sensores e publicação via MQTT',
    author='Raunick Vileforte Vieira Generoso',
    author_email='raunickbhdesign@gmail.com',
    url='https://github.com/raunick/sensor_library',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
