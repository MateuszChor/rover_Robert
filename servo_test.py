import RPi.GPIO as GPIO
import time

servo_pin_1 = 27  # GPIO pin, na którym podłączono pierwszy serwomechanizm
servo_pin_2 = 17  # GPIO pin, na którym podłączono drugi serwomechanizm
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin_1, GPIO.OUT)
GPIO.setup(servo_pin_2, GPIO.OUT)

servo_1 = GPIO.PWM(servo_pin_1, 50)  # Ustawienie częstotliwości sygnału PWM na 50 Hz
servo_2 = GPIO.PWM(servo_pin_2, 50)

servo_1.start(0)  # Uruchomienie sygnału PWM z wypełnieniem na poziomie 0%
servo_2.start(0)

try:
    while True:
        # Ustawienie kąta wychylenia serwomechanizmów w stopniach
        servo_1.ChangeDutyCycle(2.5)  # 0 stopni
        servo_2.ChangeDutyCycle(2.5)
        time.sleep(1)
        servo_1.ChangeDutyCycle(7.5)  # 90 stopni
        servo_2.ChangeDutyCycle(10)
        time.sleep(1)
        servo_1.ChangeDutyCycle(12.5)  # 180 stopni
        servo_2.ChangeDutyCycle(12.5)
        time.sleep(1)

except KeyboardInterrupt:
    servo_1.stop()  # Zatrzymanie sygnału PWM
    servo_2.stop()
    GPIO.cleanup()  # Zwolnienie zasobów GPIO