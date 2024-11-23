import tkinter as tk

# 初始化主視窗
root = tk.Tk()
root.title('健身菜單')
root.geometry('800x600+300+50')
root.resizable(False, False)
root.configure(background='skyblue')

#切換頁面的frame
page_frame = tk.Frame(root, bg="skyblue")
page_frame.place(relwidth=0.8125, relheight=1, x=150)

#主頁面
def home_page():
    for i in page_frame.winfo_children():
        i.destroy()
    home_page_frame = tk.Frame(page_frame, bg="skyblue")

    title = tk.Label(home_page_frame, text="健身菜單", font=("微軟正黑體", 24, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    label1 = tk.Label(home_page_frame, text="根據你的需求設計一套合適的訓練菜單", font=("微軟正黑體", 14, "bold"), bg="skyblue", fg="black")
    label1.pack(fill=tk.X)
    label2 = tk.Label(home_page_frame, text="選擇訓練菜單", font=("微軟正黑體", 14, "bold"), bg="skyblue", fg="black")
    label2.place(relx=0.4, rely=0.25)
    star = tk.Button(home_page_frame, text="典藏", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", height=2, width=15)
    star.place(relx=0.2, rely=0.3)
    shop = tk.Button(home_page_frame, text="購物車", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", height=2, width=15)
    shop.place(relx=0.5, rely=0.3)
    label3 = tk.Label(home_page_frame, text="已選擇XXXX", font=("微軟正黑體", 14, "bold"), bg="skyblue", fg="black")
    label3.place(relx=0.4, rely=0.5)
    start = tk.Button(home_page_frame, text="開始訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", height=2, width=15)
    start.place(relx=0.35, rely=0.7)

    home_page_frame.pack(fill="both", expand=1)


#切換頁面的函式
def create_page(page_name):
    for i in page_frame.winfo_children():
        i.destroy()
    
    page_name_frame = tk.Frame(page_frame)

    lb = tk.Label(page_name_frame, text=page_name, font=("微軟正黑體", 20, "bold"), bg='skyblue', fg="black")
    lb.pack(fill="both")

    content = tk.Label(page_name_frame, text= "點擊選項加入你的自訂菜單", font=("微軟正黑體", 14), bg='skyblue', fg="black")
    content.pack(fill="both")

    page_name_frame.pack(fill="both")

#選單的frame
menu = tk.Frame(root)
menu.pack(side=tk.LEFT, fill=tk.Y)
menu.pack_propagate(flag=False)
menu.config(width=150, bg="gray")

home = tk.Button(menu, text="主頁", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: home_page())
part1 = tk.Button(menu, text="有氧運動", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: create_page("有氧運動"))
part2 = tk.Button(menu, text="徒手訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: create_page("徒手訓練"))
part3 = tk.Button(menu, text="胸部訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: create_page("胸部訓練"))
part4 = tk.Button(menu, text="肩膀與手臂訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: create_page("肩膀與手臂訓練"))
part5 = tk.Button(menu, text="背部訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: create_page("背部訓練"))
part6 = tk.Button(menu, text="腿部訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: create_page("腿部訓練"))
part7 = tk.Button(menu, text="自訂菜單", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: create_page("自訂菜單"))
part8 = tk.Button(menu, text="系統推薦菜單", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: create_page("系統推薦菜單"))

home.pack()
part1.pack()
part2.pack()
part3.pack()
part4.pack()
part5.pack()
part6.pack()
part7.pack()
part8.pack()

home_page()
# 啟動主迴圈 常駐主視窗
root.mainloop()