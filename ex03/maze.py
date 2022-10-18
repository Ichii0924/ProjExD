import tkinter as tk

#練習5
def key_down(event):
    global key
    key = event.keysym

#練習6
def key_up(event):
    global key
    key = ""

#練習7
def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canv.coords("tori", cx, cy) 
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習1

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()#練習2

    tori = tk.PhotoImage(file="fig/9.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image = tori, tag="tori")#練習3

    key = "" #現在押されているキーを表す#練習4

    root.bind("<KeyPress>", key_down)#練習5

    root.bind("<KeyRelease>", key_up)#練習6

    main_proc()#練習7

    root.mainloop()