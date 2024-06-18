import pyautogui
import time

pyautogui.alert('O código vai começar, não pressione nenhum botão!')
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('Opera')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/u/1/folders/1CoWVba0XU3pcC8eXuQcsp9H2cjyRNynp')
pyautogui.press('enter')

pyautogui.hotkey('win', 'd')
pyautogui.moveTo(x=1304, y=52)
pyautogui.mouseDown()
pyautogui.moveTo(x=717, y=512)
pyautogui.hotkey('alt', 'tab')
pyautogui.mouseUp()
time.sleep(5)
pyautogui.alert('O código terminou de rodar, pode usar seu computador denovo!')
