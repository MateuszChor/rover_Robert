from controll_gpio import motor, servo
from evdev import InputDevice, ecodes
from codes_dict import AXIS_CODE, BUTTON_CODE


class gamepad:

    def __init__(self):
        self.gamepad_device = InputDevice('/dev/input/event1')
        self.servo_17 = servo(17)
        self.motor = motor

    def motor_move(self, postion, value):
        """
        :param postion:
        :param postion vertical or horizontal:
        :return:
        """
        motor.pwm_speed(value)

        try:
            if postion == "horizontal":
                if value < 96:
                    print("left")
                    self.motor.turn_right()

                elif value > 146:
                    print("right")
                    self.motor.turn_left()
                else:
                    self.motor.stop()

            elif postion == "vertical":
                if value < 96:
                    print("forward")
                    self.motor.forward()

                elif value > 146:
                    print("backward")
                    self.motor.backward()
                else:
                    self.motor.stop()
        finally:
            pass
            # motor.stop()


    def servo_move(self, axis_name, value):
        if axis_name == "Right stick vertical":
            try:
                scaled_value = self.servo_17.pwm_speed(value)
                print(scaled_value)
                # TODO  make it simpler scale middle center
                if scaled_value.value < 110:
                    print("left servo")
                    self.servo_17.pwm_speed(value)
                elif scaled_value > 136:
                    print("right servo")
                    self.servo_17.pwm_speed(value)

                    self.servo_17.stop()
            finally:
                self.servo_17.stop()

    def run_loop(self):
        for event in self.gamepad_device.read_loop():

            if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                if event.code in BUTTON_CODE:
                    button_name = BUTTON_CODE[event.code]
                    # print(button_name + " " + ("pressed" if event.value else "released"))

                    if button_name == "Cross" and event.value == 1:
                        print(" press")
                        if event.code in AXIS_CODE:
                            axis_name = AXIS_CODE[event.code]
                            self.servo_move(AXIS_CODE)

                    elif button_name == "Cross" and event.value == 0:
                        print(" no press")

                elif event.code in AXIS_CODE:
                    axis_name = AXIS_CODE[event.code]

                    if axis_name == "Left stick vertical":
                        axis_name = AXIS_CODE[event.code]
                        motor.pwm_speed(event.value)
                        self.motor_move("vertical", event.value)

                    elif axis_name == "Right stick vertical":
                        axis_name = AXIS_CODE[event.code]
                        motor.pwm_speed(event.value)
                        self.motor_move("horizontal", event.value)

gamepad.run_loop