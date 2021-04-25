from tkinter import *   #tkinter모듈 로드

root = Tk()
root.title("PY Gui") #타이틀 지정

btn1 = Button(root, text="Button1") #버튼 생성 이름을 "Button1" 로 지정
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="Button2") #버튼 생성 이름을 "Button2" 로 지정 추가로 버튼 위치 지정
btn2.pack()

btn3 =  Button(root, width=10, height=3, text="Button3") #버튼 생성 이름을 "Button3" 으로 지정 추가로 버튼 크기 지정
btn3.pack()

btn4 = Button(root, fg="red", bg="yellow", text="button4") #버튼 생성 이름을 "Button4" 로 지정 추가로 버튼 글씨 색, 버튼의색 지정
btn4.pack()

photo = PhotoImage(file="C:/Users/Calix/Desktop/python-gui/Button/yes.png") #photo를 사진경로와함께 지정
btn5 = Button(root, image=photo) #버튼 생성 아이콘을 photo로 지정
btn5.pack()

def btncmd(): #btncmd라는 함수
    print("Button이 클릭되었어요") #함수 작동시 Print 구문 작동

btn6 = Button(root, text="button5", command=btncmd) #버튼 생성 이름을 "Button6" 으로 지정 추가로 버튼을 누르면 btncmd라는 함수 작동
btn6.pack()

root.mainloop()