import tkinter as tk
from time import strftime
import pystray
from PIL import Image, ImageDraw
import threading
import pygame  # For playing MP3/WAV files
import os

# Initialize pygame mixer
pygame.mixer.init()

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the alarm sound file
alarm_sound_path = os.path.join(script_dir, "ჩუბინა.mp3")

# Function to update the time
def update_time():
    current_time = strftime("%H:%M:%S")
    time_label.config(text=current_time)
    check_alarm(current_time)  # Check if alarm time is reached
    time_label.after(1000, update_time)

# Function to check if the alarm time is reached
def check_alarm(current_time):
    if alarm_time.get() == current_time:
        play_alarm()

# Function to play the alarm sound
def play_alarm():
    try:
        pygame.mixer.music.load(alarm_sound_path)  # Load the alarm sound from the dynamic path
        pygame.mixer.music.play()  # Play the sound
        dismiss_button.config(state=tk.NORMAL)  # Enable the dismiss button
    except Exception as e:
        print(f"Error playing sound: {e}")

# Function to dismiss the alarm
def dismiss_alarm():
    pygame.mixer.music.stop()  # Stop the alarm sound
    dismiss_button.config(state=tk.DISABLED)  # Disable the dismiss button

# Function to create the system tray icon
def create_tray_icon():
    image = Image.new("RGB", (64, 64), "black")
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), "⏰", fill="white")  # Use a clock emoji or any icon

    menu = (
        pystray.MenuItem("Show Clock", show_window),
        pystray.MenuItem("Exit", exit_app),
    )

    icon = pystray.Icon("clock_tray", image, "Digital Clock", menu)
    icon.run()

# Function to show the clock window
def show_window(icon, item):
    icon.stop()  # Stop the tray icon
    root.deiconify()  # Restore the window

# Function to exit the application
def exit_app(icon, item):
    icon.stop()
    root.destroy()

# Hide the main window initially
def hide_window():
    root.withdraw()
    create_tray_icon()

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x250")  # Set window size
root.configure(bg="#f0f0f0")  # Light gray background for neumorphic effect
root.protocol("WM_DELETE_WINDOW", hide_window)  # Minimize to tray when closed

# Neumorphic styling
neumorphic_bg = "#f0f0f0"
neumorphic_highlight = "#ffffff"
neumorphic_shadow = "#d0d0d0"

# Create a frame for the clock
clock_frame = tk.Frame(root, bg=neumorphic_bg, bd=0, highlightthickness=0)
clock_frame.place(relx=0.5, rely=0.3, anchor="center")

# Create a label to display the time
time_label = tk.Label(clock_frame, font=("Helvetica", 48), bg=neumorphic_bg, fg="#333333")
time_label.pack(pady=10)

# Create a frame for the alarm input
alarm_frame = tk.Frame(root, bg=neumorphic_bg, bd=0, highlightthickness=0)
alarm_frame.place(relx=0.5, rely=0.6, anchor="center")

# Alarm time input
alarm_time = tk.StringVar()
alarm_label = tk.Label(alarm_frame, text="Set Alarm (HH:MM:SS):", font=("Helvetica", 12), bg=neumorphic_bg, fg="#333333")
alarm_label.grid(row=0, column=0, padx=5, pady=5)

alarm_entry = tk.Entry(alarm_frame, textvariable=alarm_time, font=("Helvetica", 12), bg=neumorphic_highlight, fg="#333333", bd=0, highlightthickness=2, highlightbackground=neumorphic_shadow)
alarm_entry.grid(row=0, column=1, padx=5, pady=5)

# Dismiss alarm button
dismiss_button = tk.Button(root, text="Dismiss Alarm", font=("Helvetica", 12), bg=neumorphic_highlight, fg="#333333", bd=0, highlightthickness=2, highlightbackground=neumorphic_shadow, state=tk.DISABLED, command=dismiss_alarm)
dismiss_button.place(relx=0.5, rely=0.8, anchor="center")

# Start updating the time
update_time()

# Run the application in a separate thread
tray_thread = threading.Thread(target=create_tray_icon, daemon=True)
tray_thread.start()

# Start the main loop
root.mainloop()
