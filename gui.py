import tkinter as tk
import main

def on_start_button_click():
    selected_items = []
    for checkbox_value, item in zip(checkbox_values, items):
        if checkbox_value.get():
            selected_items.append(item)
    main.start_button_click(selected_items)

def isAuto():
    main.isAuto(auto_value.get())

# 윈도우 생성
window = tk.Tk()
window.geometry("500x500")

# 아이템 추가
checkbox_values = []
items = ["lulu", "mal", "pan", "gank", "lee", "poppy", "ash", "blitz", "lucian", "vi"]
for item in items:
    checkbox_value = tk.BooleanVar()
    checkbox = tk.Checkbutton(window, text=item, variable=checkbox_value)
    checkbox.pack()
    checkbox_values.append(checkbox_value)

# 시작 버튼 생성
start_button = tk.Button(window, text="Start", command=on_start_button_click)
start_button.pack()

# 오토 리롤
auto_value = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="auto d", variable=auto_value)
checkbox.pack()
checkbox_values.append(auto_value)

# 윈도우 실행
window.mainloop()
