

"""
import pyautogui


import time

# Set initial target coordinates
target_x, target_y = 500, 500

# Perform the initial click and drag
pyautogui.mouseDown()

while True:
    # Update target coordinates (you can replace this with your own logic)
    target_x += 10
    target_y += 10

    # Move to the new coordinates without releasing left click
    pyautogui.moveTo(target_x, target_y, duration=0.0)

    # Add a delay to control the speed of the dragging
    time.sleep(0)
"""