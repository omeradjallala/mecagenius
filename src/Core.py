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

        if right == middle == left == 1:
            return self.driver.move(50, 'forward', 'no', 0.0)
        if right == 1:
            self.driver.move(30, 'no', 'right')
            sleep(0.2)
            if middle == 0:
                self.driver.move(30, 'no', 'right', 0.3)
            return
        if left == 1:
            self.driver.move(30, 'no', 'left')
            sleep(0.2)
            if middle == 0:
                self.driver.move(30, 'no', 'left', 0.3)
            return
        self.driver.move(40, 'forward', 'no', 0.0)

