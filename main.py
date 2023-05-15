from controll_gpio import motor
from Servo.Servo_class import PCA9685
from Sensors.distan_sensors import HC_SR04_Thread
from Sensors.led import LedControl
from evdev import InputDevice, ecodes
from codes_dict import AXIS_CODE, BUTTON_CODE

# TODO FileNotFoundError:[Errno 2] No such file or directory:'/dev/input/event1' handle power off ps3 pad on start error
gamepad = InputDevice('/dev/input/event1')
motor = motor()

camera_led = LedControl(9)

servo_claws_id = 0

Servo_hat = PCA9685(0x40, debug=False)
Servo_hat.setPWMFreq(50)

hc_sensor1 = HC_SR04_Thread(18, 23)
hc_sensor1.start()

status_cross_button = False
status_circle_button = False
status_triangle_button = False


def motor_move(position, value):
    """
    :str(horizontal or vertical) position:
    :int value
    """

    try:
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


for event in gamepad.read_loop():

    distance = hc_sensor1.get_distance()
    print("distance from hcr sensor : ", distance)

    if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
        if event.code in BUTTON_CODE:
            button_name = BUTTON_CODE[event.code]
            # print(button_name + " " + ("pressed" if event.value else "released"))

            if button_name == "Cross" and event.value == 0:
                print("cross no press")
                if not status_cross_button:
                    status_cross_button = True
                else:
                    status_cross_button = False

            elif button_name == "Circle" and event.value == 0:
                print("circle no press")
                # camera_led.turn_off()
                if not status_circle_button:
                    status_circle_button = True
                else:
                    status_circle_button = False

            elif button_name == "Triangle" and event.value == 0:
                print("Triangle no press")
                if not status_triangle_button:
                    status_triangle_button = True
                else:
                    status_triangle_button = False

        if status_circle_button:
            camera_led.turn_on()

        elif not status_circle_button:
            camera_led.turn_off()

        if status_cross_button:
            if event.code in AXIS_CODE:
                axis_name = AXIS_CODE[event.code]
                if axis_name == "Right stick vertical":
                    print("status servo claw move value is = :")
                    value = event.value * 9.5
                    print(value)
                    Servo_hat.setServoPulse(3, value)
                elif axis_name == "Left stick vertical":
                    print("status servo claw move value is = :")
                    value = event.value * 9.5
                    print(value)
                    Servo_hat.setServoPulse(2, value)

        elif status_triangle_button:
            if event.code in AXIS_CODE:
                axis_name = AXIS_CODE[event.code]
                if axis_name == "Right stick vertical":
                    print("status servo claw move value is = :")
                    value = event.value * 19
                    print(value)

                    if 0 < value < 2500:
                        Servo_hat.setServoPulse(servo_claws_id, value)

                elif axis_name == "Left stick vertical":
                    print("status servo claw move value is = :")
                    value = event.value * 9.5
                    print(value)
                    Servo_hat.setServoPulse(1, value)

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
