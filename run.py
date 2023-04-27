from evdev import InputDevice, ecodes

gamepad = InputDevice('/dev/input/event1')

def for_loop_events():
    for event in gamepad.read_loop():

        print(event)

        # print(event.code)

        # print(event.type)

        # print(ecodes)
