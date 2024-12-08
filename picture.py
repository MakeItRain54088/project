# picture.py
import os
import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
from datetime import datetime

class CameraApp:
    def __init__(self, frame):
        """初始化相機應用"""
        self.frame = frame
        self.cap = None
        self.is_running = False
        
        # 設定保存路徑
        self.save_folder = "images"
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)
            
        # 設置相機預覽區域
        self.setup_camera_ui()
        
    def setup_camera_ui(self):
        """設置相機UI元素"""
        # 視訊顯示區域
        self.video_frame = tk.Frame(self.frame)
        self.video_frame.pack(pady=10)
        
        self.video_label = tk.Label(self.video_frame)
        self.video_label.pack()
        
        # 拍照按鈕
        self.photo_button = tk.Button(
            self.frame,
            text="拍照",
            font=("微軟正黑體", 15, "bold"),
            bg="white",
            fg="black",
            height=2,
            width=10,
            command=self.take_photo
        )
        self.photo_button.pack(pady=20)
        
    def start(self):
        """啟動相機"""
        self.cap = cv2.VideoCapture(0)
        self.is_running = True
        self.update_frame()
        
    def stop(self):
        """停止相機"""
        self.is_running = False
        if self.cap is not None:
            self.cap.release()
            self.cap = None
            
    def update_frame(self):
        """更新視訊畫面"""
        if self.is_running and self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                # 轉換影像格式
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_pil = Image.fromarray(frame_rgb)
                
                # 調整大小
                frame_pil = frame_pil.resize((640, 480))
                
                # 轉換為Tkinter可用格式
                self.photo = ImageTk.PhotoImage(frame_pil)
                self.video_label.config(image=self.photo)
                
            # 持續更新
            self.frame.after(10, self.update_frame)
            
    def take_photo(self):
        """拍照並保存"""
        if self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                # 生成時間戳檔名
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                save_path = os.path.join(self.save_folder, f"{timestamp}.png")
                
                # 保存圖片
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame_rgb)
                image = image.resize((640, 480))
                image.save(save_path)
                
                messagebox.showinfo("拍照成功", f"圖片已保存到:\n{save_path}")

def create_camera_page(parent_frame):
    """創建相機頁面"""
    camera_app = CameraApp(parent_frame)
    camera_app.start()
    return camera_app

# 用於清理資源的函數
def cleanup_camera(camera_app):
    """清理相機資源"""
    if camera_app is not None:
        camera_app.stop()