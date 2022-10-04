import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    
    if num == "=": #＝が押されたら計算
        val = entry.get()
        if val == "2501":
            res = "GHOST IN THE SHELL"
            entry.delete(0, tk.END)
            entry.insert(tk.END, res)
        else:
            res = eval(val)
            entry.delete(0, tk.END)
            entry.insert(tk.END, res)
    elif num == "c":
        entry.delete(0,tk.END)    
    else:
        entry.insert(tk.END, num)#練習5
    



#練習3

root = tk.Tk()
root.geometry("375x565")


#入力ボタンの作成
BUTTON=[
    ["**","(",")","c"],
    ["9","8","7","*"],
    ["6","5","4","-"],
    ["3","2","1","/"],
    ["+","0",".","="]
]

for y, row in enumerate(BUTTON,1):
    for x, num in enumerate(row):
        btn = tk.Button(root, text=str(num), font=("", 30), width=4, height=2)
        btn.bind("<1>", click_number)
        btn.grid(row=y, column=x)

#入力欄の作成
entry = tk.Entry(root, font=("",22), width=25,  justify= "right" )
entry.grid(row=0, column=0, columnspan=4)

#ウィンドウ表示
root.mainloop()