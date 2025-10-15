
import pyautogui
import random
import time
import keyboard

# --- SETTINGS ---
x, y = 732, 960  # mouse coordinates (change this to your target spot)
phrases = [
    "w h",
    "w b",
    "w h ",
    "w cf 111",
    "w s 121"
]
intervals = [5, 7, 8, 10, 12, 13, 15]  # possible wait times in seconds
stop_key = "esc"

# --- LOOP ---
while True:
    if keyboard.is_pressed(stop_key):
        print("Stop key pressed. Exiting...")
        break
    
    # Step 1: click
    pyautogui.click(x, y)
    time.sleep(random.uniform(0.2, 0.5))  # small natural delay
    
    # Step 2: choose a random phrase and type it slowly
    phrase = random.choice(phrases)
    pyautogui.typewrite(phrase, interval=random.uniform(0.05, 0.15))  # human-like typing
    time.sleep(random.uniform(0.2, 0.5))
    
    # Step 3: press enter
    pyautogui.press("enter")
    time.sleep(random.uniform(0.2, 0.5))
    
    # Step 4: wait random interval before next loop
    wait_time = random.choice(intervals)
    print(f"Typed '{phrase}' | Waiting {wait_time}s...")
    time.sleep(wait_time)
