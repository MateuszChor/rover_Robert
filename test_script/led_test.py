import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   # Ustawienie trybu numeracji pinów
GPIO.setup(9, GPIO.OUT)   # Ustawienie pinu 11 jako wyjście

while True:
    GPIO.output(9, GPIO.HIGH)   # Ustawienie stanu "HIGH"
    time.sleep(5)                # Czekaj 5 sekund
    GPIO.output(9, GPIO.LOW)    # Ustawienie stanu "LOW"
    time.sleep(5)                # Czekaj kolejne 5 sekund