import RPi.GPIO as GPIO


class motor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.in1 = 19
        self.in2 = 13
        self.in3 = 6
        self.in4 = 5
        self.en = 26
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)
        GPIO.setup(self.en, GPIO.OUT)
        self.pwm = GPIO.PWM(self.en, 1000)

    def pwm_speed(self, value):
        """
        get pwn value and scale it for analog stick
        :param pwm value:
        :return scaled pvn value:
        get pwm value and scale it to analog stick
        """
        scaled_value = int(value / 2.55)
        print(scaled_value)

        if scaled_value < 50:
            scaled_value = 100 - scaled_value
            self.pwm.start(scaled_value)
            print(scaled_value)
            return scaled_value
        else:
            self.pwm.start(scaled_value)
            return scaled_value

    def forward(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)

    def backward(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)

    def turn_right(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)

    def turn_left(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
