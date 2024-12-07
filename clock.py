
import tkinter as tk
from math import pi, cos, sin
from tkinter import messagebox

def start_clock_page(frame):
    """設置倒數計時頁面的功能"""
    # 清空 frame
    for widget in frame.winfo_children():
        widget.destroy()

    # 初始化參數
    minutes, seconds = 0, 0
    seconds_left = 0
    total_seconds = 0
    is_paused = False  # 用來追蹤是否暫停

    # 繪製時鐘的函式
    def draw_clock():
        """繪製圓形時鐘並更新時間"""
        canvas.delete("hands")  # 清除舊的指針
        if total_seconds > 0:
            # 計算秒針角度並繪製
            seconds_angle = (seconds_left / total_seconds) * 2 * pi
            seconds_x = center_x + radius * cos(-pi / 2 + seconds_angle)
            seconds_y = center_y + radius * sin(-pi / 2 + seconds_angle)
            canvas.create_line(center_x, center_y, seconds_x, seconds_y, fill="red", width=3, tags="hands")
        # 更新時間顯示
        time_str = f"{minutes:02}:{seconds:02}"
        label.config(text=time_str)

    # 倒數計時的函式
    def start_countdown():
        """開始倒數計時"""
        nonlocal minutes, seconds, seconds_left, is_paused
        if is_paused:  # 如果暫停，則不執行倒數
            return
        if seconds_left <= 0:  # 如果秒數小於或等於 0，直接返回
            label.config(text="時間到！")
            return
        # 更新倒數時間
        seconds_left -= 1
        minutes, seconds = divmod(seconds_left, 60)
        draw_clock()  # 更新時鐘顯示
        # 每秒更新一次
        frame.after(1000, start_countdown)

    # 設置時間的函式
    def set_timer():
        """設定倒數計時"""
        nonlocal minutes, seconds, seconds_left, total_seconds
        time_input = time_entry.get()
        try:
            # 驗證格式 MM:SS
            mins, secs = map(int, time_input.split(":"))
            if mins < 0 or secs < 0 or secs >= 60:
                raise ValueError("請輸入有效的時間！")
            # 設置時間
            minutes, seconds = mins, secs
            seconds_left = minutes * 60 + seconds
            total_seconds = seconds_left
            draw_clock()  # 初始化時鐘顯示
        except ValueError:
            messagebox.showerror("無效輸入", "請輸入格式為 MM:SS 的時間！")

    # 暫停/繼續的函式
    def pause_timer():
        """暫停或繼續倒數"""
        nonlocal is_paused
        if is_paused:
            is_paused = False
            start_countdown()  # 恢復倒數
            pause_btn.config(text="暫停")
        else:
            is_paused = True
            pause_btn.config(text="繼續")

    # 添加 UI 元件到 frame
    label = tk.Label(frame, text="00:00", font=("Arial", 24), fg="black")
    label.pack(pady=10)

    # 時間輸入框
    time_entry = tk.Entry(frame, font=("Arial", 22), justify="center", width=10)
    time_entry.pack()
    time_entry.insert(0, "05:00")  # 預設值

    # 設置按鈕
    set_btn = tk.Button(frame, text="設置時間", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black", command=set_timer)
    set_btn.pack()

    # 開始按鈕
    start_btn = tk.Button(frame, text="開始倒數", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black", command=start_countdown)
    start_btn.pack()

    # 暫停/繼續按鈕
    pause_btn = tk.Button(frame, text="暫停", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black", command=pause_timer)
    pause_btn.pack()

    # 圓形時鐘畫布
    canvas = tk.Canvas(frame, width=300, height=300)
    canvas.pack(pady=10)

    # 時鐘基本參數
    center_x, center_y, radius = 150, 150, 125
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="black", width=3)
