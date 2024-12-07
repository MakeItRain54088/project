import tkinter as tk
from tkinter import messagebox, simpledialog
import webview
import csv
from PIL import Image

custom_menus = []

# str 菜單名稱 -> list 內容
custom_menus_contents = dict()

def create_training_page(page_frame, title_text, csv_filename, switch_to_clock_callback=None):
    """
    創建通用的訓練頁面
    
    Args:
        page_frame: 主要的頁面框架
        title_text: 頁面標題文字
        csv_filename: 訓練數據的CSV檔案名稱
        switch_to_clock_callback: 切換到計時器頁面的回調函數
    """
    def show_illustration(illustration):
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

        def return_to_page():
            create_training_page(page_frame, title_text, csv_filename, switch_to_clock_callback)

        back_button = tk.Button(illustration_frame, text="返回", 
                              font=("微軟正黑體", 15, "bold"), 
                              bg="white", fg="black",
                              command=return_to_page)
        back_button.pack(pady=10)

        illustration_frame.pack(fill="both", expand=1)

    for widget in page_frame.winfo_children():
        widget.destroy()

    training_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(training_page_frame, text=title_text, 
                    font=("微軟正黑體", 22, "bold"), 
                    bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    def embed_video(website, sec):
        if "youtube" in website:
            yt, video_id = website.split('/watch?v=')
            video_url = f"{yt}/embed/{video_id}?start={start_time}&end={end_time}&autoplay=1"
            start_time, end_time=sec.split('-')
            start_time=convert_time_to_seconds(start_time)
            end_time=convert_time_to_seconds(end_time)

            # 嵌入式 YouTube 網址
            video_url = f"{yt}/embed/{video_id}?start={start_time}&end={end_time}&autoplay=1"

            # 創建 WebView 視窗
            webview.create_window("YouTube Player", video_url, width=400, height=300)

            # 啟動 WebView 應用
            webview.start()
        else:
            img = Image.open('image_path.jpg')
            img.show()
        
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

    def add_to_menus(name,choose_menus):
        if choose_menus.get()!="請選擇" and choose_menus.get()!="無可用菜單":
            if name not in custom_menus_contents[choose_menus.get()]:
                custom_menus_contents[choose_menus.get()].append(name)
            else:
                custom_menus_contents[choose_menus.get()].pop(custom_menus_contents[choose_menus.get()].index(name))
            place_add_del_btn(tem,choose_menus)
            print(custom_menus_contents)
    
    def place_add_del_btn(tem,choose_menus):
        for i in range(len(tem)):

            name = tem[i]
        
            if choose_menus.get()=="請選擇" or choose_menus.get()=="無可用菜單":
                add_btn = tk.Button(training_page_frame, 
                             text="加入",
                             font=("微軟正黑體", 15, "bold"),
                             bg="white", fg="black", 
                             width=5,
                             command=lambda a=name:add_to_menus(a,choose_menus))
                add_btn.place(relx=0.8, y=48+i*54)
            else:
                if name not in custom_menus_contents[choose_menus.get()]:
                    add_btn = tk.Button(training_page_frame, 
                             text="加入",
                             font=("微軟正黑體", 15, "bold"),
                             bg="white", fg="black", 
                             width=5,
                             command=lambda a=name:add_to_menus(a,choose_menus))
                    add_btn.place(relx=0.8, y=48+i*54)
                else:
                    add_btn = tk.Button(training_page_frame, 
                             text="刪除",
                             font=("微軟正黑體", 15, "bold"),
                             bg="white", fg="black", 
                             width=5,
                             command=lambda a=name:add_to_menus(a,choose_menus))
                add_btn.place(relx=0.8, y=48+i*54)


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
                                 command=lambda a=illustration: show_illustration(a))
                button.pack(pady=5)

                tem.append(button_name)

            place_add_del_btn(tem,choose_menus)

    except FileNotFoundError:
        error_label = tk.Label(training_page_frame, 
                             text="找不到 CSV 檔案", 
                             font=("微軟正黑體", 15, "bold"), 
                             bg="skyblue", fg="red")
        error_label.pack(pady=20)

    def callback(*arg):
        place_add_del_btn(tem,choose_menus)

    choose_menus.trace("w",callback)

    if switch_to_clock_callback:
        start_button = tk.Button(training_page_frame, 
                               text="開始訓練", 
                               font=("微軟正黑體", 15, "bold"),
                               bg="white", fg="black",
                               command=switch_to_clock_callback)
        start_button.pack(pady=20)

    training_page_frame.pack(fill="both", expand=1)

def create_home_page(page_frame, switch_to_clock_callback):
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
    
    start = tk.Button(home_page_frame, text="開始訓練", 
                     font=("微軟正黑體", 15, "bold"), 
                     bg="white", fg="black", height=2, width=15, 
                     command=switch_to_clock_callback)
    start.place(relx=0.35, rely=0.7)
    
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

def create_recommend_page(page_frame):
    """創建系統推薦菜單頁面"""
    for widget in page_frame.winfo_children():
        widget.destroy()

    recommend_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(recommend_page_frame, text="系統推薦菜單", 
                    font=("微軟正黑體", 22, "bold"), 
                    bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    message = tk.Label(recommend_page_frame, 
                      text="系統推薦功能開發中", 
                      font=("微軟正黑體", 15), 
                      bg="skyblue", fg="black")
    message.pack(pady=20)

    recommend_page_frame.pack(fill="both", expand=1)

# 頁面配置字典
PAGE_CONFIG = {
    'chest': ('胸部訓練', 'training_chest.csv'),
    'back': ('背部訓練', 'training_back.csv'),
    'shoulder': ('肩膀訓練', 'training_shoulder.csv'),
    'arm': ('手臂訓練', 'training_arm.csv'),
    'belly': ('腹部訓練', 'training_belly.csv'),
    'leg': ('腿部訓練', 'training_leg.csv')
}