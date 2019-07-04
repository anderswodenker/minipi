import configparser
from error.log import ErrorLog
config_file = '/home/pi/plugpi/config/config.ini'


class Config:
    def __init__(self):
        # READ CONFIG
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)
        self.pin_name = "PINS"
        self.config_name = "LIGHT"
        self.max_key = "max"
        self.min_key = "minimum"
        self.pin_values = dict()
        self.config_values = dict()
        self.firebase_config = dict()
        self.online = False
        self.logging = ErrorLog()

    def get_config_data(self):
        try:
            self.config.read(self.config_file)
            return self.config
        except Exception as e:
            self.logging.write_log(e)

    def get_config_values(self):
        try:
            self.config.read(self.config_file)
            if self.config_name in self.config:
                for key in self.config[self.config_name]:
                    self.config_values[key] = int(self.config[self.config_name][key])

            return self.config_values

        except Exception as e:
            self.logging.write_log(e)
            return False

    def get_values(self):
        try:
            self.config.read(self.config_file)
            if self.pin_name in self.config:
                for key in self.config[self.pin_name]:
                    self.pin_values[key] = int(self.config[self.pin_name][key])

            return self.pin_values
        except Exception as e:
            self.logging.write_log(e)

    def update_config(self, name, key, value):
        try:
            self.config.set(name, key, str(value))
            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)

            return True

        except Exception as e:
            self.logging.write_log(e)
            return False
