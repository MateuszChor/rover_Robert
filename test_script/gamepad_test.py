# import evdev
from evdev import InputDevice, categorize, ecodes

# Object store input data
gamepad = InputDevice('/dev/input/event1')

# Przypisz kody klawiszy do zmiennych
button_code = {
    304: "Triangle",
    305: "Circle",
    306: "Cross",
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

# Odczytywanie danych z kontrolera PS3
def all_position_print():
    for event in gamepad.read_loop():
        # Odczytaj dane typu "key" lub "absolute"
        if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
            # Konwertuj kod klawisza na jego nazwę
            if event.code in button_code:
                button_name = button_code[event.code]
                # Wydrukuj nazwę klawisza i stan (wciśnięty lub zwolniony)
                print(button_name + " " + ("pressed" if event.value else "released"))
            # Konwertuj kod osi na jego nazwę

            elif event.code in axis_code:
                axis_name = axis_code[event.code]
                # print(axis_name + " " + str(event.value))

                # przykład na left analog gora dol 0 - 255  (środek 129-130)
                if axis_name == "Right stick vertical":
                    # Wydrukuj nazwę osi analoga horizontal vertical
                    print(axis_name + " " + str(event.value))


all_position_print()