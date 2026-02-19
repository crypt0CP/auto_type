import pyautogui
import time



pyautogui.FAILSAFE = False

for i in range(0, 1000):
    time.sleep(0.01)
    pyautogui.typewrite('zswd')
    time.sleep(0.01)
    pyautogui.press('enter')
    time.sleep(0.01)
