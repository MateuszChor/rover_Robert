import RPi.GPIO as GPIO


class servo:

    # TODO try to use pydantic to build class

    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.servo_pin = 17
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.pwn_servo = GPIO.PWM(self.servo_pin, 50)
        self.pwn_servo.start(0)

    def pwm_speed(self, value):
        """
        get pwn value and scale it for analog stick
        :param pwm value:
        """

        # 255/12.5 = 20.4

        scaled_value = int(value / 20.4)
        # print(scaled_value)

        if scaled_value < 6:
            scaled_value = 12 - scaled_value
            print(scaled_value)
            self.pwm.ChangeDutyCycle(scaled_value)

        else:
            self.pwm.ChangeDutyCycle(scaled_value)
            print(scaled_value)

    def move_servo(self, value):
        """
        get scaled value and set servo on this value
        :param sclaed value:
        """
        self.pwn_servo.ChangeDutyCycle(value)

    def stop(self):
        pass

    # servo = servo()
#
# print(servo.pwn_scale_servo(130))
