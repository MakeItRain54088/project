import tkinter as tk
from math import pi, cos, sin

def start_stopwatch_page(frame, root):
    """設置計時碼錶頁面的功能"""
    # 清空 frame
    for widget in frame.winfo_children():
        widget.destroy()

    # 初始化參數
    minutes, seconds = 0, 0
    elapsed_seconds = 0
    is_running = False  # 用來追蹤碼錶是否正在運行

    # 繪製時鐘的函式
    def draw_clock():
        """繪製圓形時鐘並更新時間"""
        canvas.delete("hands")  # 清除舊的指針
        if elapsed_seconds > 0:
            # 計算秒針角度並繪製
            seconds_angle = (elapsed_seconds % 60) / 60 * 2 * pi
            seconds_x = center_x + radius * cos(-pi / 2 + seconds_angle)
            seconds_y = center_y + radius * sin(-pi / 2 + seconds_angle)
            canvas.create_line(center_x, center_y, seconds_x, seconds_y, fill="red", width=3, tags="hands")
        # 更新時間顯示
        time_str = f"{minutes:02}:{seconds:02}"
        label.config(text=time_str)

    # 計時碼錶的函式
    def update_stopwatch():
        """更新計時碼錶"""
        nonlocal minutes, seconds, elapsed_seconds, is_running
        if is_running:
            elapsed_seconds += 1
            minutes, seconds = divmod(elapsed_seconds, 60)
            draw_clock()  # 更新時鐘顯示
            # 每秒更新一次
            root.after(1000, update_stopwatch)  # 使用 root 來設定計時

    # 開始/暫停碼錶的函式
    def toggle_stopwatch():
        """開始或暫停碼錶"""
        nonlocal is_running
        if is_running:
            is_running = False
            start_pause_btn.config(text="開始")
        else:
            is_running = True
            start_pause_btn.config(text="暫停")
            update_stopwatch()  # 開始更新計時

    # 重置碼錶的函式
    def reset_stopwatch():
        """重置碼錶"""
        nonlocal minutes, seconds, elapsed_seconds, is_running
        is_running = False
        elapsed_seconds = 0
        minutes, seconds = 0, 0
        start_pause_btn.config(text="開始")
        draw_clock()

    # 添加 UI 元件到窗口
    label = tk.Label(frame, text="00:00", font=("Arial", 24), fg="black")
    label.pack(pady=20)

    # 開始/暫停按鈕
    start_pause_btn = tk.Button(frame, text="開始", font=("微軟正黑體", 18, "bold"), bg="lightyellow", fg="black", command=toggle_stopwatch)
    start_pause_btn.pack(pady=10)

    # 重置按鈕
    reset_btn = tk.Button(frame, text="重置", font=("微軟正黑體", 18, "bold"), bg="lightyellow", fg="black", command=reset_stopwatch)
    reset_btn.pack(pady=10)

    # 圓形時鐘畫布
    canvas = tk.Canvas(frame, width=300, height=300)
    canvas.pack(pady=20)

    # 時鐘基本參數
    center_x, center_y, radius = 150, 150, 125
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="black", width=3)