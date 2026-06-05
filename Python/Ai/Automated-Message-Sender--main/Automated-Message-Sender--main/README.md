pyautogui module ko import karta hai.
time module se sleep function ko import karta hai.
4 seconds ke liye wait karta hai using sleep(4).
Ek variable message define karta hai jiska value "OK" hai.
Ek loop chalata hai (ye loop sirf ek baar run hota hai isliye loop thoda redundant hai).
pyautogui.typewrite(message) ka use karke "OK" type karta hai.
pyautogui.press('enter') ka use karke "Enter" key press karta hai.
Toh, yeh script 4 seconds wait karegi aur phir "OK" type karegi aur "Enter" key press karegi.
