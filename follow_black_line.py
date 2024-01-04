import time
import RPi.GPIO as GPIO

line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20

motor_pin_right = 21
motor_pin_left = 26

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(line_pin_right, GPIO.IN)
    GPIO.setup(line_pin_middle, GPIO.IN)
    GPIO.setup(line_pin_left, GPIO.IN)
    GPIO.setup(motor_pin_right, GPIO.OUT)
    GPIO.setup(motor_pin_left, GPIO.OUT)

def run():
    status_right = GPIO.input(line_pin_right)
    status_middle = GPIO.input(line_pin_middle)
    status_left = GPIO.input(line_pin_left)

    if status_right == 0 and status_middle == 0 and status_left == 0:
        # Les capteurs ne détectent pas la ligne, arrêt du mouvement
        stop()
    elif status_right == 1 and status_middle == 0 and status_left == 1:
        # Suivre la ligne tout droit
        forward()
    elif status_right == 1 and status_middle == 1 and status_left == 0:
        # Tourner légèrement à gauche
        turn_left()
    elif status_right == 0 and status_middle == 1 and status_left == 1:
        # Tourner légèrement à droite
        turn_right()
    elif status_right == 0 and status_middle == 1 and status_left == 0:
        # Suivre la ligne tout droit
        forward()
    else:
        # Cas d'erreur ou de situation inattendue, arrêt du mouvement
        stop()

def forward():
    GPIO.output(motor_pin_right, GPIO.HIGH)
    GPIO.output(motor_pin_left, GPIO.HIGH)

def turn_left():
    GPIO.output(motor_pin_right, GPIO.HIGH)
    GPIO.output(motor_pin_left, GPIO.LOW)

def turn_right():
    GPIO.output(motor_pin_right, GPIO.LOW)
    GPIO.output(motor_pin_left, GPIO.HIGH)

def stop():
    GPIO.output(motor_pin_right, GPIO.LOW)
    GPIO.output(motor_pin_left, GPIO.LOW)

if __name__ == '__main__':
    try:
        setup()
        while True:
            run()
            time.sleep(0.2)
    except KeyboardInterrupt:
        stop()
        GPIO.cleanup()
