import pyautogui
import keyboard
import time
import random
import pydirectinput

def start_button_click(selected_item, auto):
    print("Start button clicked with selected item:", selected_item, auto)
    find_character(selected_item, auto)

def image_search(s, x, y, width, height):
    find = pyautogui.locateCenterOnScreen("./img/"+s+".png", region=(x, y, width, height), confidence=0.7)
    if find != None:
        print(find)
        pyautogui.click(find[0]+50, find[1]-50)
        pyautogui.mouseUp(button='left')

def find_character(selected_item, auto):
    w = 50
    h = 25
    while True:
        for s in selected_item:
            image_search(s, 560, 950, w, h)
            image_search(s, 728, 950, w, h)
            image_search(s, 895, 950, w, h)
            image_search(s, 1060, 950, w, h)
            image_search(s, 1230, 950, w, h)
        else:
            if auto:
                pydirectinput.keyDown('d')
                pydirectinput.keyUp('d')
            else:
                break