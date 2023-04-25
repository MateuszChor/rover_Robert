import keyboard

def on_w_press():
    print("Klawisz 'w' został naciśnięty!")

keyboard.on_press_key("w", on_w_press)

# Zatrzymanie programu
keyboard.wait()
