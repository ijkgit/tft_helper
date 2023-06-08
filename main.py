import pyautogui
import keyboard
import time
import random
import pydirectinput

def start_button_click(selected_item, auto):
    print("Start button clicked with selected item:", selected_item, auto)
    find_character(selected_item, auto)

def find_character(selected_item, auto):
    while True:
        for s in selected_item:
            find = pyautogui.locateCenterOnScreen("./img/"+s+".png", region=(560, 940, 130, 50), confidence=0.65)
            if find != None:
                print(find)
                pyautogui.click(find[0]+50, find[1]-50)
                pyautogui.mouseUp(button='left')
            find = pyautogui.locateCenterOnScreen("./img/"+s+".png", region=(728, 940, 130, 50) , confidence=0.65)
            if find != None:
                print(find)
                pyautogui.click(find[0]+50, find[1]-50)
                pyautogui.mouseUp(button='left')
            find = pyautogui.locateCenterOnScreen("./img/"+s+".png", region=(895, 940, 130, 50), confidence=0.65)
            if find != None:
                print(find)
                pyautogui.click(find[0]+50, find[1]-50)
                pyautogui.mouseUp(button='left')
            find = pyautogui.locateCenterOnScreen("./img/"+s+".png", region=(1060, 940, 130, 50), confidence=0.65)
            if find != None:
                print(find)
                pyautogui.click(find[0]+50, find[1]-50)
                pyautogui.mouseUp(button='left')
            find = pyautogui.locateCenterOnScreen("./img/"+s+".png", region=(1230, 940, 130, 50), confidence=0.65)
            if find != None:
                print(find)
                pyautogui.click(find[0]+50, find[1]-50)
                pyautogui.mouseUp(button='left')
        else:
            if auto:
                pydirectinput.keyDown('d')
                pydirectinput.keyUp('d')
            else:
                break