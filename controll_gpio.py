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
        self.pwm_motor = GPIO.PWM(self.en, 1000)
        self.pwm_motor.start(0)

    def pwm_speed(self, value):
        """
        get pwn value and scale it for analog stick
        :param pwm value:
        :return scaled pvn value:
        get pwm value and scale it to analog stick
        """

        # print(value)
        scaled_value = int(value / 255)
        #print(scaled_value)

        if scaled_value < 50:
            scaled_value = 100 - scaled_value
            self.pwm_motor.ChangeDutyCycle(scaled_value)
            #print("2 way ", scaled_value)
        else:
            self.pwm_motor.ChangeDutyCycle(scaled_value)

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
        # GPIO.cleanup()


class servo:
    # TODO try to use pydantic to build class
    def __init__(self, pin):
        self.pin = pin
        self.pwm = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.servo_pin = pin
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.pwm_servo = GPIO.PWM(self.servo_pin, 50)
        self.pwm_servo.start(25)

    def pwm_speed(self, value):
        """
        get pwn value and scale it for analog stick
        :param pwm value:
        """

        # 255/12.5 = 20.4

        scaled_value = float(value / 20.4)
        print("pwm speed controll gpio scaled value ",scaled_value)



        if scaled_value < 6:
            scaled_value = 12.5 - scaled_value
            self.pwm_servo.ChangeDutyCycle(scaled_value)
            print(scaled_value)

        elif scaled_value > 6.5:
            self.pwm_servo.ChangeDutyCycle(scaled_value)
            print(scaled_value)

        else:
            pass
    def move_servo(self, value):
        """
        get scaled value and set servo on this value
        :param scaled value:
        """
        # self.pwn_servo.ChangeDutyCycle(value)
        pass

    def center(self):
        self.pwm_servo.ChangeDutyCycle(6)

    def clean_gpio(self):
        GPIO.clenup()
