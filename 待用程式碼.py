# 創建輸入框
entry = tk.Entry(root, width=30, font=("Arial", 14, "bold"), bg="white", fg="black")
entry.pack(pady=5)

# 定義打印 Entry 的值
def print_entry_value():
    p = entry.get()
    outcome.config(text=p)  # 修改說明標籤以顯示輸入值

# 創建按鈕 印出entry值
button_print_entry = tk.Button(root, text="Print Entry", command=print_entry_value)
button_print_entry.pack(pady=10)

# 創建標籤
outcome = tk.Label(root, text="示範輸出", font=("微軟正黑體", 14, "bold"), bg="skyblue", fg="black")
outcome.pack(pady=10)

# 創建主菜單
menu = tk.Menu(root)
root.config(menu=menu)

# 創建子菜單
submenu1 = tk.Menu(menu, activebackground="green", activeborderwidth=10, borderwidth=20)
menu.add_cascade(label="menu1", menu=submenu1)
submenu1.add_command(label="label1")
submenu1.add_separator()
submenu1.add_command(label="label2")

submenu2 = tk.Menu(menu)
menu.add_cascade(label="menu2", menu=submenu2)

# 創建文本區
text = tk.Text(root, height=5, width=30, font=("Arial", 14, "bold"), bg="blue", fg="light green")
text.insert(tk.END, "line 1\nline 2\nline 3")  # 插入多行文字
text.pack()

# 打印指定範圍的文本
def print_text_value():
    print(text.get("1.0", "2.4"))

# 創建 Spinbox
spinbox = tk.Spinbox(root, from_=0, to=10, width=5, font=("Arial", 14, "bold"), bg="red", fg="yellow")
spinbox.pack()

# 使用 Spinbox 的函數
def spinbox_used():
    print(spinbox.get())

# 創建 Scale
scale = tk.Scale(root, from_=0, to=10, font=("Arial", 14, "bold"), width=15, orient=tk.HORIZONTAL, length=200)
scale.pack()

# 使用 Scale 的函數
def scale_used(value):
    print(value)

# Radiobutton 的狀態
radio_state = tk.IntVar()

# 創建 Radiobutton
radiobutton1 = tk.Radiobutton(root, text="Option1", value=1, variable=radio_state, command=lambda: print(radio_state.get()))
radiobutton2 = tk.Radiobutton(root, text="Option2", value=2, variable=radio_state, command=lambda: print(radio_state.get()))
radiobutton1.pack()
radiobutton2.pack()

# Checkbutton 的狀態
checked_state1 = tk.IntVar()
checked_state2 = tk.IntVar()

# 創建 Checkbutton
checkbutton1 = tk.Checkbutton(root, text="Option1", variable=checked_state1, command=lambda: print(f"Option1: {checked_state1.get()}, Option2: {checked_state2.get()}"))
checkbutton2 = tk.Checkbutton(root, text="Option2", variable=checked_state2, command=lambda: print(f"Option1: {checked_state1.get()}, Option2: {checked_state2.get()}"))
checkbutton1.pack()
checkbutton2.pack()

# 創建 Listbox
listbox = tk.Listbox(root, width=15, height=4, selectmode=tk.EXTENDED)
options = ["Option1", "Option2", "Option3", "Option4"]
for item in options:
    listbox.insert(tk.END, item)
listbox.pack()