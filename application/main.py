from config.config import Config
from sensorlib.gpio import Device
from sensorlib.dht22 import DHT22


# EXAMPLE
class App:
    def __init__(self):
        self.config = Config()
        self.config_data = self.config.get_config_data()
        self.relay = Device(int(self.config_data['DEFAULT']['relay_pin']), "relay")
        self.dht22 = DHT22(int(self.config_data['DEFAULT']['dht22_pin']))

    def start(self):
        temperature, humidity = self.dht22.get_data()
        print("Temperature: {}".format(temperature))
        print("Humidity: {}".format(humidity))

        if temperature > 22:
            print("Relay is on!")
            self.relay.on()
        else:
            print("Relay is off!")
            self.relay.off()
