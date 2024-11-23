import tkinter as tk
from math import pi, cos, sin
from tkinter import PhotoImage
from PIL import Image, ImageTk
from resizeimage.resizeimage import resize_thumbnail


def draw_clock():
    """更新圓形時鐘"""
    canvas.delete("hands")  # 刪除舊的指針

    # 繪製秒針
    seconds_angle = (seconds_left / total_seconds) * 2 * pi  # 以倒數計算角度
    seconds_x = center_x + radius * cos(-pi / 2 + seconds_angle)
    seconds_y = center_y + radius * sin(-pi / 2 + seconds_angle)
    canvas.create_line(center_x, center_y, seconds_x, seconds_y, fill="red", width=3, tags="hands")
    canvas.tag_raise("hands")  # 將秒針置頂
    # 更新時間顯示
    time_str = f"{minutes:02}:{seconds:02}"
    label.config(text=time_str)

def start_countdown():
    """開始倒數"""
    global minutes, seconds, seconds_left
    if seconds_left == 0:
        label.config(text="時間到！")
        return

    # 更新倒數時間
    seconds_left -= 1
    minutes, seconds = divmod(seconds_left, 60)

    # 更新時鐘動畫
    draw_clock()

    # 每秒更新一次
    root.after(1000, start_countdown)

def set_timer():
    """設置倒數時間"""
    global minutes, seconds, seconds_left, total_seconds
    time_input = time_entry.get()
    try:
        # 確保輸入格式為 MM:SS
        if ":" not in time_input:
            raise ValueError("請輸入格式為 MM:SS 的時間！")

        mins, secs = map(int, time_input.split(":"))
        if mins < 0 or secs < 0 or secs >= 60:
            raise ValueError("請輸入有效的時間！")

        # 更新時間
        minutes, seconds = mins, secs
        seconds_left = minutes * 60 + seconds
        total_seconds = seconds_left  # 用於計算指針角度
        label.config(text=f"{minutes:02}:{seconds:02}")
        draw_clock()  # 初始化時鐘顯示
    except ValueError as e:
        tk.messagebox.showerror("無效輸入", str(e))

# 初始化參數
minutes, seconds = 0, 0
seconds_left = 0
total_seconds = 0

# 主視窗
root = tk.Tk()
root.title("圓形倒數時鐘")
root.geometry("800x500")
root.attributes('-topmost',1)
#設置背景
label_bg=tk.Label(root,width=800,height=800)
original_image1 = Image.open("C:\Users\HSU\OneDrive\桌面\python\project\project\圖片\真正的新背景.png")
original_image1.thumbnail((800,500))  # 設置圖片大小
photo1 = ImageTk.PhotoImage(original_image1)
label_bg.config(image=photo1)
label_bg.place(width=800,height=500)  # 設置Label填滿整個視窗
# 時鐘畫布
canvas = tk.Canvas(root, width=150, height=150)
canvas.place(relx=0.75,rely=0.05)#設定時鐘位置

# 圓形時鐘中心點與半徑
center_x, center_y = 75, 103
radius = 20
# 繪製外圓
# canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="black", width=3)
original_image=Image.open("C:\Users\HSU\OneDrive\桌面\python\project\project\圖片\時鐘.png")
original_image.thumbnail((150,150))#設置圖片大小
label1=tk.Label(root)
photo = ImageTk.PhotoImage(original_image)
# label1.config(image=photo)
# label1.place(x=100,y=23,width=300,height=300)
canvas.create_image(80, 80, image=photo, tags="background")#設置計時器圖片位置

# 時間顯示
label = tk.Label(root, text="00:00", font=("Arial", 24), fg="black")
label.place(relx=0.805,rely=0.35)

# 時間輸入框
time_entry = tk.Entry(root, font=("Arial", 16), justify="center", width=10)
time_entry.pack(pady=5)
time_entry.insert(0, "05:00")  # 預設值為 5 分鐘

# 設置按鈕
set_btn = tk.Button(root, text="設置時間", command=set_timer)
set_btn.pack(side="right", padx=0)

# 開始按鈕
start_btn = tk.Button(root, text="開始倒數", command=start_countdown)
start_btn.pack(side="right", padx=0)
#設置放影片的區域
label_video=tk.Label(root,bg='white')
label_video.place(relx=0.25,rely=0.28,relwidth=0.5,relheight=0.6)

# 運行主迴圈
root.mainloop()
