import RPi.GPIO as GPIO
import threading
import time

"""
HC1 (E18, T23) | HC2 (E24, T25) | HC3 (E12, T16) 
HC4 (E20, T21) | HC5 (E22, T27) | HC6 (E17, T4)
"""
class HC_SR04_Thread(threading.Thread):
    def __init__(self, echo_pin, trig_pin):
        threading.Thread.__init__(self)
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin

        self.distance = 0
        self.running = False

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

        GPIO.output(self.trig_pin, False)
        time.sleep(2)

    def run(self):
        self.running = True

        while self.running:
            GPIO.output(self.trig_pin, True)
            time.sleep(0.00001)
            GPIO.output(self.trig_pin, False)

            while GPIO.input(self.echo_pin) == 0:
                pulse_start = time.time()

            while GPIO.input(self.echo_pin) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150
            self.distance = round(distance, 2)

            time.sleep(0.1)

    def get_distance(self):
        return self.distance

    def stop(self):
        self.running = False

    def __del__(self):
        GPIO.cleanup()