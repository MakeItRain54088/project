import tkinter as tk

# 初始化主視窗
root = tk.Tk()
root.title('健身菜單')
root.geometry('800x600+300+50')
root.resizable(False, False)
root.configure(background='skyblue')

# 定義切換頁面的函數
def open_new_window(menu_name):
    new_window = tk.Toplevel(root)
    new_window.title(menu_name)
    new_window.geometry('800x600+300+50')
    new_window.configure(background='lightgreen')

    # 在新窗口中顯示菜單
    label = tk.Label(new_window, text= menu_name, font=("微軟正黑體", 24, "bold"), bg="lightgreen")
    label.pack(pady=20)

    # 可以在這裡添加更詳細的菜單內容
    content = tk.Label(new_window, text= "點擊選項加入你的自訂菜單", font=("微軟正黑體", 14), bg="lightgreen")
    content.pack(pady=10)

# 使用 grid網格 放置按鈕
frame = tk.Frame(root, bg="skyblue")  # 建立一個框架來放置按鈕
frame.grid(row=2, column=0, columnspan=2, pady=10)

# 設置列的擴展
root.grid_columnconfigure(0, weight=1)  # 第一列的權重
root.grid_columnconfigure(1, weight=1)  # 第二列的權重

part1 = tk.Button(frame, text="有氧運動", font=("微軟正黑體", 20, "bold"), bg="white", fg="black", width=15, command=lambda: open_new_window("有氧運動"))
part2 = tk.Button(frame, text="徒手訓練", font=("微軟正黑體", 20, "bold"), bg="white", fg="black", width=15, command=lambda: open_new_window("徒手訓練"))
part3 = tk.Button(frame, text="胸部訓練", font=("微軟正黑體", 20, "bold"), bg="white", fg="black", width=15, command=lambda: open_new_window("胸部訓練"))
part4 = tk.Button(frame, text="肩膀與手臂訓練", font=("微軟正黑體", 20, "bold"), bg="white", fg="black", width=15, command=lambda: open_new_window("肩膀與手臂訓練"))
part5 = tk.Button(frame, text="背部訓練", font=("微軟正黑體", 20, "bold"), bg="white", fg="black", width=15, command=lambda: open_new_window("背部訓練"))
part6 = tk.Button(frame, text="腿部訓練", font=("微軟正黑體", 20, "bold"), bg="white", fg="black", width=15, command=lambda: open_new_window("腿部訓練"))
part7 = tk.Button(frame, text="自訂菜單", font=("微軟正黑體", 20, "bold"), bg="white", fg="black", width=15, command=lambda: open_new_window("自訂菜單"))
part8 = tk.Button(frame, text="系統推薦菜單", font=("微軟正黑體", 20, "bold"), bg="white", fg="black", width=15, command=lambda: open_new_window("系統推薦菜單"))

part1.grid(row=0, column=0, padx=5, pady=5)
part2.grid(row=0, column=1, padx=5, pady=5)
part3.grid(row=1, column=0, padx=5, pady=5)
part4.grid(row=1, column=1, padx=5, pady=5)
part5.grid(row=2, column=0, padx=5, pady=5)
part6.grid(row=2, column=1, padx=5, pady=5)
part7.grid(row=3, column=0, padx=5, pady=5)
part8.grid(row=3, column=1, padx=5, pady=5)

# 標題
title = tk.Label(root, text="健身菜單", font=("微軟正黑體", 24, "bold"), bg="white", fg="black")
title.grid(row=0, column=0, pady=10, columnspan=2, sticky='nsew')

# 說明
label = tk.Label(root, text="根據你的需求設計一套合適的訓練菜單", font=("微軟正黑體", 14, "bold"), bg="skyblue", fg="black")
label.grid(row=1, column=0, pady=10, columnspan=2, sticky='nsew')

# 啟動主迴圈 常駐主視窗
root.mainloop()