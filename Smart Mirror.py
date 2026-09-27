import tkinter as tk
from datetime import datetime
import random

# Create window
root = tk.Tk()
root.title("Smart Mirror")
root.configure(bg="black")
root.attributes("-fullscreen", True)

# Time display
time_label = tk.Label(
    root,
    font=("Arial", 60),
    fg="white",
    bg="black"
)
time_label.pack(pady=40)

# Date display
date_label = tk.Label(
    root,
    font=("Arial", 30),
    fg="white",
    bg="black"
)
date_label.pack()

# Temperature display
temperature_label = tk.Label(
    root,
    font=("Arial", 25),
    fg="white",
    bg="black"
)
temperature_label.pack(pady=30)

# Welcome message
welcome_label = tk.Label(
    root,
    text="Good Day! Welcome to Smart Mirror",
    font=("Arial", 25),
    fg="white",
    bg="black"
)
welcome_label.pack(pady=20)


def update_display():
    # Get current time and date
    now = datetime.now()

    time_label.config(
        text=now.strftime("%H:%M:%S")
    )

    date_label.config(
        text=now.strftime("%A, %d %B %Y")
    )

    # Demo temperature
    temperature = random.randint(25, 35)

    temperature_label.config(
        text=f"Temperature: {temperature} °C"
    )

    # Update every second
    root.after(1000, update_display)


# Start program
update_display()

root.mainloop()
