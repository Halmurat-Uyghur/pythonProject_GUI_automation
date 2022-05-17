import pyautogui
import time

time.sleep(5)  # give time to go to paint app
distance = 300
change = 20
pyautogui.mouseDown()

while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5, button='left')
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.5, button='left')
    pyautogui.drag(-distance, 0, duration=0.5, button='left')
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.5, button='left')

if distance < 0:
    pyautogui.mouseUp()