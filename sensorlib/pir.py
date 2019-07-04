import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class PIR:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)

    def get_data(self):
        if GPIO.input(self.pin) == 1:
            return True
        else:
            return False
