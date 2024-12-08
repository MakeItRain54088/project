import os
import tkinter as tk
import webview
from PIL import Image, ImageTk
from clock import start_stopwatch_page
from picture import create_camera_page, cleanup_camera
from pages import (
    create_training_page,
    create_home_page,
    create_custom_page,
    create_recommend_page,
    create_photo_page, 
    PAGE_CONFIG,
)

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
    start_stopwatch_page(page_frame, root)

def handle_camera_page():
    """處理相機頁面"""
    camera_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(camera_page_frame, text="拍照機", 
                    font=("微軟正黑體", 22, "bold"), 
                    bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    
    # 創建並啟動相機
    camera_app = create_camera_page(camera_page_frame)
    
    # 註冊清理函數
    def cleanup():
        cleanup_camera(camera_app)
        switch_topage('home')
    
    camera_page_frame.pack(fill="both", expand=1)

def switch_topage(page_type):
    """
    統一的頁面切換函數
    
    Args:
        page_type: 頁面類型標識符
    """
    # 清除當前頁面
    for widget in page_frame.winfo_children():
        widget.destroy()

    # 根據頁面類型切換到相應頁面
    if page_type == 'home':
        create_home_page(page_frame, root, switch_to_clock)
    elif page_type in PAGE_CONFIG:
        title, csv_file = PAGE_CONFIG[page_type]
        create_training_page(page_frame, title, csv_file, switch_to_clock)
    elif page_type == 'custom':
        create_custom_page(page_frame, "自訂菜單")
    elif page_type == 'recommend':
        create_recommend_page(page_frame)
    elif page_type == 'camera':
        handle_camera_page()
    elif page_type == 'photo':
        create_photo_page(page_frame)

# 選單的frame
menu = tk.Frame(root)
menu.pack(side=tk.LEFT, fill=tk.Y)
menu.pack_propagate(flag=False)
menu.config(width=150, bg="gray")

# 定義所有按鈕的配置
buttons_config = [
    ("主頁", 'home'),
    ("胸部訓練", 'chest'),
    ("背部訓練", 'back'),
    ("肩膀訓練", 'shoulder'),
    ("手臂訓練", 'arm'),
    ("腹部訓練", 'belly'),
    ("腿部訓練", 'leg'),
    ("自訂菜單", 'custom'),
    ("系統推薦菜單", 'recommend'),
    ("拍照機", 'camera'),
    ("照片頁", 'photo')
]

# 創建所有按鈕
for button_text, page_type in buttons_config:
    button = tk.Button(
        menu,
        text=button_text,
        font=("微軟正黑體", 15, "bold"),
        bg="white",
        fg="black",
        width=15,
        command=lambda pt=page_type: switch_topage(pt)
    )
    button.pack(pady=5)

# 預設顯示主頁
switch_topage('home')

# 運行主循環
root.mainloop()