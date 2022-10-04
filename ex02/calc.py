import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn = event.widget
    num = int(btn["text"])
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num)#練習5


#練習3

root = tk.Tk()
root.geometry("300x500")

BUTTON=[
    ["9","8","7"],
    ["6","5","4"],
    ["3","2","1"],
    ["0","+"]
]

for y, row in enumerate(BUTTON,1):
    for x, num in enumerate(row):
        btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
        btn.bind("<1>", click_number)
        btn.grid(row=y, column=x)



# for i in range(9, -1, -1):
#     button = tk.Button(root, text=f"{i}", font=("Times New Roman", 30), width=4, height=2)
#     button.grid()

#入力欄の作成
entry = tk.Entry(root, font=(",40"), width=25, justify= "right")
entry.grid(row=0, column=0, columnspan=3)

# r, c = 1, 0
# for i, num in enumerate(list(range(9,-1, -1))+["+"], 1):
#     btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
#     btn.bind("<1>", click_number)
#     btn.grid(row=r, column=c)
#     c += 1
#     if i%3 == 0:
#         r += 1
#         c = 0
#練習2



root.mainloop()