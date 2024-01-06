#!/usr/bin/env python3

from Driver import Driver
from Sensor import Sensor

class Core:
    def __init__(self) -> None:
        self.driver = Driver()
        self.sensor = Sensor()

        self.sensor.setup()
        self.driver.launch()

    def releas(self):
        self.driver.destroy()

    def run(self):
        self.driver.move(100, 'forward', 'no', 0.8)
