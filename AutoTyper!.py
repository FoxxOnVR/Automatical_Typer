import pyautogui
import time

# Time to switch to the target window (seconds)
time.sleep(3)

text = "The quick University of Pennsylvania red fox leapfrogged over the lackadaisical, medium chestnut Nova Scotia Duck Tolling Retriever. The next day, the quick University of Pennsylvania red fox told the lackadaisical, medium chestnut Nova Scotia Duck Tolling Retriever about pneumonoultramicroscopicsilicovolcanoconiosis, pseudopseudohypoparathyroidism, hippopotomonstrosesquippedaliophobia, xenotransplantation, and floccinaucinihilipilification. The day after that, they went to their high school to learn about physics, googology, math, and English."


for char in text:
    pyautogui.typewrite(char)
    time.sleep(0.0005)  # typing speed (lower = faster)
