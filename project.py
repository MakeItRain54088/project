import os
import csv
import cv2
from PIL import Image, ImageTk

import tkinter as tk
from clock import start_clock_page
from picture import create_camera_page, cleanup_camera

# 初始化主視窗
root = tk.Tk()
root.title('健身菜單')
root.geometry('800x600+300+50')
root.resizable(False, False)
root.configure(background='skyblue')

# 切換頁面的frame
page_frame = tk.Frame(root, bg="skyblue")
page_frame.place(relwidth=0.8125, relheight=1, x=150)

def switch_to_clock():
    """切換到倒數計時頁面"""
    start_clock_page(page_frame)  # 調用 clock.py 的頁面函式

# 主頁面
def home_page():
    for i in page_frame.winfo_children():
        i.destroy()

    home_page_frame = tk.Frame(page_frame, bg="skyblue")

    title = tk.Label(home_page_frame, text="健身菜單", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    label1 = tk.Label(home_page_frame, text="根據你的需求設計一套合適的訓練菜單", font=("微軟正黑體", 15, "bold"), bg="skyblue", fg="black")
    label1.pack(fill=tk.X)
    label2 = tk.Label(home_page_frame, text="選擇訓練菜單", font=("微軟正黑體", 15, "bold"), bg="skyblue", fg="black")
    label2.place(relx=0.4, rely=0.25)
    
    optionlist = ['A','B','C','D','E']
    option_value = tk.StringVar()
    option_value.set("請選擇")
    option = tk.OptionMenu(home_page_frame, option_value, *optionlist)
    option.config(width=24, font=("微軟正黑體", 15, "bold"), bg="white", fg="black")
    option.place(relx=0.25, rely=0.3)

    add_option = tk.Button(home_page_frame, text="新增其他菜單", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", height=1, width=15)
    add_option.place(relx=0.35, rely=0.4)

    start = tk.Button(home_page_frame, text="開始訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", height=2, width=15, command=switch_to_clock)
    start.place(relx=0.35, rely=0.7)

    home_page_frame.pack(fill="both", expand=1)

def part1_page():
    def show_illustration(illustration):
        for widget in page_frame.winfo_children():
            widget.destroy()

        illustration_frame = tk.Frame(page_frame, bg="skyblue")
        title = tk.Label(illustration_frame, text="訓練內容", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
        title.pack(fill=tk.X, pady=10)

        illustration_label = tk.Label(illustration_frame, text=illustration, font=("微軟正黑體", 15), bg="skyblue", fg="black", wraplength=600)
        illustration_label.pack(pady=20)

        back_button = tk.Button(illustration_frame, text="返回", font=("微軟正黑體", 15, "bold"), bg="white", fg="black",
                                command=part1_page)  # 返回主頁
        back_button.pack(pady=10)

        illustration_frame.pack(fill="both", expand=1)
    
    for widget in page_frame.winfo_children():
        widget.destroy()


    part1_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part1_page_frame, text="胸部訓練", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    csv_file = "training_chest.csv"
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    continue
                button_name, illustration, website, sec = row
                button = tk.Button(part1_page_frame, text=button_name, font=("微軟正黑體", 15, "bold"),
                                   bg="white", fg="black", width=20,
                                   command=lambda a=illustration: show_illustration(a))
                button.pack(pady=5)
    except FileNotFoundError:
        error_label = tk.Label(part1_page_frame, text="找不到 CSV 檔案", font=("微軟正黑體", 15, "bold"), bg="skyblue", fg="red")
        error_label.pack(pady=20)

    part1_page_frame.pack(fill="both", expand=1)

def part2_page():
    def show_illustration(illustration):
        for widget in page_frame.winfo_children():
            widget.destroy()

        illustration_frame = tk.Frame(page_frame, bg="skyblue")
        title = tk.Label(illustration_frame, text="訓練內容", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
        title.pack(fill=tk.X, pady=10)

        illustration_label = tk.Label(illustration_frame, text=illustration, font=("微軟正黑體", 15), bg="skyblue", fg="black", wraplength=600)
        illustration_label.pack(pady=20)

        back_button = tk.Button(illustration_frame, text="返回", font=("微軟正黑體", 15, "bold"), bg="white", fg="black",
                                command=part1_page)  # 返回主頁
        back_button.pack(pady=10)

        illustration_frame.pack(fill="both", expand=1)
    
    for widget in page_frame.winfo_children():
        widget.destroy()

    part2_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part2_page_frame, text="背部訓練", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    csv_file = "training_back.csv"
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    continue
                button_name, illustration, website, sec = row
                button = tk.Button(part2_page_frame, text=button_name, font=("微軟正黑體", 15, "bold"),
                                   bg="white", fg="black", width=20,
                                   command=lambda a=illustration: show_illustration(a))
                button.pack(pady=5)
    except FileNotFoundError:
        error_label = tk.Label(part2_page_frame, text="找不到 CSV 檔案", font=("微軟正黑體", 15, "bold"), bg="skyblue", fg="red")
        error_label.pack(pady=20)

    part2_page_frame.pack(fill="both", expand=1)

def part3_page():
    def show_illustration(illustration):
        for widget in page_frame.winfo_children():
            widget.destroy()

        illustration_frame = tk.Frame(page_frame, bg="skyblue")
        title = tk.Label(illustration_frame, text="訓練內容", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
        title.pack(fill=tk.X, pady=10)

        illustration_label = tk.Label(illustration_frame, text=illustration, font=("微軟正黑體", 15), bg="skyblue", fg="black", wraplength=600)
        illustration_label.pack(pady=20)

        back_button = tk.Button(illustration_frame, text="返回", font=("微軟正黑體", 15, "bold"), bg="white", fg="black",
                                command=part1_page)  # 返回主頁
        back_button.pack(pady=10)

        illustration_frame.pack(fill="both", expand=1)

    part3_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part3_page_frame, text="肩膀訓練", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    csv_file = "training_shoulder.csv"
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    continue
                button_name, illustration, website, sec = row
                button = tk.Button(part3_page_frame, text=button_name, font=("微軟正黑體", 15, "bold"),
                                   bg="white", fg="black", width=20,
                                   command=lambda a=illustration: show_illustration(a))
                button.pack(pady=5)
    except FileNotFoundError:
        error_label = tk.Label(part3_page_frame, text="找不到 CSV 檔案", font=("微軟正黑體", 15, "bold"), bg="skyblue", fg="red")
        error_label.pack(pady=20)

    part3_page_frame.pack(fill="both", expand=1)

def part4_page():
    def show_illustration(illustration):
        for widget in page_frame.winfo_children():
            widget.destroy()

        illustration_frame = tk.Frame(page_frame, bg="skyblue")
        title = tk.Label(illustration_frame, text="訓練內容", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
        title.pack(fill=tk.X, pady=10)

        illustration_label = tk.Label(illustration_frame, text=illustration, font=("微軟正黑體", 15), bg="skyblue", fg="black", wraplength=600)
        illustration_label.pack(pady=20)

        back_button = tk.Button(illustration_frame, text="返回", font=("微軟正黑體", 15, "bold"), bg="white", fg="black",
                                command=part1_page)  # 返回主頁
        back_button.pack(pady=10)

        illustration_frame.pack(fill="both", expand=1)

    part4_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part4_page_frame, text="手臂訓練", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    csv_file = "training_arm.csv"
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    continue
                button_name, illustration, website, sec = row
                button = tk.Button(part4_page_frame, text=button_name, font=("微軟正黑體", 15, "bold"),
                                   bg="white", fg="black", width=20,
                                   command=lambda a=illustration: show_illustration(a))
                button.pack(pady=5)
    except FileNotFoundError:
        error_label = tk.Label(part4_page_frame, text="找不到 CSV 檔案", font=("微軟正黑體", 15, "bold"), bg="skyblue", fg="red")
        error_label.pack(pady=20)

    part4_page_frame.pack(fill="both", expand=1)

def part5_page():
    def show_illustration(illustration):
        for widget in page_frame.winfo_children():
            widget.destroy()

        illustration_frame = tk.Frame(page_frame, bg="skyblue")
        title = tk.Label(illustration_frame, text="訓練內容", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
        title.pack(fill=tk.X, pady=10)

        illustration_label = tk.Label(illustration_frame, text=illustration, font=("微軟正黑體", 15), bg="skyblue", fg="black", wraplength=600)
        illustration_label.pack(pady=20)

        back_button = tk.Button(illustration_frame, text="返回", font=("微軟正黑體", 15, "bold"), bg="white", fg="black",
                                command=part5_page)  # 返回主頁
        back_button.pack(pady=10)

        illustration_frame.pack(fill="both", expand=1)

    part5_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part5_page_frame, text="腹部訓練", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    csv_file = "training_belly.csv"
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    continue
                button_name, illustration, website, sec = row
                button = tk.Button(part5_page_frame, text=button_name, font=("微軟正黑體", 15, "bold"),
                                   bg="white", fg="black", width=20,
                                   command=lambda a=illustration: show_illustration(a))
                button.pack(pady=5)
    except FileNotFoundError:
        error_label = tk.Label(part5_page_frame, text="找不到 CSV 檔案", font=("微軟正黑體", 15, "bold"), bg="skyblue", fg="red")
        error_label.pack(pady=20)

    part5_page_frame.pack(fill="both", expand=1)

def part6_page():
    def show_illustration(illustration):
        for widget in page_frame.winfo_children():
            widget.destroy()

        illustration_frame = tk.Frame(page_frame, bg="skyblue")
        title = tk.Label(illustration_frame, text="訓練內容", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
        title.pack(fill=tk.X, pady=10)

        illustration_label = tk.Label(illustration_frame, text=illustration, font=("微軟正黑體", 15), bg="skyblue", fg="black", wraplength=600)
        illustration_label.pack(pady=20)

        back_button = tk.Button(illustration_frame, text="返回", font=("微軟正黑體", 15, "bold"), bg="white", fg="black",
                                command=part6_page)  # 返回主頁
        back_button.pack(pady=10)

        illustration_frame.pack(fill="both", expand=1)

    part6_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part6_page_frame, text="腿部訓練", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    csv_file = "training_leg.csv"
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    continue
                button_name, illustration, website, sec = row
                button = tk.Button(part6_page_frame, text=button_name, font=("微軟正黑體", 15, "bold"),
                                   bg="white", fg="black", width=20,
                                   command=lambda a=illustration: show_illustration(a))
                button.pack(pady=5)
    except FileNotFoundError:
        error_label = tk.Label(part6_page_frame, text="找不到 CSV 檔案", font=("微軟正黑體", 15, "bold"), bg="skyblue", fg="red")
        error_label.pack(pady=20)

    part6_page_frame.pack(fill="both", expand=1)

def part7_page():
    part7_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part7_page_frame, text="自訂菜單", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    part7_page_frame.pack(fill="both", expand=1)

def part8_page():
    part8_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part8_page_frame, text="系統推薦菜單", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    part8_page_frame.pack(fill="both", expand=1)

def part9_page():
    """相機頁面"""
    part9_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part9_page_frame, text="拍照機", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    
    # 創建並啟動相機
    camera_app = create_camera_page(part9_page_frame)
    
    # 註冊清理函數
    def cleanup():
        cleanup_camera(camera_app)
        switch_topage(home_page)
    
    part9_page_frame.pack(fill="both", expand=1)



# 切換頁面的函式
def switch_topage(page_name):
    for i in page_frame.winfo_children():
        i.destroy()
    page_name()

# 選單的frame
menu = tk.Frame(root)
menu.pack(side=tk.LEFT, fill=tk.Y)
menu.pack_propagate(flag=False)
menu.config(width=150, bg="gray")

home = tk.Button(menu, text="主頁", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: home_page())
part1 = tk.Button(menu, text="胸部訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part1_page))
part2 = tk.Button(menu, text="背部訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part2_page))
part3 = tk.Button(menu, text="肩膀訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part3_page))
part4 = tk.Button(menu, text="手臂訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part4_page))
part5 = tk.Button(menu, text="腹部訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part5_page))
part6 = tk.Button(menu, text="腿部訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part6_page))
part7 = tk.Button(menu, text="自訂菜單", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part7_page))
part8 = tk.Button(menu, text="系統推薦菜單", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part8_page))
part9 = tk.Button(menu, text="拍照機", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part9_page))

home.pack(pady=5)
part1.pack(pady=5)
part2.pack(pady=5)
part3.pack(pady=5)
part4.pack(pady=5)
part5.pack(pady=5)
part6.pack(pady=5)
part7.pack(pady=5)
part8.pack(pady=5)
part9.pack(pady=5)

# 預設顯示主頁
home_page()

# 運行主循環
root.mainloop()
