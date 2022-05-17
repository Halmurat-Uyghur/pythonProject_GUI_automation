import pyautogui
import time
import threading


def mouseHoldDown():
    global distance
    while distance > 0:
        pyautogui.mouseDown()
    if distance == 0:
        time.sleep(1)
        pyautogui.mouseUp()


def movingSpiralMouse():
    global distance
    change = 20
    while distance > 0:
        pyautogui.move(distance, 0, duration=0.25)
        distance = distance - change
        pyautogui.move(0, distance, duration=0.25)
        pyautogui.move(-distance, 0, duration=0.25)
        distance = distance - change
        pyautogui.move(0, -distance, duration=0.25)


distance = 300
time.sleep(5)

mouseObj = threading.Thread(target=mouseHoldDown)
mouseObj.start()

moveObj = threading.Thread(target=movingSpiralMouse)
moveObj.start()