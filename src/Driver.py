#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

Dir_forward     = 0
Dir_backward    = 1

left_forward    = 0
left_backward   = 1

right_forward   = 0
right_backward  = 1

left_engine = 0
right_engine = 1

class Engine:
    def __init__(self, en, pin1, pin2) -> None:
        self.en = en
        self.pin1 = pin1
        self.pin2 = pin2
        self.pwm = 0

    def start(self):
        GPIO.output(self.en, GPIO.OUT)
        GPIO.output(self.pin1, GPIO.OUT)
        GPIO.output(self.pin2, GPIO.OUT)

    def stop(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
        GPIO.output(self.en, GPIO.LOW)

    def activePWM(self):
        self.pwm = GPIO.PWM(self.en, 1000)

    @property
    def PMW(self):
        return self.pwm

class Driver:
    def __init__(self) -> None:
        self.right_engine = Engine(4, 14, 15)
        self.left_engine = Engine(17, 27, 18)

    def launch(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.right_engine.start()
        self.left_engine.start()
        self.shutdown()
        try:
            self.right_engine.activePWM()
            self.left_engine.activePWM()
        except:
            pass

    def shutdown(self):
        self.right_engine.stop()
        self.right_engine.stop()

    def motorRight(self, status, direction, speed):
        if status == 0:
            self.right_engine.stop()
        elif direction == Dir_forward:
            GPIO.output(self.right_engine.pin1, GPIO.HIGH)
            GPIO.output(self.right_engine.pin2, GPIO.LOW)
            self.right_engine.PMW.start(100)
            self.right_engine.PMW.ChangeDutyCycle(speed)
        elif direction == Dir_backward:
            GPIO.output(self.right_engine.pin1, GPIO.LOW)
            GPIO.output(self.right_engine.pin2, GPIO.HIGH)
            self.right_engine.PMW.start(0)
            self.right_engine.PMW.ChangeDutyCycle(speed)
        return direction

    def motorLeft(self, status, direction, speed):
        if status == 0:
            self.left_engine.stop()
        elif direction == Dir_backward:
            GPIO.output(self.left_engine.pin1, GPIO.HIGH)
            GPIO.output(self.left_engine.pin2, GPIO.LOW)
            self.left_engine.PMW.start(100)
            self.left_engine.PMW.ChangeDutyCycle(speed)
        elif direction == Dir_forward:
            GPIO.output(self.left_engine.pin1, GPIO.LOW)
            GPIO.output(self.left_engine.pin2, GPIO.HIGH)
            self.left_engine.PMW.start(0)
            self.left_engine.PMW.ChangeDutyCycle(speed)
        return direction

    def move(self, speed, direction, turn, radius=0.6):
        match(direction):
            case 'forward':
                if turn == 'right':
                    self.motorLeft(0, left_forward, int(speed*radius))
                    self.motorRight(1, right_backward, speed)
                elif turn == 'left':
                    self.motorLeft(1, left_backward, speed)
                    self.motorRight(0, right_forward, int(speed*radius))
                else:
                    self.motorLeft(1, left_backward, speed)
                    self.motorRight(1, right_backward, speed)

            case 'backward':
                if turn == 'right':
                    self.motorLeft(0, left_backward, int(speed*radius))
                    self.motorRight(1, right_forward, speed)
                elif turn == 'left':
                    self.motorLeft(1, left_forward, speed)
                    self.motorRight(0, right_backward, int(speed*radius))
                else:
                    self.motorLeft(1, left_forward, speed)
                    self.motorRight(1, right_forward, speed)

            case 'no':
                if turn == 'right':
                    self.motorLeft(1, left_backward, speed)
                    self.motorRight(1, right_forward, speed)
                elif turn == 'left':
                    self.motorLeft(1, left_forward, speed)
                    self.motorRight(1, right_backward, speed)
                else:
                    self.motorStop()

            case _: pass

    def destroy(self):
        self.shutdown()
        GPIO.cleanup()
