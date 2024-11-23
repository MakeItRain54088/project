#/Users/aa/Desktop/python程式/python期末/拍貼機.png
import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
from datetime import datetime  # 用於生成時間戳記

# 定義背景圖片路徑
background_path = "C:\Users\HSU\OneDrive\桌面\python\project\project\圖片\拍貼機.png"

# 定義儲存圖片的路徑（基礎路徑）
save_folder = "C:\Users\HSU\OneDrive\桌面\python\project\project\圖片"

def update_video():
    """更新攝像頭畫面"""
    global cap, photo

    # 從攝像頭讀取畫面
    ret, frame = cap.read()
    if ret:
        # 計算攝像頭畫面裁剪區域
        h, w, _ = frame.shape
        aspect_ratio = white_width / white_height

        # 根據白色區域的比例裁剪畫面
        if w / h > aspect_ratio:
            # 寬大於高，裁剪左右
            new_w = int(h * aspect_ratio)
            offset = (w - new_w) // 2
            frame = frame[:, offset:offset + new_w]
        else:
            # 高大於寬，裁剪上下
            new_h = int(w / aspect_ratio)
            offset = (h - new_h) // 2
            frame = frame[offset:offset + new_h, :]

        # 調整畫面大小
        frame = cv2.resize(frame, (white_width, white_height))

        # 將畫面轉換為 RGB 格式
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_image = Image.fromarray(frame_rgb)

        # 將背景圖片與攝像頭畫面合併
        combined = background_image.copy()
        combined.paste(frame_image, (white_x, white_y))

        # 將合成的圖片轉為 PhotoImage
        photo = ImageTk.PhotoImage(combined)

        # 更新畫布上的圖片
        video_label.config(image=photo)
        video_label.image = photo

    # 每 10 毫秒更新一次畫面
    root.after(10, update_video)

def take_photo():
    """拍照並保存圖片"""
    ret, frame = cap.read()
    if ret:
        # 計算攝像頭畫面裁剪區域
        h, w, _ = frame.shape
        aspect_ratio = white_width / white_height

        # 根據白色區域的比例裁剪畫面
        if w / h > aspect_ratio:
            # 寬大於高，裁剪左右
            new_w = int(h * aspect_ratio)
            offset = (w - new_w) // 2
            frame = frame[:, offset:offset + new_w]
        else:
            # 高大於寬，裁剪上下
            new_h = int(w / aspect_ratio)
            offset = (h - new_h) // 2
            frame = frame[offset:offset + new_h, :]

        # 調整畫面大小
        frame = cv2.resize(frame, (white_width, white_height))

        # 將畫面轉為 RGB 格式
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_image = Image.fromarray(frame_rgb)

        # 合成背景圖與攝像頭畫面
        combined = background_image.copy()
        combined.paste(frame_image, (white_x, white_y))

        # 生成包含時間戳的檔名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 格式：YYYYMMDD_HHMMSS
        save_path = f"{save_folder}captured_image_{timestamp}.png"

        # 儲存合成圖片
        combined.save(save_path)
        messagebox.showinfo("拍照成功", f"圖片已保存到:\n{save_path}")

def on_closing():
    """關閉視窗時釋放資源"""
    global cap
    cap.release()  # 釋放攝像頭
    root.destroy()

# 初始化 Tkinter 主窗口
root = tk.Tk()
root.title("拍貼機")
root.geometry("800x800")

# 載入背景圖片
background_image = Image.open(background_path)

# 設定背景圖顯示大小
frame_width, frame_height = 640, 640
background_image.thumbnail((frame_width, frame_height))

# 定義白色區域的位置和大小（根據圖片內容調整）
white_x, white_y = 150, 150  # 左上角坐標 (x, y)
white_width, white_height = 340, 340  # 寬和高

# 創建攝像頭
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    messagebox.showerror("錯誤", "無法打開攝像頭")
    root.quit()

# 顯示攝像頭畫面的 Label
video_label = tk.Label(root)
video_label.pack(pady=20)

# 拍照按鈕
capture_btn = tk.Button(root, text="拍照", command=take_photo, font=("Arial", 16))
capture_btn.pack(pady=10)

# 綁定窗口關閉事件
root.protocol("WM_DELETE_WINDOW", on_closing)

# 開始更新畫面
update_video()

# 運行主循環
root.mainloop()
