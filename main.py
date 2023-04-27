from controll_gpio import motor, servo

from evdev import InputDevice, ecodes
from codes_dict import AXIS_CODE, BUTTON_CODE

gamepad = InputDevice('/dev/input/event1')

motor = motor()
servo_17 = servo(17)


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


def servo_move(axis_name, event):
    if axis_name == "Right stick vertical":
        print("servo_move")
        try:
            value = servo_17.pwm_speed(event.value)
            print(event.value)
            # TODO  make it simpler scale middle center
            if event.value < 110:
                print("left servo")
                servo_17.pwm_speed(value)
            elif event.value > 136:
                print("right servo")
                servo_17.pwm_speed(value)

            else:
                servo_17.center()
        finally:
            pass
            # servo_17.stop()


status_cross_button = 0

for event in gamepad.read_loop():

    if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
        if event.code in BUTTON_CODE:
            button_name = BUTTON_CODE[event.code]
            # print(button_name + " " + ("pressed" if event.value else "released"))

            if button_name == "Cross" and event.value == 1:
                print(" press")
                if event.code in AXIS_CODE:
                    print(" in if")
                    axis_name = AXIS_CODE[event.code]
                    servo_move(axis_name, event)
                    status_cross_button = 1

            elif button_name == "Cross" and event.value == 0:
                print(" no press")
                status_cross_button = 0

            if status_cross_button == 0:
                if event.code in AXIS_CODE:
                    axis_name = AXIS_CODE[event.code]

                    if axis_name == "Left stick vertical":
                        axis_name = AXIS_CODE[event.code]
                        motor.pwm_speed(event.value)
                        motor_move("vertical", event.value)

                    elif axis_name == "Right stick vertical":
                        axis_name = AXIS_CODE[event.code]
                        motor.pwm_speed(event.value)
                        motor_move("horizontal", event.value)
