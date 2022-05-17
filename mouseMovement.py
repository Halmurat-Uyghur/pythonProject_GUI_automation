import time
import pyautogui

print(pyautogui.size())

time.sleep(3)
print(pyautogui.position())

# move the mouse over time
#pyautogui.moveTo(100,100,3)

# move the mouse relative to its current position
#pyautogui.moveRel(100,100,3)


#click
# pyautogui.click(100,100,3,3,button="left")
# pyautogui.click(200,200,3,3,button="right")
# pyautogui.rightClick()
# pyautogui.leftClick()
# pyautogui.doubleClick(200,200,3,3)
# pyautogui.tripleClick()
# pyautogui.click(1286,47,3)
#
# pyautogui.moveTo(986,527,3)
# pyautogui.scroll(2)


time.sleep(3)
pyautogui.moveTo(986,527,3)
pyautogui.mouseDown(986,527)
pyautogui.moveTo(1230,527,3)
pyautogui.mouseUp()
