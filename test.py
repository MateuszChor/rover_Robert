import evdev
import RPi.GPIO as GPIO

class PS3Controller:
    def __init__(self, device_path):
        self.device = evdev.InputDevice(device_path)
        self.left_stick_x = 0
        self.left_stick_y = 0
        self.right_stick_x = 0
        self.right_stick_y = 0
        self.buttons = {
            "cross": False,
            "circle": False,
            "triangle": False,
            "square": False,
            "l1": False,
            "l2": False,
            "r1": False,
            "r2": False,
            "select": False,
            "start": False,
            "left_stick": False,
            "right_stick": False,
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)

    def handle_event(self, event):
        if event.type == evdev.ecodes.EV_ABS:
            if event.code == evdev.ecodes.ABS_X:
                self.left_stick_x = event.value
            elif event.code == evdev.ecodes.ABS_Y:
                self.left_stick_y = event.value
            elif event.code == evdev.ecodes.ABS_RX:
                self.right_stick_x = event.value
            elif event.code == evdev.ecodes.ABS_RY:
                self.right_stick_y = event.value
        elif event.type == evdev.ecodes.EV_KEY:
            if event.code == evdev.ecodes.BTN_CROSS:
                self.buttons["cross"] = True if event.value == 1 else False
            elif event.code == evdev.ecodes.BTN_CIRCLE:
                self.buttons["circle"] = True if event.value == 1 else False
            elif event.code == evdev.ecodes.BTN_TRIANGLE:
                self.buttons["triangle"] = True if event.value == 1 else False
            elif event.code == evdev.ecodes.BTN_SQUARE:
                self.buttons["square"] = True if event.value == 1 else False
            elif event.code == evdev.ecodes.BTN_TL:
                self.buttons["l1"] = True if event.value == 1 else False
            elif event.code == evdev.ecodes.BTN_TR:
                self.buttons["r1"] = True if event.value == 1 else False
            elif event.code == evdev.ecodes.BTN_TL2:
                self.buttons["l2"] = True if event.value == 1 else False
                if event.value == 1:
                    GPIO.output(20, GPIO.HIGH)
                else:
                    GPIO.output(20, GPIO.LOW)
            elif event.code == evdev.ecodes.BTN_TR2:
                self.buttons["r2"] = True if event.value == 1 else False
                if event.value == 1:
                    GPIO.output(21, GPIO.HIGH)
                else:
                    GPIO.output(21, GPIO.LOW)
            elif event.code == evdev.ecodes.BTN_SELECT:
                self.buttons["select"] = True if event.value == 1 else False
            elif event.code == evdev.ecodes.BTN_START:
                self.buttons["start"] = True if event.value == 1 else False
