import RPi.GPIO as GPIO

# 15.53
# power battery 10.95 V

# 16.16
# power battery 10.77 V

from evdev import InputDevice, categorize, ecodes

# Object store input data
gamepad = InputDevice('/dev/input/event1')

# Przypisz kody klawiszy do zmiennych
button_code = {
    304: "Cross",
    305: "Circle",
    306: "Triangle",
    307: "Square",
    308: "Left bumper",
    309: "Right bumper",
    310: "Left trigger",
    311: "Right trigger",
    314: "Select",
    315: "Start",
    316: "Left stick button",
    317: "Right stick button",
    318: "PlayStation button",
    319: "Touchpad button"
}

# Przypisz kody osi analogowych do zmiennych
axis_code = {
    0: "Left stick horizontal",
    1: "Left stick vertical",
    2: "Right stick horizontal",
    3: "Right stick vertical",
    16: "DPad horizontal",
    17: "DPad vertical"
}


# in1 orange
# in2 yellow
# in3 green
# in4 blue
# en bronze

in1 = 19
in2 = 13
in3 = 6
in4 = 5
en = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

pwn_mode = GPIO.PWM(en, 1000)

pwn_mode.start(25)


for event in gamepad.read_loop():
    # Odczytaj dane typu "key" lub "absolute"
    if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
        # Konwertuj kod klawisza na jego nazwę
        if event.code in button_code:
            button_name = button_code[event.code]

            # print(button_name + " " + ("pressed" if event.value else "released"))

            if button_name == "Cross" and event.value == 1:
                print(" press")
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in3, GPIO.HIGH)

            elif button_name == "Cross" and event.value == 0:
                print(" no press")
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in3, GPIO.LOW)

        elif event.code in axis_code:
            axis_name = axis_code[event.code]

            if axis_name == "Left stick vertical" and event.value == 0:
                print("gora")
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in3, GPIO.HIGH)

            if axis_name == "Left stick vertical" and event.value == 255:
                print("dol")
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in3, GPIO.LOW)




