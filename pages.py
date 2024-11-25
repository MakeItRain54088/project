import tkinter as tk
import csv

def create_training_page(page_frame, title_text, csv_filename):
    """
    創建通用的訓練頁面
    
    Args:
        page_frame: 主要的頁面框架
        title_text: 頁面標題文字
        csv_filename: 訓練數據的CSV檔案名稱
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

        # 使用閉包來保存當前頁面的狀態
        def return_to_page():
            create_training_page(page_frame, title_text, csv_filename)

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

    try:
        with open(csv_filename, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
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
    except FileNotFoundError:
        error_label = tk.Label(training_page_frame, 
                             text="找不到 CSV 檔案", 
                             font=("微軟正黑體", 15, "bold"), 
                             bg="skyblue", fg="red")
        error_label.pack(pady=20)

    training_page_frame.pack(fill="both", expand=1)

def create_home_page(page_frame, switch_to_clock_callback):
    """創建主頁面"""
    for i in page_frame.winfo_children():
        i.destroy()

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
    
    optionlist = ['A','B','C','D','E']
    option_value = tk.StringVar()
    option_value.set("請選擇")
    option = tk.OptionMenu(home_page_frame, option_value, *optionlist)
    option.config(width=24, font=("微軟正黑體", 15, "bold"), 
                 bg="white", fg="black")
    option.place(relx=0.25, rely=0.3)

    add_option = tk.Button(home_page_frame, text="新增其他菜單", 
                          font=("微軟正黑體", 15, "bold"), 
                          bg="white", fg="black", height=1, width=15)
    add_option.place(relx=0.35, rely=0.4)

    start = tk.Button(home_page_frame, text="開始訓練", 
                     font=("微軟正黑體", 15, "bold"), 
                     bg="white", fg="black", height=2, width=15, 
                     command=switch_to_clock_callback)
    start.place(relx=0.35, rely=0.7)

    home_page_frame.pack(fill="both", expand=1)

def create_custom_page(page_frame, title_text):
    """創建自訂菜單和系統推薦菜單頁面"""
    custom_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(custom_page_frame, text=title_text, 
                    font=("微軟正黑體", 22, "bold"), 
                    bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    custom_page_frame.pack(fill="both", expand=1)

# 頁面配置字典
PAGE_CONFIG = {
    'chest': ('胸部訓練', 'training_chest.csv'),
    'back': ('背部訓練', 'training_back.csv'),
    'shoulder': ('肩膀訓練', 'training_shoulder.csv'),
    'arm': ('手臂訓練', 'training_arm.csv'),
    'belly': ('腹部訓練', 'training_belly.csv'),
    'leg': ('腿部訓練', 'training_leg.csv')
}