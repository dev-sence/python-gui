from tkinter import *   #tkinter모듈 로드

root = Tk()
root.title("PY Gui") #타이틀 지정
root.geometry("230x403")

"https://www.youtube.com/watch?v=bKPIcoou9N8"

def btncmd():
    pass

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()