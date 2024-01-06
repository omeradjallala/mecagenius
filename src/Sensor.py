import RPi.GPIO as GPIO

class Sensor:
    def __init__(self) -> None:
        self.line_pin_right = 19
        self.line_pin_middle = 16
        self.line_pin_left = 20

    def feed(self):
        status_right = GPIO.input(self.line_pin_right)
        status_middle = GPIO.input(self.line_pin_middle)
        status_left = GPIO.input(self.line_pin_left)
        return (status_right, status_middle, status_left)

    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.line_pin_right,GPIO.IN)
        GPIO.setup(self.line_pin_middle,GPIO.IN)
        GPIO.setup(self.line_pin_left,GPIO.IN)
