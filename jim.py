import pyautogui
import time

print("Move your mouse to the target spot... (Ctrl+C to quit)")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse position: X={x}, Y={y}", end="\r")  # updates in place
        time.sleep(0.2)  # update every 0.2 sec
except KeyboardInterrupt:
    print("\nStopped.")
