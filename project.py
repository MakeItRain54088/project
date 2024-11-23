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

    title = tk.Label(home_page_frame, text="健身菜單", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    label1 = tk.Label(home_page_frame, text="根據你的需求設計一套合適的訓練菜單", font=("微軟正黑體", 15, "bold"), bg="skyblue", fg="black")
    label1.pack(fill=tk.X)
    label2 = tk.Label(home_page_frame, text="選擇訓練菜單", font=("微軟正黑體", 15, "bold"), bg="skyblue", fg="black")
    label2.place(relx=0.4, rely=0.25)
    
    optionlist = ['A','B','C','D','E']
    option_value = tk.StringVar()
    option_value.set("請選擇")
    option = tk.OptionMenu(home_page_frame, option_value, *optionlist)
    option.config(width=24, font=("微軟正黑體", 15, "bold"), bg="white", fg="black")
    option.place(relx=0.25, rely=0.3)

    add_option = tk.Button(home_page_frame, text="新增其他菜單", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", height=1, width=15)
    add_option.place(relx=0.35, rely=0.4)

    start = tk.Button(home_page_frame, text="開始訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", height=2, width=15)
    start.place(relx=0.35, rely=0.7)

    home_page_frame.pack(fill="both", expand=1)



def part1_page():
    part1_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part1_page_frame, text="有氧運動", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)

    label1 = tk.Label(part1_page_frame, text="part1", font=("微軟正黑體", 15, "bold"), bg="skyblue", fg="black")
    label1.pack(fill=tk.X)
    
    part1_page_frame.pack(fill="both", expand=1)

def part2_page():
    part2_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part2_page_frame, text="徒手訓練", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    part2_page_frame.pack(fill="both", expand=1)

def part3_page():
    part3_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part3_page_frame, text="胸部訓練", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    part3_page_frame.pack(fill="both", expand=1)

def part4_page():
    part4_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part4_page_frame, text="肩膀與手臂訓練", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    part4_page_frame.pack(fill="both", expand=1)

def part5_page():
    part5_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part5_page_frame, text="背部訓練", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    part5_page_frame.pack(fill="both", expand=1)

def part6_page():
    part6_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part6_page_frame, text="腿部訓練", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    part6_page_frame.pack(fill="both", expand=1)

def part7_page():
    part7_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part7_page_frame, text="自訂菜單", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    part7_page_frame.pack(fill="both", expand=1)

def part8_page():
    part8_page_frame = tk.Frame(page_frame, bg="skyblue")
    title = tk.Label(part8_page_frame, text="系統推薦菜單", font=("微軟正黑體", 22, "bold"), bg="lightyellow", fg="black")
    title.pack(fill=tk.X)
    part8_page_frame.pack(fill="both", expand=1)



#切換頁面的函式
def switch_topage(page_name):
    for i in page_frame.winfo_children():
        i.destroy()
    page_name()

#選單的frame
menu = tk.Frame(root)
menu.pack(side=tk.LEFT, fill=tk.Y)
menu.pack_propagate(flag=False)
menu.config(width=150, bg="gray")

home = tk.Button(menu, text="主頁", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: home_page())
part1 = tk.Button(menu, text="有氧運動", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part1_page))
part2 = tk.Button(menu, text="徒手訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part2_page))
part3 = tk.Button(menu, text="胸部訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part3_page))
part4 = tk.Button(menu, text="肩膀與手臂訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part4_page))
part5 = tk.Button(menu, text="背部訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part5_page))
part6 = tk.Button(menu, text="腿部訓練", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part6_page))
part7 = tk.Button(menu, text="自訂菜單", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part7_page))
part8 = tk.Button(menu, text="系統推薦菜單", font=("微軟正黑體", 15, "bold"), bg="white", fg="black", width=15, command=lambda: switch_topage(part8_page))

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