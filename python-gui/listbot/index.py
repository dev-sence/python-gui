from tkinter import *   #tkinter모듈 로드

root = Tk()
root.title("PY Gui") #타이틀 지정
root.geometry("230x403")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "apple")
listbox.insert(1, "banana")
listbox.insert(2, "watermelon")
listbox.insert(3, "grape")
listbox.insert(END, "mango")
listbox.pack()

def btncmd():
#    listbox.delete(END)

#    print("There are", listbox.size(), "items in the list")

#    print("1~3 Items will be printed : ", listbox.get(0, 2))

    print("You have selected", listbox.curselection(), "items")

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()