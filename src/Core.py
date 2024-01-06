#!/usr/bin/env python3

from src.Driver import Driver
from src.Sensor import Sensor

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

        self.driver.move(70, 'no', 'left', 0.8)

        # if left:
        #     self.driver.move(70, 'no', 'left', 0.8)
        #     self.rot = 'left'
        # if right:
        #     self.driver.move(70, 'no', 'right', 0.8)
        #     self.rot = 'right'
        # if middle:
        #     self.driver.move(20, 'forward', 'no', 0.8)
        # if right == 0 and middle == 0 and left == 0:
        #     self.driver.move(20, 'no', self.rot, 0.8)
            # self.driver.move(50, 'backward', 'no', 0.8)
        print(right, middle, left, self.rot)
