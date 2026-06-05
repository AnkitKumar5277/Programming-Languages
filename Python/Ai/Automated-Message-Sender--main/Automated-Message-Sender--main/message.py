# WARNING USE THIS VERY CAREFULL !
# CODE KO RUN KARNE K BAAD JHA MESSAGES BHEJNE HAI WHA CURSOR LE JAAYE
import pyautogui
from time import sleep
sleep(4)
message = "OK"
for i in range(1):
    pyautogui.typewrite(message)
    pyautogui.press('enter')
