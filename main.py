from controll_gpio import motor, servo

from evdev import InputDevice, ecodes
from codes_dict import AXIS_CODE, BUTTON_CODE

gamepad = InputDevice('/dev/input/event1')
motor = motor()
servo_tilt_17 = servo(17, 40)
servo_rotate_27 = servo(27, 0)

def motor_move(postion, value):
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
                motor.turn_right()

            elif value > 146:
                print("right")
                motor.turn_left()
            else:
                motor.stop()

        elif postion == "vertical":
            if value < 96:
                print("forward")
                motor.forward()

            elif value > 146:
                print("backward")
                motor.backward()
            else:
                motor.stop()
    finally:
        pass
        # motor.stop()


def servo_move(servo, half=False):
    if event.value not in range(110, 135):
        servo.pwm_speed(event.value, half)
        # TODO  make it simpler scale middle center
    else:
        print("don't move with analog")

status_cross_button = False

for event in gamepad.read_loop():

    if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
        if event.code in BUTTON_CODE:
            button_name = BUTTON_CODE[event.code]
            # print(button_name + " " + ("pressed" if event.value else "released"))

            if button_name == "Cross" and event.value == 1:
                print(" press")

            elif button_name == "Cross" and event.value == 0:
                print(" no press")
                if not status_cross_button:
                    status_cross_button = True
                else:
                    status_cross_button = False

        if status_cross_button:
            if event.code in AXIS_CODE:
                axis_name = AXIS_CODE[event.code]
                if axis_name == "Right stick vertical":
                    servo_move(servo_rotate_27)
                elif axis_name == "Left stick vertical":
                    servo_move(servo_tilt_17, True)

        elif event.code in AXIS_CODE:
            axis_name = AXIS_CODE[event.code]

            if axis_name == "Left stick vertical":
                axis_name = AXIS_CODE[event.code]
                motor.pwm_speed(event.value)
                motor_move("vertical", event.value)

            elif axis_name == "Right stick vertical":
                axis_name = AXIS_CODE[event.code]
                motor.pwm_speed(event.value)
                motor_move("horizontal", event.value)
