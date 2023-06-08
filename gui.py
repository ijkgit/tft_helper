import tkinter as tk
import main

def on_start_button_click():
    selected_items = []
    for checkbox_value, item in zip(checkbox_values, items):
        if checkbox_value.get():
            selected_items.append(item)
    main.start_button_click(selected_items, auto_value.get())

# 윈도우 생성d
window = tk.Tk()
window.geometry("500x500")

# 프레임 생성
frame = tk.Frame(window)
frame.pack()

# 체크박스와 텍스트를 묶은 프레임 생성
checkbox_text_frame = tk.Frame(frame)
checkbox_text_frame.pack(side="left")

# "우세 룰루덱" 텍스트 생성
text_label = tk.Label(checkbox_text_frame, text="우세 룰루덱")
text_label.pack()

# 우세 룰루덱
checkbox_values = []
items = ["lulu", "mal", "pan", "gank", "lee"]
for item in items:
    checkbox_value = tk.BooleanVar()
    checkbox = tk.Checkbutton(checkbox_text_frame, text=item, variable=checkbox_value)
    checkbox.pack(side="left")
    checkbox_values.append(checkbox_value)

# # 1코스트 프레임 생성
# frame = tk.Frame(window)
# frame.pack()

# # 체크박스와 텍스트를 묶은 프레임 생성
# checkbox_text_frame = tk.Frame(frame)
# checkbox_text_frame.pack(side="left")

# # "우세 룰루덱" 텍스트 생성
# text_label = tk.Label(checkbox_text_frame, text="우세 룰루덱")
# text_label.pack()

# # 나머지 1코스트들
# checkbox_values = []
# items = ["poppy", "ash", "blitz", "lucian", "vi"]
# for item in items:
#     checkbox_value = tk.BooleanVar()
#     checkbox = tk.Checkbutton(checkbox_text_frame, text=item, variable=checkbox_value)
#     checkbox.pack(side="left")
#     checkbox_values.append(checkbox_value)

# 시작 버튼 생성
start_button = tk.Button(window, text="Start", command=on_start_button_click)
start_button.pack()

# 오토 리롤 체크 박스
auto_value = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="auto d", variable=auto_value)
checkbox.pack()
checkbox_values.append(auto_value)

# 50 keep 체크 박스
# auto_value = tk.BooleanVar()
# checkbox = tk.Checkbutton(window, text="50 keep", variable=)
# checkbox.pack()
# checkbox_values.append(auto_value)

# 윈도우 실행
window.mainloop()