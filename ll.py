import pyautogui
import time
import keyboard  # Library to detect key presses

# Toggle state
toggle = False

print("Press F2 to start/stop the down arrow key presses.")

while True:
    # Toggle on/off with F2
    if keyboard.is_pressed('F2'):
        toggle = not toggle
        if toggle:
            print("Started pressing the down arrow key.")
        else:
            print("Stopped pressing the down arrow key.")
        time.sleep(0.5)  # Debounce to avoid multiple toggles

    # If toggled on, press the down arrow key
    if toggle:
        pyautogui.press('down')
        time.sleep(0.3)  # Wait for 1.5 seconds
