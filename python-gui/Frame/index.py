from tkinter import *   #tkinter모듈 로드

root = Tk()
root.title("PY Gui") #타이틀 지정
root.geometry("640x480") #가로 * 세로 (창 크기)
#root.geometry("640x480+300+100") #가로 * 세로 (창 크기) X좌표 + Y좌표 (창이 뜨는 위치)

root.resizable(False, False) #창 크기변경 락

root.mainloop()