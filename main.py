import RPI.GPIO as GPIO

# in1 orange
# in2 yellow
# in3 green
# in4 blue
# en bronze

in1 = 19
in2 = 13
in3 = 6
in4 = 5
en = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

GPIO.setup(in1, GPIO.LOW)
GPIO.setup(in2, GPIO.LOW)
GPIO.setup(in3, GPIO.LOW)
GPIO.setup(in4, GPIO.LOW)

pwn_mode = GPIO.PWM(en, 1000)

pwn_mode.start(25)
