# &/xZ
# Site: https://m.joguix.com/jogar/piano-tiles-2-online/
# Personal Record: 1962
import pyautogui
import time
import keyboard
import win32api, win32con

def click():
    for i in range(4):
        if pyautogui.pixel(rec_px[i], 600)[0] == 0:
            win32api.SetCursorPos((rec_px[i], 600)) 
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.01) # Time is necessary cause it confirm the "click"
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

i = 0
# Pixels on the screen
rec_px = [760, 920, 1050, 1200]
while i == 0:
    # s is the ket to start
    if keyboard.is_pressed('s') == True:
        close = False
        while close == False:
            try:
                click()
            # If it cant click, try again
            except OSError:
                click()

            # q is the key to close
            if keyboard.is_pressed('q') == True:
                close = True
                i = 1
                                       

