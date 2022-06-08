import time

import pyautogui


pyautogui.PAUSE = 0.5
pyautogui.hotkey('win', 'd')
pyautogui.press('win')
pyautogui.write('note', 0.02)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('hello', 0.02)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write(['\t', '\t', '\t', '\t', '\t', '\t', 'enter'], 0.02)
time.sleep(1)
pyautogui.write('Desktop', 0.02)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write(['\t', '\t', '\t', '\t', '\t'], 0.02)
pyautogui.write('green.txt')
pyautogui.write(['\t', '\t', '\t', '\t', 'enter'], 0.02)
pyautogui.hotkey('alt', 'f4')