import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import webview
import csv
from PIL import Image, ImageTk
from datetime import datetime
from collections import defaultdict
from clock import start_stopwatch_page
from shared import custom_menus, custom_menus_contents

def create_training_page(page_frame, title_text, csv_filename, switch_to_clock_callback=None):
    """
    創建通用的訓練頁面
    
    Args:
        page_frame: 主要的頁面框架
        title_text: 頁面標題文字
        csv_filename: 訓練數據的CSV檔案名稱
        switch_to_clock_callback: 切換到計時器頁面的回調函數
    """
    def convert_time_to_seconds(time_str):
        """將時間格式 'mm:ss' 或 'hh:mm:ss' 轉換為秒數"""
        time_parts = list(map(int, time_str.split(':')))
        if len(time_parts) == 2:  # mm:ss
            minutes, seconds = time_parts
            return minutes * 60 + seconds
        elif len(time_parts) == 3:  # hh:mm:ss
            hours, minutes, seconds = time_parts
            return hours * 3600 + minutes * 60 + seconds
        return 0

    def embed_video(website, sec):
        if "youtube" in website:
            yt, video_id = website.split('/watch?v=')
            start_time, end_time = sec.split('-')
            start_time = convert_time_to_seconds(start_time)
            end_time = convert_time_to_seconds(end_time)

            # 嵌入式 YouTube 網址
            video_url = f"{yt}/embed/{video_id}?start={start_time}&end={end_time}&autoplay=1"

            # 創建 WebView 視窗
            webview.create_window("YouTube Player", video_url, width=400, height=300)

            # 啟動 WebView 應用
            webview.start()
        else:
            img = Image.open('image_path.jpg')
            img.show()

    def show_illustration(illustration, website=None, sec=None):
        """
        顯示訓練內容說明頁面，包含文字說明和影片播放功能
        
        Args:
            illustration: 說明文字
            website: 影片網址或圖片路徑
            sec: 影片播放時間區間 (格式: "開始時間-結束時間")
        """
        for widget in page_frame.winfo_children():
            widget.destroy()

        illustration_frame = tk.Frame(page_frame, bg="skyblue")
        title = tk.Label(illustration_frame, text="訓練內容", font=("微軟正黑體", 22, "bold"), 
                        bg="lightyellow", fg="black")
        title.pack(fill=tk.X, pady=10)

        illustration_label = tk.Label(illustration_frame, text=illustration, 
                                    font=("微軟正黑體", 15), bg="skyblue", 
                                    fg="black", wraplength=600)
        illustration_label.pack(pady=20)

        # 如果有提供影片網址，加入播放按鈕
        if website and sec:
            play_button = tk.Button(illustration_frame, text="播放示範影片", 
                                  font=("微軟正黑體", 15, "bold"), 
                                  bg="white", fg="black",
                                  command=lambda: embed_video(website, sec))
            play_button.pack(pady=10)

        def return_to_page():
            create_training_page(page_frame, title_text, csv_filename, switch_to_clock_callback)

        back_button = tk.Button(illustration_frame, text="返回", 
                              font=("微軟正黑體", 15, "bold"), 
                              bg="white", fg="black",
                              command=return_to_page)
        back_button.pack(pady=10)

        illustration_frame.pack(fill="both", expand=1)

    # 清除現有的元件
    for widget in page_frame.winfo_children():
        widget.destroy()

    # 創建主要訓練頁面框架
    training_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(training_page_frame, text=title_text, 
                    font=("微軟正黑體", 22, "bold"), 
                    bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    # 選擇菜單部分
    label = tk.Label(training_page_frame, 
                     text="選擇要更動的菜單", 
                     font=("微軟正黑體", 15, "bold"), 
                     bg="skyblue", fg="black")
    label.place(relx=0.02, rely=0.35)

    choose_menus = tk.StringVar()
    choose_menus.set("請選擇")

    if not custom_menus:
        choose_menus_option = tk.OptionMenu(training_page_frame, choose_menus, "無可用菜單")
        choose_menus_option.configure(state="disabled")
        choose_menus.set("無可用菜單")
    else:
        choose_menus_option = tk.OptionMenu(training_page_frame, choose_menus, *custom_menus)

    choose_menus_option.config(width=10, font=("微軟正黑體", 15, "bold"), 
                              bg="white", fg="black")
    choose_menus_option.place(relx=0.02, rely=0.4)

    def add_to_menus(name, choose_menus):
        if choose_menus.get() != "請選擇" and choose_menus.get() != "無可用菜單":
            if name not in custom_menus_contents[choose_menus.get()]:
                custom_menus_contents[choose_menus.get()].append(name)
            else:
                custom_menus_contents[choose_menus.get()].pop(
                    custom_menus_contents[choose_menus.get()].index(name))
            place_add_del_btn(tem, choose_menus)
            print(custom_menus_contents)

    def place_add_del_btn(tem, choose_menus):
        for i in range(len(tem)):
            name = tem[i]
            
            if choose_menus.get() == "請選擇" or choose_menus.get() == "無可用菜單":
                add_btn = tk.Button(training_page_frame, 
                                  text="加入",
                                  font=("微軟正黑體", 15, "bold"),
                                  bg="white", fg="black", 
                                  width=5,
                                  command=lambda a=name: add_to_menus(a, choose_menus))
                add_btn.place(relx=0.8, y=48+i*54)
            else:
                if name not in custom_menus_contents[choose_menus.get()]:
                    add_btn = tk.Button(training_page_frame, 
                                      text="加入",
                                      font=("微軟正黑體", 15, "bold"),
                                      bg="white", fg="black", 
                                      width=5,
                                      command=lambda a=name: add_to_menus(a, choose_menus))
                else:
                    add_btn = tk.Button(training_page_frame, 
                                      text="刪除",
                                      font=("微軟正黑體", 15, "bold"),
                                      bg="white", fg="black", 
                                      width=5,
                                      command=lambda a=name: add_to_menus(a, choose_menus))
                add_btn.place(relx=0.8, y=48+i*54)

    # 讀取CSV檔案並創建按鈕
    try:
        with open(csv_filename, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            tem = []

            for row in reader:
                if len(row) != 4:
                    continue
                button_name, illustration, website, sec = row
                button = tk.Button(training_page_frame, 
                                 text=button_name,
                                 font=("微軟正黑體", 15, "bold"),
                                 bg="white", fg="black", 
                                 width=20,
                                 command=lambda a=illustration, w=website, s=sec: 
                                     show_illustration(a, w, s))
                button.pack(pady=5)
                tem.append(button_name)

            place_add_del_btn(tem, choose_menus)

    except FileNotFoundError:
        error_label = tk.Label(training_page_frame, 
                             text="找不到 CSV 檔案", 
                             font=("微軟正黑體", 15, "bold"), 
                             bg="skyblue", fg="red")
        error_label.pack(pady=20)

    def callback(*arg):
        place_add_del_btn(tem, choose_menus)

    choose_menus.trace("w", callback)

    # 添加開始訓練按鈕
    if switch_to_clock_callback:
        start_button = tk.Button(training_page_frame, 
                               text="開始訓練", 
                               font=("微軟正黑體", 15, "bold"),
                               bg="white", fg="black",
                               command=switch_to_clock_callback)
        start_button.pack(pady=20)

    training_page_frame.pack(fill="both", expand=1)
    
def create_home_page(page_frame, root, switch_to_clock_callback):
    """創建主頁面"""
    for widget in page_frame.winfo_children():
        widget.destroy()

    home_page_frame = tk.Frame(page_frame, bg="skyblue")

    title = tk.Label(home_page_frame, text="健身菜單", 
                    font=("微軟正黑體", 22, "bold"), 
                    bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    
    label1 = tk.Label(home_page_frame, 
                     text="根據你的需求設計一套合適的訓練菜單", 
                     font=("微軟正黑體", 15, "bold"), 
                     bg="skyblue", fg="black")
    label1.pack(fill=tk.X)
    
    label2 = tk.Label(home_page_frame, text="選擇訓練菜單", 
                     font=("微軟正黑體", 15, "bold"), 
                     bg="skyblue", fg="black")
    label2.place(relx=0.4, rely=0.25)
    
    option_value = tk.StringVar()
    option_value.set("請選擇")
    
    if not custom_menus:
        option = tk.OptionMenu(home_page_frame, option_value, "無可用菜單")
        option.configure(state="disabled")
    else:
        option = tk.OptionMenu(home_page_frame, option_value, *custom_menus)
    
    option.config(width=24, font=("微軟正黑體", 15, "bold"), 
                 bg="white", fg="black")
    option.place(relx=0.25, rely=0.3)

    def start_training():
        selected_menu = option_value.get()
        if selected_menu and selected_menu != "請選擇" and selected_menu != "無可用菜單":
            # 修改回調函數以傳遞所選菜單
            if switch_to_clock_callback:
                start_stopwatch_page(page_frame, root, selected_menu)
        else:
            messagebox.showwarning("警告", "請先選擇訓練菜單")
    
    start = tk.Button(home_page_frame, text="開始訓練", 
                     font=("微軟正黑體", 15, "bold"), 
                     bg="white", fg="black", height=2, width=15, 
                     command=start_training)
    start.place(relx=0.35, rely=0.7)

    def add_menu_and_switch():
        menu_name = simpledialog.askstring("新增菜單", 
                                         "請輸入菜單名稱：",
                                         initialvalue=f"自訂菜單 {len(custom_menus) + 1}")
        if menu_name and menu_name.strip():
            menu_name = menu_name.strip()
            custom_menus.append(menu_name)
            custom_menus_contents[menu_name] = []
            create_blank_training_page(page_frame, menu_name, switch_to_clock_callback=None)

    add_option = tk.Button(home_page_frame, text="新增其他菜單", 
                          font=("微軟正黑體", 15, "bold"), 
                          bg="white", fg="black", height=1, width=15,
                          command=add_menu_and_switch)
    add_option.place(relx=0.35, rely=0.4)

    home_page_frame.pack(fill="both", expand=1)

def create_blank_training_page(page_frame, menu_name, switch_to_clock_callback=None):
    """創建空白的訓練頁面"""
    for widget in page_frame.winfo_children():
        widget.destroy()

    blank_page_frame = tk.Frame(page_frame, bg="skyblue")
    
    title_frame = tk.Frame(blank_page_frame, bg="lightyellow")
    title_frame.pack(fill=tk.X)
    
    title = tk.Label(title_frame, text=menu_name, 
                    font=("微軟正黑體", 22, "bold"), 
                    bg="lightyellow", fg="black")
    title.pack(side=tk.LEFT, padx=10)
    
    button_frame = tk.Frame(title_frame, bg="lightyellow")
    button_frame.pack(side=tk.RIGHT, padx=10)
    
    edit_btn = tk.Button(button_frame, text="編輯名稱", 
                        font=("微軟正黑體", 12), 
                        bg="#4CAF50", fg="white",
                        command=lambda: edit_menu_name(menu_name, blank_page_frame, page_frame, 1))
    edit_btn.pack(side=tk.LEFT, padx=5)
    
    delete_btn = tk.Button(button_frame, text="刪除菜單", 
                          font=("微軟正黑體", 12), 
                          bg="red", fg="white",
                          command=lambda: delete_menu(menu_name, blank_page_frame, page_frame))
    delete_btn.pack(side=tk.LEFT, padx=5)


    back_btn = tk.Button(button_frame, text="返回", 
                          font=("微軟正黑體", 12), 
                          bg="blue", fg="white",
                          command=lambda: create_custom_page(page_frame, "自訂菜單"))
    back_btn.pack(side=tk.LEFT, padx=5)

    #自訂菜單內容
    def place_custom_menus_contents(menu_name):

        for i in range(len(custom_menus_contents[menu_name])):

            button = tk.Button(blank_page_frame, 
                             text=custom_menus_contents[menu_name][i],
                             font=("微軟正黑體", 15, "bold"),
                             bg="white", fg="black", 
                             width=20)
            button.pack(pady=5)
            if i!=0:
                up_btn = tk.Button(blank_page_frame, 
                                 text="A",
                                 font=("微軟正黑體", 15, "bold"),
                                 bg="white", fg="black", 
                                 width=2,
                                 command=lambda a=i: up_down_switch(menu_name,a,-1))
                up_btn.place(relx=0.75, y=48+i*54)

            if i!=len(custom_menus_contents[menu_name])-1:
                down_btn = tk.Button(blank_page_frame, 
                                    text="V",
                                    font=("微軟正黑體", 15, "bold"),
                                    bg="white", fg="black", 
                                    width=2,
                                    command=lambda a=i: up_down_switch(menu_name,a,1))
                down_btn.place(relx=0.8, y=48+i*54)
    
    def up_down_switch(menu_name,a,j):
        
        custom_menus_contents[menu_name][a],custom_menus_contents[menu_name][a+j]=custom_menus_contents[menu_name][a+j],custom_menus_contents[menu_name][a]

        create_blank_training_page(page_frame, menu_name, switch_to_clock_callback=None)
        print(custom_menus_contents)
    place_custom_menus_contents(menu_name)



    if switch_to_clock_callback:
        start_button = tk.Button(blank_page_frame, 
                               text="開始訓練", 
                               font=("微軟正黑體", 15, "bold"),
                               bg="white", fg="black",
                               command=switch_to_clock_callback)
        start_button.pack(pady=20)

    blank_page_frame.pack(fill="both", expand=1)

def edit_menu_name(menu_name, menu_button, page_frame, a):
    """編輯菜單名稱"""
    new_name = simpledialog.askstring("編輯菜單名稱", 
                                    "請輸入新的菜單名稱：",
                                    initialvalue=menu_name)
    if new_name and new_name.strip():
        new_name = new_name.strip()
        index = custom_menus.index(menu_name)
        custom_menus[index] = new_name

        custom_menus_contents[new_name]=custom_menus_contents.pop(menu_name)
        
    #a值為是否已在菜單頁面裡
    if a==1:
        create_blank_training_page(page_frame, new_name, switch_to_clock_callback=None)
    else: create_custom_page(page_frame, "自訂菜單")

def delete_menu(menu_name, menu_button, page_frame):
    """刪除指定的菜單"""
    if messagebox.askyesno("確認刪除", f"確定要刪除 {menu_name} 嗎？"):

        custom_menus_contents.pop(menu_name)
        
        custom_menus.remove(menu_name)
        menu_button.destroy()
        create_custom_page(page_frame, "自訂菜單")

def create_custom_page(page_frame, title_text):
    """創建自訂菜單頁面"""
    for widget in page_frame.winfo_children():
        widget.destroy()

    custom_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(custom_page_frame, text=title_text, 
                    font=("微軟正黑體", 22, "bold"), 
                    bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    def add_menu():
        menu_name = simpledialog.askstring("新增菜單", 
                                         "請輸入菜單名稱：",
                                         initialvalue=f"自訂菜單 {len(custom_menus) + 1}")
        if menu_name and menu_name.strip():
            menu_name = menu_name.strip()
            custom_menus.append(menu_name)
            create_menu_button(menu_buttons_frame, menu_name, page_frame)

            custom_menus_contents[menu_name] = []
            

    add_button = tk.Button(custom_page_frame, 
                          text="新增菜單",
                          font=("微軟正黑體", 15, "bold"),
                          bg="white", fg="black", 
                          width=20,
                          command=add_menu)
    add_button.pack(pady=20)

    menu_buttons_frame = tk.Frame(custom_page_frame, bg="skyblue")
    menu_buttons_frame.pack(fill="both", expand=1)

    for menu_name in custom_menus:
        create_menu_button(menu_buttons_frame, menu_name, page_frame)

    custom_page_frame.pack(fill="both", expand=1)

def create_menu_button(parent_frame, menu_name, page_frame):
    """創建菜單按鈕和控制按鈕"""
    button_frame = tk.Frame(parent_frame, bg="skyblue")
    button_frame.pack(fill=tk.X, pady=2)
    
    menu_button = tk.Button(button_frame, 
                           text=menu_name,
                           font=("微軟正黑體", 15, "bold"),
                           bg="white", fg="black", 
                           width=15,
                           command=lambda: create_blank_training_page(page_frame, menu_name, switch_to_clock_callback=None))
    menu_button.pack(side=tk.LEFT, padx=5)
    
    edit_button = tk.Button(button_frame, 
                           text="✎",
                           font=("微軟正黑體", 15, "bold"),
                           bg="#4CAF50", fg="white",
                           width=2,
                           command=lambda: edit_menu_name(menu_name, button_frame, page_frame, a=0))
    edit_button.pack(side=tk.LEFT, padx=2)
    
    delete_button = tk.Button(button_frame, 
                             text="×",
                             font=("微軟正黑體", 15, "bold"),
                             bg="red", fg="white",
                             width=2,
                             command=lambda: delete_menu(menu_name, button_frame, page_frame))
    delete_button.pack(side=tk.LEFT, padx=2)
    
    return button_frame

import tkinter as tk
from tkinter import simpledialog, messagebox
import csv
import random

def create_recommend_page(page_frame):
    """創建系統推薦菜單頁面"""
    for widget in page_frame.winfo_children():
        widget.destroy()

    recommend_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(recommend_page_frame, text="系統推薦菜單", 
                    font=("微軟正黑體", 22, "bold"), 
                    bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    def read_exercises_from_csv(csv_filename):
        """從CSV檔案讀取訓練動作"""
        exercises = []
        try:
            with open(csv_filename, newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 1:
                        exercises.append(row[0])  # 只取動作名稱
        except FileNotFoundError:
            print(f"找不到檔案: {csv_filename}")
        return exercises

    def generate_random_menu():
        """生成隨機訓練菜單"""
        all_exercises = {}
        for key, (name, csv_file) in PAGE_CONFIG.items():
            exercises = read_exercises_from_csv(csv_file)
            if exercises:
                num_exercises = random.randint(1, 2)  # 每個部位隨機1-2個動作
                selected = random.sample(exercises, min(num_exercises, len(exercises)))
                all_exercises[name] = selected

        return all_exercises

    def display_menu(exercises_dict):
        """顯示生成的菜單"""
        # 清除之前的內容
        for widget in menu_frame.winfo_children():
            widget.destroy()

        row = 0  # 控制行數
        col = 0  # 控制列數

        for part, exercises in exercises_dict.items():
            # 顯示部位標題
            part_label = tk.Label(menu_frame, 
                                text=part,
                                font=("微軟正黑體", 15, "bold"),
                                bg="skyblue", fg="black", width=20, anchor="center")
            part_label.grid(row=row, column=col, pady=(10, 5), padx=10, sticky="n")
            row += 1

            # 顯示該部位的動作，分兩排排列
            for idx, exercise in enumerate(exercises):
                # 每行顯示兩個動作
                row_in_grid = row + (idx // 2)  # 當 idx 是偶數，放在同一排，否則放在下一排
                col_in_grid = idx % 2  # 列數，每排最多顯示兩個動作
                exercise_label = tk.Label(menu_frame,
                                        text=exercise,
                                        font=("微軟正黑體", 12),
                                        bg="white", fg="black", width=15, anchor="center", relief="solid", bd=1)
                exercise_label.grid(row=row_in_grid, column=col_in_grid, pady=5, padx=10, sticky="nsew")
            
            row += (len(exercises) // 2 + 1)  # 每兩個動作一排，換行

    def save_to_custom_menu():
        """將當前推薦菜單保存為自訂菜單"""
        menu_name = simpledialog.askstring("儲存菜單",
                                         "請輸入菜單名稱：",
                                         initialvalue=f"推薦菜單 {len(custom_menus) + 1}")
        
        if menu_name and menu_name.strip():
            menu_name = menu_name.strip()
            custom_menus.append(menu_name)
            custom_menus_contents[menu_name] = []
            
            # 將所有顯示的動作加入自訂菜單
            for part, exercises in current_menu.items():
                for exercise in exercises:
                    custom_menus_contents[menu_name].append(exercise)
            
            messagebox.showinfo("成功", "菜單已儲存！")

    # 創建按鈕框架
    button_frame = tk.Frame(recommend_page_frame, bg="skyblue")
    button_frame.pack(pady=10)

    # 重新生成按鈕
    regenerate_btn = tk.Button(button_frame,
                              text="重新生成",
                              font=("微軟正黑體", 15, "bold"),
                              bg="white", fg="black",
                              command=lambda: display_menu(generate_random_menu()))
    regenerate_btn.pack(side=tk.LEFT, padx=10)

    # 儲存按鈕
    save_btn = tk.Button(button_frame,
                        text="儲存為自訂菜單",
                        font=("微軟正黑體", 15, "bold"),
                        bg="white", fg="black",
                        command=save_to_custom_menu)
    save_btn.pack(side=tk.LEFT, padx=10)

    # 創建顯示菜單的框架
    menu_frame = tk.Frame(recommend_page_frame, bg="skyblue")
    menu_frame.pack(fill="both", expand=True)

    # 生成並顯示初始菜單
    current_menu = generate_random_menu()
    display_menu(current_menu)

    recommend_page_frame.pack(fill="both", expand=1)


def create_photo_page(page_frame):
    """
    顯示照片頁面，按月份分類並顯示該資料夾中的照片和拍照日期
    """
    # 照片存放資料夾
    photo_folder = r"C:\Users\HSU\OneDrive\桌面\python\project\project\每日照片"
    
    # 確保該資料夾存在
    if not os.path.exists(photo_folder):
        print(f"資料夾 {photo_folder} 不存在!")
        return
    
    # 獲取資料夾中所有照片檔案
    photo_files = [f for f in os.listdir(photo_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    if not photo_files:
        print("資料夾中沒有照片!")
        return

    # 按月份分組照片
    photos_by_month = defaultdict(list)
    for photo_file in photo_files:
        photo_path = os.path.join(photo_folder, photo_file)
        
        # 取得檔案的修改時間並格式化為日期
        mod_time = os.path.getmtime(photo_path)
        month_taken = datetime.fromtimestamp(mod_time).strftime("%Y-%m")  # 格式化為 "YYYY-MM"
        
        # 根據月份將照片分組
        photos_by_month[month_taken].append(photo_path)
    
    # 顯示每個月的照片
    for month, photos in sorted(photos_by_month.items()):  # 按月份排序
        month_label = tk.Label(page_frame, text=f"{month} 的照片", font=("微軟正黑體", 16, "bold"), bg="lightyellow")
        month_label.pack(pady=10)
        
        # 顯示每張照片
        for photo_path in photos:
            img = Image.open(photo_path)
            img.thumbnail((300, 300))  # 縮小圖片以適應視窗大小
            img_tk = ImageTk.PhotoImage(img)
            
            # 取得檔案的修改時間並格式化為日期
            mod_time = os.path.getmtime(photo_path)
            date_taken = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M:%S")
            
            # 顯示圖片
            img_label = tk.Label(page_frame, image=img_tk)
            img_label.image = img_tk  # 保持對圖片的引用
            img_label.pack(pady=10)
            
            # 顯示拍攝日期
            date_label = tk.Label(page_frame, text=f"拍照日期: {date_taken}", font=("微軟正黑體", 10))
            date_label.pack(pady=5)

# 頁面配置字典
PAGE_CONFIG = {
    'chest': ('胸部訓練', 'training_chest.csv'),
    'back': ('背部訓練', 'training_back.csv'),
    'shoulder': ('肩膀訓練', 'training_shoulder.csv'),
    'arm': ('手臂訓練', 'training_arm.csv'),
    'belly': ('腹部訓練', 'training_belly.csv'),
    'leg': ('腿部訓練', 'training_leg.csv')
}