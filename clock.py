import tkinter as tk
from math import pi, cos, sin
from shared import custom_menus_contents

def start_stopwatch_page(frame, root, selected_menu=None):
    """設置計時碼錶頁面的功能，並顯示所選訓練菜單"""
    # 清空 frame
    for widget in frame.winfo_children():
        widget.destroy()

    # 建立左右分割的框架
    main_frame = tk.Frame(frame, bg="skyblue")
    main_frame.pack(fill="both", expand=True)

    # 左側計時器框架
    left_frame = tk.Frame(main_frame, bg="skyblue")
    left_frame.pack(side=tk.LEFT, fill="both", expand=True)

    # 右側菜單框架
    right_frame = tk.Frame(main_frame, bg="skyblue")
    right_frame.pack(side=tk.RIGHT, fill="both", expand=True)

    # 初始化參數
    minutes, seconds = 0, 0
    elapsed_seconds = 0
    is_running = False

    # 繪製時鐘的函式
    def draw_clock():
        canvas.delete("hands")
        if elapsed_seconds > 0:
            seconds_angle = (elapsed_seconds % 60) / 60 * 2 * pi
            seconds_x = center_x + radius * cos(-pi / 2 + seconds_angle)
            seconds_y = center_y + radius * sin(-pi / 2 + seconds_angle)
            canvas.create_line(center_x, center_y, seconds_x, seconds_y, fill="red", width=3, tags="hands")
        time_str = f"{minutes:02}:{seconds:02}"
        label.config(text=time_str)

    # 計時碼錶的函式
    def update_stopwatch():
        nonlocal minutes, seconds, elapsed_seconds, is_running
        if is_running:
            elapsed_seconds += 1
            minutes, seconds = divmod(elapsed_seconds, 60)
            draw_clock()
            root.after(1000, update_stopwatch)

    # 開始/暫停碼錶的函式
    def toggle_stopwatch():
        nonlocal is_running
        if is_running:
            is_running = False
            start_pause_btn.config(text="開始")
        else:
            is_running = True
            start_pause_btn.config(text="暫停")
            update_stopwatch()

    # 重置碼錶的函式
    def reset_stopwatch():
        nonlocal minutes, seconds, elapsed_seconds, is_running
        is_running = False
        elapsed_seconds = 0
        minutes, seconds = 0, 0
        start_pause_btn.config(text="開始")
        draw_clock()

    # 添加計時器 UI 元件到左側框架
    label = tk.Label(left_frame, text="00:00", font=("Arial", 24), fg="black", bg="skyblue")
    label.pack(pady=20)

    start_pause_btn = tk.Button(left_frame, text="開始", font=("微軟正黑體", 18, "bold"), 
                               bg="lightyellow", fg="black", command=toggle_stopwatch)
    start_pause_btn.pack(pady=10)

    reset_btn = tk.Button(left_frame, text="重置", font=("微軟正黑體", 18, "bold"), 
                         bg="lightyellow", fg="black", command=reset_stopwatch)
    reset_btn.pack(pady=10)

    canvas = tk.Canvas(left_frame, width=300, height=300, bg="skyblue")
    canvas.pack(pady=20)

    center_x, center_y, radius = 150, 150, 125
    canvas.create_oval(center_x - radius, center_y - radius, 
                      center_x + radius, center_y + radius, outline="black", width=3)

    # 在右側框架顯示訓練菜單
    if selected_menu and selected_menu in custom_menus_contents:
        menu_title = tk.Label(right_frame, text=f"訓練菜單: {selected_menu}", 
                            font=("微軟正黑體", 18, "bold"), bg="lightyellow", fg="black")
        menu_title.pack(pady=10, fill=tk.X)

        menu_frame = tk.Frame(right_frame, bg="skyblue")
        menu_frame.pack(fill="both", expand=True)

        for i, exercise in enumerate(custom_menus_contents[selected_menu], 1):
            exercise_label = tk.Label(menu_frame, text=f"{i}. {exercise}", 
                                    font=("微軟正黑體", 14), bg="white", fg="black")
            exercise_label.pack(pady=5, padx=10, fill=tk.X)