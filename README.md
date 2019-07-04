# Miniframework for your Raspberry Pi (pure Python)

Create simple or complex applications with common components for the Raspberry Pi

Supports the following sensors:

- All Types of GPIO Parts (Relay, LED etc...)
- DS18B20 (One Wire Temperature sensor)
- DHT22 (Temperature and Humidity sensor)
- IR Motion Sensor (PIR)
- HX711 (Load Cell Amplifier for Scales)
 
 
 ### Example in /application/main.py
 
`class App:
    def __init__(self):
        self.config = Config()
        self.config_data = self.config.get_config_data()
        self.relay = Device(int(self.config_data['DEFAULT']['relay_pin']), "relay")
        self.dht22 = DHT22(int(self.config_data['DEFAULT']['dht22_pin']))`

    `def start(self):
        temperature, humidity = self.dht22.get_data()
        print("Temperature: {}".format(temperature))
        print("Humidity: {}".format(humidity))

        if temperature > 22:
            print("Relay is on!")
            self.relay.on()
        else:
            print("Relay is off!")
            self.relay.off()`
            


### Thanks to:

- https://github.com/RogerWoollett (DS18B20)
- https://github.com/adafruit/Adafruit_Python_DHT (DHT22)
- https://github.com/adafruit/Adafruit_Python_GPIO (GPIO)
- https://github.com/JGUINO/3189-capteurs-pressions (HX711)
