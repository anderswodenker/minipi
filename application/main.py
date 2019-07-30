from config.config import Config
from sensorlib.gpio import Device
from sensorlib.dht22 import DHT22
from sensorlib.scale import Scale


# EXAMPLE
class App:
    def __init__(self):
        # CONFIG DATA
        self.config = Config()
        self.config_data = self.config.get_config_data()

        # RELAY PIN
        self.relay_pin = int(self.config_data['DEFAULT']['relay_pin'])
        # DHT 22 PIN
        self.dht22_pin = int(self.config_data['DEFAULT']['dht22_pin'])

        # INIT RELAY
        self.relay = Device(self.relay_pin, "relay")

        # INIT DHT22 SENSOR
        self.dht22 = DHT22(self.dht22_pin)

        # INIT SCALE
        self.scale = Scale()

    def calibrate_scale(self): # QUICK AND EASY CALIBRATE FUNCTION FOR THE SCALE
        input("Remove any items from scale and press Enter...")
        self.scale.setup()
        input("Please place an item of known weight on the scale and press Enter...")
        weight = input("Please enter the item's weight in grams: ")
        self.scale.calibrate(int(weight))
        print("The scale is now calibrated and the offset ist saved in the config.ini")

        # GET SCALE DATA (QUICK AND EASY!)
        print("Weight: {}g".format(self.scale.get_data()))

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
