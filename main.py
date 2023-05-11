from controll_gpio import motor, servo
from Sensors.distan_sensors import HC_SR04_Thread
from evdev import InputDevice, ecodes
from codes_dict import AXIS_CODE, BUTTON_CODE

# TODO FileNotFoundError: [Errno 2] No such file or directory: '/dev/input/event1' handle power off ps3 pad on start error
gamepad = InputDevice('/dev/input/event1')
motor = motor()
servo_tilt_17 = servo(17, 40)
servo_rotate_27 = servo(27, 0)

hc_sensor1 = HC_SR04_Thread(18, 23)
hc_sensor1.start()

def motor_move(position, value):
    """
    :str(horizontal or vertical) position:
    :int value
    """

    try:
        distance = hc_sensor1.get_distance()
        print(distance)
        if position == "horizontal":
            if value < 96:
                print("left")
                motor.pwm_speed(value)
                motor.turn_right()

            elif value > 146:
                print("right")
                motor.pwm_speed(value)
                motor.turn_left()
            else:
                motor.stop()

        elif position == "vertical":
            if value < 96:
                print("forward")
                motor.pwm_speed(value)
                motor.forward()

            elif value > 146:
                print("backward")
                motor.pwm_speed(value)
                motor.backward()
            else:
                motor.stop()
    finally:
        pass
        # motor.stop()


def servo_move(servo_object, sleep_position):
    if event.value not in range(96, 146):
        scaled_value = servo_object.pwm_speed(event.value)
        # TODO  make it simpler scale middle center
        servo_object.set_angle(scaled_value)

    else:
        print("don't move with analog")

        if sleep_position == "center":
            servo_object.center()
            print("center")

        elif sleep_position == "max":
            print("max")
            servo_object.max_value()

        elif sleep_position == "min":
            print("min")
            servo_object.min_value()

        else:
            pass


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
                    servo_move(servo_rotate_27, "center", )
                elif axis_name == "Left stick vertical":
                    pass
                    servo_move(servo_tilt_17, "min")

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

hc_sensor1.stop()
hc_sensor1.join()
