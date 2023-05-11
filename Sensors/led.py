import RPi.GPIO as GPIO
import time


class LedControl:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def blink(self, duration):
        self.turn_on()
        time.sleep(duration)
        self.turn_off()
        time.sleep(duration)