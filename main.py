import pyautogui
import keyboard
import time
import random
import pydirectinput

def start_button_click(selected_item):
    print("Start button clicked with selected item:", selected_item)
    find_character(selected_item)

def isAuto(auto_value):
    global auto
    auto = auto_value

def find_character(selected_item):
    while True:
        for s in selected_item:
            find = pyautogui.locateCenterOnScreen("./img/"+s+".png", region=(413, 900, 130, 25), confidence=0.6)
            if find != None:
                print(find)
                pyautogui.click(find[0]+100, find[1])
                pyautogui.mouseUp(button='left')
            find = pyautogui.locateCenterOnScreen("./img/"+s+".png", region=(576, 900, 130, 25), confidence=0.6)
            if find != None:
                print(find)
                pyautogui.click(find[0]+100, find[1])
                pyautogui.mouseUp(button='left')
            find = pyautogui.locateCenterOnScreen("./img/"+s+".png", region=(743, 900, 130, 25), confidence=0.6)
            if find != None:
                print(find)
                pyautogui.click(find[0]+100, find[1])
                pyautogui.mouseUp(button='left')
            find = pyautogui.locateCenterOnScreen("./img/"+s+".png", region=(912, 900, 130, 25), confidence=0.6)
            if find != None:
                print(find)
                pyautogui.click(find[0]+100, find[1])
                pyautogui.mouseUp(button='left')
            find = pyautogui.locateCenterOnScreen("./img/"+s+".png", region=(1082, 900, 130, 25), confidence=0.6)
            if find != None:
                print(find)
                pyautogui.click(find[0]+100, find[1])
                pyautogui.mouseUp(button='left')
        else:
            if auto:
                pydirectinput.keyDown('d')
                pydirectinput.keyUp('d')
