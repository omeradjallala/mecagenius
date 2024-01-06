#!/usr/bin/env python3

from src.Driver import Driver
from src.Sensor import Sensor
from time import sleep, time

class Core:
    def __init__(self) -> None:
        self.driver = Driver()
        self.sensor = Sensor()

        self.sensor.setup()
        self.driver.launch()
        self.rot = 'no'

    def releas(self):
        self.driver.destroy()

    def run(self):
        right, middle, left = self.sensor.feed()
        while right:
            self.driver.move(50,  'no', 'right', 0.8)
            sleep(0.3)
        while left:
            self.driver.move(50,  'no', 'left', 0.8)
            sleep(0.3)
        self.driver.move(80, 'forward', 'no')
        print(right, middle, left, self.rot)
