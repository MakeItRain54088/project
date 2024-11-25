import os
import csv
import tkinter as tk

# 初始化主視窗
root = tk.Tk()
root.title('健身菜單')
root.geometry('800x600+300+50')
root.resizable(False, False)
root.configure(background='skyblue')

# 切換頁面的frame
page_frame = tk.Frame(root, bg="skyblue")
page_frame.place(relwidth=0.8125, relheight=1, x=150)

def part4_page():
    def show_illustration(illustration):
        for widget in page_frame.winfo_children():
            widget.destroy()

        illustration_frame = tk.Frame(page_frame, bg="skyblue")
        title = tk.Label(illustration_frame, text="訓練內容", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
        title.pack(fill=tk.X, pady=10)

        illustration_label = tk.Label(illustration_frame, text=illustration, font=("微軟正黑體", 15), bg="skyblue", fg="black", wraplength=600)
        illustration_label.pack(pady=20)

        back_button = tk.Button(illustration_frame, text="返回", font=("微軟正黑體", 15, "bold"), bg="white", fg="black",
                                command=part4_page)  # 返回主頁
        back_button.pack(pady=10)

        illustration_frame.pack(fill="both", expand=1)

    part4_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part4_page_frame, text="手臂訓練", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    csv_file = "training_arm.csv"
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    continue
                button_name, illustration, website, sec = row
                button = tk.Button(part4_page_frame, text=button_name, font=("微軟正黑體", 15, "bold"),
                                   bg="white", fg="black", width=20,
                                   command=lambda a=illustration: show_illustration(a))
                button.pack(pady=5)
    except FileNotFoundError:
        error_label = tk.Label(part4_page_frame, text="找不到 CSV 檔案", font=("微軟正黑體", 15, "bold"), bg="skyblue", fg="red")
        error_label.pack(pady=20)

    part4_page_frame.pack(fill="both", expand=1)