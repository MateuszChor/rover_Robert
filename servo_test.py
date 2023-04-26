import RPi.GPIO as GPIO
from time import sleep

# servo 1 16
# servo 2 20

GPIO.setmode(GPIO.BOARD)
GPIO.setup(20, GPIO.OUT)


pwm=GPIO.PWM(20, 50)
pwm.start(0)


pwm.ChangeDutyCycle(5) # left -90 deg position
sleep(1)
pwm.ChangeDutyCycle(7.5) # neutral position
sleep(1)
pwm.ChangeDutyCycle(10) # right +90 deg position
sleep(1)

pwm.stop()
GPIO.cleanup()


