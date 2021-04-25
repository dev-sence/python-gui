from tkinter import *   #tkinter모듈 로드

root = Tk()
root.title("PY Gui") #타이틀 지정

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "Write Words")

e = Entry(root, width=30)
e.pack()
e.insert(0, "Write one line")

def btncmd():
    print("<TXT(Big) >: " + txt.get("1.0", END))
    print("<ENTRY(Small) >: " + e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()